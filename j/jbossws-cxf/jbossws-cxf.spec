BuildRequires: maven-antrun-plugin
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-cxf
%define version 4.0.2
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-cxf
Version:          4.0.2
Release:          alt3_2jpp7
Summary:          JBoss Web Services CXF stack
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws
Source0:          http://download.jboss.org/jbossws/jbossws-cxf-%{namedversion}-src.zip


Patch0:           0001-Remove-parent.patch
Patch1:           0002-Enable-only-resources-module.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin

Requires:         jpackage-utils
Source44: import.info

%description
JBoss Web Services CXF integration stack

#%package javadoc
#Summary:          Javadocs for %{name}
#Group:            Documentation
#Requires:         jpackage-utils

#%description javadoc
#This package contains the API documentation for %{name}.

%prep
%setup -q -n jbossws-cxf-src-dist

%patch0 -p1
%patch1 -p1

%build
mvn-rpmbuild -Dno-testsuite -Pjboss711 install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 modules/resources/target/jbossws-cxf-resources-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-resources.jar
install -pm 644 modules/resources/target/jbossws-cxf-resources-%{namedversion}-jboss711.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-resources-jboss711.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
install -pm 644 modules/resources/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-resources.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}-resources.pom %{name}/%{name}-resources.jar

# APIDOCS
#cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

#%files javadoc
#%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt3_2jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt2_2jpp7
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_2jpp7
- new version

