Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name bean-validation-api
%define version 1.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             bean-validation-api
Version:          1.1.0
Release:          alt1_5jpp8
Summary:          Bean Validation API (JSR 349)
License:          ASL 2.0
URL:              http://beanvalidation.org/
Source0:          https://github.com/beanvalidation/beanvalidation-api/archive/%{namedversion}.tar.gz

BuildRequires:    java-devel

# test deps
BuildRequires:    mvn(org.testng:testng)

BuildRequires:    maven-local
BuildRequires:    maven-plugin-bundle
BuildRequires:    maven-surefire-provider-testng

BuildArch:        noarch
Source44: import.info

%description
This package contains Bean Validation (JSR-349) API.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n beanvalidation-api-%{namedversion}

# Disable javadoc jar
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"
# Disable source jar
%pom_remove_plugin :maven-source-plugin

%build

%mvn_file : %{name}
%mvn_build -- -Dmaven.test.skip.exec=true

%install
%mvn_install

%files -f .mfiles
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_5jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_4jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_8jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp7
- new fc release

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp7
- fc build

