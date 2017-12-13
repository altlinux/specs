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
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         milochristiansen
%global repo            lua
# https://github.com/milochristiansen/lua
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          9cfe53dd9ceb6eec2638c96927350163705a4d4c
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
# commit 9cfe53dd9ceb6eec2638c96927350163705a4d4c == version 1.1.4

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.1.4
Release:        alt1_1
Summary:        Lua 5.3 VM and compiler written in Go

# License is confirmed to be zlib: https://github.com/milochristiansen/lua/issues/5
License:        zlib
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}/%{project}-%{repo}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}

# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
This is a Lua 5.3 VM and compiler written in Go. This is
intended to allow easy embedding into Go programs, with
minimal fuss and bother.

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/ast) = %{version}-%{release}
Provides:      golang(%{import_path}/lmodbase) = %{version}-%{release}
Provides:      golang(%{import_path}/lmodmath) = %{version}-%{release}
Provides:      golang(%{import_path}/lmodpackage) = %{version}-%{release}
Provides:      golang(%{import_path}/lmodstring) = %{version}-%{release}
Provides:      golang(%{import_path}/lmodtable) = %{version}-%{release}
Provides:      golang(%{import_path}/luautil) = %{version}-%{release}
Provides:      golang(%{import_path}/supermeta) = %{version}-%{release}
Provides:      golang(%{import_path}/testhelp) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Group: Development/Other
Summary:         Unit tests for %{name} package

# test subpackage tests code from devel subpackage

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{version}

# This test requires gopher-lua; I'm uninterested in packaging that at present.
# (It does benchmarking).
rm fib_test.go

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
echo "%%dir %%{go_path}/src/%%{import_path}/vendor" >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
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
export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%endif

%gotest %{import_path}
%gotest %{import_path}/supermeta
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE
%doc README.md
%endif

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_1
- new version

