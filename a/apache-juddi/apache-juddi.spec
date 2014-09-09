BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             apache-juddi
Version:          3.1.5
Release:          alt1_2jpp7
Summary:          Client API for UDDI
Group:            Development/Java
License:          ASL 2.0
URL:              http://juddi.apache.org/

# svn export http://svn.apache.org/repos/asf/juddi/tags/juddi-3.1.5/ apache-juddi
# tar cafJ apache-juddi-3.1.5.tar.xz apache-juddi
Source0:          %{name}-%{version}.tar.xz

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
%patch3 -p1

%pom_disable_module uddi-tck-base
%pom_disable_module juddi-core
%pom_disable_module juddi-core-openjpa
%pom_disable_module juddiv3-war
%pom_disable_module juddi-examples
%pom_disable_module juddi-tomcat
%pom_disable_module uddi-tck

%pom_xpath_set "pom:groupId[text()='org.apache.geronimo.specs']" "org.jboss.spec.javax.xml.ws" uddi-ws
%pom_xpath_set "pom:artifactId[text()='geronimo-jaxws_2.2_spec']" "jboss-jaxws-api_2.2_spec" uddi-ws

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc RELEASE_NOTES.html LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt2_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt2_1jpp7
- rebuild with maven-local

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_1jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.3-alt1_4jpp7
- new release

