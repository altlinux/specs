BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-logging-tools
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logging-tools
Version:          1.0.0
Release:          alt2_3jpp7
Summary:          JBoss Logging I18n Annotation Processor
Group:            Development/Java
License:          LGPLv2+
URL:              https://github.com/jboss-logging/jboss-logging-tools

# git clone git://github.com/jboss-logging/jboss-logging-tools.git
# cd jboss-logging-tools && git archive --format=tar --prefix=jboss-logging-tools-1.0.0.Final/ 1.0.0.Final | xz > jboss-logging-tools-1.0.0.Final.tar.xz
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
BuildRequires:    maven-surefire-plugin
BuildRequires:    jboss-parent
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    junit4
BuildRequires:    jboss-logging

Requires:         jboss-logging
Requires:         jpackage-utils
Source44: import.info

%description
This pacakge contains JBoss Logging I18n Annotation Processor

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
install -pm 644 target/jboss-logging-processor-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/jboss-logging-processor.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-jboss-logging-processor.pom

%add_maven_depmap JPP-jboss-logging-processor.pom jboss-logging-processor.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp7
- new version

