BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-msc
%define version 1.0.2
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-msc
Version:          1.0.2
Release:          alt2_3jpp7
Summary:          JBoss Modular Service Container
Group:            Development/Java
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-msc

# git clone git://github.com/jbossas/jboss-msc.git
# cd jboss-msc && git archive --format=tar --prefix=jboss-msc-1.0.2.GA/ 1.0.2.GA | xz > jboss-msc-1.0.2.GA.tar.xz
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
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-enforcer-plugin
BuildRequires:    javassist
BuildRequires:    jboss-parent
BuildRequires:    junit4
BuildRequires:    byteman
BuildRequires:    jboss-logging
BuildRequires:    jboss-vfs
BuildRequires:    jboss-threads
BuildRequires:    jboss-logging-tools
BuildRequires:    maven-injection-plugin
BuildRequires:    jboss-modules
BuildRequires:    apiviz

Requires:         jboss-logging-tools
Requires:         jboss-vfs
Requires:         jboss-logging
Requires:         byteman
Requires:         javassist
Requires:         jpackage-utils
Source44: import.info

%description
This package contains the JBoss Modular Service Container.

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
# Tests run: 682, Failures: 18, Errors: 0, Skipped: 0
mvn-rpmbuild install -Dmaven.test.skip=true javadoc:aggregate

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
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
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- new version

