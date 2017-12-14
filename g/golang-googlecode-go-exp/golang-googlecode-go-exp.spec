Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 1
%global with_bundled 0
%global with_debug 0
%global with_check 1
%global with_unit_test 1
%else
%global with_devel 0
%global with_bundled 0
%global with_debug 0
%global with_check 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         golang
%global repo            exp
# https://github.com/golang/exp
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     golang.org/x/exp
%global commit          d00e13ec443927751b2bd49e97dea7bf3b6a6487
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global gi_name         golang-%{provider}-%{project}-%{repo}
%global gc_import_path  code.google.com/p/go.exp

Name:           golang-googlecode-go-exp
Version:        0
Release:        alt1_0.16.git%{shortcommit}
Summary:        Experimental tools and packages for Go
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{gc_import_path}/ebnf) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/inotify) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/old/netchan) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/utf8string) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/winfsnotify) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gc_import_path} prefix.

%package -n %{gi_name}-devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{import_path}/ebnf) = %{version}-%{release}
Provides:      golang(%{import_path}/inotify) = %{version}-%{release}
Provides:      golang(%{import_path}/old/netchan) = %{version}-%{release}
Provides:      golang(%{import_path}/utf8string) = %{version}-%{release}
Provides:      golang(%{import_path}/winfsnotify) = %{version}-%{release}

%description -n %{gi_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test}
%package unit-test
Group: Development/Other
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%if 0%{?fedora} >= 23
BuildRequires:   golang-docs
%endif
%endif

# test subpackage tests code from devel subpackage
%if 0%{?fedora} >= 23
Requires:        golang-docs
%endif

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{gc_import_path}/
echo "%%dir %%{go_path}/src/%%{gc_import_path}" >> gc_devel.file-list
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}" >> devel.file-list

# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> devel.file-list.dir
    done
    install -d -p %{buildroot}/%{go_path}/src/%{gc_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{gc_import_path}/$file
    echo "%%{go_path}/src/%%{gc_import_path}/$file" >> gc_devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{gc_import_path}/$filedir" >> gc_devel.file-list.dir
    done
done
[ -s devel.file-list.dir ] && sort -u devel.file-list.dir >> devel.file-list
[ -s gc_devel.file-list.dir ] && sort -u gc_devel.file-list.dir >> gc_devel.file-list
pushd %{buildroot}/%{go_path}/src/%{gc_import_path}/
# from https://groups.google.com/forum/#!topic/golang-nuts/eD8dh3T9yyA, first post
sed -i 's/"golang\.org\/x\//"code\.google\.com\/p\/go\./g' \
        $(find . -name '*.go')
popd
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> unit-test.file-list.dir
    done
done
[ -s unit-test.file-list.dir ] && sort -u unit-test.file-list.dir >> unit-test.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%else
export GOPATH=%{buildroot}/%{go_path}:$(pwd)/Godeps/_workspace:%{go_path}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/ebnf
%if 0%{?fedora} >= 23
%gotest %{import_path}/ebnflint
%endif
# fails in arm
#%%gotest %%{import_path}/fsnotify
%gotest %{import_path}/inotify
%gotest %{import_path}/old/netchan
%gotest %{import_path}/utf8string
#%%gotest %%{import_path}/winfsnotify
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f gc_devel.file-list
%doc LICENSE
%doc README AUTHORS CONTRIBUTORS PATENTS

%files -n %{gi_name}-devel -f devel.file-list
%doc LICENSE
%doc README AUTHORS CONTRIBUTORS PATENTS
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc README AUTHORS CONTRIBUTORS PATENTS
%endif

%changelog
* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.16.gitd00e13e
- new version

