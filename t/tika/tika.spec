Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Conditionals to help breaking tika <-> vorbis-java-tika dependency cycle
%if 0%{?fedora}
%bcond_with vorbis_tika
# Disable only for now
%bcond_with tika_parsers
%bcond_with tika_app
%bcond_with tika_server
%endif

Name:          tika
Version:       1.12
Release:       alt1_4jpp8
Summary:       A content analysis toolkit
License:       ASL 2.0
Url:           http://tika.apache.org/
# sh tika-repack.sh <VERSION>
Source0:       %{name}-%{version}-clean.tar.xz
Source1:       tika-repack.sh

Patch0:        tika-1.11-poi3.14.patch
Patch1:        tika-1.12-port-tika-translate-to-jackson-2.7.x.patch

BuildRequires: maven-local
BuildRequires: mvn(biz.aQute:bndlib)
BuildRequires: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider) >= 2.7.1
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.cxf:cxf-rt-frontend-jaxrs) >= 3.0.3
BuildRequires: mvn(org.apache.cxf:cxf-rt-rs-client)
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
BuildRequires: mvn(com.googlecode.json-simple:json-simple)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.healthmarketscience.jackcess:jackcess)
BuildRequires: mvn(com.healthmarketscience.jackcess:jackcess-encrypt)
BuildRequires: mvn(com.pff:java-libpst)
BuildRequires: mvn(com.rometools:rome)
BuildRequires: mvn(org.codelibs:jhighlight)
BuildRequires: mvn(org.gagravarr:vorbis-java-core)
BuildRequires: mvn(com.googlecode.juniversalchardet:juniversalchardet)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(de.l3s.boilerpipe:boilerpipe)
BuildRequires: mvn(edu.ucar:cdm) >= 4.5.5
BuildRequires: mvn(edu.ucar:grib) >= 4.5.5
BuildRequires: mvn(edu.ucar:httpservices) >= 4.5.5
BuildRequires: mvn(edu.ucar:netcdf4) >= 4.5.5
%if %{without tika_app}
BuildRequires: mvn(log4j:log4j:1.2.17)
%endif
BuildRequires: mvn(net.sourceforge.jmatio:jmatio)
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.apache.commons:commons-csv)
BuildRequires: mvn(org.apache.commons:commons-exec)
BuildRequires: mvn(org.apache.felix:org.apache.felix.scr.annotations)
BuildRequires: mvn(org.apache.james:apache-mime4j-core)
BuildRequires: mvn(org.apache.james:apache-mime4j-dom)
BuildRequires: mvn(org.apache.james:james-project:pom:)
BuildRequires: mvn(org.apache.opennlp:opennlp-tools)
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
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:jul-to-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.tukaani:xz)
BuildRequires: mvn(org.xerial:sqlite-jdbc)
%if %{with tika_server}
BuildRequires: mvn(com.qmino:miredot-maven-plugin) >= 1.4
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(javax.mail:mail)
BuildRequires: mvn(net.sf.opencsv:opencsv) >= 2.0
BuildRequires: mvn(org.apache.cxf:cxf-rt-transports-http-jetty) >= 3.0.3
BuildRequires: mvn(org.apache.cxf:cxf-rt-rs-security-cors)
BuildRequires: mvn(org.apache.cxf:cxf-rt-rs-service-description)
BuildRequires: mvn(org.slf4j:slf4j-jcl)
%endif
%endif

BuildArch:     noarch
Source44: import.info

%description
The Apache Tika toolkit detects and extracts meta-data and
structured text content from various documents using existing
parser libraries.

%if %{without tika_parsers}
%if %{without tika_app}
%package app
Group: Development/Java
Summary:       Apache Tika Application
Requires:      mvn(log4j:log4j:1.2.17)

%description app
Apache Tika standalone application.
%endif

%package batch
Group: Development/Java
Summary:       Apache Tika Batch

%description batch
Apache Tika Batch offers robust batch processing code
filesystem input -> filesystem output on a single machine.

%package java7
Group: Development/Java
Summary:       Apache Tika Java-7 Components

%description java7
Java-7 reliant components, including FileTypeDetector
implementations.

%package parsers
Group: Development/Java
Summary:       Apache Tika Parsers

%description parsers
Apache Tika Parsers implementation that matches the
type of the document, once it is known, using
Mime Type detection.

%if %{with tika_server}
%package server
Group: Development/Java
Summary:       Apache Tika JAX-RS Server

%description server
Apache Tika JAX-RS Server.
%endif

%package xmp
Group: Development/Java
Summary:       Apache Tika XMP

%description xmp
Converts Tika metadata to XMP.
%endif

%package parent
Group: Development/Java
Summary:       Apache Tika parent POM

%description parent
Apache Tika parent POM.

%package pom
Group: Development/Java
Summary:       Apache Tika Aggregator POM

%description pom
Apache Tika Aggregator POM.

%package serialization
Group: Development/Java
Summary:       Apache Tika serialization

%description serialization
Use GSON library support to serialize/deserialize
JSON Metadata objects.

%package translate
Group: Development/Java
Summary:       Apache Tika translate

%description translate
This is the translate Apache Tika toolkit.
Translator implementations may depend on
web services.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%pom_disable_module %{name}-bundle
%pom_disable_module %{name}-example

# Unavailable plugins
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin %{name}-core

%pom_remove_plugin org.apache.felix:maven-scr-plugin %{name}-xmp
%pom_remove_plugin org.apache.felix:maven-scr-plugin %{name}-java7
%pom_remove_plugin -r de.thetaphi:forbiddenapis %{name}-parent
%pom_remove_plugin :maven-shade-plugin %{name}-parent
%pom_remove_plugin :maven-release-plugin %{name}-parent

%pom_change_dep :ant-nodeps :ant

# Require com.drewnoakes:metadata-extractor:2.6.2 and fedora metadata-extractor pkg is too old
# see https://bugzilla.redhat.com/show_bug.cgi?id=947457
%pom_change_dep :metadata-extractor ::2  %{name}-parsers

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
%if %{without tika_server}
%pom_disable_module %{name}-server
%else
%pom_remove_plugin :maven-shade-plugin %{name}-server
# TODO %% pom_remove_plugin :miredot-maven-plugin %%{name}-server
%endif
%endif

# tika-translate
# https://gil.fedorapeople.org/microsoft-translator-java-api-0.6.2-1.fc19.src.rpm
%pom_remove_dep :microsoft-translator-java-api %{name}-translate
rm %{name}-translate/src/main/java/org/apache/tika/language/translate/MicrosoftTranslator.java \
 %{name}-translate/src/test/java/org/apache/tika/language/translate/MicrosoftTranslatorTest.java
sed -i '/MicrosoftTranslator/d' %{name}-translate/src/main/resources/META-INF/services/org.apache.tika.language.translate.Translator
rm %{name}-translate/src/main/resources/org/apache/tika/language/translate/translator.microsoft.properties
# package org.apache.cxf.jaxrs.client does not exist
%pom_add_dep org.apache.cxf:cxf-rt-rs-client %{name}-translate
%pom_change_dep :junit ::4.11:test %{name}-translate

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
 %{name}-parsers/src/test/java/org/apache/tika/parser/journal \
 %{name}-parsers/src/main/java/org/apache/tika/parser/ner/corenlp

# This test require network
rm %{name}-core/src/test/java/org/apache/tika/mime/MimeDetectionTest.java \
 %{name}-core/src/test/java/org/apache/tika/detect/MimeDetectionWithNNTest.java
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

rm -r %{name}-parsers/src/test/java/org/apache/tika/parser/microsoft/ooxml/OOXMLParserTest.java \
 %{name}-parsers/src/test/java/org/apache/tika/parser/microsoft/OfficeParserTest.java

%build
# skip tests for now because there are test failures:
# Tests which use cglib fail because of incompatibility with asm4
# Test fails for unavailable build deps: com.googlecode.mp4parser:isoparser
# Error occurred during initialization of VM
# Could not reserve enough space for 2097152KB object heap
%mvn_build -sf -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%if %{without tika_app}
%jpackage_script org.apache.tika.cli.TikaCLI "" "" %{name}:opennlp:jwnl:jackcess-encrypt:jackcess:google-gson:commons-io:commons-logging:log4j12-1.2.17:metadata-extractor2-2:juniversalchardet:apache-commons-codec:boilerpipe:thredds:bea-stax-api:commons-compress:felix/org.apache.felix.scr.annotations:apache-mime4j/core:apache-mime4j/dom:pdfbox:poi/poi:poi/poi-scratchpad:poi/poi-ooxml:bcmail:bcprov:tagsoup:objectweb-asm/asm-all:rome:fontbox:vorbis-java:dom4j:xmlbeans:poi/poi-ooxml-schemas:jempbox:xmpcore:slf4j/api:slf4j/log4j12:jdom:jdom2 %{name}-app true
%endif

%files -f .mfiles-%{name}-core
%doc CHANGES.txt HEADER.txt KEYS README.md
%doc LICENSE.txt NOTICE.txt

%if %{without tika_parsers}
%if %{without tika_app}
%files app -f .mfiles-%{name}-app
%{_bindir}/%{name}-app
%endif
%files batch -f .mfiles-%{name}-batch
%files java7 -f .mfiles-%{name}-java7
%files parsers -f .mfiles-%{name}-parsers
%if %{with tika_server}
%files server -f .mfiles-%{name}-server
%doc %{name}-server/README.md
%endif
%files xmp -f .mfiles-%{name}-xmp
%endif

%files parent -f .mfiles-%{name}-parent
%doc LICENSE.txt NOTICE.txt

%files pom -f .mfiles-%{name}
%doc LICENSE.txt NOTICE.txt

%files serialization -f .mfiles-%{name}-serialization
%files translate -f .mfiles-%{name}-translate

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_4jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_3jpp8
- new version

* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

