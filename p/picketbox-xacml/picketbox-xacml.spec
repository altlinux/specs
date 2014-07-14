BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name picketbox-xacml
%define version 2.0.7
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             picketbox-xacml
Version:          2.0.7
Release:          alt2_3jpp7
Summary:          JBoss XACML
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/picketbox

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/security/security-xacml/tags/2.0.7.Final/ picketbox-xacml-2.0.7.Final
# tar cafJ picketbox-xacml-2.0.7.Final.tar.xz picketbox-xacml-2.0.7.Final
Source0:          %{name}-%{namedversion}.tar.xz
Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    junit4
BuildRequires:    picketbox-commons

Requires:         picketbox-commons
Requires:         jpackage-utils
Source44: import.info

%description
JBoss XACML Library

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

rm .classpath

%build
# Disabled tests because OpenDS is needed
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 jboss-xacml/target/jboss-xacml-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -pm 644 jboss-sunxacml/target/jboss-sunxacml-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/picketbox-sunxacml.jar

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 parent/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-parent.pom
install -pm 644 jboss-xacml/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 jboss-sunxacml/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-picketbox-sunxacml.pom
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-main.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.jboss.security:jbossxacml"
%add_maven_depmap JPP-picketbox-sunxacml.pom picketbox-sunxacml.jar
%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}-main.pom

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt1_3jpp7
- new version

