BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaxb-2.2-api
%define version 1.0.4
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name: jboss-jaxb-2.2-api
Version: 1.0.4
Release: alt2_3jpp7
Summary: Java Architecture for XML Binding 2.2
Group: Development/Java
License: CDDL or GPLv2 with exceptions
URL: http://www.jboss.org

# git clone git://github.com/jboss/jboss-jaxb-api_spec.git jboss-jaxb-2.2-api
# cd jboss-jaxb-2.2-api/ && git archive --format=tar --prefix=jboss-jaxb-2.2-api-1.0.4.Final/ jboss-jaxb-api_2.2_spec-1.0.4.Final | xz > jboss-jaxb-2.2-api-1.0.4.Final.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

Requires: jpackage-utils
Source44: import.info


%description
Java Architecture for XML Binding Version 2.2 classes.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{namedversion}


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/jboss-jaxb-api_2.2_spec-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE
%doc README


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE
%doc README


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3jpp7
- new release

