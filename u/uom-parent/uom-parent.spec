Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: uom-parent
Version: 1.0.3
Release: alt1_6jpp8
Summary: Units of Measurement Project Parent POM
License: BSD
URL: https://github.com/unitsofmeasurement/uom-parent
Source0: https://github.com/unitsofmeasurement/uom-parent/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: maven-local
BuildRequires: maven-install-plugin
Source44: import.info

%description
Main parent POM for all Units of Measurement Maven projects.

%prep
%setup -q -n %{name}-%{version}
%pom_remove_parent

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Tue Oct 08 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6jpp8
- new version

