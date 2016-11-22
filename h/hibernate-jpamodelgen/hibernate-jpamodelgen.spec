Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate-jpamodelgen
%define version 1.3.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

#def_with test
%bcond_with test

Name:          hibernate-jpamodelgen
Version:       1.3.0
Release:       alt1_2jpp8
Summary:       Hibernate JPA 2 Metamodel Generator
License:       ASL 2.0
Url:           http://www.hibernate.org/subprojects/jpamodelgen.html
# https://github.com/hibernate/hibernate-metamodelgen
Source0:       http://downloads.sourceforge.net/hibernate/%{name}-%{namedversion}-dist.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:jaxb2-maven-plugin)
BuildRequires: mvn(org.jboss.maven.plugins:maven-injection-plugin)

# Test deps
%if %{without test}
# Compatibility problem with hibernate-core: use 4.2.3.Final available 4.3.5.Final
BuildRequires: mvn(org.hibernate:hibernate-core)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-report-plugin)
%endif

BuildArch:     noarch
Source44: import.info

%description
Annotation Processor to generate JPA 2 static meta-model classes.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
find . -name "*.jar" -delete
find . -name "*.class" -delete
rm -rf docs/api

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-jdocbook-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin
%if %{with test}
%pom_remove_plugin :maven-surefire-plugin
%pom_remove_plugin :maven-surefire-report-plugin
%endif

%mvn_file :%{name} %{name}

%build

# test skip unavailable deps
%if %{with test}
opts="-f"
%endif
%mvn_build $opts -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md changelog.txt
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1jpp8
- unbootsrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2jpp7
- new version

