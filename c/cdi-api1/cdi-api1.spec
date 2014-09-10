# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cdi-api1
%define version 1.0
%global namedtag SP4
%global namedreltag .%{namedtag}
%global namedversion %{version}%{?namedreltag}
%global upstreamversion %{version}-%{namedtag}

Name:             cdi-api1
Version:          1.0
Release:          alt1_11.SP4jpp7
Summary:          CDI API 1.0
Group:            Development/Java
License:          ASL 2.0
URL:              http://seamframework.org/Weld

# svn export http://anonsvn.jboss.org/repos/weld/cdi-api/tags/1.0-SP4/ cdi-api-1.0.SP4
# tar cafJ cdi-api-1.0.SP4.tar.xz cdi-api-1.0.SP4
Source0:          cdi-api-%{namedversion}.tar.xz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-build-helper
BuildRequires:    testng
BuildRequires:    jboss-el-2.2-api
BuildRequires:    jboss-interceptors-1.1-api
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    geronimo-annotation
BuildRequires:    geronimo-parent-poms
BuildRequires:    weld-parent
BuildRequires:    jpackage-utils

Requires:         jpackage-utils
Requires:         jboss-el-2.2-api
Requires:         jboss-interceptors-1.1-api
Requires:         jboss-ejb-3.1-api
Requires:         geronimo-annotation
Source44: import.info

%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.
Group:            Documentation
Requires:         jpackage-utils

%prep
%setup -q -n cdi-api-%{namedversion}

cp %{SOURCE1} .

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

# JAR
install -pm 644 target/cdi-api-%{upstreamversion}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar

# POM
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom

%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar -v "1,%{upstreamversion}"

# JAVADOC
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE-2.0.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_11.SP4jpp7
- new version

