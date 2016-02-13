Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define fedora 23
# Conditionals to help breaking tika <-> vorbis-java-tika dependency cycle
%if 0%{?fedora}
#def_with vorbis_tika
%bcond_with vorbis_tika
# Disable only for now
#def_with tika_parsers
%bcond_with tika_parsers
#def_with tika_app
%bcond_with tika_app
%endif

Name:          tika
Version:       1.11
Release:       alt1_2jpp8
Summary:       A content analysis toolkit
License:       ASL 2.0
Url:           http://tika.apache.org/
# sh tika-repack.sh <VERSION>
Source0:       %{name}-%{version}-clean.tar.xz
Source1:       tika-repack.sh

BuildRequires: maven-local
BuildRequires: mvn(biz.aQute:bndlib)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(xml-apis:xml-apis)

%if %{without vorbis_tika}
BuildRequires: mvn(org.gagravarr:vorbis-java-tika)
%endif

%if %{without tika_parsers}
BuildRequires: mvn(com.adobe.xmp:xmpcore)
BuildRequires: mvn(com.drewnoakes:metadata-extractor:2) >= 2.8.1
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.googlecode.json-simple:json-simple)
BuildRequires: mvn(com.googlecode.juniversalchardet:juniversalchardet)
BuildRequires: mvn(com.healthmarketscience.jackcess:jackcess)
BuildRequires: mvn(com.healthmarketscience.jackcess:jackcess-encrypt)
BuildRequires: mvn(com.pff:java-libpst)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(de.l3s.boilerpipe:boilerpipe)
BuildRequires: mvn(edu.ucar:cdm) >= 4.5.5
BuildRequires: mvn(edu.ucar:grib) >= 4.5.5
BuildRequires: mvn(edu.ucar:httpservices) >= 4.5.5
BuildRequires: mvn(edu.ucar:netcdf4) >= 4.5.5
BuildRequires: mvn(net.sourceforge.jmatio:jmatio)
%if %{without tika_app}
BuildRequires: mvn(log4j:log4j:1.2.17)
%endif
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.apache.commons:commons-csv)
BuildRequires: mvn(org.apache.commons:commons-exec)
BuildRequires: mvn(org.apache.felix:org.apache.felix.scr.annotations)
BuildRequires: mvn(org.apache.james:apache-mime4j-core)
BuildRequires: mvn(org.apache.james:apache-mime4j-dom)
BuildRequires: mvn(org.apache.james:james-project:pom:)
BuildRequires: mvn(org.apache.opennlp:opennlp-tools) >= 1.5.3
BuildRequires: mvn(org.apache.pdfbox:pdfbox) >= 1.8.10
BuildRequires: mvn(org.apache.poi:poi) >= 3.13
BuildRequires: mvn(org.apache.poi:poi-scratchpad) >= 3.13
BuildRequires: mvn(org.apache.poi:poi-ooxml) >= 3.13
BuildRequires: mvn(org.bouncycastle:bcmail-jdk15on)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.ccil.cowan.tagsoup:tagsoup)
BuildRequires: mvn(org.codelibs:jhighlight)
BuildRequires: mvn(org.gagravarr:vorbis-java-core)
BuildRequires: mvn(org.ow2.asm:asm-debug-all)
BuildRequires: mvn(rome:rome)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:jul-to-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.tukaani:xz)
BuildRequires: mvn(org.xerial:sqlite-jdbc)
%endif

%if 0
# tika-parsers
BuildRequires: mvn(org.apache.cxf:cxf-rt-rs-client:3.0.3)
# tika-server deps
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(javax.mail:mail)
BuildRequires: mvn(net.sf.opencsv:opencsv:2.0)
BuildRequires: mvn(org.apache.cxf:cxf-rt-frontend-jaxrs:3.0.3)
BuildRequires: mvn(org.apache.cxf:cxf-rt-transports-http-jetty:3.0.3)
BuildRequires: mvn(org.apache.cxf:cxf-rt-rs-client:3.0.3)
BuildRequires: mvn(org.apache.cxf:cxf-rt-rs-security-cors:3.0.3)
BuildRequires: mvn(org.apache.cxf:cxf-rt-rs-service-description:3.0.3)
BuildRequires: mvn(org.slf4j:slf4j-jcl)
# tika-translate
# https://gil.fedorapeople.org/microsoft-translator-java-api-0.6.2-1.fc19.src.rpm
BuildRequires: mvn(com.memetix:microsoft-translator-java-api)
BuildRequires: mvn(org.apache.cxf:cxf-rt-frontend-jaxrs:2.7.8)
BuildRequires: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)
%endif

BuildArch:     noarch
Source44: import.info

%description
The Apache Tika toolkit detects and extracts meta-data and
structured text content from various documents using existing
parser libraries.

%if %{without tika_parsers}
%package batch
Group: Development/Java
Summary:       Apache Tika Batch

%description batch
Apache Tika Batch offers robust batch processing code
filesystem input -> filesystem output on a single machine.

%package parsers
Group: Development/Java
Summary:       Apache Tika Parsers

%description parsers
Apache Tika Parsers implementation that matches the
type of the document, once it is known, using
Mime Type detection.

%package java7
Group: Development/Java
Summary:       Apache Tika Java-7 Components

%description java7
Java-7 reliant components, including FileTypeDetector
implementations.

%package xmp
Group: Development/Java
Summary:       Apache Tika XMP

%description xmp
Converts Tika metadata to XMP.

%if %{without tika_app}
%package app
Group: Development/Java
Summary:       Apache Tika Application
Requires:      mvn(log4j:log4j:1.2.17)

%description app
Apache Tika standalone application.
%endif
%endif

%package serialization
Group: Development/Java
Summary:       Apache Tika Serialization

%description serialization
Apache Tika Serialization integrated the
GSON library to serialize/deserialize
Metadata objects.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%pom_disable_module %{name}-bundle
%pom_disable_module %{name}-example
%pom_disable_module %{name}-server
%pom_disable_module %{name}-translate

# Unavailable plugins
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin %{name}-core
%pom_remove_plugin org.apache.felix:maven-scr-plugin %{name}-xmp
%pom_remove_plugin org.apache.felix:maven-scr-plugin %{name}-java7
%pom_remove_plugin -r de.thetaphi:forbiddenapis %{name}-parent
%pom_remove_plugin :maven-shade-plugin %{name}-parent

%pom_change_dep :ant-nodeps :ant

# Require com.drewnoakes:metadata-extractor:2.6.2 and fedora metadata-extractor pkg is too old
# see https://bugzilla.redhat.com/show_bug.cgi?id=947457
%pom_xpath_set "pom:dependency[pom:artifactId='metadata-extractor']/pom:version" 2  %{name}-parsers
# Disable vorbis-java-tika support, cause circular dependency
%if %{with vorbis_tika}
%pom_remove_dep :vorbis-java-tika %{name}-parsers
%endif

%if %{with tika_parsers}
%pom_disable_module %{name}-parsers
%pom_disable_module %{name}-xmp
%else
%if %{with tika_app}
%pom_disable_module %{name}-app
%else
# No bundled libraries are shipped
%pom_remove_plugin :maven-shade-plugin %{name}-app
%pom_remove_plugin :maven-antrun-plugin %{name}-app
%endif
%endif

# Unavailable build dep com.googlecode.mp4parser:isoparser
# MP4 is non-free remove support for it
%pom_remove_dep com.googlecode.mp4parser:isoparser %{name}-parsers
rm -rf %{name}-parsers/src/main/java/org/apache/tika/parser/mp4/MP4Parser.java \
 %{name}-parsers/src/main/java/org/apache/tika/parser/mp4/DirectFileReadDataSource.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/mp4/MP4ParserTest.java
# NON FREE under UnRar License
%pom_remove_dep com.github.junrar:junrar %{name}-parsers
rm %{name}-parsers/src/main/java/org/apache/tika/parser/pkg/RarParser.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/pkg/RarParserTest.java
# sis & geoapi use NON FREE deps: javax.measure:jsr-275
%pom_remove_dep org.apache.sis.core:sis-utility %{name}-parsers
%pom_remove_dep org.apache.sis.storage:sis-netcdf %{name}-parsers
%pom_remove_dep org.apache.sis.core:sis-metadata %{name}-parsers
#  https://github.com/opengeospatial/geoapi/issues/8
%pom_remove_dep org.opengis:geoapi %{name}-parsers
rm -r %{name}-parsers/src/main/java/org/apache/tika/parser/geoinfo \
 %{name}-parsers/src/test/java/org/apache/tika/parser/geoinfo
%pom_remove_dep org.apache.ctakes:ctakes-core %{name}-parsers
rm -r %{name}-parsers/src/main/java/org/apache/tika/parser/ctakes

# Remove NON FREE json.org support
%pom_remove_dep org.json:json %{name}-parsers
rm -r %{name}-parsers/src/main/java/org/apache/tika/parser/journal \
 %{name}-parsers/src/test/java/org/apache/tika/parser/journal

# TODO org.apache.cxf:cxf-rt-rs-client:3.0.3 https://bugzilla.redhat.com/show_bug.cgi?id=1276555
%pom_remove_dep org.apache.cxf:cxf-rt-rs-client %{name}-parsers

# This test require network
rm %{name}-core/src/test/java/org/apache/tika/mime/MimeDetectionTest.java \
 tika-core/src/test/java/org/apache/tika/detect/MimeDetectionWithNNTest.java
# These test fails for unavailable deps: com.googlecode.mp4parser:isoparser and org.gagravarr:vorbis-java-tika
rm -r %{name}-parsers/src/test/java/org/apache/tika/parser/mail/RFC822ParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/mbox/MboxParserTest.java
rm -r %{name}-parsers/src/test/java/org/apache/tika/detect/TestContainerAwareDetector.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/AutoDetectParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/asm/ClassParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/pkg/Bzip2ParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/pkg/GzipParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/pkg/TarParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/pkg/ZipParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/pkg/ZlibParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/pkg/Seven7ParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/pkg/CompressParserTest.java
rm -r %{name}-parsers/src/test/java/org/apache/tika/parser/image/ImageMetadataExtractorTest.java
# Fails for unavailable test resources
rm -r %{name}-parsers/src/test/java/org/apache/tika/parser/microsoft/ProjectParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/mp3/Mp3ParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/mime/TestMimeTypes.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/iwork/IWorkParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/pkg/ArParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/executable/ExecutableParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/ibooks/iBooksParserTest.java \
 %{name}-app/src/test/java/org/apache/tika/cli/TikaCLITest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/pdf/PDFParserTest.java

# NullPointerException: null
rm -r %{name}-parsers/src/test/java/org/apache/tika/parser/fork/ForkParserIntegrationTest.java
# NoClassDefFoundError: org/w3c/dom/ElementTraversal
%pom_add_dep xml-apis:xml-apis::test %{name}-parsers

# ComparisonFailure: Date/Time Original for when the photo was taken, unspecified time zone expected:<2009-08-11T[09]:09:45> but was:<2009-08-11T[11]:09:45>
rm -r %{name}-parsers/src/test/java/org/apache/tika/parser/jpeg/JpegParserTest.java
# Fail on ARM builder TestTimedOutException: test timed out after 30000 milliseconds
rm -r %{name}-batch/src/test/java/org/apache/tika/batch/fs/BatchDriverTest.java

%mvn_package :%{name} %{name}
%mvn_package :%{name}-core %{name}
%mvn_package :%{name}-parent %{name}

%build

# skip tests for now because there are test failures:
# Tests which use cglib fail because of incompatibility with asm>=4
# Test fails for unavailable build deps: com.googlecode.mp4parser:isoparser
# On ARM builder only
# [ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.19:test (default-test)
# on project tika-batch: Execution default-test of goal org.apache.maven.plugins:maven-surefire-plugin:2.19:test
# failed: The forked VM terminated without properly saying goodbye. VM crash or System.exit called?
# [ERROR] Command was /bin/sh -c cd /builddir/build/BUILD/tika-1.11/tika-batch &&
# /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.65-5.b17.fc24.arm/jre/bin/java -Xmx2048m -jar
# /builddir/build/BUILD/tika-1.11/tika-batch/target/surefire/surefirebooter7260304071560324729.jar
# /builddir/build/BUILD/tika-1.11/tika-batch/target/surefire/surefire575868159465048587tmp
# /builddir/build/BUILD/tika-1.11/tika-batch/target/surefire/surefire_31877375323011518356tmp
# [ERROR] -> [Help 1]
%mvn_build -sf -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%if %{without tika_app}
%jpackage_script org.apache.tika.cli.TikaCLI "" "" %{name}:opennlp:jwnl:google-gson:commons-io:commons-logging:log4j12-1.2.17:metadata-extractor2-2:juniversalchardet:apache-commons-codec:boilerpipe:thredds:bea-stax-api:commons-compress:felix/org.apache.felix.scr.annotations:apache-mime4j/core:apache-mime4j/dom:pdfbox:poi/poi:poi/poi-scratchpad:poi/poi-ooxml:bcmail:bcprov:tagsoup:objectweb-asm/asm-all:rome:fontbox:vorbis-java:dom4j:xmlbeans:poi/poi-ooxml-schemas:jempbox:xmpcore:slf4j/api:slf4j/log4j12:jdom:jdom2 %{name}-app true
%endif

%files -f .mfiles-%{name}
%doc CHANGES.txt HEADER.txt KEYS README.md
%doc LICENSE.txt NOTICE.txt

%if %{without tika_parsers}
%files batch -f .mfiles-%{name}-batch
%doc LICENSE.txt NOTICE.txt

%files parsers -f .mfiles-%{name}-parsers
%doc LICENSE.txt NOTICE.txt

%files java7 -f .mfiles-%{name}-java7
%doc LICENSE.txt NOTICE.txt

%files xmp -f .mfiles-%{name}-xmp
%doc LICENSE.txt NOTICE.txt

%if %{without tika_app}
%files app -f .mfiles-%{name}-app
%doc LICENSE.txt NOTICE.txt
%{_bindir}/%{name}-app
%endif
%endif

%files serialization -f .mfiles-%{name}-serialization
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

