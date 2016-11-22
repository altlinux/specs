Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name wildfly-security-manager
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
# TMP solution until the proper tag will be pushed
%global namedversion 910aac63caf7a96f189fac832be22fccc416095d

Name:             wildfly-security-manager
Version:          1.0.0
Release:          alt1_4jpp8
Summary:          WildFly Security Manager
License:          LGPLv2+
Url:              http://www.jboss.org
Source0:          https://github.com/wildfly/security-manager/archive/%{namedversion}.tar.gz

BuildRequires:    jboss-parent
BuildRequires:    jboss-invocation
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-logmanager
BuildRequires:    jboss-modules
BuildRequires:    junit
BuildRequires:    maven-local

BuildArch:        noarch
Source44: import.info

%description
The Security Manager for WildFly Application Server.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n security-manager-%{namedversion}

%pom_remove_plugin "org.jboss.seven2six:seven2six"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- java 8 mass update

