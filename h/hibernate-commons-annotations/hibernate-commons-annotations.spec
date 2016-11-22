Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate-commons-annotations
%define version 4.0.4
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             hibernate-commons-annotations
Version:          4.0.4
Release:          alt1_3jpp8
Summary:          Hibernate Annotations

# For details see:
# - https://github.com/hibernate/hibernate-commons-annotations/commit/4a902b4f97f923f9044a4127357b44fe5dc39cdc
# - https://github.com/hibernate/hibernate-commons-annotations/commit/a11c44cd65dadcedaf8981379b94a2c4e31428d1
License:          LGPLv2
URL:              http://www.hibernate.org/
Source0:          https://github.com/hibernate/hibernate-commons-annotations/archive/%{namedversion}.tar.gz

Source1:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/hibernate/common/hibernate-commons-annotations/%{namedversion}/hibernate-commons-annotations-%{namedversion}.pom

BuildArch:        noarch

BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools >= 1.2.0
BuildRequires:    junit
BuildRequires:    slf4j
BuildRequires:    apache-commons-logging
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    maven-local
BuildRequires:    maven-processor-plugin
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-injection-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-source-plugin
BuildRequires:    maven-surefire-plugin
Source44: import.info

%description
Following the DRY (Don't Repeat Yourself) principle, 
Hibernate Validator let's you express your domain 
constraints once (and only once) and ensure their 
compliance at various level of your system 
automatically.

Common reflection code used in support of annotation processing.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n hibernate-commons-annotations-%{namedversion}

cp %{SOURCE1} pom.xml

%pom_add_dep org.jboss.logging:jboss-logging-processor:1.2.0:provided
%pom_add_dep junit:junit:4:test

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc changelog.txt lgpl.txt readme.txt

%files javadoc -f .mfiles-javadoc
%doc lgpl.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_2jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1_2jpp7
- new version

