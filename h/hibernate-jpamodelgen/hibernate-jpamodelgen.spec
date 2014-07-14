BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate-jpamodelgen
%define version 1.2.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global with_test 0
Name:          hibernate-jpamodelgen
Version:       1.2.0
Release:       alt2_2jpp7
Summary:       Hibernate JPA 2 Metamodel Generator
Group:         Development/Java
License:       ASL 2.0
Url:           http://www.hibernate.org/subprojects/jpamodelgen.html
Source0:       http://sourceforge.net/projects/hibernate/files/hibernate-jpamodelgen/1.2.0.Final/hibernate-jpamodelgen-1.2.0.Final-dist.tar.gz
#Source1:       ...
# change 
#       jaxb2-maven-plugin with maven-jaxb22-plugin (configuration)
# remove
#       maven-jdocbook-plugin
Patch0:        hibernate-jpamodelgen-1.2.0.Final-pom.patch

Patch1:        hibernate-jpamodelgen-1.2.0.Final-remove-maven-surefire.patch

BuildRequires: jpackage-utils

%if %with_test
BuildRequires: hibernate-core >= 4.0.0
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: slf4j
BuildRequires: testng >= 6.3.1
BuildRequires: maven-surefire-report-plugin >= 2.11
%endif

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-injection-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jaxb2-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Annotation Processor to generate JPA 2 static metamodel classes.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
find . -name "*.jar" -delete
find . -name "*.class" -delete
rm -rf docs/api

%patch0 -p0
%if !%with_test
%patch1 -p0
%endif

%build
# test skip unavailable deps
mvn-rpmbuild \
%if !%with_test
  -Dmaven.test.skip=true \
%endif
  -Dproject.build.sourceEncoding=UTF-8 \
  install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc README.md changelog.txt license.txt

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2jpp7
- new version

