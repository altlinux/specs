Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package   %{nil}

%global provider        github
%global provider_tld    com
%global project         bgentry
%global repo            go-netrc
# https://github.com/bgentry/go-netrc
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          9fd32a8b3d3d3f9d43c341bfe098430e07609480
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global commitdate      20140422

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        alt1_0.3.%{commitdate}git%{shortcommit}
Summary:        A netrc file parser for the Go programming language
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
A Golang package for reading and writing netrc files. This package can parse
netrc files, make changes to them, and then serialize them back to netrc
format, while preserving any whitespace that was present in the source file.

%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{import_path}/netrc) = %{version}-%{release}

%description devel
A Golang package for reading and writing netrc files. This package can parse
netrc files, make changes to them, and then serialize them back to netrc
format, while preserving any whitespace that was present in the source file.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package unit-test-devel
Group: Development/Other
Summary:         Unit tests for %{name} package

# test subpackage tests code from devel subpackage

%description unit-test-devel
A Golang package for reading and writing netrc files. This package can parse
netrc files, make changes to them, and then serialize them back to netrc
format, while preserving any whitespace that was present in the source file.

This package contains unit tests for project
providing packages with %{import_path} prefix.

%prep
%setup -q -n %{repo}-%{commit}


%build

%install
install -d -p %{buildroot}%{go_path}/src/%{import_path}/netrc/
install -Dpm0644 netrc/*.go %{buildroot}%{go_path}/src/%{import_path}/netrc/
install -d -p %{buildroot}%{go_path}/src/%{import_path}/netrc/examples/
install -Dpm0644 netrc/examples/*.netrc %{buildroot}%{go_path}/src/%{import_path}/netrc/examples/

%check
export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%gotest %{import_path}/netrc

%files devel
%doc LICENSE
%doc README.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%dir %{go_path}/src/%{import_path}
%dir %{go_path}/src/%{import_path}/netrc
%{go_path}/src/%{import_path}/netrc/netrc.go

%files unit-test-devel
%doc LICENSE
%doc README.md
%{go_path}/src/%{import_path}/netrc/netrc_test.go
%{go_path}/src/%{import_path}/netrc/examples/

%changelog
* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.3.20140422git9fd32a8
- new version

