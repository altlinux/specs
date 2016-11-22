Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-logging
%define version 3.1.4
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logging
Version:          3.1.4
Release:          alt1_6jpp8
Summary:          The JBoss Logging Framework
License:          ASL 2.0
URL:              https://github.com/jboss-logging/jboss-logging
Source0:          https://github.com/jboss-logging/jboss-logging/archive/%{namedversion}.tar.gz

Patch0:           0001-SLF4j-1.7-upgrade.patch

BuildArch:        noarch

BuildRequires:    git
BuildRequires: graphviz libgraphviz
BuildRequires:    maven-local
BuildRequires:    mvn(log4j:log4j:12)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.apiviz:apiviz)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(org.slf4j:slf4j-api)
# Missing apiviz dep ...
BuildRequires:    mvn(jdepend:jdepend)
Source44: import.info

%description
This package contains the JBoss Logging Framework.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-logging-%{namedversion}

%patch0 -p1

%pom_change_dep log4j: ::12
# Unneeded task
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc src/main/resources/META-INF/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc src/main/resources/META-INF/LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_6jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_4jpp8
- java 8 mass update

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1_1jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt3_4jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_4jpp7
- new version

