Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-native
%define version 4.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-native
Version:          4.1.0
Release:          alt1_5jpp7
Summary:          JBossWS Native
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/stack/native/tags/jbossws-native-4.1.0.Final/ jbossws-native-4.1.0.Final
# tar cafJ jbossws-native-4.1.0.Final.tar.xz jbossws-native-4.1.0.Final
Source0:          jbossws-native-%{namedversion}.tar.xz

Patch0:           0001-xerces-2.11-support.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-jaxrpc-1.1-api
BuildRequires:    jboss-saaj-1.3-api
BuildRequires:    jboss-jaxb-2.2-api
BuildRequires:    jboss-common-core
BuildRequires:    jbossws-parent
BuildRequires:    jbossws-api
BuildRequires:    jbossws-spi
BuildRequires:    jbossws-common
BuildRequires:    jbossws-common-tools
BuildRequires:    jbossws-cxf
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    javassist
BuildRequires:    netty
BuildRequires:    wsdl4j
BuildRequires:    xerces-j2
BuildRequires:    jbossxb
BuildRequires:    junit

Requires:         jpackage-utils
Requires:         jboss-servlet-3.0-api
Requires:         jboss-ejb-3.1-api
Requires:         jboss-jaxrpc-1.1-api
Requires:         jboss-saaj-1.3-api
Requires:         jboss-jaxb-2.2-api
Requires:         jboss-common-core
Requires:         jbossws-api
Requires:         jbossws-spi
Requires:         jbossws-common
Requires:         jbossws-common-tools
Requires:         jbossws-cxf
Requires:         jboss-logging
Requires:         jboss-logging-tools
Requires:         javassist
Requires:         netty
Requires:         wsdl4j
Requires:         xerces-j2
Requires:         jbossxb
Source44: import.info

%description
JBoss WS Native classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbossws-native-%{namedversion}

%patch0 -p1

%build
mvn-rpmbuild \
  -Dno-testsuite \
  -Dproject.build.sourceEncoding=UTF-8 \
  package javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 modules/core/target/jbossws-native-core-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core.jar
install -pm 644 modules/services/target/jbossws-native-services-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-services.jar
install -pm 644 modules/resources/target/jbossws-native-resources-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-resources.jar
install -pm 644 modules/resources/target/jbossws-native-resources-%{namedversion}-jboss720.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-resources-jboss720.jar
install -pm 644 modules/resources/target/jbossws-native-resources-%{namedversion}-jboss712.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-resources-jboss712.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
install -pm 644 modules/core/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom
install -pm 644 modules/services/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-services.pom
install -pm 644 modules/resources/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-resources.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}-core.pom %{name}/%{name}-core.jar
%add_maven_depmap JPP.%{name}-%{name}-services.pom %{name}/%{name}-services.jar
%add_maven_depmap JPP.%{name}-%{name}-resources.pom %{name}/%{name}-resources.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.1.0-alt1_5jpp7
- new version

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt7_1jpp6
- fixed build with new glassfish-jaxb

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt6_1jpp6
- fixed build with glassfish-jaxws

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt5_1jpp6
- fixed components-info

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt4_1jpp6
- fixed jaxbintros version in repolib

* Mon Nov 01 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt3_1jpp6
- build with wstx 3.2.8

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt2_1jpp6
- rebuild with new xml-security

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt1_1jpp5
- full version

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.0.1-alt0.1jpp
- bootstrap for jbossas

