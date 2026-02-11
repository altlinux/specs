Name:		voms-api-java
Version:	3.3.5
Release:	alt1
Summary:	Virtual Organization Membership Service Java API

License:	Apache-2.0
Group:	    Development/Other
URL:		https://wiki.italiangrid.it/VOMS
Source0:	https://github.com/italiangrid/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires(pre):	 rpm-macros-java
BuildRequires:	maven-local
BuildRequires:	/proc rpm-build-java
BuildRequires:	java-17-openjdk-devel

BuildRequires:	mvn(eu.eu-emi.security:canl)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.mockito:mockito-core)
Requires:	mvn(eu.eu-emi.security:canl) >= 2.8.3
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

# F33+ and EPEL8+ doesn't use the maven-javadoc-plugin to generate javadoc
# Remove maven-javadoc-plugin configuration to avoid build failure
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Do not enforce requirements
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Jan 15 2026 Anton Meleshnikov <alton@altlinux.org> 3.3.5-alt1
- new version

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

