# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          msv
Epoch:         1
Version:       2013.5.1
Release:       alt1_6jpp7
Summary:       Multi-Schema Validator
Group:         Development/Java
License:       BSD and ASL 1.1
URL:           http://msv.java.net/

# To generate tarball from upstream source control:
# $ ./create-tarball
Source0:       %{name}-%{version}-clean.tar.gz

# Parent POM is no longer in svn, get it from Maven central repository
Source1:       http://repo1.maven.org/maven2/net/java/dev/%{name}/%{name}-parent/2009.1/%{name}-parent-2009.1.pom

Source2:       http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:       create-tarball.sh

# Use CatalogResolver from xml-commons-resolver package
Patch1:        %{name}-Use-CatalogResolver-class-from-xml-commons-resolver.patch

BuildRequires: java-javadoc
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-plugin-build-helper
BuildRequires: isorelax
BuildRequires: isorelax-javadoc
BuildRequires: relaxngDatatype
BuildRequires: relaxngDatatype-javadoc
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: junit
BuildRequires: jvnet-parent
BuildRequires: xml-commons-resolver
BuildRequires: isorelax

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
Summary:       Multi-Schema Validator Core
Group:         Development/Java
# src/com/sun/msv/reader/xmlschema/DOMLSInputImpl.java is under ASL 2.0
# msv/src/com/sun/msv/writer/ContentHandlerAdaptor.java is partially under Public Domain
License:       BSD and ASL 1.1 and ASL 2.0 and Public Domain
Requires:      jpackage-utils
Requires:      isorelax
Requires:      relaxngDatatype
Requires:      xerces-j2
Requires:      msv-xsdlib

%description   msv
%{summary}.

%package       rngconv
Summary:       Multi-Schema Validator RNG Converter
Group:         Development/Java
Requires:      jpackage-utils
Requires:      isorelax
Requires:      relaxngDatatype
Requires:      xerces-j2
Requires:      msv-msv
Requires:      msv-xsdlib

%description   rngconv
%{summary}.

%package       xmlgen
Summary:       Multi-Schema Validator Generator
Group:         Development/Java
Requires:      jpackage-utils
Requires:      isorelax
Requires:      relaxngDatatype
Requires:      xerces-j2
Requires:      msv-msv
Requires:      msv-xsdlib

%description    xmlgen
%{summary}.

%package       xsdlib
Summary:       Multi-Schema Validator XML Schema Library
Group:         Development/Java
Requires:      jpackage-utils
Requires:      isorelax
Requires:      relaxngDatatype
Requires:      xerces-j2

%description   xsdlib
%{summary}.

 Sun XML Datatypes Library. An implementation of W3C XML Schema Part 2.

%package       javadoc
Summary:       API documentation for Multi-Schema Validator
Group:         Development/Java
License:       BSD and ASL 1.1 and ASL 2.0 and Public Domain
Requires:      java-javadoc
Requires:      jpackage-utils
Requires:      isorelax-javadoc
Requires:      relaxngDatatype-javadoc
BuildArch: noarch

%description   javadoc
%{summary}.

%package       manual
Summary:       Manual for Multi-Schema Validator
Group:         Development/Java
License:       BSD
BuildArch: noarch

%description   manual
%{summary}.

%package       demo
Summary:       Samples for Multi-Schema Validator
Group:         Development/Java
License:       BSD
Requires:      msv-msv
Requires:      msv-xsdlib
Requires:      jpackage-utils

%description   demo
%{summary}.

%prep
%setup -q

# We don't have this plugin
%pom_remove_plugin :buildnumber-maven-plugin

# Needed becuase of patch3
%pom_add_dep xml-resolver:xml-resolver

cp %{SOURCE1} parent-pom.xml

# ASL 2.0 license text
cp %{SOURCE2} Apache-LICENSE-2.0.txt

# Delete anything pre-compiled
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.zip' -exec rm -f '{}' \;

# Delete class-path entries from manifests
for m in $(find . -name MANIFEST.MF) ; do
  sed --in-place -e '/^[Cc]lass-[Pp]ath:/d' $m
done

# Apply patches
%patch1 -p1

# Fix isorelax groupId
%pom_xpath_replace "pom:dependency[pom:groupId[text()='com.sun.xml.bind.jaxb']]/pom:groupId" "<groupId>isorelax</groupId>"
%pom_xpath_replace "pom:dependency[pom:groupId[text()='com.sun.xml.bind.jaxb']]/pom:groupId" "<groupId>isorelax</groupId>" generator
%pom_xpath_replace "pom:dependency[pom:groupId[text()='com.sun.xml.bind.jaxb']]/pom:groupId" "<groupId>isorelax</groupId>" msv
%pom_xpath_replace "pom:dependency[pom:groupId[text()='com.sun.xml.bind.jaxb']]/pom:groupId" "<groupId>isorelax</groupId>" rngconverter
%pom_xpath_replace "pom:dependency[pom:groupId[text()='com.sun.xml.bind.jaxb']]/pom:groupId" "<groupId>isorelax</groupId>" xsdlib

# Change encoding of non utf-8 files
for m in $(find . -name copyright.txt) ; do
  iconv -f iso-8859-1 -t utf-8 < $m > $m.utf8
  mv $m.utf8 $m
done

%build
mvn-rpmbuild -Dmaven.test.failure.ignore=true install javadoc:aggregate

%install
# Jars
install -pD -T msv/target/%{name}-core-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-core.jar
install -pD -T rngconverter/target/%{name}-rngconverter-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-rngconverter.jar
install -pD -T generator/target/%{name}-generator-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-generator.jar
install -pD -T xsdlib/target/xsdlib-%{version}.jar \
  %{buildroot}%{_javadir}/xsdlib.jar
install -pD -T testharness/target/%{name}-testharness-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-testharness.jar

# Alternate jar names
ln -s %{name}-core.jar         \
  %{buildroot}%{_javadir}/%{name}-msv.jar
ln -s %{name}-rngconverter.jar \
  %{buildroot}%{_javadir}/%{name}-rngconv.jar
ln -s %{name}-generator.jar    \
  %{buildroot}%{_javadir}/%{name}-xmlgen.jar
ln -s xsdlib.jar               \
  %{buildroot}%{_javadir}/%{name}-xsdlib.jar

# Poms
install -pD -T -m 644 pom.xml              %{buildroot}%{_mavenpomdir}/JPP-msv.pom
install -pD -T -m 644 parent-pom.xml       %{buildroot}%{_mavenpomdir}/JPP-msv-parent.pom
install -pD -T -m 644 msv/pom.xml          %{buildroot}%{_mavenpomdir}/JPP-msv-core.pom
install -pD -T -m 644 rngconverter/pom.xml %{buildroot}%{_mavenpomdir}/JPP-msv-rngconverter.pom
install -pD -T -m 644 generator/pom.xml    %{buildroot}%{_mavenpomdir}/JPP-msv-generator.pom
install -pD -T -m 644 testharness/pom.xml  %{buildroot}%{_mavenpomdir}/JPP-msv-testharness.pom
install -pD -T -m 644 xsdlib/pom.xml       %{buildroot}%{_mavenpomdir}/JPP-xsdlib.pom
%add_maven_depmap JPP-%{name}.pom
%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}-core.pom         %{name}-core.jar -a "msv:msv"
%add_maven_depmap JPP-%{name}-rngconverter.pom %{name}-rngconverter.jar
%add_maven_depmap JPP-%{name}-generator.pom    %{name}-generator.jar
%add_maven_depmap JPP-%{name}-testharness.pom  %{name}-testharness.jar
%add_maven_depmap JPP-xsdlib.pom               xsdlib.jar -a "com.sun.msv.datatype.xsd:xsdlib"

# Javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

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
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/msv
cp -pr msv/examples/* %{buildroot}%{_datadir}/%{name}-%{version}/msv
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/xsdlib
cp -pr xsdlib/examples/* %{buildroot}%{_datadir}/%{name}-%{version}/xsdlib

# Scripts
%jpackage_script com.sun.msv.driver.textui.Driver "" "" msv-msv:msv-xsdlib:relaxngDatatype:isorelax msv true
%jpackage_script com.sun.msv.generator.Driver "" "" msv-xmlgen:msv-msv:msv-xsdlib:relaxngDatatype:isorelax:xerces-j2 xmlgen true
%jpackage_script com.sun.msv.writer.relaxng.Driver "" "" msv-rngconv:msv-msv:msv-xsdlib:relaxngDatatype:isorelax:xerces-j2 rngconv true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/msv.conf`
touch $RPM_BUILD_ROOT/etc/java/msv.conf

%files msv
%{_bindir}/msv
%{_mavenpomdir}/JPP-%{name}-core.pom
%{_mavenpomdir}/JPP-%{name}-testharness.pom
%{_javadir}/%{name}-core.jar
%{_javadir}/%{name}-msv.jar
%{_javadir}/%{name}-testharness*
%doc License.txt
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc Apache-LICENSE-2.0.txt
%config(noreplace,missingok) /etc/java/msv.conf

%files rngconv
%{_bindir}/rngconv
%{_mavenpomdir}/JPP-%{name}-rngconverter.pom
%{_javadir}/%{name}-rngconverter.jar
%{_javadir}/%{name}-rngconv.jar
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc License.txt

%files xmlgen
%{_bindir}/xmlgen
%{_mavenpomdir}/JPP-%{name}-generator.pom
%{_javadir}/%{name}-generator.jar
%{_javadir}/%{name}-xmlgen.jar
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc License.txt

%files xsdlib
%{_mavenpomdir}/JPP-xsdlib.pom
%{_javadir}/xsdlib.jar
%{_javadir}/%{name}-xsdlib.jar
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc License.txt

# This subpackage wins the parent poms and the depmap because all the other
# subpackages require this one
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-parent.pom
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}
%doc License.txt
%doc msv/doc/Apache-LICENSE-1.1.txt
%doc Apache-LICENSE-2.0.txt

%files manual
%doc %{_docdir}/%{name}
%doc License.txt

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2013.5.1-alt1_6jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:2013.2.3-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:2009.1-alt4_12jpp7
- dropped compat msv provides

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:2009.1-alt3_12jpp7
- fixed deps

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
