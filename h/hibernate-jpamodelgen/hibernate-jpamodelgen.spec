Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate-jpamodelgen
%define version 1.2.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global with_test 0
Name:          hibernate-jpamodelgen
Version:       1.2.0
Release:       alt2_6jpp7
Summary:       Hibernate JPA 2 Metamodel Generator
License:       ASL 2.0
Url:           http://www.hibernate.org/subprojects/jpamodelgen.html
Source0:       http://sourceforge.net/projects/hibernate/files/%{name}/%{namedversion}/%{name}-%{namedversion}-dist.tar.gz


%if %with_test
BuildRequires: hibernate >= 4.0.0
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: slf4j
BuildRequires: testng >= 6.3.1
BuildRequires: maven-surefire-report-plugin >= 2.11
%endif

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-injection-plugin
BuildRequires: jaxb2-maven-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-report-plugin

BuildArch:     noarch
Source44: import.info

%description
Annotation Processor to generate JPA 2 static metamodel classes.

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

%pom_remove_plugin :maven-jdocbook-plugin
%if !%with_test
%pom_remove_plugin :maven-surefire-plugin
%endif

%build

%mvn_file :%{name} %{name}
# test skip unavailable deps
%mvn_build \
%if !%with_test
  -f \
%endif
  -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md changelog.txt license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2jpp7
- new version

