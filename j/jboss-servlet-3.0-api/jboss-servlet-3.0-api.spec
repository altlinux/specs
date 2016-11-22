# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-servlet-3.0-api
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-servlet-3.0-api
Version:          1.0.2
Release:          alt1_5jpp8
Summary:          Java Servlet 3.0 API
Group:            Development/Other
License:          CDDL
Url:              http://www.jboss.org
Source0:          https://github.com/jboss/jboss-servlet-api_spec/archive/jboss-servlet-api_3.0_spec-1.0.2.Final.tar.gz
Source1:          cddl.txt

BuildRequires:    jboss-parent
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin

BuildArch:        noarch
Source44: import.info

%description
The Java Servlet 3.0 API classes.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-servlet-api_spec-jboss-servlet-api_3.0_spec-%{namedversion}

cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE README cddl.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE README cddl.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new version

