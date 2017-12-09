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
%global project         syndtr
%global repo            gosnappy
# https://github.com/syndtr/gosnappy
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          156a073208e131d7d2e212cb749feae7c339e846
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global g_commit          723cc1e459b8eea2dea4583200fd60757d40097a
%global g_shortcommit     %(c=%{g_commit}; echo ${c:0:7})
%global g_provider_prefix github.com/golang/snappy
%global g_import_path     %{g_provider_prefix}
%global g_name            golang-github-golang-snappy

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.11.git%{shortcommit}
Summary:        Implementation of the Snappy compression format for Go
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source1:        https://%{g_provider_prefix}/archive/%{g_commit}/snappy-%{g_shortcommit}.tar.gz

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

Provides:      golang(%{import_path}/snappy) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package -n %{g_name}-devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
%endif

Provides:      golang(%{g_import_path}) = %{version}-%{release}

%description -n %{g_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{g_import_path} prefix.

%endif

%if 0%{?with_unit_test}
%package -n %{g_name}-unit-test
Group: Development/Other
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage

%description -n %{g_name}-unit-test
%{summary}

This package contains unit tests for project
providing packages with %{g_import_path} prefix.
%endif

%prep
%setup -q -n snappy-%{g_commit} -T -b 1
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
install -d -p %{buildroot}/%{go_path}/src/%{g_import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
echo "%%dir %%{go_path}/src/%%{g_import_path}/." >> g_devel.file-list

# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{go_path}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
done

pushd ../snappy-%{g_commit}

# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{go_path}/src/%%{g_import_path}/$(dirname $file)" >> ../%{repo}-%{commit}/g_devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{g_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{g_import_path}/$file
    echo "%%{go_path}/src/%%{g_import_path}/$file" >> ../%{repo}-%{commit}/g_devel.file-list
done

popd
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{go_path}/src/%{g_import_path}/
# find all *_test.go files and generate unit-test.file-list

pushd ../snappy-%{g_commit}

for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{go_path}/src/%%{g_import_path}/$(dirname $file)" >> ../%{repo}-%{commit}/g_devel.file-list
    install -d -p %{buildroot}/%{go_path}/src/%{g_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{g_import_path}/$file
    echo "%%{go_path}/src/%%{g_import_path}/$file" >> ../%{repo}-%{commit}/unit-test.file-list
done
popd
%endif

%if 0%{?with_devel}
sort -u -o g_devel.file-list g_devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%else
export GOPATH=%{buildroot}/%{go_path}:$(pwd)/Godeps/_workspace:%{go_path}:/usr/include:/usr/lib64
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{g_import_path}
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc README AUTHORS CONTRIBUTORS
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}

%files -n %{g_name}-devel -f g_devel.file-list
%doc LICENSE
%doc README AUTHORS CONTRIBUTORS
%dir %{go_path}/src/github.com/golang
%endif

%if 0%{?with_unit_test}
%files -n %{g_name}-unit-test -f unit-test.file-list
%doc LICENSE
%doc README AUTHORS CONTRIBUTORS
%endif

%changelog
* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.11.git156a073
- new version

