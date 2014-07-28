Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-parent
%define version 1.1.0
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-parent
Version:          1.1.0
Release:          alt1_3jpp7
Summary:          JBossWS Parent
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws
Source0:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ws/jbossws-parent/%{namedversion}/jbossws-parent-%{namedversion}.pom

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    maven-war-plugin
BuildRequires:    maven-help-plugin
BuildRequires:    maven-dependency-plugin

Requires:         jpackage-utils
Source44: import.info

%description
This package contains the JBossWS Parent

%prep
cp %{SOURCE0} pom.xml

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_3jpp7
- new release

* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_1jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_4jpp6
- use maven-plugin-build-helper

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_4jpp6
- new jpp release

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_3jpp6
- new jpp release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_1jpp5
- new jpp release

