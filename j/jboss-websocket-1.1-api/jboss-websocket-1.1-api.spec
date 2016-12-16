Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-websocket-1.1-api
%define version 1.1.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-websocket-1.1-api
Version:          1.1.1
Release:          alt1_1jpp8
Summary:          JSR-356: Java WebSocket 1.1 API
License:          CDDL or GPLv2 with exceptions
Url:              https://github.com/jboss/jboss-websocket-api_spec
Source0:          https://github.com/jboss/jboss-websocket-api_spec/archive/%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)

BuildArch:        noarch
Source44: import.info

%description
The JSR-356: Java WebSocket 1.1 API classes.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-websocket-api_spec-%{namedversion}

%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE README

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2jpp8
- java 8 mass update

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

