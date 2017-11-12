Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.3
%global namedreltag .SP2
%global namedversion %{version}%{?namedreltag}

Name:             weld-api
Version:          2.3
Release:          alt1_4.SP2jpp8
Summary:          Weld API
License:          ASL 2.0
URL:              http://weld.cdi-spec.org
Source0:          https://github.com/weld/api/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(javax.enterprise:cdi-api)
BuildRequires:    mvn(javax.inject:javax.inject)
BuildRequires:    mvn(javax.validation:validation-api)
BuildRequires:    mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires:    mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:    mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:    mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires:    mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.2_spec)
BuildRequires:    mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)
BuildRequires:    mvn(org.jboss.weld:weld-parent:pom:)
BuildRequires:    mvn(org.testng:testng::jdk15:)
Source44: import.info

%description
Weld specifc extensions to the CDI API

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n api-%{namedversion}

%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin ":maven-checkstyle-plugin" weld/pom.xml
%pom_remove_plugin ":maven-checkstyle-plugin" weld-spi/pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_4.SP2jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_3.SP2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_2.SP2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_4.SP3jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2.SP3jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp7
- new version

