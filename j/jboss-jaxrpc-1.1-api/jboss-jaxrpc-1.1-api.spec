# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaxrpc-1.1-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaxrpc-1.1-api
Version:          1.0.1
Release:          alt3_1jpp7
Summary:          Java API for XML-Based RPC (JAX-RPC) 1.1
Group:            Development/Java
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-jaxrpc-api_spec.git jboss-jaxrpc-1.1-api
# cd jboss-jaxrpc-1.1-api/ && git archive --format=tar --prefix=jboss-jaxrpc-1.1-api/ jboss-jaxrpc-api_1.1_spec-1.0.1.Final | xz > jboss-jaxrpc-1.1-api-1.0.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    jboss-servlet-3.0-api
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
BuildRequires:    maven-ejb-plugin

Requires:         jboss-servlet-3.0-api
Requires:         jpackage-utils

BuildArch:        noarch
Source44: import.info

%description
The JAX-RPC 1.1 API classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q -n jboss-jaxrpc-1.1-api

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-jaxrpc-api_1.1_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc README LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_1jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_1jpp7
- fc update

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.1.20120309gita3c227jpp7
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_0.1.20120309gita3c227jpp7
- new version

