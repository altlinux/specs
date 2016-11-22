Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cdi-api1
%define version 1.0
%global namedtag SP4
%global namedreltag .%{namedtag}
%global namedversion %{version}%{?namedreltag}
%global upstreamversion %{version}-%{namedtag}

Name:             cdi-api1
Version:          1.0
Release:          alt1_18.SP4jpp8
Summary:          CDI API 1.0
License:          ASL 2.0
URL:              http://seamframework.org/Weld

# svn export http://anonsvn.jboss.org/repos/weld/cdi-api/tags/1.0-SP4/ cdi-api-1.0.SP4
# tar cafJ cdi-api-1.0.SP4.tar.xz cdi-api-1.0.SP4
Source0:          cdi-api-%{namedversion}.tar.xz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(javax.annotation:jsr250-api)
BuildRequires:    mvn(javax.inject:javax.inject)
BuildRequires:    mvn(org.apache.geronimo.specs:specs-parent:pom:)
BuildRequires:    mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:    mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.el:jboss-el-api_2.2_spec)
BuildRequires:    mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.1_spec)
BuildRequires:    mvn(org.jboss.weld:weld-parent:pom:)
BuildRequires:    mvn(org.testng:testng::jdk15:)
Source44: import.info


%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n cdi-api-%{namedversion}

cp %{SOURCE1} .

# Use el-api 2.2 instead of (glassifish-el-api) 3.0
%pom_xpath_set pom:properties/pom:uel.api.version 1.0.2.Final
%pom_change_dep :el-api org.jboss.spec.javax.el:jboss-el-api_2.2_spec

%build

%mvn_compat_version : %{namedversion} %{upstreamversion} %{version} 1
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_18.SP4jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_16.SP4jpp8
- java 8 mass update

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_11.SP4jpp7
- new version

