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

%define copying() \
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7 \
%license %{*} \
%else \
%doc %{*} \
%endif

%global provider        github
%global provider_tld    com
%global project         go-gcfg
%global repo            gcfg
# https://github.com/go-gcfg/gcfg
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     gopkg.in/gcfg.v1
%global commit          5866678811acbcbc248097f2c524cbc4d13abd8b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global gc_import_path  code.google.com/p/gcfg
%global gopkg_name      golang-gopkg-gcfg
%global devel_main      golang-gopkg-gcfg-devel

Name:           golang-googlecode-gcfg
Version:        0
Release:        alt1_0.13.git%{shortcommit}
Summary:        Gcfg reads INI-style configuration files into Go structs
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# If go_arches not defined fall through to implicit golang archs
%if 0%{?go_arches:1}
%else
ExclusiveArch:   %{ix86} x86_64 %{arm}
%endif
# If gccgo_arches does not fit or is not defined fall through to golang
%ifarch 0%{?gccgo_arches}
%else
BuildRequires:   golang
%endif
Source44: import.info

%description
%{summary}

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{gc_import_path}) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/scanner) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/token) = %{version}-%{release}
Provides:      golang(%{gc_import_path}/types) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gc_import_path} prefix.

%package -n %{gopkg_name}-devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
%endif


Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/scanner) = %{version}-%{release}
Provides:      golang(%{import_path}/token) = %{version}-%{release}
Provides:      golang(%{import_path}/types) = %{version}-%{release}

%description -n %{gopkg_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test}
%package unit-test
Group: Development/Other
Summary:         Unit tests for %{name} package
# If go_arches not defined fall through to implicit golang archs
%if 0%{?go_arches:1}
%else
ExclusiveArch:   %{ix86} x86_64 %{arm}
%endif
# If gccgo_arches does not fit or is not defined fall through to golang
%ifarch 0%{?gccgo_arches}
%else
BuildRequires:   golang
%endif

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage

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
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
install -d -p %{buildroot}/%{go_path}/src/%{gc_import_path}/

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
pushd %{buildroot}/%{go_path}/src/%{gc_import_path}
sed -i 's/"gopkg\.in\/gcfg\.v1/"code\.google\.com\/p\/gcfg/g' \
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
for file in $(find testdata -iname "*.gcfg"); do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test.file-list
done
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%ifarch 0%{?gccgo_arches}
function gotest { %{gcc_go_test} "$@"; }
%else
%if 0%{?golang_test:1}
function gotest { %{golang_test} "$@"; }
%else
function gotest { go test "$@"; }
%endif
%endif

export GOPATH=%{buildroot}/%{go_path}:%{go_path}
gotest %{import_path}
gotest %{import_path}/scanner
gotest %{import_path}/token
gotest %{import_path}/types
%endif

%if 0%{?with_devel}
%files devel -f gc_devel.file-list
%doc LICENSE
%doc README
%dir %{go_path}/src/%{gc_import_path}

%files -n %{gopkg_name}-devel -f devel.file-list
%doc LICENSE
%doc README
%dir %{go_path}/src/%{import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc README
%endif

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.13.git5866678
- new version

