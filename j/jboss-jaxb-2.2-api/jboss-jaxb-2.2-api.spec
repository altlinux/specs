Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.4
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-jaxb-2.2-api
Version:       1.0.4
Release:       alt2_16jpp8
Summary:       Java Architecture for XML Binding 2.2
License:       CDDL or GPLv2 with exceptions
URL:           http://www.jboss.org

# git clone git://github.com/jboss/jboss-jaxb-api_spec.git jboss-jaxb-2.2-api
# cd jboss-jaxb-2.2-api/ && git archive --format=tar --prefix=jboss-jaxb-2.2-api-1.0.4.Final/ jboss-jaxb-api_2.2_spec-1.0.4.Final | xz > jboss-jaxb-2.2-api-1.0.4.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
Java Architecture for XML Binding Version 2.2 classes.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Unneeded plugin
%pom_remove_plugin :maven-source-plugin

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE
%doc README

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_14jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_12jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_11jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3jpp7
- new release

