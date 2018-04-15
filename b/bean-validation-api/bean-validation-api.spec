Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             bean-validation-api
Version:          1.1.0
Release:          alt1_9jpp8
Summary:          Bean Validation API (JSR 349)
License:          ASL 2.0
URL:              http://beanvalidation.org/
Source0:          https://github.com/beanvalidation/beanvalidation-api/archive/%{namedversion}.tar.gz

BuildRequires:    java-devel
BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires:    mvn(org.testng:testng)

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

# The byte array allocation should have triggered a OutOfMemoryError
find src/test/java -name "ValidationTest.java" -print -delete

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_7jpp8
- new jpp release

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

