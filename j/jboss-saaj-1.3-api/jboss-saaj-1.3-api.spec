Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-saaj-1.3-api
%define version 1.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-saaj-1.3-api
Version:       1.0.3
Release:       alt1_1jpp8
Summary:       SOAP with Attachments API for Java 1.3
License:       CDDL or GPLv2 with exceptions
URL:           http://www.jboss.org

Source0:       https://github.com/jboss/jboss-saaj-api_spec/archive/jboss-saaj-api_1.3_spec-%{namedversion}.tar.gz

BuildArch:     noarch
BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
The SOAP with Attachments API for Java Version 1.3 classes.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-saaj-api_spec-jboss-saaj-api_1.3_spec-%{namedversion}

# Unneeded plugin
%pom_remove_plugin :maven-source-plugin

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%doc LICENSE
%doc README

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt4_12jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt4_11jpp8
- java8 mass update

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- new version

