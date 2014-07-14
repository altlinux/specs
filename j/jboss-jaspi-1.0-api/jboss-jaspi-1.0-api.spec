Provides: jaspi_1_0_api
Epoch: 1
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaspi-1.0-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:		jboss-jaspi-1.0-api
Version:	1.0.1
Release:	alt2_3jpp7
Summary:	JBoss Java Authentication SPI for Containers 1.0 API
Group:		Development/Java
License:	CDDL or GPLv2 with exceptions
URL:		http://www.jboss.org

# git clone git://github.com/jboss/jboss-jaspi-api_spec.git
# cd jboss-jaspi-api_spec/ && git archive --format=tar --prefix=jboss-jaspi-1.0-api/ jboss-jaspi-api_1.0_spec-1.0.1.Final | xz > jboss-jaspi-1.0-api-1.0.1.Final.tar.xz
Source0:	%{name}-%{namedversion}.tar.xz

BuildRequires:	jpackage-utils
BuildRequires:	maven
BuildRequires:	jboss-logging
BuildRequires:	maven-compiler-plugin
BuildRequires:	maven-enforcer-plugin
BuildRequires:	maven-install-plugin
BuildRequires:	maven-jar-plugin
BuildRequires:	maven-javadoc-plugin

Requires:	jpackage-utils

BuildArch:	noarch
Source44: import.info

%description
The Java Authentication SPI for Containers 1.0 API classes

%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jaspi-1.0-api

# Fixing JDK7 ASCII issues
files='
src/main/java/javax/security/auth/message/callback/PasswordValidationCallback.java
src/main/java/javax/security/auth/message/config/AuthConfigFactory.java
src/main/java/javax/security/auth/message/config/AuthConfigProvider.java
src/main/java/javax/security/auth/message/config/ClientAuthConfig.java
src/main/java/javax/security/auth/message/config/ServerAuthConfig.java
src/main/java/javax/security/auth/message/module/ClientAuthModule.java
src/main/java/javax/security/auth/message/module/ServerAuthModule.java
'

for f in ${files}; do
  native2ascii -encoding UTF8 ${f} ${f}
done

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-jaspi-api_1.0_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE README

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE README

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_3jpp7
- new version

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt4_2jpp6
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt3_2jpp6
- build w/o jms-1.1-api

* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt2_2jpp6
- built with patched assembly plugin

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt1_2jpp6
- new version

