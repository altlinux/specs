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
%global project         mitchellh
%global repo            mapstructure
# https://github.com/mitchellh/mapstructure
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          d0303fe809921458f417bcf828397a65db30a7e4
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

# temporary mitchellh-cli
%global t_repo            cli
%global t_import_path     %{provider}.%{provider_tld}/%{project}/%{t_repo}
%global t_commit          8102d0ed5ea2709ade1243798785888175f6e415
%global t_shortcommit     %(c=%{t_commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.17.git%{shortcommit}
Summary:        Go library for decoding generic map values into native Go structures
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{t_import_path}/archive/%{commit}/%{t_repo}-%{t_shortcommit}.tar.gz
Source1:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
mapstructure is a Go library for decoding generic map values to structures
and vice versa, while providing helpful error handling.

This library is most useful when decoding values from some data stream (JSON,
Gob, etc.) where you don't quite know the structure of the underlying data
until you read a part of it. You can therefore read a map[string]interface{}
and use this library to decode it into the proper underlying
native Go structure.

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
%endif

Provides:      golang(%{import_path}) = %{version}-%{release}

%description devel
mapstructure is a Go library for decoding generic map values to structures
and vice versa, while providing helpful error handling.

This library is most useful when decoding values from some data stream (JSON,
Gob, etc.) where you don't quite know the structure of the underlying data
until you read a part of it. You can therefore read a map[string]interface{}
and use this library to decode it into the proper underlying
native Go structure.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

# remove this package once golang-github-mitchellh-cli is built
%package -n golang-github-mitchellh-cli-devel-temporary
Group: Development/Other
Summary: golang-github-mitchellh-cli source codes temporary
BuildArch:     noarch
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
Requires:      golang(golang.org/x/crypto/ssh/terminal)


%description -n golang-github-mitchellh-cli-devel-temporary
Temporary devel subpackage for golang-github-mitchellh-cli source codes

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
%setup -q -n %{t_repo}-%{t_commit}
%setup -q -n %{repo}-%{commit} -T -b 1

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{go_path}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
done
pushd ../%{t_repo}-%{t_commit}
install -d -p %{buildroot}/%{go_path}/src/%{t_import_path}/
echo "%%dir %%{go_path}/src/%%{t_import_path}/." >> ../%{repo}-%{commit}/temp_devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{go_path}/src/%%{t_import_path}/$(dirname $file)" >> ../%{repo}-%{commit}/temp_devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{t_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{t_import_path}/$file
    echo "%%{go_path}/src/%%{t_import_path}/$file" >> ../%{repo}-%{commit}/temp_devel.file-list
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
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}

%files -n golang-github-mitchellh-cli-devel-temporary -f temp_devel.file-list
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
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.17.gitd0303fe
- new version

