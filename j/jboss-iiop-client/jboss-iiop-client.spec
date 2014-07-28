# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-iiop-client
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-iiop-client
Version:          1.0.0
Release:          alt2_6jpp7
Summary:          JBoss IIOP Client
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossiiop

# git clone git://github.com/jbossas/jboss-iiop-client.git
# cd jboss-iiop-client/ && git archive --format=tar --prefix=jboss-iiop-client-1.0.0.Final/ 1.0.0.Final | xz > jboss-iiop-client-1.0.0.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

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
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-parent
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    junit

Requires:         jpackage-utils
Requires:         jboss-ejb-3.1-api
Source44: import.info

%description
Client library for EJB applications working against JBoss AS using
the IIOP protocol

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
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-iiop-client-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp7
- new version

