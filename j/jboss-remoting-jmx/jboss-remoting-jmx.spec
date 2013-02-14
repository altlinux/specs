# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-remoting-jmx
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-remoting-jmx
Version:       1.0.2
Release:       alt2_4jpp7
Summary:       JMX via JBoss Remoting
Group:         Development/Java
License:       LGPLv2+
URL:           http://www.jboss.org/

# git clone git://github.com/jbossas/remoting-jmx.git
# cd remoting-jmx/ && git archive --format=tar --prefix=jboss-remoting-jmx-1.0.2.Final/ 1.0.2.Final | xz > jboss-remoting-jmx-1.0.2.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: jpackage-utils
BuildRequires: jboss-parent
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-injection-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-checkstyle-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-dependency-plugin
BuildRequires: maven-ear-plugin
BuildRequires: maven-eclipse-plugin
BuildRequires: maven-ejb-plugin
BuildRequires: jboss-logging
BuildRequires: jboss-logging-tools
BuildRequires: jboss-logmanager
BuildRequires: jboss-marshalling
BuildRequires: jboss-remoting >= 3.2.2-1
BuildRequires: jboss-sasl
BuildRequires: xnio

Requires:      jpackage-utils
Requires:      jboss-logging
Requires:      jboss-logging-tools
Requires:      jboss-logmanager
Requires:      jboss-marshalling
Requires:      jboss-remoting >= 3.2.2-1
Requires:      jboss-sasl
Requires:      xnio

BuildArch:     noarch
Source44: import.info

%description
Library for making JMX accessible using Remoting 3 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
mvn-rpmbuild -e -Dmaven.test.failure.ignore=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/remoting-jmx-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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
%doc COPYING.txt

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING.txt

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_4jpp7
- fixed build

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4jpp7
- new version

