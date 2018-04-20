Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.1.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global pname jboss-jstl-api_spec
%global oname jboss-jstl-api_1.2_spec

Name:          jboss-jstl-1.2-api
Version:       1.1.2
Release:       alt1_5jpp8
Summary:       JSP Standard Template Library 1.2 API
License:       ASL 2.0 and (CDDL or GPLv2 with exceptions)
URL:           https://github.com/jboss/jboss-jstl-api_spec
Source0:       https://github.com/jboss/jboss-jstl-api_spec/archive/%{oname}-%{namedversion}.tar.gz
# Fix the FSF address in the license file:
Patch0:        %{name}-fix-fsf-address.patch
Patch1:        %{name}-endorse_xalan.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.spec.javax.el:jboss-el-api_3.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.3_spec)
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
%setup -q -n %{pname}-%{oname}-%{namedversion}
# Apply the patches:
%patch0 -p1
# only for EL, in fedora ibm jdk is not available
%if 0%{?el7}
%patch1 -p1
%endif

%pom_remove_plugin :maven-source-plugin

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE README
%doc CHANGES.txt README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE README

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_4jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_3jpp8
- new jpp release

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

