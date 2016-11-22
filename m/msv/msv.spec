Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          msv
Epoch:         1
Version:       2013.6.1
Release:       alt1_8jpp8
Summary:       Multi-Schema Validator
License:       BSD and ASL 1.1
URL:           http://msv.java.net/

# To generate tarball from upstream source control:
# $ ./create-tarball
Source0:       %{name}-%{version}-clean.tar.gz

Source2:       http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:       create-tarball.sh

# Use CatalogResolver from xml-commons-resolver package
Patch1:        %{name}-Use-CatalogResolver-class-from-xml-commons-resolver.patch

BuildRequires:  maven-local
BuildRequires:  mvn(isorelax:isorelax)
BuildRequires:  mvn(jdom:jdom)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-resolver:xml-resolver)

BuildArch:     noarch

Obsoletes:     %{name}-relames < %{version}-%{release}
Source44: import.info

%description
The Sun Multi-Schema XML Validator (MSV) is a Java technology tool to validate
XML documents against several kinds of XML schemata. It supports RELAX NG,
RELAX Namespace, RELAX Core, TREX, XML DTDs, and a subset of XML Schema Part 1.
This latest (version 1.2) release includes several bug fixes and adds better
conformance to RELAX NG/W3C XML standards and JAXP masquerading.

%package       msv
Group: Development/Java
Summary:       Multi-Schema Validator Core
# src/com/sun/msv/reader/xmlschema/DOMLSInputImpl.java is under ASL 2.0
# msv/src/com/sun/msv/writer/ContentHandlerAdaptor.java is partially under Public Domain
License:       BSD and ASL 1.1 and ASL 2.0 and Public Domain

%description   msv
%{summary}.

%package       rngconv
Group: Development/Java
Summary:       Multi-Schema Validator RNG Converter

%description   rngconv
%{summary}.

%package       xmlgen
Group: Development/Java
Summary:       Multi-Schema Validator Generator

%description   xmlgen
%{summary}.

%package       xsdlib
Group: Development/Java
Summary:       Multi-Schema Validator XML Schema Library

%description   xsdlib
%{summary}.

 Sun XML Datatypes Library. An implementation of W3C XML Schema Part 2.

%package       javadoc
Group: Development/Java
Summary:       API documentation for Multi-Schema Validator
License:       BSD and ASL 1.1 and ASL 2.0 and Public Domain
BuildArch: noarch

%description   javadoc
%{summary}.

%package       manual
Group: Development/Java
Summary:       Manual for Multi-Schema Validator
License:       BSD
BuildArch: noarch

%description   manual
%{summary}.

%package       demo
Group: Development/Java
Summary:       Samples for Multi-Schema Validator
License:       BSD
Requires:      msv-msv
Requires:      msv-xsdlib

%description   demo
%{summary}.

%prep
%setup -q

# We don't have this plugin
%pom_remove_plugin :buildnumber-maven-plugin

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin

# Needed becuase of patch3
%pom_add_dep xml-resolver:xml-resolver

# ASL 2.0 license text
cp %{SOURCE2} Apache-LICENSE-2.0.txt

# Delete anything pre-compiled
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.zip' -exec rm -f '{}' \;

# Test sources in default package break BND
rm -f testharness/src/*.java

# Delete class-path entries from manifests
for m in $(find . -name MANIFEST.MF) ; do
  sed --in-place -e '/^[Cc]lass-[Pp]ath:/d' $m
done

# Apply patches
%patch1 -p1

# Fix isorelax groupId
%pom_xpath_replace "pom:dependency[pom:groupId[text()='com.sun.xml.bind.jaxb']]/pom:groupId" "<groupId>isorelax</groupId>"
%pom_xpath_replace "pom:dependency[pom:groupId[text()='com.sun.xml.bind.jaxb']]/pom:groupId" "<groupId>isorelax</groupId>" msv

# Change encoding of non utf-8 files
for m in $(find . -name copyright.txt) ; do
  iconv -f iso-8859-1 -t utf-8 < $m > $m.utf8
  mv $m.utf8 $m
done

%mvn_file ":%{name}-core" %{name}-core %{name}-%{name}
%mvn_file ":%{name}-rngconverter" %{name}-rngconverter %{name}-rngconv
%mvn_file ":%{name}-generator" %{name}-generator %{name}-xmlgen
%mvn_file ":xsdlib" xsdlib %{name}-xsdlib

%mvn_alias ":xsdlib" "com.sun.msv.datatype.xsd:xsdlib"

%mvn_package ":*::{tests,javadoc,sources}:" __noinstall
%mvn_package ":%{name}{,-testharness}::{}:" __noinstall
%mvn_package ":%{name}{,-core}::{}:" %{name}-msv

%build
%mvn_build -s

%install
%mvn_install

# Manuals
install -d -m 755 %{buildroot}%{_docdir}/%{name}/msv
install -m 644 msv/doc/*.html     %{buildroot}%{_docdir}/%{name}/msv
install -m 644 msv/doc/*.gif      %{buildroot}%{_docdir}/%{name}/msv
install -m 644 msv/doc/README.txt %{buildroot}%{_docdir}/%{name}/msv

install -d -m 755 %{buildroot}%{_docdir}/%{name}/rngconverter
install -m 644 rngconverter/README.txt %{buildroot}%{_docdir}/%{name}/rngconverter

install -d -m 755 %{buildroot}%{_docdir}/%{name}/generator
install -m 644 generator/*.html     %{buildroot}%{_docdir}/%{name}/generator
install -m 644 generator/README.txt %{buildroot}%{_docdir}/%{name}/generator

install -d -m 755 %{buildroot}%{_docdir}/%{name}/xsdlib
install -m 644 xsdlib/*.html     %{buildroot}%{_docdir}/%{name}/xsdlib
install -m 644 xsdlib/README.txt %{buildroot}%{_docdir}/%{name}/xsdlib

# Examples
install -d -m 755 %{buildroot}%{_datadir}/%{name}/msv
cp -pr msv/examples/* %{buildroot}%{_datadir}/%{name}/msv
install -d -m 755 %{buildroot}%{_datadir}/%{name}/xsdlib
cp -pr xsdlib/examples/* %{buildroot}%{_datadir}/%{name}/xsdlib

# Scripts
%jpackage_script com.sun.msv.driver.textui.Driver "" "" msv-msv:msv-xsdlib:relaxngDatatype:isorelax msv true
%jpackage_script com.sun.msv.generator.Driver "" "" msv-xmlgen:msv-msv:msv-xsdlib:relaxngDatatype:isorelax:xerces-j2 xmlgen true
%jpackage_script com.sun.msv.writer.relaxng.Driver "" "" msv-rngconv:msv-msv:msv-xsdlib:relaxngDatatype:isorelax:xerces-j2 rngconv true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/msv.conf`
touch $RPM_BUILD_ROOT/etc/java/msv.conf

%files msv -f .mfiles-msv-msv
%{_bindir}/msv
%doc License.txt
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc Apache-LICENSE-2.0.txt
%config(noreplace,missingok) /etc/java/msv.conf

%files rngconv -f .mfiles-msv-rngconverter
%{_bindir}/rngconv
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc License.txt

%files xmlgen -f .mfiles-msv-generator
%{_bindir}/xmlgen
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc License.txt

%files xsdlib -f .mfiles-xsdlib
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc License.txt

%files javadoc -f .mfiles-javadoc
%doc License.txt
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc Apache-LICENSE-2.0.txt

%files manual
%doc %{_docdir}/%{name}
%doc License.txt

%files demo
%{_datadir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2013.6.1-alt1_8jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1:2013.6.1-alt1_7jpp8
- java8 mass update

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1:2009.1-alt2_12jpp7
- applied repocop patches

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:2009.1-alt1_12jpp7
- new version

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_0.20050722.7jpp6
- ant 18 support; added description (closes: #22125)

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_0.20050722.6jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_0.20050722.6jpp5
- fixed docdir ownership

* Fri Sep 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_0.20050722.6jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.20050722.6jpp5
- converted from JPackage by jppimport script

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.20050722.3jpp1.7
- build without bootstrap

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1_0.20050722.3jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt0.1
- Initial build for ALT Linux Sisyphus
- cvs version 20050424
