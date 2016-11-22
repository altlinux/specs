Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaxr-1.0-api
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global oname jboss-jaxr-api_1.0_spec
Name:          jboss-jaxr-1.0-api
Version:       1.0.2
Release:       alt2_10jpp8
Summary:       Java API for XML Registries 1.0 (JAXR)
License:       CDDL or GPLv2 with exceptions
URL:           http://www.jboss.org/
# git clone git://github.com/jboss/jboss-jaxr-api_spec.git jboss-jaxr-1.0-api
# cd jboss-jaxr-1.0-api/ && git archive --format=tar --prefix=jboss-jaxr-1.0-api/ jboss-jaxr-api_1.0_spec-1.0.2.Final  | xz > jboss-jaxr-1.0-api-1.0.2.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: jboss-specs-parent

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

BuildArch:     noarch
Source44: import.info

%description
JSR 93: Java API for XML Registries 1.0 (JAXR).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}
%pom_remove_dep javax.activation:activation

%mvn_file :%{oname} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_2jpp7
- new version

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt4_2jpp6
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt3_2jpp6
- build w/o jms-1.1-api

* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt2_2jpp6
- built with patched assembly plugin

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt1_2jpp6
- new version

