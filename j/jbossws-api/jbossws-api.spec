# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-api
Version:          1.0.1
Release:          alt1_3jpp7
Summary:          JBossWS API
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/api/tags/jbossws-api-1.0.1.Final/ jbossws-api-1.0.1.Final
# tar cafJ jbossws-api-1.0.1.Final.tar.xz jbossws-api-1.0.1.Final
Source0:          jbossws-api-%{namedversion}.tar.xz

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
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    jbossws-parent

Requires:         jpackage-utils
Requires:         jboss-logging
Requires:         jboss-logging-tools
Source44: import.info

%description
JBoss WS public API

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbossws-api-%{namedversion}

%build
mvn-rpmbuild package javadoc:aggregate

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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1jpp7
- update

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

