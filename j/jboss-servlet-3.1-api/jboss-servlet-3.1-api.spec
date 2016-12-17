Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-servlet-3.1-api
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-servlet-3.1-api
Version:          1.0.0
Release:          alt1_1jpp8
Summary:          Java Servlet 3.1 API
License:          (CDDL or GPLv2 with exceptions) and ASL 2.0
Url:              http://www.jboss.org
Source0:          https://github.com/jboss/jboss-servlet-api_spec/archive/jboss-servlet-api_3.1_spec-%{namedversion}.tar.gz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:          http://repository.jboss.org/licenses/cddl.txt

BuildRequires:    maven-local
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:        noarch
Source44: import.info

%description
The Java Servlet 3.1 API classes.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-servlet-api_spec-jboss-servlet-api_3.1_spec-%{namedversion}

cp %{SOURCE1} .
cp %{SOURCE2} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE cddl.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE cddl.txt LICENSE-2.0.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.6.Beta1jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Beta1jpp8
- new version

