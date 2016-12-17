Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaxrpc-1.1-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaxrpc-1.1-api
Version:          1.0.1
Release:          alt3_12jpp8
Summary:          Java API for XML-Based RPC (JAX-RPC) 1.1
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org
BuildArch:        noarch

# git clone git://github.com/jboss/jboss-jaxrpc-api_spec.git jboss-jaxrpc-1.1-api
# cd jboss-jaxrpc-1.1-api/ && git archive --format=tar --prefix=jboss-jaxrpc-1.1-api/ jboss-jaxrpc-api_1.1_spec-1.0.1.Final | xz > jboss-jaxrpc-1.1-api-1.0.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
Source44: import.info


%description
The JAX-RPC 1.1 API classes.

%package javadoc
Group: Development/Other
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jaxrpc-1.1-api

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_12jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_3jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_1jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_1jpp7
- fc update

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.1.20120309gita3c227jpp7
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_0.1.20120309gita3c227jpp7
- new version

