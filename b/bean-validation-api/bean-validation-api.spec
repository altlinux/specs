Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:           bean-validation-api
Summary:        Bean Validation API (JSR 349)
Version:        2.0.1
Release:        alt1_2jpp8
License:        ASL 2.0

URL:            http://beanvalidation.org/
Source0:        https://github.com/beanvalidation/beanvalidation-api/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.testng:testng)
Source44: import.info

%description
This package contains Bean Validation (JSR-349) API.


%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n beanvalidation-api-%{namedversion}

%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%mvn_file : %{name}

# The byte array allocation should have triggered a OutOfMemoryError
find src/test/java -name "ValidationTest.java" -print -delete

%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc README.md
%doc --no-dereference license.txt copyright.txt

%files javadoc -f .mfiles-javadoc
%doc README.md
%doc --no-dereference license.txt copyright.txt


%changelog
* Mon Oct 12 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_11jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_10jpp8
- fc29 update

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

