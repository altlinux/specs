BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-invocation
%define version 1.1.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-invocation
Version:          1.1.1
Release:          alt2_4jpp7
Summary:          JBoss Invocation API 
Group:            Development/Java
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-invocation

# git clone git://github.com/jbossas/jboss-invocation.git
# cd jboss-invocation/ && git archive --format=tar --prefix=jboss-invocation-1.1.1.Final/ 1.1.1.Final | xz > jboss-invocation-1.1.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz
# Wrong dep artifcat id
Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    maven-ejb-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    junit4
BuildRequires:    jboss-parent
BuildRequires:    jboss-logging
BuildRequires:    jboss-marshalling
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-classfilewriter
BuildRequires:    jboss-interceptors-1.1-api

Requires:         jboss-classfilewriter
Requires:         jboss-logging-tools
Requires:         jboss-marshalling
Requires:         jboss-logging
Requires:         jpackage-utils
Requires:         jboss-interceptors-1.1-api
Source44: import.info

%description
This package contains JBoss Invocation API

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
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

# JAR
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# JAVADOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_4jpp7
- new version

