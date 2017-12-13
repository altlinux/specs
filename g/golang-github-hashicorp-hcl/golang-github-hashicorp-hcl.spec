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
%global project         hashicorp
%global repo            hcl
# https://github.com/hashicorp/hcl
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          ef8133da8cda503718a74741312bf50821e6de79
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.13.git%{shortcommit}
Summary:        HCL is a configuration language
License:        MPLv2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

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
Provides:      golang(%{import_path}/hcl/ast) = %{version}-%{release}
Provides:      golang(%{import_path}/hcl/fmtcmd) = %{version}-%{release}
Provides:      golang(%{import_path}/hcl/parser) = %{version}-%{release}
Provides:      golang(%{import_path}/hcl/printer) = %{version}-%{release}
Provides:      golang(%{import_path}/hcl/scanner) = %{version}-%{release}
Provides:      golang(%{import_path}/hcl/strconv) = %{version}-%{release}
Provides:      golang(%{import_path}/hcl/token) = %{version}-%{release}
Provides:      golang(%{import_path}/json/parser) = %{version}-%{release}
Provides:      golang(%{import_path}/json/scanner) = %{version}-%{release}
Provides:      golang(%{import_path}/json/token) = %{version}-%{release}
Provides:      golang(%{import_path}/testhelper) = %{version}-%{release}

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

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
BuildRequires: golang(github.com/davecgh/go-spew/spew)
%endif

# test subpackage tests code from devel subpackage
Requires: golang(github.com/davecgh/go-spew/spew)

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
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
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
done
sort -u devel.file-list.dir >> devel.file-list
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
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
sort -u unit-test.file-list.dir >> unit-test.file-list
echo "%%{go_path}/src/%%{import_path}/test-fixtures" >> unit-test.file-list
cp -r ./test-fixtures %{buildroot}/%{go_path}/src/%{import_path}/.

echo "%%{go_path}/src/%%{import_path}/hcl/parser/test-fixtures" >> unit-test.file-list
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/hcl/parser
cp -r ./hcl/parser/test-fixtures %{buildroot}/%{go_path}/src/%{import_path}/hcl/parser/.
echo "%%{go_path}/src/%%{import_path}/hcl/printer/testdata" >> unit-test.file-list
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/hcl/printer
cp -r ./hcl/printer/testdata %{buildroot}/%{go_path}/src/%{import_path}/hcl/printer/.

echo "%%{go_path}/src/%%{import_path}/json/parser/test-fixtures" >> unit-test.file-list
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/json/parser
cp -r ./json/parser/test-fixtures %{buildroot}/%{go_path}/src/%{import_path}/json/parser/.

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
%gotest %{import_path}/hcl/ast
%gotest %{import_path}/hcl/parser
%gotest %{import_path}/hcl/printer
%gotest %{import_path}/hcl/scanner
%gotest %{import_path}/hcl/strconv
%gotest %{import_path}/hcl/token
%gotest %{import_path}/json/parser
%gotest %{import_path}/json/scanner
%gotest %{import_path}/json/token
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
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc README.md
%endif

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.13.gitef8133d
- new version

