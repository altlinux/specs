# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-ejb-client
%define version 1.0.5
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-ejb-client
Version:       1.0.5
Release:       alt2_5jpp7
Summary:       JBoss EJB client
Group:         Development/Java
License:       LGPLv2+
URL:           http://www.jboss.org/

# git clone git://github.com/jbossas/jboss-ejb-client.git
# cd jboss-ejb-client/ && git archive --format=tar --prefix=jboss-ejb-client-1.0.5.Final/ 1.0.5.Final | xz > jboss-ejb-client-1.0.5.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: jpackage-utils
BuildRequires: jboss-parent
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-injection-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-checkstyle-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-dependency-plugin
BuildRequires: maven-ear-plugin
BuildRequires: maven-eclipse-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: jboss-ejb-3.1-api
BuildRequires: jboss-logging
BuildRequires: jboss-logging-tools
BuildRequires: jboss-logmanager
BuildRequires: jboss-marshalling
BuildRequires: jboss-remoting
BuildRequires: jboss-sasl
BuildRequires: jboss-transaction-1.1-api
BuildRequires: xnio

Requires:      jpackage-utils
Requires:      jboss-ejb-3.1-api
Requires:      jboss-logging
Requires:      jboss-logging-tools
Requires:      jboss-logmanager
Requires:      jboss-marshalling
Requires:      jboss-remoting
Requires:      jboss-sasl
Requires:      jboss-transaction-1.1-api
Requires:      xnio

BuildArch:     noarch
Source44: import.info

%description
Client library for EJB applications working against JBoss AS

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
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-ejb-client-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_3jpp7
- new version

