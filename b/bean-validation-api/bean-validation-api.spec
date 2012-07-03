BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name bean-validation-api
%define version 1.0.0
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             bean-validation-api
Version:          1.0.0
Release:          alt1_4jpp7
Summary:          Bean Validation API
Group:            Development/Java
License:          ASL 2.0
URL:              http://www.hibernate.org/subprojects/validator.html

# svn export http://anonsvn.jboss.org/repos/hibernate/beanvalidation/api/tags/v1_0_0_GA/ bean-validation-api-1.0.0.GA
# tar czf bean-validation-api-1.0.0.GA-src-svn.tar.gz bean-validation-api-1.0.0.GA
Source0:          %{name}-%{namedversion}-src-svn.tar.gz

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit

Requires:         jpackage-utils
BuildArch:        noarch
Source44: import.info

%description
This package contains Bean Validation (JSR-303) API

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/validation-api-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc license.txt

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp7
- fc build

