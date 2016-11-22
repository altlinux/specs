Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jstl-1.2-api
%define version 1.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-jstl-1.2-api
Version:       1.0.3
Release:       alt4_14jpp8
Summary:       JSP Standard Template Library 1.2 API
License:       CDDL or GPLv2 with exceptions
URL:           http://www.jboss.org
# git clone git://github.com/jboss/jboss-jstl-api_spec.git jboss-jstl-1.2-api
# cd jboss-jstl-1.2-api/ && git archive --format=tar --prefix=jboss-jstl-1.2-api-1.0.3.Final/ jboss-jstl-api_1.2_spec-1.0.3.Final | xz > jboss-jstl-1.2-api-1.0.3.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz
# Fix the FSF address in the license file:
Patch0:        %{name}-fix-fsf-address.patch
Patch1:        %{name}-endorse_xalan.patch

BuildRequires: maven-local
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.spec.javax.el:jboss-el-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.2_spec)
BuildRequires: mvn(xalan:xalan)

BuildArch:     noarch
Source44: import.info

%description
Java Server Pages Standard Template Library 1.2 API.

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
%patch1 -p1

%pom_remove_plugin :maven-source-plugin

%mvn_file : %{name}

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
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt4_14jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt4_13jpp8
- java8 mass update

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4jpp7
- new version

