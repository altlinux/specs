Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.4.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logging
Version:          3.4.1
Release:          alt1_6jpp11
Summary:          The JBoss Logging Framework
License:          ASL 2.0

URL:              https://github.com/jboss-logging/jboss-logging
Source0:          %{url}/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.logging.log4j:log4j-1.2-api)
BuildRequires:    mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(org.slf4j:slf4j-api)
Source44: import.info

%description
This package contains the JBoss Logging Framework.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Unneeded task
%pom_remove_plugin :maven-source-plugin

# switch from log4j 1.2 compat package to log4j 1.2 API shim
%pom_change_dep log4j:log4j org.apache.logging.log4j:log4j-1.2-api

cp -p src/main/resources/META-INF/LICENSE.txt .
sed -i 's/\r//' LICENSE.txt

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 3.4.1-alt1_6jpp11
- fc34 update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 3.4.1-alt1_2jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_5jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_6jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_4jpp8
- java 8 mass update

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1_1jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt3_4jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_4jpp7
- new version

