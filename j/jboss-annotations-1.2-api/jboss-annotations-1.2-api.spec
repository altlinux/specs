Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-annotations-1.2-api
%define version 1.0.0
%global namedreltag .Alpha1
%global namedversion %{version}%{?namedreltag}

Name:       jboss-annotations-1.2-api
Version:    1.0.0
Release:    alt1_0.6.Alpha1jpp8
Summary:    Common Annotations 1.2 API
License:    CDDL or GPLv2 with exceptions
URL:        http://www.jboss.org
Source0:    https://github.com/jboss/jboss-annotations-api_spec/archive/jboss-annotations-api_1.2_spec-%{namedversion}.tar.gz
Source1:    cddl.txt

BuildRequires: jboss-parent
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

BuildArch: noarch
Source44: import.info

%description
This package contains Common Annotations 1.2 API.

%package javadoc
Group: Development/Java
Summary: Javadocs for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-annotations-api_spec-jboss-annotations-api_1.2_spec-%{namedversion}

cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE
%doc README
%doc cddl.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE
%doc README
%doc cddl.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.6.Alpha1jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Alpha1jpp8
- java 8 mass update

