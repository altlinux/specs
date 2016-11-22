Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-annotations-1.1-api
%define version 1.0.1
%global namedreltag .20120212git76e1a2
%global namedversion %{version}%{?namedreltag}

Name:          jboss-annotations-1.1-api
Version:       1.0.1
Release:       alt2_0.12.20120212git76e1a2jpp8
Summary:       Common Annotations 1.1 API
License:       CDDL or GPLv2 with exceptions
URL:           http://www.jboss.org

# git clone git://github.com/jboss/jboss-annotations-api_spec.git jboss-annotations-1.1-api
# cd jboss-annotations-1.1-api
# git archive --format=tar --prefix=jboss-annotations-1.1-api-1.0.1/ 76e1a2c85e025342710a29cd9dfff109d730a483 | xz > jboss-annotations-1.1-api-1.0.1.20120212git76e1a2.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(org.jboss:jboss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
This package contains Common Annotations 1.1 API.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

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
%doc README

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.12.20120212git76e1a2jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.11.20120212git76e1a2jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.6.20120212git76e1a2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.5.20120212git76e1a2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.3.20120212git76e1a2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_0.3.20120212git76e1a2jpp7
- new version

