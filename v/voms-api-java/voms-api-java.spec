Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		voms-api-java
Version:	3.2.0
Release:	alt1_4jpp8
Summary:	Virtual Organization Membership Service Java API

License:	ASL 2.0
URL:		https://wiki.italiangrid.it/VOMS
Source0:	https://github.com/italiangrid/%{name}/archive/v%{version}.tar.gz
#		Disable tests using non-local network interface
Patch0:		%{name}-no-local.patch
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(eu.eu-emi.security:canl)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.mockito:mockito-core)
BuildRequires:	mvn(com.mycila.maven-license-plugin:maven-license-plugin)
BuildRequires:	mvn(net.jcip:jcip-annotations)
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

%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin

%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:groupId='com.mycila.maven-license-plugin']/pom:configuration/pom:excludes" "<exclude>.xmvn/**</exclude>"
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:groupId='com.mycila.maven-license-plugin']/pom:configuration/pom:strictCheck"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
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

