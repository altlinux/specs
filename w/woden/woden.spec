BuildRequires: apache-parent
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oversion 1.0M9

Name:           woden
Version:        1.0
Release:        alt2_0.14.M9jpp8
Summary:        Web Service Description Language (WSDL) validating parser
License:        ASL 2.0
URL:            http://ws.apache.org/woden/
# svn export https://svn.apache.org/repos/asf/webservices/woden/tags/1.0M9/ woden-1.0M9
# tar caf woden-1.0M9.tar.xz woden-1.0M9
Source0:        %{name}-%{oversion}.tar.xz
BuildArch:      noarch
  
BuildRequires: maven-local
BuildRequires: XmlSchema
BuildRequires: apache-commons-logging
BuildRequires: log4j12
BuildRequires: xerces-j2
BuildRequires: axiom
BuildRequires: maven-plugin-bundle
Source44: import.info

Provides: ws-commons-%name = %version-%release
Conflicts:  ws-commons-%name <= 1.0-alt3_0.5.M9jpp7
Obsoletes:  ws-commons-%name <= 1.0-alt3_0.5.M9jpp7


%description
The Woden project is a sub-project of the Apache Web Services Project
to develop a Java class library for reading, manipulating, creating
and writing WSDL documents, initially to support WSDL 2.0 but with the
longer term aim of supporting past, present and future versions of WSDL.

%package javadoc
Group: Development/Java
Summary:      API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{oversion}

# Disable modules whose dependencies are not present in Fedora.  
%pom_disable_module woden-tests
%pom_disable_module woden-tool
%pom_disable_module woden-converter-maven-plugin
%pom_disable_module woden-ant

# This test should be excluded on java >= 5
rm woden-qname/src/test/java/javax/xml/namespace/QNameDeserializeTest.java

sed -i "s|<lof4j.version>1.2.15</lof4j.version>|<lof4j.version>1.2.17</lof4j.version>|" pom.xml

%build
%mvn_build

# Fix encoding
iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.utf8
mv LICENSE.utf8 LICENSE

%install
%mvn_install

%files -f .mfiles
%doc README release-notes.html
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.14.M9jpp8
- added BR: apache-parent for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.14.M9jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.13.M9jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.12.M9jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.11.M9jpp8
- java 8 mass update

