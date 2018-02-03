Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global   debug_package   %{nil}
%global   repo            dbus-factory
%global   import_path     dbus

Name:           golang-deepin-%{repo}
Version:        3.1.11
Release:        alt1_1
Summary:        Golang DBus factory for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/dbus-factory
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

BuildRequires:  golang(pkg.deepin.io/lib)
BuildRequires:  deepin-dbus-generator
BuildRequires:  jq libjq
BuildRequires:  libxml2 xml-utils
Provides:       deepin-go-%{repo} = %{version}-%{release}
Obsoletes:      deepin-go-%{repo} < %{version}-%{release}
Source44: import.info

%description
Golang DBus factory for Deepin Desktop Environment.

%package devel
Group: Development/Other
Summary:        %{summary}
BuildArch:      noarch

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%setup -q -n %{repo}-%{version}

%build
%make_build

%install
%makeinstall_std GOPATH=%{go_path}

%files devel
%doc README.md
%doc --no-dereference LICENSE
%{go_path}/src/dbus/

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.11-alt1_1
- update to new release by fcimport

* Sat Dec 16 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.10-alt1_1
- new version

