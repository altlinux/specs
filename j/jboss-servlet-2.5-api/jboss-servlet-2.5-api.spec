Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-servlet-2.5-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-servlet-2.5-api
Version:          1.0.1
Release:          alt3_11jpp8
Summary:          Java Servlet 2.5 API
License:          ASL 2.0 and W3C
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-servlet-api_spec.git
# cd jboss-servlet-api_spec/ && git archive --format=tar --prefix=jboss-servlet-2.5-api/ jboss-servlet-api_2.5_spec-1.0.1.Final | xz > jboss-servlet-2.5-api-1.0.1.Final.tar.xz
Source0:          jboss-servlet-2.5-api-%{namedversion}.tar.xz

BuildRequires:    maven-local
BuildRequires:    mvn(org.jboss.spec:jboss-specs-parent:pom:)

BuildArch:        noarch
Source44: import.info

%description
The Java Servlet 2.5 API classes.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-servlet-2.5-api

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_11jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_10jpp8
- java8 mass update

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new version

