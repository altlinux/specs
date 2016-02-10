# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:		voms-api-java
Version:	3.0.5
Release:	alt1_3jpp8
Summary:	Virtual Organization Membership Service Java API

Group:		Development/Java
License:	ASL 2.0
URL:		https://wiki.italiangrid.it/VOMS
Source0:	https://github.com/italiangrid/%{name}/archive/v%{version}.tar.gz
#		Patch for bouncycastle 1.47+ (Fedora 21+, EPEL 7+)
Patch0:		%{name}-bc147.patch
#		Disable tests using non-local network interface
Patch1:		%{name}-no-local.patch
#		Fix javadoc warnings/errors
Patch2:		%{name}-javadoc.patch
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:	mvn(eu.eu-emi.security:canl)
BuildRequires:	mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.mockito:mockito-core)
%if %{?fedora}%{!?fedora:0}
#		Missing in EPEL
BuildRequires:	mvn(com.mycila.maven-license-plugin:maven-license-plugin)
BuildRequires:	mvn(net.jcip:jcip-annotations)
%endif
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
Summary:	Virtual Organization Membership Service Java API Documentation
Group:		Development/Java
BuildArch: noarch

%description javadoc
Virtual Organization Membership Service (VOMS) Java API Documentation.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId='bcmail']/pom:groupId" "org.bouncycastle"
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId='bcmail']/pom:artifactId" "bcpkix-jdk15on"

%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin

%if %{?fedora}%{!?fedora:0}
%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:groupId='com.mycila.maven-license-plugin']/pom:configuration/pom:excludes" "<exclude>.xmvn/**</exclude>"
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:groupId='com.mycila.maven-license-plugin']/pom:configuration/pom:strictCheck"
%else
# Missing in EPEL
%pom_remove_plugin com.mycila.maven-license-plugin:maven-license-plugin
%pom_remove_dep net.jcip:jcip-annotations
%endif

%build
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install -J target/site/javadoc/apidocs

%files -f .mfiles
%dir %{_javadir}/%{name}
%if %{?fedora}%{!?fedora:0} >= 21 || %{?rhel}%{!?rhel:0} >= 8
%dir %{_mavenpomdir}/%{name}
%endif
%doc AUTHORS README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.5-alt1_3jpp8
- new version

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_4jpp7
- new release

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_2jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1_2jpp7
- new version

