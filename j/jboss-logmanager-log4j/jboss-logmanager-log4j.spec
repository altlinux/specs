BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-logmanager-log4j
%define version 1.0.0
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logmanager-log4j
Version:          1.0.0
Release:          alt2_5jpp7
Summary:          JBoss LogManager Log4j Compatibility Library 
Group:            Development/Java
License:          LGPLv2+
URL:              https://github.com/jboss-logging/jboss-logmanager-log4j

# git clone git://github.com/jboss-logging/jboss-logmanager-log4j.git
# cd jboss-logmanager-log4j/ && git archive --format=tar --prefix=jboss-logmanager-log4j-1.0.0.GA/ 1.0.0.GA | xz > jboss-logmanager-log4j-1.0.0.GA.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

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

BuildRequires:    jboss-parent
BuildRequires:    log4j
BuildRequires:    jboss-logmanager

Requires:         jboss-logmanager
Requires:         log4j
Requires:         jpackage-utils
Source44: import.info

%description
This package contains JBoss LogManager Log4j Compatibility Library 

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
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp7
- new version

