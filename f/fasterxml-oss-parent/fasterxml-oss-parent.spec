Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname oss-parent

Name:          fasterxml-oss-parent
Version:       40
Release:       alt1_1jpp11
Summary:       FasterXML parent pom
License:       ASL 2.0

URL:           https://github.com/FasterXML/oss-parent
Source0:       %{url}/archive/%{srcname}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:     noarch
Source44: import.info

%description
FasterXML is the business behind the Woodstox streaming XML parser,
Jackson streaming JSON parser, the Aalto non-blocking XML parser, and
a growing family of utility libraries and extensions.

FasterXML offers consulting services for adoption, performance tuning,
and extension.

This package contains the parent pom file for FasterXML.com projects.

%prep
%setup -q -n %{srcname}-%{srcname}-%{version}

# Stuff unnecessary for RPM builds
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-scm-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :nexus-maven-plugin
%pom_remove_plugin :jdepend-maven-plugin
%pom_remove_plugin :taglist-maven-plugin
%pom_xpath_remove "pom:build/pom:extensions"

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.creole
%doc --no-dereference LICENSE NOTICE

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 40-alt1_1jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 38-alt1_2jpp8
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 34-alt1_1jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 26-alt1_7jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 26-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 26-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 26-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 26-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 24-alt1_3jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 18e-alt1_2jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 18e-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4-alt2_3jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 4-alt2_1jpp7
- fixed maven1 dependency

* Mon Dec 24 2012 Igor Vlasenko <viy@altlinux.ru> 4-alt1_1jpp7
- use /var/lock/serial

