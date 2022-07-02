Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           options
Version:        1.7
Release:        alt1_3jpp11
Summary:        Library for managing sets of JVM properties to configure an app or library
License:        ASL 2.0
URL:            https://github.com/headius/%{name}
BuildArch:      noarch

Source0:        https://github.com/headius/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
Source44: import.info

%description
Provides a simple mechanism for defining JVM property-based
configuration for an application or library.

%{?javadoc_package}

%prep
%setup -q -n %{name}-%{name}-%{version}


# remove unnecessary dependency on parent POM
%pom_remove_parent

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files  -f .mfiles
%doc --no-dereference LICENSE
%doc README.md

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.7-alt1_3jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.2-alt1_18jpp11
- fc34 update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_14jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_12jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_10jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_9jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_8jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_6jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_5jpp8
- unbootsrap build

