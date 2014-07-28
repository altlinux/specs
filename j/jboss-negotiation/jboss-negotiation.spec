# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-negotiation
%define version 2.2.0
%global namedreltag .SP1
%global namedversion %{version}%{?namedreltag}

Name:             jboss-negotiation
Version:          2.2.0
Release:          alt2_9.SP1jpp7
Summary:          JBoss Negotiation
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/picketlink/Negotiation

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/security/security-negotiation/tags/security-negotiation-2.2.0.SP1/ jboss-negotiation-2.2.0.SP1
# tar cafJ jboss-negotiation-2.2.0.SP1.tar.xz jboss-negotiation-2.2.0.SP1
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
BuildRequires:    maven-war-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    picketbox
BuildRequires:    picketbox-commons
BuildRequires:    jboss-logging
BuildRequires:    jboss-web
BuildRequires:    jboss-servlet-3.0-api

Requires:         jboss-logging
Requires:         jboss-servlet-3.0-api
Requires:         jboss-web
Requires:         picketbox-commons
Requires:         jpackage-utils
Source44: import.info

%description
Negotiation project provides SPNEGO/Kerberos support in JBoss

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
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

for m in common extras net ntlm spnego; do
  # JAR
  install -pm 644 jboss-negotiation-${m}/target/jboss-negotiation-${m}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
  # POM
  install -pm 644 jboss-negotiation-${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-main.pom
install -pm 644 parent/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-main.pom

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_9.SP1jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_7.SP1jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_7.SP1jpp7
- new version

