Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc jdepend
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-logging
%define version 3.1.4
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logging
Version:          3.1.4
Release:          alt1_4jpp8
Summary:          The JBoss Logging Framework
License:          ASL 2.0
URL:              https://github.com/jboss-logging/jboss-logging
Source0:          https://github.com/jboss-logging/jboss-logging/archive/%{namedversion}.tar.gz

Patch0:           0001-SLF4j-1.7-upgrade.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    jboss-logmanager
BuildRequires:    slf4j
BuildRequires:    log4j
BuildRequires:    apiviz
BuildRequires:    jboss-parent
BuildRequires:    maven-surefire-provider-junit
Source44: import.info

%description
This package contains the JBoss Logging Framework.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-logging-%{namedversion}

%patch0 -p1

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc src/main/resources/META-INF/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc src/main/resources/META-INF/LICENSE.txt

%changelog
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

