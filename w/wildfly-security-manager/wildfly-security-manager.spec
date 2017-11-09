Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.1.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             wildfly-security-manager
Version:          1.1.2
Release:          alt1_3jpp8
Summary:          WildFly Security Manager
# Not available license file https://github.com/wildfly-security/security-manager/issues/9
# ASL 2.0: ./src/main/java/org/wildfly/security/ParametricPrivilegedExceptionAction.java
# ./src/main/java/org/wildfly/security/manager/StackInspector.java
# ./src/main/java/org/wildfly/security/ParametricPrivilegedAction.java
# ./src/test/java/org/wildfly/security/manager/TestStackInspector.java
License:          ASL 2.0 and LGPLv2+
Url:              https://github.com/wildfly-security/security-manager/
Source0:          https://github.com/wildfly-security/security-manager/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(org.jboss.modules:jboss-modules)
BuildRequires:    mvn(org.kohsuke.metainf-services:metainf-services)

BuildArch:        noarch
Source44: import.info

%description
The Security Manager for WildFly Application Server.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n security-manager-%{namedversion}

%pom_remove_plugin "org.jboss.seven2six:seven2six"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- java 8 mass update

