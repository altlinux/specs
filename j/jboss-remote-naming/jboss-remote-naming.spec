# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-remote-naming
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-remote-naming
Version:       1.0.2
Release:       alt2_6jpp7
Summary:       JBoss Remote Naming
Group:         Development/Java
License:       LGPLv2+
URL:           http://www.jboss.org/

# git clone git://github.com/jbossas/jboss-remote-naming.git
# cd jboss-remote-naming/ && git archive --format=tar --prefix=jboss-remote-naming-1.0.2.Final/ 1.0.2.Final | xz > jboss-remote-naming-1.0.2.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: jpackage-utils
BuildRequires: jboss-parent
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-checkstyle-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-dependency-plugin
BuildRequires: maven-ear-plugin
BuildRequires: maven-eclipse-plugin
BuildRequires: jboss-logging
BuildRequires: jboss-logging-tools
BuildRequires: jboss-ejb-client
BuildRequires: jboss-logmanager
BuildRequires: jboss-marshalling
BuildRequires: jboss-remoting
BuildRequires: jboss-sasl
BuildRequires: xnio

Requires:      jpackage-utils
Requires:      jboss-logging
Requires:      jboss-logging-tools
Requires:      jboss-ejb-client
Requires:      jboss-logmanager
Requires:      jboss-marshalling
Requires:      jboss-remoting
Requires:      jboss-sasl
Requires:      xnio

BuildArch:     noarch
Source44: import.info

%description
Library for remote naming (JNDI) with JBoss AS

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
## Tests skipped because of the patch allowing to build against remoting 3.2.2.GA
## The tests were not updated though
#mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-remote-naming-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4jpp7
- new version

