Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jastow
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jastow
Version:          1.0.0
Release:          alt1_5jpp8
Summary:          Jasper fork
License:          ASL 2.0
Url:              https://github.com/undertow-io/jastow
Source0:          http://github.com/undertow-io/jastow/archive/%{namedversion}.tar.gz

BuildRequires:    jboss-parent
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-logmanager
BuildRequires:    jboss-servlet-3.1-api
BuildRequires:    jboss-jsp-2.3-api
BuildRequires:    xnio
BuildRequires:    ecj
BuildRequires:    maven-local
BuildRequires:    maven-injection-plugin
BuildRequires:    maven-injection-plugin
BuildRequires:    undertow

BuildArch:        noarch
Source44: import.info

%description
The Jasper fork for Undertow.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jastow-%{namedversion}

%pom_remove_dep "org.glassfish:javax.el"

%build
# we don't want to have cyclic dep
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE README NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- unbootsrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

