Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jsp-2.3-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jsp-2.3-api
Version:          1.0.1
Release:          alt1_1jpp8
Summary:          JavaServer Pages 2.3 API (JSP)
License:          (CDDL or GPLv2 with exceptions) or ASL 2.0
URL:              https://github.com/jboss/jboss-jsp-api_spec
Source0:          https://github.com/jboss/jboss-jsp-api_spec/archive/jboss-jsp-api_2.3_spec-%{namedversion}.tar.gz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.spec.javax.el:jboss-el-api_3.0_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)

BuildArch:        noarch
Source44: import.info

%description
JSR-000245: JavaServer Pages 2.3

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jsp-api_spec-jboss-jsp-api_2.3_spec-%{namedversion}

cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE LICENSE-2.0.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.6.Beta1jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Beta1jpp8
- java 8 mass update

