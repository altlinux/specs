Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name picketbox
%define version 4.9.6
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             picketbox
Version:          4.9.6
Release:          alt1_1jpp8
Summary:          Security framework for Java Applications
License:          LGPLv2+
URL:              http://picketbox.jboss.org

Source0:          https://github.com/picketbox/picketbox/archive/v%{namedversion}.tar.gz
Source1:          picketbox-%{namedversion}-pom.xml

# Until this is merged: https://github.com/picketbox/picketbox/pull/61
Patch0:           picketbox-assembly.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(javax.persistence:persistence-api)
BuildRequires:    mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:    mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:    mvn(org.hibernate:hibernate-core:3)
BuildRequires:    mvn(org.hibernate:hibernate-entitymanager:3)
BuildRequires:    mvn(org.infinispan:infinispan-core)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires:    mvn(org.jboss.modules:jboss-modules)
BuildRequires:    mvn(org.jboss.security:jbossxacml)
BuildRequires:    mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec)
BuildRequires:    mvn(org.jboss.spec.javax.security.auth.message:jboss-jaspi-api_1.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.security.jacc:jboss-jacc-api_1.5_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires:    mvn(org.picketbox:picketbox-commons)
Source44: import.info

%description
Java Security Framework that provides Java developers the following
functionality:

- Authentication Support
- Authorization Support
- Audit Support
- Security Mapping Support
- An Oasis XACML v2.0 compliant engine

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%patch0 -p1

# Change hibernate version
%pom_change_dep org.hibernate: ::3 security-jboss-sx/acl

%pom_remove_dep "org.hibernate:hibernate-annotations" security-jboss-sx/acl/pom.xml
%pom_change_dep :servlet-api org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec security-spi/spi
%pom_change_dep :servlet-api org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec:1.0.2.Final security-spi/parent

# Disable default-jar execution of maven-jar-plugin, which is causing
# problems with version 3.0.0 of the plugin.
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
<execution>
  <id>default-jar</id>
  <phase>skip</phase>
</execution>" security-jboss-sx/jbosssx-client

%build

%mvn_build -f

%install
%mvn_install

# Assembly jar
install -pm 644  assembly/target/picketbox-%{namedversion}-bin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 4.9.6-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.21-alt1_0.3.Beta1jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.21-alt1_0.2.Beta1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.18-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.6-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.6-alt1_7jpp7
- new version

