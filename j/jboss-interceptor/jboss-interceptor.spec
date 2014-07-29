# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-interceptor
%define version 2.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-interceptor
Version:          2.0.0
Release:          alt2_6jpp7
Summary:          JBoss EJB Interceptor Library
Group:            Development/Java
License:          ASL 2.0 and LGPLv2.1+
URL:              http://www.jboss.org

# git clone git://github.com/jbossinterceptors/jbossinterceptors.git
# cd jbossinterceptors/ && git archive --format=tar --prefix=jboss-interceptor-2.0.0.Final/ 2.0.0.Final | xz > jboss-interceptor-2.0.0.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

# Fixed jboss-ejb3-api gid:aid
Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    maven-ejb-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    apiviz >= 1.3.1-6
BuildRequires:    jboss-interceptors-1.1-api
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    guava
BuildRequires:    javassist
BuildRequires:    slf4j

Requires:         jpackage-utils
Requires:         jboss-interceptors-1.1-api
Requires:         guava
Requires:         javassist
Requires:         slf4j
Source44: import.info

%description
JBoss EJB 3.1 Common Interceptor Library

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

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 jboss-interceptor-core/target/jboss-interceptor-core.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-core.jar
install -pm 644 jboss-interceptor-spi/target/jboss-interceptor-spi.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-spi.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-parent.pom
install -pm 644 jboss-interceptor-core/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-core.pom
install -pm 644 jboss-interceptor-spi/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-spi.pom

# DEPMAP
%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}-core.pom %{name}-core.jar
%add_maven_depmap JPP-%{name}-spi.pom %{name}-spi.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_4jpp7
- new version

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

