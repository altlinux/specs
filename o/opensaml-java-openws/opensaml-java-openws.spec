# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           opensaml-java-openws
Version:        1.4.4
Release:        alt1_6jpp7
Summary:        Java OpenWS library
License:        ASL 2.0
Group:          Development/Java
URL:            http://www.opensaml.org/

# svn export https://svn.shibboleth.net/java-openws/tags/1.4.4/ opensaml-java-openws-1.4.4
# tar cafJ opensaml-java-openws-1.4.4.tar.xz opensaml-java-openws-1.4.4
Source0:        opensaml-java-openws-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  opensaml-java-parent
BuildRequires:  opensaml-java-xmltooling
BuildRequires:  xalan-j2
BuildRequires:  apache-commons-codec
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  tomcat-servlet-3.0-api
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
BuildRequires:  junit
BuildRequires:  logback
Source44: import.info

%description
The OpenWS library provides a growing set of tools to work with web services at
a low level. These tools include classes for creating and reading SOAP
messages, transport-independent clients for connecting to web services,
and various transports for use with those clients.

%package javadoc
Summary:       Javadocs for %{name}
Group:         Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

sed -i "s|\${xerces.groupId}|xerces|" pom.xml

%pom_remove_dep "xerces:xml-apis"
%pom_remove_dep "xerces:serializer"

%build
# tests disabled because of missing dependency org.springframework:spring-mock
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc doc
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc doc

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt1_4jpp7
- new release

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt1_2jpp7
- fc update

