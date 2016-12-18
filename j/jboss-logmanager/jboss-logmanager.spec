Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-logmanager
%define version 2.0.4
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logmanager
Version:          2.0.4
Release:          alt1_1jpp8
Summary:          JBoss Log Manager
License:          ASL 2.0
URL:              https://github.com/jboss-logging/jboss-logmanager
Source0:          https://github.com/jboss-logging/jboss-logmanager/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.modules:jboss-modules)
Source44: import.info

%description
This package contains the JBoss Log Manager

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Unneeded task
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_5jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_4jpp8
- java8 mass update

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_3jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_3jpp6
- new version

