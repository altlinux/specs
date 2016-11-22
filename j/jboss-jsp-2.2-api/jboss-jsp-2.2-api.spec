Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jsp-2.2-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jsp-2.2-api
Version:          1.0.1
Release:          alt5_13jpp8
Summary:          JavaServer(TM) Pages 2.2 API
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org/

# git clone git://github.com/jboss/jboss-jsp-api_spec.git jboss-jsp-2.2-api
# cd jboss-jsp-2.2-api/ && git archive --format=tar --prefix=jboss-jsp-2.2-api-1.0.1.Final/ jboss-jsp-api_2.2_spec-1.0.1.Final | xz > jboss-jsp-2.2-api-1.0.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    maven-local
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.spec.javax.el:jboss-el-api_2.2_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)

BuildArch:        noarch
Source44: import.info

%description
JSR-000245: JavaServer(TM) Pages 2.2

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin :maven-source-plugin

%mvn_file : %{name}
%mvn_alias : javax.servlet.jsp:jsp-api

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt5_13jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt5_12jpp8
- java8 mass update

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_3jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3jpp7
- fixed build

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new version

