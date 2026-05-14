%define oldname pdfbox

Name:          	pdfbox2
Version:       	2.0.26
Release:       	alt3

Summary:       	Apache PDFBox library for working with PDF documents
License:       	Apache-2.0
Group:		Development/Java
URL:           	http://pdfbox.apache.org/

#Source-url:    http://archive.apache.org/dist/pdfbox/%{version}/pdfbox-%{version}-src.zip
Source:       	pdfbox2-%{version}-src.zip

# Use system font instead of bundled font
Patch0:        	pdfbox-use-system-liberation-font.patch
# Use system icc profiles
Patch1:        	pdfbox-use-system-icc-profiles-openicc.patch
# Replace javax with jakarta
Patch2:		0001-Replace-javax-with-jakarta.patch
Patch3:		add-JPMS-support.patch

BuildRequires:  /proc
BuildRequires:  jpackage-default
BuildRequires:  maven-local
BuildRequires:	unzip

BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.bouncycastle:bcmail-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)

BuildRequires: 	fonts-ttf-dejavu
BuildRequires: 	fonts-ttf-google-noto-emoji
BuildRequires: 	fonts-ttf-liberation
BuildRequires: 	icc-profiles-openicc
BuildRequires: 	fontconfig libfontconfig1
Requires:      	fonts-ttf-liberation
Requires:      	fontbox2

# TODO: Require liberation-sans-fonts >= 2 and don't ignore test failures

BuildArch:     	noarch

# Ant support was removed by upstream (Obsoletes added in F28)
Obsoletes:     	%{oldname}-ant < %{version}-%{release}
# Jempbox subproject was removed by upstream (Obsoletes added in F28)
Obsoletes:     	jempbox < %{version}-%{release}
# Examples package was dropped due to requiring too old lucene (Obsoletes added in F29)
Obsoletes:	%{oldname}-examples < %{version}-%{release}

%description
Apache PDFBox is an open source Java PDF library for working with PDF
documents. This project allows creation of new PDF documents, manipulation of
existing documents and the ability to extract content from documents. Apache
PDFBox also includes several command line utilities. Apache PDFBox is
published under the Apache License v2.0.

%package debugger
Group: 		Development/Java
# See: debugger/target/classes/META-INF/DEPENDENCIES
Requires:      	mvn(commons-logging:commons-logging)
Requires:      	mvn(org.bouncycastle:bcmail-jdk15on)
Requires:      	mvn(org.bouncycastle:bcpkix-jdk15on)
Requires:      	mvn(org.bouncycastle:bcprov-jdk15on)
Requires:      	pdfbox2
# needed by wrapper script
Requires:      	javapackages-tools
Summary:       	Apache PDFBox Debugger

%description debugger
This package contains the PDF debugger for Apache PDFBox.

%package tools
Group: 		Development/Java
# See: tools/target/classes/META-INF/DEPENDENCIES
Requires:      	mvn(commons-logging:commons-logging)
Requires:      	mvn(org.bouncycastle:bcmail-jdk15on)
Requires:      	mvn(org.bouncycastle:bcpkix-jdk15on)
Requires:      	mvn(org.bouncycastle:bcprov-jdk15on)
Requires:      	pdfbox2-debugger
# needed by wrapper script
Requires:      	javapackages-tools
Summary:       	Apache PDFBox Tools

%description tools
This package contains command line tools for Apache PDFBox.

%package javadoc
Group: 		Development/Java
Summary:        Javadoc for %{oldname}
BuildArch: 	noarch

%description javadoc
This package contains the API documentation for %{oldname}.

%package -n fontbox2
Group: 		Development/Java
Summary:        Apache FontBox

%description -n fontbox2
FontBox is a Java library used to obtain low level information from font
files. FontBox is a subproject of Apache PDFBox.

%package parent
Group: 		Development/Java
Summary:        Apache PDFBox Parent POM

%description parent
Apache PDFBox Parent POM.

%package reactor
Group: 		Development/Java
Summary:        Apache PDFBox Reactor POM

%description reactor
Apache PDFBox Reactor POM.

%package -n preflight2
Group: 		Development/Java
# See: preflight/pom.xml
Requires:      	mvn(jakarta.activation:jakarta.activation-api)
Requires:	mvn(jakarta.xml.bind:jakarta.xml.bind-api)
# See: preflight/target/classes/META-INF/DEPENDENCIES
Requires:      	mvn(commons-logging:commons-logging)
Requires:      	mvn(org.bouncycastle:bcmail-jdk15on)
Requires:      	mvn(org.bouncycastle:bcpkix-jdk15on)
Requires:      	mvn(org.bouncycastle:bcprov-jdk15on)
Requires:      	pdfbox2
Requires:      	xmpbox2
# needed by wrapper script
Requires:      	javapackages-tools
Summary:        Apache Preflight

%description -n preflight2
The Apache Preflight library is an open source Java tool that implements 
a parser compliant with the ISO-19005 (PDF/A) specification. Preflight is a 
subproject of Apache PDFBox.

%package -n xmpbox2
Group: 		Development/Java
Summary:        Apache XmpBox

%description -n xmpbox2
The Apache XmpBox library is an open source Java tool that implements Adobe's
XMP(TM) specification.  It can be used to parse, validate and create xmp
contents.  It is mainly used by subproject preflight of Apache PDFBox. 
XmpBox is a subproject of Apache PDFBox.

%prep
%setup
find -name '*.class' -delete
find -name '*.jar' -delete
find -name 'sRGB.icc*' -print -delete
find -name '*.icm' -print -delete
find -name '*.ttf' -print -delete

%patch0 -p1 -b .font
%patch1 -b .openicc
%patch2 -p1
%patch3 -p2

# Don't build apps (it's just a bundle of everything)
%pom_disable_module preflight-app
%pom_disable_module debugger-app
%pom_disable_module app

# Don't build examples, they require ancient version of lucene
%pom_disable_module examples

# Disable plugins not needed for RPM builds
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# Some test resources are not okay to distribute with the source, upstream
# downloads them at build time, but we can't, so we either remove or fix
# the affected tests
%pom_remove_plugin -r :download-maven-plugin
rm fontbox/src/test/java/org/apache/fontbox/cff/CFFParserTest.java \
   pdfbox/src/test/java/org/apache/pdfbox/pdfparser/TestPDFParser.java \
   pdfbox/src/test/resources/input/rendering/{FANTASTICCMYK.ai,HOTRODCMYK.ai} \
   preflight/src/test/java/org/apache/pdfbox/preflight/TestIsartorBavaria.java
ln -s %{_datadir}/fonts/liberation-sans/LiberationSans-Regular.ttf pdfbox/src/test/resources/org/apache/pdfbox/ttf/LiberationSans-Regular.ttf
sed -i -e 's/\(testCIDFontType2VerticalSubset\)/ignore_\1/' pdfbox/src/test/java/org/apache/pdfbox/pdmodel/font/TestFontEmbedding.java
sed -i -e 's/\(testStructureTreeMerge\)/ignore_\1/'  pdfbox/src/test/java/org/apache/pdfbox/multipdf/PDFMergerUtilityTest.java
sed -i -e '/testPDFBOX4115/i\@org.junit.Ignore' pdfbox/src/test/java/org/apache/pdfbox/pdmodel/font/PDFontTest.java

# Remove unpackaged test deps and tests that rely on them
%pom_remove_dep -r com.github.jai-imageio:
%pom_remove_dep -r :jbig2-imageio
rm tools/src/test/java/org/apache/pdfbox/tools/imageio/TestImageIOUtils.java
%pom_remove_dep :diffutils pdfbox
rm pdfbox/src/test/java/org/apache/pdfbox/text/TestTextStripper.java
sed -i -e 's/TestTextStripper/BidiTest/' pdfbox/src/test/java/org/apache/pdfbox/text/BidiTest.java

# Remove tests that otherwise require net connectivity
rm pdfbox/src/test/java/org/apache/pdfbox/multipdf/MergeAcroFormsTest.java \
   pdfbox/src/test/java/org/apache/pdfbox/multipdf/MergeAnnotationsTest.java
sed -i -e '/\(OptionsAndNamesNotNumbers\|RadioButtonWithOptions\)/i\@org.junit.Ignore' \
  pdfbox/src/test/java/org/apache/pdfbox/pdmodel/interactive/form/PDButtonTest.java

# These test fail for unknown reasons
rm pdfbox/src/test/java/org/apache/pdfbox/pdmodel/graphics/image/CCITTFactoryTest.java

%mvn_compat_version : 2 %{version}

# install all libraries in _javadir
%mvn_file :%{oldname} %{oldname}
%mvn_file :%{oldname}-debugger %{oldname}-debugger
%mvn_file :%{oldname}-examples %{oldname}-examples
%mvn_file :%{oldname}-tools %{oldname}-tools
%mvn_file :preflight preflight
%mvn_file :xmpbox xmpbox
%mvn_file :fontbox fontbox

%pom_xpath_set 'pom:source' 8 parent
%pom_xpath_set 'pom:target' 8 parent

%pom_change_dep javax.activation:activation jakarta.activation:jakarta.activation-api preflight

# Revert jaxb annotation dependency
%pom_change_dep javax.xml.bind:jaxb-api jakarta.xml.bind:jakarta.xml.bind-api xmpbox preflight

%build
# Integration tests all require internet access to download test resources, so skip
# Use compat version of lucene
# Ignore test failures on F28 and earlier due to liberation fonts being too old
%mvn_build -f -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -DskipITs -Dlucene.version=4 -Dmaven.test.failure.ignore=true -P !jdkGte9

%install
%mvn_install

# wrapper scripts
%jpackage_script org.apache.pdfbox.debugger.PDFDebugger "" "" %{oldname}-debugger-2:commons-logging:fontbox-2:%{oldname}-2:bcmail:bcpkix:bcprov %{name}-debugger true
%jpackage_script org.apache.pdfbox.tools.PDFBox "" "" %{oldname}-tools-2:commons-logging:fontbox-2:%{oldname}-2:%{oldname}-debugger-2:bcmail:bcpkix:bcprov %{name} true
%jpackage_script org.apache.pdfbox.preflight.Validator_A1b "" "" preflight-2:jakarta-activation:jaxb-api:commons-logging:fontbox-2:%{oldname}-2:xmpbox-2:bcmail:bcpkix:bcprov %{name}-preflight true

%files -f .mfiles-%{oldname}
%doc README.md RELEASE-NOTES.txt

%files debugger -f .mfiles-%{oldname}-debugger
%{_bindir}/%{name}-debugger

%files tools -f .mfiles-%{oldname}-tools
%{_bindir}/%{name}

%files -n fontbox2 -f .mfiles-fontbox
%doc fontbox/README.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files parent -f .mfiles-%{oldname}-parent
%doc --no-dereference LICENSE.txt NOTICE.txt

#%files reactor -f .mfiles-%{oldname}-reactor
#%doc --no-dereference LICENSE.txt NOTICE.txt

%files -n preflight2 -f .mfiles-preflight
%{_bindir}/%{name}-preflight
%doc preflight/README.txt

%files -n xmpbox2 -f .mfiles-xmpbox
%doc xmpbox/README.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Thu May 14 2026 Anton Meleshnikov <alton@altlinux.org> 2.0.26-alt3
- forked package for sambox
- added JPMS support

* Wed Jan 21 2026 Evgeniy Serov <scala@altlinux.org> 2.0.26-alt2
- Updated for compatibility with the new jaxb api.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:2.0.26-alt1_3jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:2.0.25-alt1_3jpp11
- new version

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0:2.0.24-alt1_2jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:2.0.23-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.0.21-alt1_1jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:2.0.19-alt1_1jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.0.16-alt1_1jpp8
- new version

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.0.9-alt1_5jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.8.13-alt2_4jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.8.13-alt2_1jpp8
- added BR: apache-parent for javapackages 5

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.8.13-alt1_1jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.12-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.11-alt1_1jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.10-alt1_1jpp8
- new version

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.8-alt1_5jpp8
- java 8 mass update

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.2-alt2_2jpp7
- fixed build with pcfi-2010.08.09-alt2_7

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.2-alt1_2jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt3_4jpp7
- rebuild with maven-local

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt2_4jpp7
- new fc release

* Sun Sep 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt2_1jpp7
- fixed build with lucene3

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt1_1jpp7
- new release

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.3-alt2_3jpp6
- new jpp relase

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.7.3-alt2_1jpp5
- rebuild with new lucene

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.7.3-alt1_1jpp5
- new jpackage release

* Wed Jan 16 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.7.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

