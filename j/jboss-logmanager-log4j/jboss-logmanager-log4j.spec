Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-logmanager-log4j
%define version 1.0.0
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logmanager-log4j
Version:          1.0.0
Release:          alt2_14jpp8
Summary:          JBoss LogManager Log4j Compatibility Library 
License:          LGPLv2+
URL:              https://github.com/jboss-logging/jboss-logmanager-log4j

# git clone git://github.com/jboss-logging/jboss-logmanager-log4j.git
# cd jboss-logmanager-log4j/ && git archive --format=tar --prefix=jboss-logmanager-log4j-1.0.0.GA/ 1.0.0.GA | xz > jboss-logmanager-log4j-1.0.0.GA.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(log4j:log4j:12)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
Source44: import.info

%description
This package contains JBoss LogManager Log4j Compatibility Library 

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_xpath_set "pom:dependency[pom:artifactId = 'log4j']/pom:version" 12

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_14jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_13jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp7
- new version

