Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-logmanager
%define version 1.2.2
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logmanager
Version:          1.2.2
Release:          alt2_3jpp7
Summary:          JBoss Log Manager
Group:            Development/Java
License:          LGPLv2+
URL:              https://github.com/jboss-logging/jboss-logmanager

# git clone git://github.com/jboss-logging/jboss-logmanager.git
# cd jboss-logmanager/ && git archive --format=tar --prefix=jboss-logmanager-1.2.2.GA/ 1.2.2.GA | xz > jboss-logmanager-1.2.2.GA.tar.xz
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
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    maven-ejb-plugin
BuildRequires:    testng
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    qdox
BuildRequires:    jboss-parent

Requires:         jpackage-utils
Source44: import.info

%description
This package contains the JBoss Log Manager

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
%doc COPYING.txt

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_3jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_3jpp6
- new version

