Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-connector-1.7-api
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-connector-1.7-api
Version:          1.0.0
Release:          alt1_4jpp8
Summary:          Connector Architecture 1.7 API
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org
Source0:          https://github.com/jboss/jboss-connector-api_spec/archive/jboss-connector-api_1.7_spec-%{namedversion}.tar.gz
Source1:          cddl.txt

BuildRequires:    jboss-parent
BuildRequires:    maven-local
BuildRequires:    maven-enforcer-plugin
BuildRequires:    jboss-transaction-1.2-api

BuildArch:        noarch
Source44: import.info

%description
Java EE Connector Architecture 1.7 API classes

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-connector-api_spec-jboss-connector-api_1.7_spec-%{namedversion}

cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc cddl.txt

%files javadoc -f .mfiles-javadoc
%doc cddl.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- java 8 mass update

