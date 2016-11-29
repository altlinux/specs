Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-logging-tools
%define version 1.2.0
%global namedreltag .Beta1
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logging-tools
Version:          1.2.0
Release:          alt1_0.4.Beta1jpp8
Summary:          JBoss Logging I18n Annotation Processor
License:          LGPLv2+
URL:              https://github.com/jboss-logging/jboss-logging-tools
Source0:          https://github.com/jboss-logging/jboss-logging-tools/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    testng
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    jboss-parent
BuildRequires:    jboss-logging
BuildRequires:    jboss-logmanager
BuildRequires:    jdeparser
Source44: import.info

%description
This pacakge contains JBoss Logging I18n Annotation Processor

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-logging-tools-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_0.4.Beta1jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_0.3.Beta1jpp8
- java 8 mass update

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_3jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp7
- new version

