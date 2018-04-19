Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-transaction-1.2-api
Version:          1.0.1
Release:          alt1_4jpp8
Summary:          Transaction 1.2 API
License:          CDDL or GPLv2 with exceptions
Url:              https://github.com/jboss/jboss-transaction-api_spec
Source0:          https://github.com/jboss/jboss-transaction-api_spec/archive/jboss-transaction-api_1.2_spec-%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(javax.enterprise:cdi-api)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)

BuildArch:        noarch
Source44: import.info

%description
The Java Transaction 1.2 API classes.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-transaction-api_spec-jboss-transaction-api_1.2_spec-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Alpha3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.4.Alpha3jpp8
- new version

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.2.Alpha3jpp7
- new version

