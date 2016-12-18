Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jastow
%define version 2.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jastow
Version:          2.0.1
Release:          alt1_1jpp8
Summary:          Jasper fork
License:          ASL 2.0
Url:              https://github.com/undertow-io/jastow
Source0:          https://github.com/undertow-io/jastow/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(io.undertow:undertow-servlet)
BuildRequires:    mvn(org.eclipse.jdt.core.compiler:ecj)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.3_spec)

BuildArch:        noarch
Source44: import.info

%description
The Jasper fork for Undertow.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_dep "org.glassfish:javax.el"

%build
# we don't want to have cyclic dep
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- unbootsrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

