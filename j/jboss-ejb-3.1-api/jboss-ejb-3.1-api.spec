Epoch: 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-ejb-3.1-api
Version:          1.0.2
Release:          alt2_18jpp8
Summary:          EJB 3.1 API
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org
BuildArch:        noarch

Source0:          https://github.com/jboss/jboss-ejb-api_spec/archive/jboss-ejb-api_3.1_spec-%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.xml.rpc:jboss-jaxrpc-api_1.1_spec)
Source44: import.info


%description
The Java EJB 3.1 API classes.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-ejb-api_spec-jboss-ejb-api_3.1_spec-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_18jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_17jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_16jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_15jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_14jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_13jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_3jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_4jpp6
- new version

