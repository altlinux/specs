# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 18
Name:             guacamole-ext
Version:          0.7.0
Release:          alt1_2jpp7
Summary:          Common interfaces for extending the main Guacamole web application
License:          MPLv1.1 or GPLv2+ or LGPLv2+
Group:            Development/Java
URL:              http://guac-dev.org/
Source0:          http://guac-dev.org/pub/dist/source/%{name}-%{version}.tar.gz
BuildArch:        noarch

# Generic Buildrequires:
# https://fedoraproject.org/wiki/Packaging:Java#maven_3

# Specific ones:
BuildRequires:    guacamole-common >= 0.7.0
Requires:         guacamole-common >= 0.7.0
%if 0%{?fedora} || 0%{?rhel} > 6
%else
%endif
Source44: import.info

%description
Guacamole is an HTML5 web application that provides access to desktop
environments using remote desktop protocols such as VNC or RDP. A centralized
server acts as a tunnel and proxy, allowing access to multiple desktops through
a web browser. No plugins are needed: the client requires nothing more than a
web browser supporting HTML5 and AJAX.

%%{name} is a Java library used by the Guacamole web application to allow
its built-in functionality, such as authentication, to be extended or modified.
%%{name} provides an interface for retrieving a set of authorized
connection configurations for a given set of arbitrary credentials. Classes
implementing this interface can be referenced in guacamole.properties to allow
different authentication mechanisms (such as LDAP or SSL client authentication)
to be used. 

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q -n %{name}-%{version}

%build
mvn-rpmbuild install javadoc:aggregate

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}/guacamole
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/guacamole/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.guacamole-%{name}.pom

%add_maven_depmap JPP.guacamole-%{name}.pom guacamole/%{name}.jar


%files
%doc LICENSE README
%{_mavenpomdir}/JPP.guacamole-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/guacamole/%{name}.jar

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}


%changelog
* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_2jpp7
- fc update

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_2jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_6jpp7
- new version

