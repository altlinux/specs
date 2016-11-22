Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jacc-1.4-api
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:           jboss-jacc-1.4-api
Version:        1.0.2
Release:        alt2_11jpp8
Summary:        JBoss JACC 1.4 API
License:        CDDL or GPLv2 with exceptions
URL:            http://www.jboss.org

# git clone git://github.com/jboss/jboss-jacc-api_spec.git jboss-jacc-1.4-api
# cd jboss-jacc-1.4-api/ && git archive --format=tar --prefix=jboss-jacc-1.4-api/ jboss-jacc-api_1.4_spec-1.0.2.Final | xz > jboss-jacc-1.4-api-1.0.2.Final.tar.xz

Source0:        %{name}-%{namedversion}.tar.xz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)

BuildArch:      noarch
Source44: import.info

%description
JBoss Java Authorization Contract for Containers 1.4 API.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%mvn_file : %{name}/%{name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE README

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- new version

