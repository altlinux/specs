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
# both tests failing
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
%global project         go-yaml
%global repo            yaml
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          cd8b52f8269e0feb286dfeef29f8fe4d5b397e0b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global import_path     gopkg.in/v2/yaml
%global import_path_sec gopkg.in/yaml.v2

%global v1_commit          1b9791953ba4027efaeb728c7355e542a203be5e
%global v1_shortcommit     %(c=%{v1_commit}; echo ${c:0:7})
%global v1_import_path     gopkg.in/v1/yaml
%global v1_import_path_sec gopkg.in/yaml.v1

%global devel_main      golang-gopkg-yaml-devel-v2

Name:           golang-gopkg-yaml
Version:        1
Release:        alt1_19
Summary:        Enables Go programs to comfortably encode and decode YAML values
License:        LGPLv3 with exceptions
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/yaml-%{shortcommit}.tar.gz
Source1:        https://%{provider_prefix}/archive/%{v1_commit}/yaml-%{v1_commit}.tar.gz

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
Summary:        Enables Go programs to comfortably encode and decode YAML values
BuildArch:      noarch

%if 0%{?with_check}
%endif

Provides:       golang(%{v1_import_path}) = %{version}-%{release}
Provides:       golang(%{v1_import_path_sec}) = %{version}-%{release}

%description devel
The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within Canonical as part of the juju project, and
is based on a pure Go port of the well-known libyaml C library to parse and
generate YAML data quickly and reliably.

The yaml package is almost compatible with YAML 1.1, including support for
anchors, tags, etc. There are still a few missing bits, such as document
merging, base-60 floats (huh?), and multi-document unmarshalling. These
features are not hard to add, and will be introduced as necessary.

This package contains library source intended for
building other packages which use import path with
%{v1_import_path} prefix.

%package devel-v2
Group: Development/Other
Summary:        Enables Go programs to comfortably encode and decode YAML values
BuildArch:      noarch

%if 0%{?with_check}
%endif

Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path_sec}) = %{version}-%{release}

%description devel-v2
The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within Canonical as part of the juju project, and
is based on a pure Go port of the well-known libyaml C library to parse and
generate YAML data quickly and reliably.

The yaml package supports most of YAML 1.1 and 1.2,
including support for anchors, tags, map merging, etc.
Multi-document unmarshalling is not yet implemented, and base-60 floats
from YAML 1.1 are purposefully not supported since they're a poor design
 and are gone in YAML 1.2.

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
BuildRequires:  golang(gopkg.in/check.v1)
%endif

Requires:  golang(gopkg.in/check.v1)

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel-v2 = %{version}-%{release}

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n yaml-%{commit}
%setup -q -n yaml-%{v1_commit} -T -b 1

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path}/
install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path_sec}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{v1_import_path}/$file
    echo "%%{go_path}/src/%%{v1_import_path}/$file" >> v1_devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path_sec}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{v1_import_path_sec}/$file
    echo "%%{go_path}/src/%%{v1_import_path_sec}/$file" >> v1_devel.file-list
done
pushd ../yaml-%{commit}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
install -d -p %{buildroot}/%{go_path}/src/%{import_path_sec}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> ../yaml-%{v1_commit}/devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{import_path_sec}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path_sec}/$file
    echo "%%{go_path}/src/%%{import_path_sec}/$file" >> ../yaml-%{v1_commit}/devel.file-list
done
popd
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path}/
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{go_path}/src/%{v1_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{v1_import_path}/$file
    echo "%%{go_path}/src/%%{v1_import_path}/$file" >> unit-test.file-list
done
pushd ../yaml-%{commit}
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> ../yaml-%{v1_commit}/unit-test.file-list
done
popd
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
export GOPATH=%{buildroot}/%{go_path}:%{go_path}

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}
pushd ../yaml-%{v1_commit}
%gotest %{v1_import_path}
popd
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f v1_devel.file-list
%doc LICENSE LICENSE.libyaml
%doc README.md
%dir %{go_path}/src/gopkg.in/v1
%dir %{go_path}/src/%{v1_import_path}
%dir %{go_path}/src/%{v1_import_path_sec}

%files devel-v2 -f devel.file-list
%doc LICENSE LICENSE.libyaml
%doc README.md
%dir %{go_path}/src/gopkg.in/v2
%dir %{go_path}/src/%{import_path}
%dir %{go_path}/src/%{import_path_sec}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%doc LICENSE LICENSE.libyaml
%doc README.md
%endif

%changelog
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 1-alt1_19
- new version

