Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
# Failing on aarch and arm
%global with_check 0
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         go-check
%global repo            check
# https://github.com/go-check/check
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     gopkg.in/check.v1
%global import_path_sec launchpad.net/gocheck
%global commit          4f90aeace3a26ad7021961c297b22c42160c7b25
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global gimport_path    github.com/go-check/check

# github.com/motain/gocheck, cloned from github.com/go-check/check on Oct 23, 2013
%global mcommit         10bfe0586b48cbca10fe6c43d6e18136f25f8c0c
%global mscommit        %(c=%{mcommit}; echo ${c:0:7})
%global mimport_path    github.com/motain/gocheck

Name:           golang-gopkg-%{repo}
Version:        1
Release:        alt1_16
Summary:        Rich testing for the Go language
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{mcommit}/%{repo}-%{mscommit}.tar.gz
Source1:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Obsoletes:      golang-launchpad-gocheck

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
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
Provides:      golang(%{import_path_sec}) = %{version}-%{release}
Provides:      golang(%{mimport_path}) = %{version}-%{release}
Provides:      golang(%{gimport_path}) = %{version}-%{release}
Obsoletes:     golang-launchpad-gocheck-devel

%description devel
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
%endif

# test subpackage tests code from devel subpackage

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -n %{repo}-%{mcommit} -q
%setup -n %{repo}-%{commit} -q -T -b 1

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
install -d -p %{buildroot}/%{go_path}/src/%{import_path_sec}/
install -d -p %{buildroot}/%{go_path}/src/%{gimport_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list

    install -d -p %{buildroot}/%{go_path}/src/%{import_path_sec}/$(dirname $file)
    cp $file %{buildroot}/%{go_path}/src/%{import_path_sec}/$file
    echo "%%{go_path}/src/%%{import_path_sec}/$file" >> devel.file-list

    install -d -p %{buildroot}/%{go_path}/src/%{gimport_path}/$(dirname $file)
    cp $file %{buildroot}/%{go_path}/src/%{gimport_path}/$file
    echo "%%{go_path}/src/%%{gimport_path}/$file" >> devel.file-list
done
%endif

pushd ../%{repo}-%{mcommit}
install -d -p %{buildroot}/%{go_path}/src/%{mimport_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{mimport_path}/$(dirname $file)
    cp $file %{buildroot}/%{go_path}/src/%{mimport_path}/$file
    echo "%%{go_path}/src/%%{mimport_path}/$file" >> ../%{repo}-%{commit}/devel.file-list
done
popd

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test.file-list
done
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
%dir %{go_path}/src/%{import_path}
%dir %{go_path}/src/%{import_path_sec}
%dir %{go_path}/src/%{gimport_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc README.md
%endif

%changelog
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 1-alt1_16
- new version

