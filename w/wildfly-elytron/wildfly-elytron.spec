Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:          wildfly-elytron
Version:       1.0.2
Release:       alt1_4jpp8
Summary:       Security, Authentication, and Authorization SPIs for the WildFly project
# LGPLv2: ./src/main/java/org/wildfly/security/permission/PermissionActions.java
# most of the code in ./src/main/java/org/wildfly/security/manager/
License:       ASL 2.0 and LGPLv2+
URL:           http://wildfly.org/
Source0:       https://github.com/wildfly-security/wildfly-elytron/archive/%{namedversion}.tar.gz

BuildRequires: graphviz libgraphviz
BuildRequires: maven-local
BuildRequires: mvn(jdepend:jdepend)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.apiviz:apiviz)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires: mvn(org.jboss.logmanager:log4j-jboss-logmanager)
BuildRequires: mvn(org.jboss.modules:jboss-modules)
BuildRequires: mvn(org.jboss.slf4j:slf4j-jboss-logmanager)
BuildRequires: mvn(org.kohsuke.metainf-services:metainf-services)
BuildRequires: mvn(org.wildfly.common:wildfly-common)

BuildArch:     noarch
Source44: import.info

%description
WildFly Elytron is a new WildFly sub-project which
is completely replacing the combination of PicketBox and
JAAS as the WildFly client and server security mechanism.

An "elytron" (A.lA.A.A.A.trA.n, plural "elytra") is the hard,
protective casing over a wing of certain flying insects
(e.g. beetles).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Use not available org.wildfly.checkstyle:wildfly-checkstyle-config:1.0.3.Final
%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file org.wildfly.security:%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp8
- new version

