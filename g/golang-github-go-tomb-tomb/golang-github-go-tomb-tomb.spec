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
%global project         go-tomb
%global repo            tomb
# https://github.com/go-tomb/tomb
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     gopkg.in/tomb.v2
%global commit          d5d1b5820637886def9eef33e03a27a9f166942c
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global import_path_sec gopkg.in/v2/tomb

%global v1_commit          dd632973f1e7218eb1089048e0798ec9ae7dceb8
%global v1_shortcommit     %(c=%{v1_commit}; echo ${c:0:7})
%global v1_provider_prefix github.com/go-tomb/tomb
%global v1_import_path     gopkg.in/tomb.v1
%global v1_import_path_sec gopkg.in/v1/tomb
%global v1_name            golang-gopkg-tomb-v1


Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.11.git%{shortcommit}
Summary:        Helps with clean goroutine termination in the Go language
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source1:        https://%{v1_provider_prefix}/archive/%{v1_commit}/%{repo}-%{v1_shortcommit}.tar.gz

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

%if 0%{?with_check}
BuildRequires: golang(golang.org/x/net/context)
%endif

Requires: golang(golang.org/x/net/context)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path_sec}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package -n %{v1_name}-devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
%endif

Provides:      golang(%{v1_import_path}) = %{version}-%{release}
Provides:      golang(%{v1_import_path_sec}) = %{version}-%{release}

%description -n %{v1_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{v1_import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test
Group: Development/Other
Summary:         Unit tests for %{name} package
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

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
%setup -q -n %{repo}-%{v1_commit} -T -b 1
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
install -d -p %{buildroot}/%{go_path}/src/%{import_path_sec}/
echo "%%dir %%{go_path}/src/%%{import_path_sec}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{go_path}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
    echo "%%dir %%{go_path}/src/%%{import_path_sec}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{import_path_sec}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path_sec}/$file
    echo "%%{go_path}/src/%%{import_path_sec}/$file" >> devel.file-list
done

pushd ../%{repo}-%{v1_commit}

install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path}/
echo "%%dir %%{go_path}/src/%%{v1_import_path}/." >> ../%{repo}-%{commit}/v1_devel.file-list
install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path_sec}/
echo "%%dir %%{go_path}/src/%%{v1_import_path_sec}/." >> ../%{repo}-%{commit}/v1_devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{go_path}/src/%%{v1_import_path}/$(dirname $file)" >> ../%{repo}-%{commit}/v1_devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{v1_import_path}/$file
    echo "%%{go_path}/src/%%{v1_import_path}/$file" >> ../%{repo}-%{commit}/v1_devel.file-list
    echo "%%dir %%{go_path}/src/%%{v1_import_path_sec}/$(dirname $file)" >> ../%{repo}-%{commit}/v1_devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path_sec}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{v1_import_path_sec}/$file
    echo "%%{go_path}/src/%%{v1_import_path_sec}/$file" >> ../%{repo}-%{commit}/v1_devel.file-list
done

popd
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{go_path}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
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

%gotest %{import_path}
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc README.md
%dir %{go_path}/src/%{import_path_sec}

%files -n %{v1_name}-devel -f v1_devel.file-list
%doc LICENSE
%doc README.md
%dir %{go_path}/src/%{v1_import_path_sec}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc README.md
%endif

%changelog
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.11.gitd5d1b58
- new version

