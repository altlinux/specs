Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name picketbox-xacml
%define version 2.0.7
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             picketbox-xacml
Version:          2.0.7
Release:          alt3_11jpp8
Summary:          JBoss XACML
License:          LGPLv2+
URL:              http://www.jboss.org/picketbox

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/security/security-xacml/tags/2.0.7.Final/ picketbox-xacml-2.0.7.Final
# tar cafJ picketbox-xacml-2.0.7.Final.tar.xz picketbox-xacml-2.0.7.Final
Source0:          %{name}-%{namedversion}.tar.xz
Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.picketbox:picketbox-commons)
Source44: import.info

%description
JBoss XACML Library

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

rm .classpath

%mvn_file :jboss-xacml %{name}
%mvn_file :jboss-sunxacml picketbox-sunxacml
%mvn_alias :jboss-xacml org.jboss.security:jbossxacml
%mvn_package ::pom: __noinstall

%build
# Disabled tests because OpenDS is needed
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt3_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt3_10jpp8
- new version

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt3_5jpp7
- fixed build

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt1_3jpp7
- new version

