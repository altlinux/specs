# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name picketbox
%define version 4.0.6
%global namedreltag .final
%global namedversion %{version}%{?namedreltag}

Name:             picketbox
Version:          4.0.6
Release:          alt2_9jpp7
Summary:          Security framework for Java Applications
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/picketbox

# svn export http://anonsvn.jboss.org/repos/picketbox/tags/4.0.6.final/ picketbox-4.0.6.final
# tar cafJ picketbox-4.0.6.final.tar.xz picketbox-4.0.6.final
Source0:          %{name}-%{namedversion}.tar.xz
Source1:          %{name}-%{namedversion}-pom.xml

Patch0:           %{name}-%{namedversion}-assembly.patch
Patch1:           %{name}-%{namedversion}-pom.patch
# REMOVE THIS! (at some point)
Patch2:           %{name}-%{namedversion}-ugly.patch

BuildArch:        noarch

BuildRequires:    concurrent
BuildRequires:    hibernate-jpa-2.0-api >= 1.0.1-5
BuildRequires:    hsqldb
BuildRequires:    infinispan
BuildRequires:    javacc-maven-plugin
BuildRequires:    jboss-connector-1.6-api
BuildRequires:    jboss-jacc-1.4-api
BuildRequires:    jboss-jaspi-1.0-api
BuildRequires:    jboss-parent
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-injection-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    picketbox-commons
BuildRequires:    picketbox-xacml
BuildRequires:    rhq-plugin-annotations

Requires:         concurrent
Requires:         hibernate-jpa-2.0-api >= 1.0.1-5
Requires:         hsqldb
Requires:         infinispan
Requires:         jboss-connector-1.6-api
Requires:         jboss-jacc-1.4-api
Requires:         jboss-jaspi-1.0-api
Requires:         jboss-servlet-3.0-api
Requires:         jboss-transaction-1.1-api
Requires:         jpackage-utils
Requires:         picketbox
Requires:         picketbox-xacml
Requires:         rhq-plugin-annotations
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
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# Because of ugly patch
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644  assembly/target/picketbox-%{namedversion}-bin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar
install -pm 644  picketbox/target/picketbox-bare-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/bare.jar

install -pm 644  security-spi/acl/target/acl-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/security-spi-acl.jar
install -pm 644  security-spi/identity/target/identity-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/security-spi-identity.jar
install -pm 644  security-spi/authorization/target/authorization-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/security-spi-authorization.jar
install -pm 644  security-spi/spi/target/picketbox-spi-bare-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/spi-bare.jar
install -pm 644  picketbox-infinispan/target/picketbox-infinispan-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/infinispan.jar

install -pm 644  security-jboss-sx/acl/target/picketbox-acl-impl-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/acl-impl.jar
install -pm 644  security-jboss-sx/identity/target/picketbox-identity-impl-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/identity-impl.jar
install -pm 644  security-jboss-sx/jbosssx-client/target/jbosssx-client-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbosssx-client.jar
install -pm 644  security-jboss-sx/jbosssx/target/jbosssx-bare.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbosssx-bare.jar

# POM
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
install -pm 644 parent/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-parent.pom
install -pm 644 security-spi/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-security-spi-parent.pom
install -pm 644 security-spi/parent/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-security-spi-parent-parent.pom
install -pm 644 security-jboss-sx/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-impl-parent.pom
install -pm 644 security-jboss-sx/parent/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-impl-parent-parent.pom
install -pm 644 picketbox-infinispan/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-infinispan.pom

install -pm 644 picketbox/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-bare.pom
install -pm 644 security-spi/acl/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-security-spi-acl.pom
install -pm 644 security-spi/identity/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-security-spi-identity.pom
install -pm 644 security-spi/authorization/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-security-spi-authorization.pom
install -pm 644 security-spi/spi/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-spi-bare.pom
install -pm 644 security-jboss-sx/acl/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-acl-impl.pom
install -pm 644 security-jboss-sx/identity/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-identity-impl.pom
install -pm 644 security-jboss-sx/jbosssx/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-jbosssx-bare.pom
install -pm 644 security-jboss-sx/jbosssx-client/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-jbosssx-client.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar
%add_maven_depmap JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-security-spi-parent.pom
%add_maven_depmap JPP.%{name}-security-spi-parent-parent.pom
%add_maven_depmap JPP.%{name}-impl-parent.pom
%add_maven_depmap JPP.%{name}-impl-parent-parent.pom

%add_maven_depmap JPP.%{name}-bare.pom %{name}/bare.jar
%add_maven_depmap JPP.%{name}-security-spi-acl.pom %{name}/security-spi-acl.jar
%add_maven_depmap JPP.%{name}-security-spi-identity.pom %{name}/security-spi-identity.jar
%add_maven_depmap JPP.%{name}-security-spi-authorization.pom %{name}/security-spi-authorization.jar
%add_maven_depmap JPP.%{name}-spi-bare.pom %{name}/spi-bare.jar
%add_maven_depmap JPP.%{name}-acl-impl.pom %{name}/acl-impl.jar
%add_maven_depmap JPP.%{name}-identity-impl.pom %{name}/identity-impl.jar
%add_maven_depmap JPP.%{name}-jbosssx-bare.pom %{name}/jbosssx-bare.jar
%add_maven_depmap JPP.%{name}-jbosssx-client.pom %{name}/jbosssx-client.jar
%add_maven_depmap JPP.%{name}-infinispan.pom %{name}/infinispan.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.6-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.6-alt1_7jpp7
- new version

