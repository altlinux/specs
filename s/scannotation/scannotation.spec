BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name scannotation
%define version 1.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global alphatag r12

Name: scannotation
Version: 1.0.3
Release:  alt2_0.4.r12jpp7
Summary: A Java annotation scanner
Group: Development/Java
License: ASL 2.0
URL: http://scannotation.sourceforge.net

# How we created tarball:
# svn export -r 12  https://scannotation.svn.sourceforge.net/svnroot/scannotation scannotation-1.0.3.Final
# tar -caJf scannotation-1.0.3.Final.tar.xz scannotation-1.0.3.Final
Source0: %{name}-%{namedversion}.tar.xz
#Adding License file
Source1: License.txt

Patch0: %{name}-%{namedversion}-remove-dependencies.patch

BuildArch: noarch

BuildRequires: junit4
BuildRequires: javassist

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-provider-junit4

Requires: jpackage-utils
Requires: javassist
Source44: import.info

%description
Scannotation is a Java library that creates an annotation database 
from a set of .class files.This database is really just a set of maps that index
what annotations are used and what classes are using them. Why do you need this? 
What if you are an annotation framework like an EJB 3.0 container and you want 
to automatically scan your classpath for EJB annotations so that you know what 
to deploy? Scannotation gives you apis that allow you to find archives in your 
classpath or WAR (web application) that you want to scan, then automatically 
scans them without loading each and every class within those archives

%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1 -b .p0
cp -p %SOURCE1 .

%build
# building jar files using mvn
mvn-rpmbuild install javadoc:aggregate

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{name}/target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-all.pom
install -pm 644 %{name}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP - this is still ok, but we use different pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# all is the proper name in this case, this just to be there - not usable at all :)
%add_maven_depmap JPP-%{name}-all.pom

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc License.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_0.4.r12jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_0.4.r12jpp7
- new version

