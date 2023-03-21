Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: hid4java
Version: 0.7.0
Release: alt1_3jpp11
Summary: Java wrapper for the hidapi library

License: MIT
URL: https://github.com/gary-rowe/hid4java
Source0: https://github.com/gary-rowe/%{name}/archive/%{name}-%{version}.tar.gz
Patch0: load-correct-library-name.patch
BuildArch: noarch

Requires: libhidapi

BuildRequires: maven-local
BuildRequires: mvn(net.java.dev.jna:jna)
BuildRequires: maven-surefire maven-surefire-provider-junit5
BuildRequires: junit5
BuildRequires: apiguardian
Source44: import.info


%description
hid4java supports USB HID devices through a common API. The API is very simple
but provides great flexibility such as support for feature reports and blocking
reads with timeouts. Attach/detach events are provided to allow applications to
respond instantly to device availability.


%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%patch0 -p1

find -name '*.so' -print -delete
find -name '*.dylib' -print -delete
find -name '*.dll' -print -delete

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc AUTHORS README.md
%doc --no-dereference LICENSE

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0.7.0-alt1_3jpp11
- new version

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 0.5.0-alt1_8jpp11
- new version

