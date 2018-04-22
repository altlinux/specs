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

Name:          jaxws-undertow-httpspi
Version:       1.0.1
Release:       alt1_5jpp8
Summary:       Undertow to JAXWS 2.2 HTTP SPI bridge
# Missing license file: 
# https://github.com/jbossws/jaxws-undertow-httpspi/issues/1
# https://issues.jboss.org/browse/JBWS-4023
License:       LGPLv2+
URL:           http://jbossws.jboss.org/
Source0:       https://github.com/jbossws/jaxws-undertow-httpspi/archive/%{name}-%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(io.undertow:undertow-core)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.xml.ws:jboss-jaxws-api_2.2_spec)
BuildRequires: mvn(org.jboss.ws:jbossws-parent:pom:)
# test deps
# BuildRequires: mvn(org.apache.cxf:cxf-rt-frontend-jaxws:2.7.13)

BuildArch:     noarch
Source44: import.info

%description
This package contains the JBoss httpserver to JAXWS 2.2 HTTP SPI bridge.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}

%build

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_5jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4jpp8
- new version

