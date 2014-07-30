# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jaxws-jboss-httpserver-httpspi
%define version 1.0.1
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jaxws-jboss-httpserver-httpspi
Version:          1.0.1
Release:          alt1_4jpp7
Summary:          JBoss httpserver to JAXWS 2.2 HTTP SPI bridge
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/projects/jaxws-jboss-httpserver-httpspi/tags/jaxws-jboss-httpserver-httpspi-1.0.1.GA/
# tar cafJ jaxws-jboss-httpserver-httpspi-1.0.1.GA.tar.xz jaxws-jboss-httpserver-httpspi-1.0.1.GA
Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-dependency-plugin
BuildRequires:    cxf-rt
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jboss-jaxws-2.2-api
BuildRequires:    jboss-httpserver
BuildRequires:    junit

Requires:         jpackage-utils
Requires:         cxf-rt
Requires:         jboss-servlet-3.0-api
Requires:         jboss-jaxws-2.2-api
Requires:         jboss-httpserver
Source44: import.info

%description
This package contains the JBoss httpserver to JAXWS 2.2 HTTP SPI bridge.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Remove the parent as it is not packaged
%pom_xpath_remove "pom:parent"

%build
# Some Apache CXF modules are still not avialable
mvn-rpmbuild -Dmaven.test.skip=true package javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4jpp7
- new release

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2jpp7
- new version

