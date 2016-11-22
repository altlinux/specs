Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jacc-1.5-api
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jacc-1.5-api
Version:          1.0.0
Release:          alt1_5jpp8
Summary:          JACC 1.5 API (JSR-115)
License:          (CDDL or GPLv2 with exceptions) or LGPLv2+
URL:              https://github.com/jboss/jboss-jacc-api_spec
Source0:          https://github.com/jboss/jboss-jacc-api_spec/archive/jboss-jacc-api_1.5_spec-%{namedversion}.tar.gz

BuildRequires:    jboss-servlet-3.1-api
BuildRequires:    junit
BuildRequires:    maven-local
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-surefire-provider-junit

BuildArch:        noarch

Provides:         javax.security.jacc
Source44: import.info

%description
JSR-000115 Java Authorization Contract for Containers 1.5 API

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jacc-api_spec-jboss-jacc-api_1.5_spec-%{namedversion}

%mvn_file :{jboss-jacc-api_1.5_spec} %{name} %{name}/%{name} javax.security.jacc/%{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%dir %{_javadir}/javax.security.jacc
%{_javadir}/%{name}.jar
%doc README LICENSE

%files javadoc -f .mfiles-javadoc
%doc README LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- dropped dep on xmldb-api-sdk

