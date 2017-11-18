BuildRequires: apache-parent
Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          pdfbox
Version:       1.8.13
Release:       alt2_1jpp8
Summary:       Java library for working with PDF documents
License:       ASL 2.0
URL:           http://pdfbox.apache.org/
Source0:       http://www.apache.org/dist/pdfbox/%{version}/%{name}-%{version}-src.zip
# Don't download anything
Patch0:        pdfbox-nodownload.patch
# Use system bitream-vera-sans-fonts instead of bundled fonts
Patch1:        pdfbox-1.2.0-bitstream.patch
Patch2:        pdfbox-1.8.13-port-to-bouncycastle1.54.patch
# Skip testImageIOUtils https://issues.apache.org/jira/browse/PDFBOX-2084
Patch3:        pdfbox-1.8.12-testImageIOUtils.patch
# https://java.net/jira/browse/JAVACC-292 thanks to Michael Simacek <msimacek@redhat.com>
Patch4:        pdfbox-1.8.12-javacc6.patch
# https://issues.apache.org/jira/browse/PDFBOX-3571
Patch5:        pdfbox-1.8.13-use-system-icc-profiles-openicc.patch
# Fix test and remove unavailable ArialMT.ttf referencies
Patch6:        pdfbox-1.8.12-examples-use-system-bitstream-vera-sans-fonts.patch

Patch7:        pdfbox-1.8.13-preflight-syncmetadata.patch

BuildRequires: fonts-ttf-vera
BuildRequires: fontconfig
BuildRequires: icc-profiles-openicc
BuildRequires: maven-local
BuildRequires: mvn(com.adobe.pdf:pcfi)
BuildRequires: mvn(com.ibm.icu:icu4j)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.apache.rat:apache-rat-plugin)
BuildRequires: mvn(org.bouncycastle:bcmail-jdk15on)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)

Requires:      fonts-ttf-vera
Requires:      icc-profiles-openicc
Requires:      java >= 1.6.0

# ./pdfbox/src/main/resources/org/apache/pdfbox/resources/cmap/*
# (FILES) With multiple versions
Provides:      bundled(adobe-cmap-resources)
BuildArch:     noarch
Source44: import.info

%description
Apache PDFBox is an open source Java PDF library for working with PDF
documents. This project allows creation of new PDF documents, manipulation of
existing documents and the ability to extract content from documents. Apache
PDFBox also includes several command line utilities. Apache PDFBox is
published under the Apache License v2.0.

%package examples
Group: Development/Java
Summary:        Examples for %{name}

%description examples
This package contains examples for %{name}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package ant
Group: Development/Java
Summary:        Apache PDFBox for Ant

%description ant
%{summary}.

%package -n fontbox
Group: Development/Java
Summary:        Apache FontBox

%description -n fontbox
FontBox is a Java library used to obtain low level information from font
files. FontBox is a subproject of Apache PDFBox.

%package -n jempbox
Group: Development/Java
Summary:        Apache JempBox

%description -n jempbox
JempBox is an open source Java library that implements Adobe's XMP(TM)
specification. JempBox is a subproject of Apache PDFBox.

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
find -name '*.icc' -print -delete
find -name '*.icm' -print -delete

%patch0 -p1 -b .nodownload
%patch1 -p1 -b .bitstream
# Remove included fonts
rm -r pdfbox/src/main/resources/org/apache/pdfbox/resources/ttf
%patch2 -p1 -b .bouncycastle1.54
# Use jdk15on version of bcprov
%pom_change_dep -r :bcmail-jdk15 :bcmail-jdk15on:1.54
%pom_change_dep -r :bcprov-jdk15 :bcprov-jdk15on:1.54
%pom_add_dep org.bouncycastle:bcpkix-jdk15on:1.54 pdfbox
%patch3 -p1 -b .testImageIOUtils
rm -f pdfbox/src/test/java/org/apache/pdfbox/util/TestImageIOUtils.java 
%patch4 -p1 -b .javacc
%patch5 -p1 -b .icc-profiles
rm -r examples/src/main/resources/org/apache/pdfbox/resources/pdfa
#rm pdfbox/src/test/resources/org/apache/pdfbox/pdmodel/*Profile.icm*
%patch6 -p1 -b .bitstream-vera-sans-fonts

%patch7 -p1 -b .preflight-syncmetadata

%pom_disable_module war
#Disable lucene, not compatible with lucene 3.6
%pom_disable_module lucene
# Don't build app (it's just a bundle of everything)
%pom_disable_module preflight-app
%pom_disable_module app

%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :maven-deploy-plugin
# cobertura-maven-plugin has been retired
%pom_remove_plugin :cobertura-maven-plugin preflight
%pom_remove_dep javax.activation:activation preflight

%pom_change_dep -r :ant-nodeps :ant
%pom_change_dep -r :log4j ::1.2.17

# Fix line endings
for file in RELEASE-NOTES.txt README.txt fontbox/README.txt jempbox/README.txt preflight/README.txt xmpbox/README.txt; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

# Remove META-INF file that does not exist
sed -i -e '/META-INF/d' pdfbox/pom.xml

rm examples/src/main/java/org/apache/pdfbox/examples/signature/CreateSignature.java \
 examples/src/main/java/org/apache/pdfbox/examples/signature/CreateVisibleSignature.java \
 examples/src/test/java/org/apache/pdfbox/examples/pdfa/CreatePDFATest.java
# IllegalArgumentException: Parameter 'directory' is not a directory
rm -r preflight/src/test/java/org/apache/pdfbox/preflight/integration/TestValidFiles.java

# Remove unpackaged deps for the above tests
# com.github.jai-imageio:jai-imageio-core:1.3.1,jai-imageio-jpeg2000:1.3.0
%pom_remove_dep com.github.jai-imageio: pdfbox
# https://bugzilla.redhat.com/show_bug.cgi?id=1094417
%pom_remove_dep com.levigo.jbig2:levigo-jbig2-imageio pdfbox

rm pdfbox/src/test/java/org/apache/pdfbox/pdmodel/graphics/xobject/PDJpegTest.java \
 pdfbox/src/test/java/org/apache/pdfbox/pdmodel/graphics/xobject/PDCcittTest.java
sed -i -e /PDJpegTest/d pdfbox/src/test/java/org/apache/pdfbox/TestAll.java
sed -i -e /PDCcittTest/d pdfbox/src/test/java/org/apache/pdfbox/TestAll.java

# com.googlecode.maven-download-plugin:maven-download-plugin:1.1.0 used for get 
# test resources: http://www.pdfa.org/wp-content/uploads/2011/08/isartor-pdfa-2008-08-13.zip
%pom_remove_plugin :maven-download-plugin preflight

# Disable filtering
sed -i -e /filtering/d examples/pom.xml

# install all libraries in _javadir
%mvn_file :jempbox jempbox
%mvn_file :%{name} %{name}
%mvn_file :%{name}-ant %{name}-ant
%mvn_file :%{name}-examples %{name}-examples
%mvn_file :preflight preflight
%mvn_file :xmpbox xmpbox
%mvn_file :fontbox fontbox

%build

%mvn_build -s -- -Dadobefiles.jar=$(build-classpath pcfi)

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.txt RELEASE-NOTES.txt

%files examples -f .mfiles-%{name}-examples
%files ant -f .mfiles-%{name}-ant

%files -n fontbox -f .mfiles-fontbox
%doc fontbox/README.txt
%doc LICENSE.txt NOTICE.txt

%files -n jempbox -f .mfiles-jempbox
%doc jempbox/README.txt
%doc LICENSE.txt NOTICE.txt

%files parent -f .mfiles-%{name}-parent
%doc LICENSE.txt NOTICE.txt

%files reactor -f .mfiles-%{name}-reactor
%doc LICENSE.txt NOTICE.txt

%files -n preflight -f .mfiles-preflight
%doc preflight/README.txt

%files -n xmpbox -f .mfiles-xmpbox
%doc xmpbox/README.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
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

