BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-saaj-1.3-api
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name: jboss-saaj-1.3-api
Version: 1.0.2
Release: alt2_3jpp7
Summary: SOAP with Attachments API for Java 1.3
Group: Development/Java
License: CDDL or GPLv2 with exceptions
URL: http://www.jboss.org

# git clone git://github.com/jboss/jboss-saaj-api_spec.git jboss-saaj-1.3-api
# cd jboss-saaj-1.3-api/ && git archive --format=tar --prefix=jboss-saaj-1.3-api-1.0.2.Final/ jboss-saaj-api_1.3_spec-1.0.2.Final | xz > jboss-saaj-1.3-api-1.0.2.Final.tar.xz
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
The SOAP with Attachments API for Java Version 1.3 classes.


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
install -pm 644 target/jboss-saaj-api_1.3_spec-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

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
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- new version

