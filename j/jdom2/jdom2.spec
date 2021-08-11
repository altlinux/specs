Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:          jdom2
Version:       2.0.6
Release:       alt1_23jpp11
Summary:       Java manipulation of XML made easy
License:       Saxpath
URL:           http://www.jdom.org/
# ./generate-tarball.sh
Source0:       %{name}-%{version}.tar.gz
# Bnd tool configuration
Source3:       bnd.properties
# Remove bundled jars that might not have clear licensing
Source4:       generate-tarball.sh
# Use system libraries
# Disable gpg signatures
# Process contrib and junit pom files
Patch0:        0001-Adapt-build.patch

BuildRequires: javapackages-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires: ant
BuildRequires: ant-junit
%endif

BuildArch:     noarch
Source44: import.info

%description
JDOM is a Java-oriented object model which models XML documents.
It provides a Java-centric means of generating and manipulating
XML documents. While JDOM inter-operates well with existing
standards such as the Simple API for XML (SAX) and the Document
Object Model (DOM), it is not an abstraction layer or
enhancement to those APIs. Rather, it seeks to provide a robust,
light-weight means of reading and writing XML data without the
complex and memory-consumptive options that current API
offerings provide.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jdom-JDOM-%{version}

%patch0 -p1

sed -i 's/\r//' LICENSE.txt README.txt

# Unable to run coverage: use log4j12 but switch to log4j 2.x
sed -i.coverage "s|coverage, jars|jars|" build.xml

# XPath functionality is not needed
rm -rf core/src/java/org/jdom2/xpath/
sed -i '/import org.jdom2.xpath.XPathFactory/d' core/src/java/org/jdom2/JDOMConstants.java

%build
mkdir lib
%ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Dversion=%{version} -Dcompile.source=1.6 -Dcompile.target=1.6 -Dj2se.apidoc=%{_javadocdir}/java maven

# Make jar into an OSGi bundle
# XXX disabled until BND is fixed
#bnd wrap --output build/package/jdom-%{version}.bar --properties %{SOURCE3} \
#         --version %{version} build/package/jdom-%{version}.jar
#mv build/package/jdom-%{version}.bar build/package/jdom-%{version}.jar

%install
%mvn_artifact build/maven/core/%{name}-%{version}.pom build/package/jdom-%{version}.jar
%mvn_install -J build/apidocs

%files -f .mfiles
%doc CHANGES.txt COMMITTERS.txt README.txt TODO.txt
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.0.6-alt1_23jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.0.6-alt1_21jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.0.6-alt1_19jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_15jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_13jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_8jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_5jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_4jpp8
- new version

