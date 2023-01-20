Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
%define fedora 34
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		voms-api-java
Version:	3.3.2
Release:	alt2_6jpp11
Summary:	Virtual Organization Membership Service Java API

License:	ASL 2.0
URL:		https://wiki.italiangrid.it/VOMS
Source0:	https://github.com/italiangrid/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(eu.eu-emi.security:canl) >= 2.6
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.hamcrest:hamcrest-library)
BuildRequires:	mvn(org.mockito:mockito-core)
Requires:	mvn(eu.eu-emi.security:canl) >= 2.6
Source44: import.info

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides a java client API for VOMS.

%package javadoc
Group: Development/Java
Summary:	Virtual Organization Membership Service Java API Documentation
BuildArch: noarch

%description javadoc
Virtual Organization Membership Service (VOMS) Java API Documentation.

%prep
%setup -q

# Remove unused dependency
%pom_remove_dep net.jcip:jcip-annotations

# Use default location for javadoc output
%pom_xpath_remove "//pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:outputDirectory"
%pom_xpath_remove "//pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:reportOutputDirectory"

%if %{?fedora}%{!?fedora:0} >= 33 || %{?rhel}%{!?rhel:0} >= 8
# F33+ and EPEL8+ doesn't use the maven-javadoc-plugin to generate javadoc
# Remove maven-javadoc-plugin configuration to avoid build failure
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%endif

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Cobertura no longer in Fedora due to licensing issues
%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin

# Remove license plugin
%pom_remove_plugin com.mycila.maven-license-plugin:maven-license-plugin

# These tests fail due to changes to the ASN1TaggedObject class in
# bouncycastle 1.70 - remove until fixed
# https://github.com/italiangrid/voms-api-java/issues/28
rm src/test/java/org/italiangrid/voms/test/ac/TestACGeneration.java
rm src/test/java/org/italiangrid/voms/test/ac/TestFakeVOMSACService.java

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc AUTHORS README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Fri Jan 20 2023 Igor Vlasenko <viy@altlinux.org> 3.3.2-alt2_6jpp11
- fixed build

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 3.3.2-alt1_6jpp11
- update

* Wed Aug 18 2021 Igor Vlasenko <viy@altlinux.org> 3.3.2-alt1_3jpp11
- rebuild with new bouncycastle

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 3.3.2-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.3.0-alt1_11jpp11
- update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 3.3.0-alt1_7jpp11
- update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_4jpp8
- new version

* Wed May 16 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_1jpp8
- java fc28 update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_1jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.5-alt1_3jpp8
- new version

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_4jpp7
- new release

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_2jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1_2jpp7
- new version

