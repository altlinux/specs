BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-rmi-1.0-api
%define version 1.0.4
%define namedreltag .Final
%define namedversion %{version}%{?namedreltag}

Name: jboss-rmi-1.0-api
Version: 1.0.4
Release: alt1_3jpp7
Summary: Java Remote Method Invocation 1.0 API
Group: Development/Java
License: GPLv2 with exceptions
URL: http://www.jboss.org

# git clone https://github.com/jboss/jboss-rmi-api_spec
# cd jboss-rmi-api_spec/ && git archive --format=tar --prefix=jboss-rmi-1.0-api-1.0.4.Final/ jboss-rmi-api_1.0_spec-1.0.4.Final | xz > jboss-rmi-1.0-api-1.0.4.Final.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

# Remove the implementation, as it needs jacorb and we want the interface only
# at the moment (the sources are removed as well before building):
Patch0: %{name}-remove-implementation.patch

# Fix the address of the FSF in the license file:
Patch1: %{name}-fix-fsf-address.patch

BuildRequires: jboss-parent
BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

Requires: jpackage-utils

BuildArch:noarch
Source44: import.info


%description
Java Remote Method Invocation 1.0 API classes.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc	
This package contains the API documentation for %{name}.


%prep

# Unpack the sources:
%setup -q -n %{name}-%{namedversion}

# Apply the patches:
%patch0 -p1
%patch1 -p1

# Remove all the implementation classes and resources as we want the interfaces
# only at the moment:
rm -rf src/main/resources/org
rm -rf src/main/java/org


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/jboss-rmi-api_1.0_spec-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc src/main/resources/LICENSE


%files javadoc
%{_javadocdir}/%{name}
%doc src/main/resources/LICENSE


%changelog
* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3jpp7
- new version

