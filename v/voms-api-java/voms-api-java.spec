Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		voms-api-java
Version:	3.3.0
Release:	alt1_4jpp8
Summary:	Virtual Organization Membership Service Java API

License:	ASL 2.0
URL:		https://wiki.italiangrid.it/VOMS
Source0:	https://github.com/italiangrid/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
#		Disable tests using non-local network interface
Patch0:		%{name}-no-local.patch
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(eu.eu-emi.security:canl) >= 2.5
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.hamcrest:hamcrest-library)
BuildRequires:	mvn(org.mockito:mockito-core)
BuildRequires:	mvn(net.jcip:jcip-annotations)
Requires:	mvn(eu.eu-emi.security:canl) >= 2.5
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
%patch0 -p1

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Cobertura no longer in Fedora due to licensing issues
%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin

# Remove license plugin
%pom_remove_plugin com.mycila.maven-license-plugin:maven-license-plugin

%build
%mvn_build

%install
%mvn_install -J target/site/javadoc/apidocs

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc AUTHORS README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
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

