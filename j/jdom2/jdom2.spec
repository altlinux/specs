Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jdom2
Version:       2.0.6
Release:       alt1_9jpp8
Summary:       Java manipulation of XML made easy
License:       ASL 1.1 or BSD
URL:           http://www.jdom.org/
Source0:       https://github.com/hunterhacker/jdom/archive/JDOM-%{version}.tar.gz
# originally taken from http://repo1.maven.org/maven2/org/jdom/jdom-contrib/1.1.3/jdom-contrib-1.1.3.pom
Source1:       jdom-contrib-template.pom
Source2:       jdom-junit-template.pom
# Bnd tool configuration
Source3:       bnd.properties
# Use system libraries
# Disable gpg signatures
# Process contrib and junit pom files
Patch0:        jdom-2.0.5-build.patch

BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: bea-stax-api
BuildRequires: isorelax
BuildRequires: jaxen
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
BuildRequires: log4j12
BuildRequires: objectweb-asm3
BuildRequires: aqute-bnd

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
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%patch0 -p1

cp -p %{SOURCE1} maven/contrib.pom
cp -p %{SOURCE2} maven/junit.pom

sed -i 's/\r//' LICENSE.txt README.txt

# Unable to run coverage: use log4j12 but switch to log4j 2.x
sed -i.coverage "s|coverage, jars|jars|" build.xml

build-jar-repository lib xerces-j2 xml-commons-apis jaxen junit isorelax xalan-j2 xalan-j2-serializer

%build
ant -Dversion=%{version} -Dj2se.apidoc=%{_javadocdir}/java maven

# Make jar into an OSGi bundle
bnd wrap --output build/package/jdom-%{version}.bar --properties %{SOURCE3} \
         --version %{version} build/package/jdom-%{version}.jar
mv build/package/jdom-%{version}.bar build/package/jdom-%{version}.jar

%install
%mvn_artifact build/maven/core/%{name}-%{version}.pom build/package/jdom-%{version}.jar
%mvn_artifact build/maven/core/%{name}-%{version}-contrib.pom build/package/jdom-%{version}-contrib.jar
%mvn_artifact build/maven/core/%{name}-%{version}-junit.pom build/package/jdom-%{version}-junit.jar
%mvn_install -J build/apidocs

%files -f .mfiles
%doc CHANGES.txt COMMITTERS.txt README.txt TODO.txt
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
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

