Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-spi
%define version 2.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-spi
Version:          2.1.0
Release:          alt1_4jpp7
Summary:          JBossWS SPI
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/spi/tags/jbossws-spi-2.1.0.Final/ jbossws-spi-2.1.0.Final
# tar cafJ jbossws-spi-2.1.0.Final.tar.xz jbossws-spi-2.1.0.Final
Source0:          jbossws-spi-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    maven-war-plugin
BuildRequires:    maven-help-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    jboss-jms-1.1-api
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jbossws-api >= 1.0.1
BuildRequires:    jbossws-parent

Requires:         jpackage-utils
Requires:         jboss-jms-1.1-api
Requires:         jboss-logging
Requires:         jboss-logging-tools
Requires:         jboss-servlet-3.0-api
Requires:         jbossws-api >= 1.0.1
Source44: import.info

%description
JBoss WS SPI classes

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbossws-spi-%{namedversion}

%build
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_4jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_1jpp7
- update

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.3-alt1_3jpp7
- new version

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- new jpp release

