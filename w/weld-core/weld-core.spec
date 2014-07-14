BuildRequires: maven-enforcer-plugin geronimo-jta geronimo-jpa

BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name weld-core
%define version 1.1.5
%global namedreltag .AS71.Final
%global namedversion %{version}%{?namedreltag}

Name: weld-core
Version: 1.1.5
Release: alt2_4.AS71.Finaljpp7
Summary: Reference Implementation for JSR-299: Contexts and Dependency Injection (CDI)
Group: Development/Java
License: ASL 2.0 and LGPLv2+ and (CDDL or GPLv2 with exceptions)
URL: http://seamframework.org/Weld

# git clone git://github.com/weld/core.git weld-core
# cd weld-core && git checkout 1.1.5.AS71.Final && git checkout-index -f -a --prefix=weld-core-1.1.5.AS71.Final/
# find weld-core-1.1.5.AS71.Final -name '*.jar' -delete
# tar -cJf weld-core-1.1.5.AS71.Final-CLEAN.tar.xz weld-core-1.1.5.AS71.Final
Source0: %{name}-%{namedversion}-CLEAN.tar.xz

# Removing chestyle:
Patch0: %{name}-remove-checkstyle.patch

# Support for JDK7:
Patch1: %{name}-fix-compilation-problem-on-jdk7.patch

# Fix issue with bridge methods:
Patch2: %{name}-fix-issue-with-bridge-methods.patch

BuildArch: noarch

BuildRequires: findbugs
BuildRequires: jpackage-utils
BuildRequires: jboss-interceptor
BuildRequires: jboss-jsf-2.1-api
BuildRequires: jboss-jsp-2.2-api
BuildRequires: jboss-servlet-3.0-api
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: weld-api
BuildRequires: weld-parent

Requires: jpackage-utils
Requires: jboss-interceptor
Requires: jboss-jsf-2.1-api
Requires: jboss-jsp-2.2-api
Requires: jboss-servlet-3.0-api
Requires: weld-api
Source44: import.info


%description
Weld is the reference implementation (RI) for JSR-299: Java Contexts and
Dependency Injection for the Java EE platform (CDI). CDI is the Java standard
for dependency injection and contextual lifecycle management, and integrates
cleanly with the Java EE platform. Any Java EE 6-compliant application server
provides support for JSR-299 (even the web profile). 


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 impl/target/weld-core-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-parent.pom
install -pm 644 impl/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Dependencies map:
%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*


%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt2_4.AS71.Finaljpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1_4.AS71.Finaljpp7
- new version

