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
%global namedreltag .20120319git49a904
%global namedversion %{version}%{?namedreltag}

Name:             jboss-interceptors-1.1-api
Version:          1.0.2
Release:          alt2_0.17.20120319git49a904jpp8
Summary:          Interceptors 1.1 API
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org
BuildArch:        noarch

# git clone git://github.com/jboss/jboss-interceptors-api_spec.git jboss-interceptors-1.1-api
# cd jboss-interceptors-1.1-api/ && git archive --format=tar --prefix=jboss-interceptors-1.1-api/ 49a90471d8108b5b2a2da6063b5591a9f41ed24a | xz > jboss-interceptors-1.1-api-1.0.2.20120319git49a904.tar.xz
Source0:          jboss-interceptors-1.1-api-%{namedversion}.tar.xz

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
Source44: import.info


%description
This package contains The JavaEE Interceptors 1.1 API classes from JSR 318.

%package javadoc
Group: Development/Other
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-interceptors-1.1-api

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
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.17.20120319git49a904jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.16.20120319git49a904jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.15.20120319git49a904jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.14.20120319git49a904jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.13.20120319git49a904jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.12.20120319git49a904jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.7.20120319git49a904jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.5.20120319git49a904jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.3.20120319git49a904jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_0.3.20120319git49a904jpp7
- new version

