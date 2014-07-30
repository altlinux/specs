# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name picketbox-commons
%define version 1.0.0
%global namedreltag .final
%global namedversion %{version}%{?namedreltag}

Name:             picketbox-commons
Version:          1.0.0
Release:          alt2_6jpp7
Summary:          Common classes for security projects
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/picketbox

# svn export http://anonsvn.jboss.org/repos/picketbox/commons/tags/1.0.0.final/picketbox-commons/ picketbox-commons-1.0.0.final
# tar cafJ picketbox-commons-1.0.0.final.tar.xz picketbox-commons-1.0.0.final
Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin

Requires:         jpackage-utils
Source44: import.info

%description
This file contains common classes for security projects

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
rm -rf .classpath .project .settings

%build
mvn-rpmbuild install javadoc:aggregate

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
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

