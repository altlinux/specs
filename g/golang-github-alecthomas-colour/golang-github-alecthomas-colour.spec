Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global   debug_package   %{nil}

%global   provider        github
%global   provider_tld    com
%global   project         alecthomas
%global   repo            colour
# https://github.com/alecthomas/colour
%global   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global   import_path     %{provider_prefix}
%global   commit          60882d9e27213e8552dcff6328914fe4c2b44bc9
%global   shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.1.git%{shortcommit}
Summary:        Quake-style colour formatting for Unix terminals
License:        MIT
URL:            https://%{provider_prefix}
Source0:        %{url}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}.

%package devel
Group: Development/Other
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  golang(github.com/mattn/go-isatty)
Requires:       golang(github.com/mattn/go-isatty)
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package unit-test-devel
Group: Development/Other
Summary:        Unit tests for %{name} package
BuildArch:      noarch
# test subpackage tests code from devel subpackage

%description unit-test-devel
%{summary}.

This package contains unit tests for project
providing packages with %{import_path} prefix.


%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
install -d %{buildroot}%{go_path}/src/%{import_path}/
install -m644 colour.go %{buildroot}%{go_path}/src/%{import_path}/
install -m644 colour_test.go %{buildroot}%{go_path}/src/%{import_path}/

%check
export GOPATH=%{buildroot}%{go_path}:%{go_path}

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}

%files devel
%doc README.md
%doc COPYING
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%{go_path}/src/%{import_path}/colour.go
%dir %{go_path}/src/%{import_path}

%files unit-test-devel
%{go_path}/src/%{import_path}/colour_test.go
%dir %{go_path}/src/%{import_path}

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.1.git60882d9
- new version

