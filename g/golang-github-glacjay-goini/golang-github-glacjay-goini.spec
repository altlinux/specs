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
# Dict cannot be stringified as expected.
%global with_check 0
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
%global project         glacjay
%global repo            goini
# https://github.com/glacjay/goini
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          5261baf26f41eeffae5fd27be784302e389b7699
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

# github.com/rakyll/goini has no license.
# But it is forked from github.com/glacjay/goini and unchanged.
# Lets provide these source codes as well.
%global rcommit         907cca0f578a5316fb864ec6992dc3d9730ec58c
%global rscommit        %(c=%{rcommit}; echo ${c:0:7})
%global rimport_path    %{provider}.%{provider_tld}/rakyll/goini

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.10.git%{shortcommit}
Summary:        INI file parser in go
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{rcommit}/%{repo}-%{rscommit}.tar.gz
Source1:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

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
%endif

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{rimport_path}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
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
%setup -q -n %{repo}-%{rcommit}
%setup -q -n %{repo}-%{commit} -T -b 1

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
install -d -p %{buildroot}/%{go_path}/src/%{rimport_path}/
echo "%%dir %%{go_path}/src/%%{rimport_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{go_path}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
done

pushd ../%{repo}-%{rcommit}
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{go_path}/src/%%{rimport_path}/$(dirname $file)" >> ../%{repo}-%{commit}/devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{rimport_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{rimport_path}/$file
    echo "%%{go_path}/src/%%{rimport_path}/$file" >> ../%{repo}-%{commit}/devel.file-list
done
popd
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
cp -pav empty.ini %{buildroot}/%{go_path}/src/%{import_path}/.
cp -pav example.ini %{buildroot}/%{go_path}/src/%{import_path}/.
echo "%%{go_path}/src/%%{import_path}/empty.ini" >> unit-test.file-list
echo "%%{go_path}/src/%%{import_path}/example.ini" >> unit-test.file-list
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
%doc LICENSE.txt
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%dir %{go_path}/src/%{provider}.%{provider_tld}/rakyll
%dir %{go_path}/src/%{rimport_path}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test -f unit-test.file-list
%doc LICENSE.txt
%endif

%changelog
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.10.git5261baf
- new version

