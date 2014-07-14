BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-connector-1.6-api
%define version 1.0.1
%global namedreltag .20120310git9dc9a5
%global namedversion %{version}%{?namedreltag}

Name:             jboss-connector-1.6-api
Version:          1.0.1
Release:          alt2_0.3.20120310git9dc9a5jpp7
Summary:          Connector Architecture 1.6 API
Group:            Development/Java
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-connector-api_spec.git jboss-connector-1.6-api
# cd jboss-connector-1.6-api/ && git archive --format=tar --prefix=jboss-connector-1.6-api/ 9dc9a58fb8672609790db93abcaac3875901243c | xz > jboss-connector-1.6-api-1.0.1.20120310git9dc9a5.tar.xz

Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    jboss-specs-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    jboss-transaction-1.1-api

Requires:         jboss-transaction-1.1-api
Requires:         jpackage-utils

BuildArch:        noarch
Source44: import.info

%description
Java EE Connector Architecture 1.6 API classes

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%build
export LANG=en_US.ISO8859-1
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-connector-api_1.6_spec-%{version}-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc README LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.3.20120310git9dc9a5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_0.3.20120310git9dc9a5jpp7
- new version

