# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cdi-api
%define version 1.0
%global namedreltag .SP4
%global namedversion %{version}%{?namedreltag}

Name:             cdi-api
Version:          1.0
Release:          alt1_6.SP4jpp7
Summary:          CDI API
Group:            Development/Java
License:          ASL 2.0
URL:              http://seamframework.org/Weld

# svn export http://anonsvn.jboss.org/repos/weld/cdi-api/tags/1.0-SP4/ cdi-api-1.0.SP4
# tar cafJ cdi-api-1.0.SP4.tar.xz cdi-api-1.0.SP4
Source0:          cdi-api-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    maven-enforcer-plugin
BuildRequires:    testng
BuildRequires:    jboss-el-2.2-api
BuildRequires:    jboss-interceptors-1.1-api
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    geronimo-annotation
BuildRequires:    weld-parent

Requires:         jpackage-utils
Requires:         jboss-el-2.2-api
Requires:         jboss-interceptors-1.1-api
Requires:         jboss-ejb-3.1-api
Requires:         geronimo-annotation
Source44: import.info

%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q -n cdi-api-%{namedversion}

%build
mvn-rpmbuild package javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

# JAR
install -pm 644 target/cdi-api-%{version}-SP4.jar %{buildroot}%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap

# APIDOCS
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6.SP4jpp7
- fc update

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4.SP4jpp7
- new version

