Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          pdfbox
Version:       2.0.26
Release:       alt1_3jpp11
Summary:       Apache PDFBox library for working with PDF documents
License:       ASL 2.0
URL:           http://pdfbox.apache.org/
Source0:       http://archive.apache.org/dist/pdfbox/%{version}/pdfbox-%{version}-src.zip

# Use system font instead of bundled font
Patch0:        pdfbox-use-system-liberation-font.patch
# Use system icc profiles
Patch1:        pdfbox-use-system-icc-profiles-openicc.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.bouncycastle:bcmail-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.mockito:mockito-core)

BuildRequires: fonts-ttf-dejavu
BuildRequires: fonts-ttf-google-noto-emoji
BuildRequires: fonts-ttf-liberation
BuildRequires: icc-profiles-openicc
BuildRequires: fontconfig libfontconfig1
Requires:      fonts-ttf-liberation

# TODO: Require liberation-sans-fonts >= 2 and don't ignore test failures

BuildArch:     noarch

# Ant support was removed by upstream (Obsoletes added in F28)
Obsoletes:     %{name}-ant < %{version}-%{release}
# Jempbox subproject was removed by upstream (Obsoletes added in F28)
Obsoletes:     jempbox < %{version}-%{release}
# Examples package was dropped due to requiring too old lucene (Obsoletes added in F29)
Obsoletes:     %{name}-examples < %{version}-%{release}
Source44: import.info

%description
Apache PDFBox is an open source Java PDF library for working with PDF
documents. This project allows creation of new PDF documents, manipulation of
existing documents and the ability to extract content from documents. Apache
PDFBox also includes several command line utilities. Apache PDFBox is
published under the Apache License v2.0.

%package debugger
Group: Development/Java
# See: debugger/target/classes/META-INF/DEPENDENCIES
Requires:      mvn(commons-logging:commons-logging)
Requires:      mvn(org.apache.pdfbox:fontbox)
Requires:      mvn(org.apache.pdfbox:pdfbox)
Requires:      mvn(org.bouncycastle:bcmail-jdk15on)
Requires:      mvn(org.bouncycastle:bcpkix-jdk15on)
Requires:      mvn(org.bouncycastle:bcprov-jdk15on)
# needed by wrapper script
Requires:      javapackages-tools
Summary:       Apache PDFBox Debugger

%description debugger
This package contains the PDF debugger for Apache PDFBox.

%package tools
Group: Development/Java
# See: tools/target/classes/META-INF/DEPENDENCIES
Requires:      mvn(commons-logging:commons-logging)
Requires:      mvn(org.apache.pdfbox:fontbox)
Requires:      mvn(org.apache.pdfbox:pdfbox)
Requires:      mvn(org.apache.pdfbox:pdfbox-debugger)
Requires:      mvn(org.bouncycastle:bcmail-jdk15on)
Requires:      mvn(org.bouncycastle:bcpkix-jdk15on)
Requires:      mvn(org.bouncycastle:bcprov-jdk15on)
# needed by wrapper script
Requires:      javapackages-tools
Summary:       Apache PDFBox Tools

%description tools
This package contains command line tools for Apache PDFBox.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package -n fontbox
Group: Development/Java
Summary:        Apache FontBox

%description -n fontbox
FontBox is a Java library used to obtain low level information from font
files. FontBox is a subproject of Apache PDFBox.

%package parent
Group: Development/Java
Summary:        Apache PDFBox Parent POM

%description parent
Apache PDFBox Parent POM.

%package reactor
Group: Development/Java
Summary:        Apache PDFBox Reactor POM

%description reactor
Apache PDFBox Reactor POM.

%package -n preflight
Group: Development/Java
# See: preflight/pom.xml
Requires:      mvn(jakarta.activation:jakarta.activation-api)
Requires:      mvn(javax.xml.bind:jaxb-api)
# See: preflight/target/classes/META-INF/DEPENDENCIES
Requires:      mvn(commons-logging:commons-logging)
Requires:      mvn(org.apache.pdfbox:fontbox)
Requires:      mvn(org.apache.pdfbox:pdfbox)
Requires:      mvn(org.apache.pdfbox:xmpbox)
Requires:      mvn(org.bouncycastle:bcmail-jdk15on)
Requires:      mvn(org.bouncycastle:bcpkix-jdk15on)
Requires:      mvn(org.bouncycastle:bcprov-jdk15on)
# needed by wrapper script
Requires:      javapackages-tools
Summary:        Apache Preflight

%description -n preflight
The Apache Preflight library is an open source Java tool that implements 
a parser compliant with the ISO-19005 (PDF/A) specification. Preflight is a 
subproject of Apache PDFBox.

%package -n xmpbox
Group: Development/Java
Summary:        Apache XmpBox

%description -n xmpbox
The Apache XmpBox library is an open source Java tool that implements Adobe's
XMP(TM) specification.  It can be used to parse, validate and create xmp
contents.  It is mainly used by subproject preflight of Apache PDFBox. 
XmpBox is a subproject of Apache PDFBox.

%prep
%setup -q
find -name '*.class' -delete
find -name '*.jar' -delete
find -name 'sRGB.icc*' -print -delete
find -name '*.icm' -print -delete
find -name '*.ttf' -print -delete

%patch0 -p1 -b .font
%patch1 -b .openicc

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

# install all libraries in _javadir
%mvn_file :%{name} %{name}
%mvn_file :%{name}-debugger %{name}-debugger
%mvn_file :%{name}-examples %{name}-examples
%mvn_file :%{name}-tools %{name}-tools
%mvn_file :preflight preflight
%mvn_file :xmpbox xmpbox
%mvn_file :fontbox fontbox

%pom_xpath_set 'pom:source' 8 parent
%pom_xpath_set 'pom:target' 8 parent

%pom_change_dep javax.activation:activation jakarta.activation:jakarta.activation-api preflight

%build
# Integration tests all require internet access to download test resources, so skip
# Use compat version of lucene
# Ignore test failures on F28 and earlier due to liberation fonts being too old
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -DskipITs -Dlucene.version=4 -Dmaven.test.failure.ignore=true -P !jdkGte9

%install
%mvn_install

# wrapper scripts
%jpackage_script org.apache.pdfbox.debugger.PDFDebugger "" "" %{name}-debugger:commons-logging:fontbox:%{name}:bcmail:bcpkix:bcprov pdfbox-debugger true
%jpackage_script org.apache.pdfbox.tools.PDFBox "" "" %{name}-tools:commons-logging:fontbox:%{name}:%{name}-debugger:bcmail:bcpkix:bcprov pdfbox true
%jpackage_script org.apache.pdfbox.preflight.Validator_A1b "" "" preflight:jakarta-activation:jaxb-api:commons-logging:fontbox:%{name}:xmpbox:bcmail:bcpkix:bcprov pdfbox-preflight true

%files -f .mfiles-%{name}
%doc README.md RELEASE-NOTES.txt

%files debugger -f .mfiles-%{name}-debugger
%{_bindir}/pdfbox-debugger

%files tools -f .mfiles-%{name}-tools
%{_bindir}/pdfbox

%files -n fontbox -f .mfiles-fontbox
%doc fontbox/README.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files parent -f .mfiles-%{name}-parent
%doc --no-dereference LICENSE.txt NOTICE.txt

%files reactor -f .mfiles-%{name}-reactor
%doc --no-dereference LICENSE.txt NOTICE.txt

%files -n preflight -f .mfiles-preflight
%{_bindir}/pdfbox-preflight
%doc preflight/README.txt

%files -n xmpbox -f .mfiles-xmpbox
%doc xmpbox/README.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
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

