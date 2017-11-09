Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.3
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             slf4j-jboss-logmanager
Version:          1.0.3
Release:          alt1_3jpp8
Summary:          SLF4J backend for JBoss LogManager
License:          LGPLv2+
URL:              https://github.com/jboss-logging/slf4j-jboss-logmanager
Source0:          https://github.com/jboss-logging/slf4j-jboss-logmanager/archive/%{namedversion}.tar.gz

BuildArch:        noarch
BuildRequires:    maven-local
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(org.slf4j:slf4j-api)
Source44: import.info

%description
This package contains SLF4J backend for JBoss LogManager

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin :maven-source-plugin

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_12jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_11jpp8
- java8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

