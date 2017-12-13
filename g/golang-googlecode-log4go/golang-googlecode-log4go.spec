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

%global provider        google
%global provider_sub    code
%global provider_tld    com
%global repo            log4go
%global provider_prefix %{provider_sub}.%{provider}.%{provider_tld}/p/%{repo}
%global import_path     %{provider_prefix}
%global rev             c3294304d93f48a37d3bed1d382882a9c2989f99
%global shortrev        %(r=%{rev}; echo ${r:0:12})

Name:           golang-%{provider}%{provider_sub}-%{repo}
Version:        0
Release:        alt1_0.9.hg%{shortrev}
Summary:        Logging package similar to log4j for the Go programming language
License:        BSD
URL:            http://%{provider_prefix}
Source0:        https://%{repo}.%{provider}%{provider_sub}.%{provider_tld}/archive/%{rev}.tar.gz

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

The goal of log4go is to be a robust, configurable, powerful logging package
to empower Go developers to debug their programs more effectively on the fly
and diagnose problems in the field without hampering their effectiveness
during development or hampering the performance of their applications.

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:        Logging package similar to log4j for the Go programming language
BuildArch:      noarch

%if 0%{?with_check}
%endif

Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

The goal of log4go is to be a robust, configurable, powerful logging package
to empower Go developers to debug their programs more effectively on the fly
and diagnose problems in the field without hampering their effectiveness
during development or hampering the performance of their applications. 

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
%setup -n %{repo}-%{shortrev} -q

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
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

export GOPATH=%{go_path}:%{buildroot}/%{go_path}
gotest %{import_path}
%endif

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc README
%{go_path}/src/%{import_path}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%doc LICENSE
%doc README
%endif

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.9.hgc3294304d93f
- new version

