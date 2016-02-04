Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name weld-api
%define version 2.2
%global namedreltag .SP3
%global namedversion %{version}%{?namedreltag}

Name:             weld-api
Version:          2.2
Release:          alt1_2.SP3jpp8
Summary:          Weld API
License:          ASL 2.0
URL:              http://seamframework.org/Weld
Source0:          https://github.com/weld/api/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    bean-validation-api
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    cdi-api
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jboss-interceptors-1.2-api
BuildRequires:    jboss-ejb-3.2-api
BuildRequires:    jboss-jsf-2.1-api
BuildRequires:    hibernate-jpa-2.0-api
BuildRequires:    geronimo-jta
BuildRequires:    geronimo-jpa
BuildRequires:    geronimo-annotation
BuildRequires:    weld-parent
BuildRequires:    geronimo-parent-poms
BuildRequires:    maven-plugin-build-helper
Source44: import.info

%description
Weld specifc extensions to the CDI API

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n api-%{namedversion}

%pom_remove_plugin ":maven-checkstyle-plugin" weld/pom.xml
%pom_remove_plugin ":maven-checkstyle-plugin" weld-spi/pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2.SP3jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp7
- new version

