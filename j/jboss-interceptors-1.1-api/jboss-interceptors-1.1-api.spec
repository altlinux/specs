BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-interceptors-1.1-api
%define version 1.0.2
%global namedreltag .20120319git49a904
%global namedversion %{version}%{?namedreltag}

Name:             jboss-interceptors-1.1-api
Version:          1.0.2
Release:          alt2_0.3.20120319git49a904jpp7
Summary:          Interceptors 1.1 API
Group:            Development/Java
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-interceptors-api_spec.git jboss-interceptors-1.1-api
# cd jboss-interceptors-1.1-api/ && git archive --format=tar --prefix=jboss-interceptors-1.1-api/ 49a90471d8108b5b2a2da6063b5591a9f41ed24a | xz > jboss-interceptors-1.1-api-1.0.2.20120319git49a904.tar.xz
Source0:          jboss-interceptors-1.1-api-%{namedversion}.tar.xz

BuildRequires:    jboss-specs-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-eclipse-plugin

Requires:         jpackage-utils
BuildArch:        noarch
Source44: import.info

%description
This package contains The JavaEE Interceptors 1.1 API classes from JSR 318.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-interceptors-1.1-api

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-interceptors-api_1.1_spec-%{version}.Final-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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
%doc LICENSE README

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_0.3.20120319git49a904jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_0.3.20120319git49a904jpp7
- new version

