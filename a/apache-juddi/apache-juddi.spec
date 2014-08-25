BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             apache-juddi
Version:          3.1.4
Release:          alt2_4jpp7
Summary:          Client API for UDDI
Group:            Development/Java
License:          ASL 2.0
URL:              http://juddi.apache.org/

# svn export http://svn.apache.org/repos/asf/juddi/tags/juddi-3.1.4/ apache-juddi
# tar cafJ apache-juddi-3.1.4.tar.xz apache-juddi
Source0:          %{name}-%{version}.tar.xz

Patch1:           0001-Build-only-client-module.patch
Patch2:           0002-Change-jaxws-api-dependency.patch
Patch3:           0003-Disable-ReadWSDLTest.readFromJar.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    jboss-jaxws-2.2-api
BuildRequires:    wsdl4j
Source44: import.info

%description
jUDDI is an open source Java implementation of the Universal Description,
Discovery, and Integration (UDDI v3) specification for Web Services.

This package includes only the client side of jUDDI.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc RELEASE_NOTES.html LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt2_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt2_1jpp7
- rebuild with maven-local

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_1jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.3-alt1_4jpp7
- new release

