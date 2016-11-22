# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaxrs-1.1-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-jaxrs-1.1-api
Version:       1.0.1
Release:       alt2_11jpp8
Summary:       Java API for RESTful Web Services (JAX-RS) 1.1
Group:         Development/Other
License:       CDDL
URL:           http://www.jboss.org

# git clone git://github.com/jboss/jboss-jaxrs-api_spec.git
# cd jboss-jaxrs-api_spec/ && git archive --format=tar --prefix=jboss-jaxrs-1.1-api/ jboss-jaxrs-api_1.1_spec-1.0.1.Final | xz > jboss-jaxrs-1.1-api-1.0.1.Final.tar.xz
Source0:       jboss-jaxrs-1.1-api-%{namedversion}.tar.xz

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-enforcer-plugin

BuildArch:     noarch
Source44: import.info

%description
JSR 311: The Javai API for RESTful Web Services (JAX-RS) 1.1

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jaxrs-1.1-api

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new version

