Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jsf-2.1-api
%define version 2.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:    jboss-jsf-2.1-api
Version: 2.0.2
Release: alt3_12jpp8
Summary: JavaServer Faces 2.1 API
License: CDDL or GPLv2 with exceptions
URL:     http://www.jboss.org

# git clone git://github.com/jboss/jboss-jsf-api_spec.git jboss-jsf-2.1-api
# cd jboss-jsf-2.1-api/ && git archive --format=tar --prefix=jboss-jsf-2.1-api-2.0.2.Final/ jboss-jsf-api_2.1_spec-2.0.2.Final | xz > jboss-jsf-2.1-api-2.0.2.Final.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

# Fix the FSF address in the license file:
Patch0:  %{name}-fix-fsf-address.patch

BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.spec.javax.el:jboss-el-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jstl:jboss-jstl-api_1.2_spec)
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: objenesis

BuildArch:     noarch
Source44: import.info


%description
JavaServer Faces API classes based on Version 2.1 of Specification.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep

# Unpack the sources:
%setup -q -n %{name}-%{namedversion}
# Apply the patches:
%patch0 -p1

%mvn_file :jboss-jsf-api_2.1_spec %{name}
%mvn_alias :jboss-jsf-api_2.1_spec javax.faces:jsf-api

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%doc LICENSE
%doc README

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_12jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_3jpp7
- new version

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_3jpp7
- new version

