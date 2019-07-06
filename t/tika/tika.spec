Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
%define fedora 30
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
%endif

Name:          tika
Version:       1.17
Release:       alt1_4jpp8
Summary:       A content analysis toolkit
License:       ASL 2.0
Url:           http://tika.apache.org/
# sh tika-repack.sh <VERSION>
Source0:       %{name}-%{version}-clean.tar.xz
Source1:       tika-repack.sh

# The upstream PDFBox project retired the JempBox sub-project, so patch out it's use
# Upstream Tika should migrate to the PDFBox's XMPBox lib instead
Patch0:        tika-no-jempbox.patch

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute:bndlib)
BuildRequires:  mvn(com.adobe.xmp:xmpcore)
BuildRequires:  mvn(com.drewnoakes:metadata-extractor:2)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.googlecode.json-simple:json-simple)
BuildRequires:  mvn(com.googlecode.juniversalchardet:juniversalchardet)
BuildRequires:  mvn(com.h2database:h2)
BuildRequires:  mvn(com.healthmarketscience.jackcess:jackcess)
BuildRequires:  mvn(com.healthmarketscience.jackcess:jackcess-encrypt)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(com.optimaize.languagedetector:language-detector)
BuildRequires:  mvn(com.pff:java-libpst)
BuildRequires:  mvn(com.rometools:rome)
BuildRequires:  mvn(de.l3s.boilerpipe:boilerpipe)
BuildRequires:  mvn(edu.ucar:cdm)
BuildRequires:  mvn(edu.ucar:grib)
BuildRequires:  mvn(edu.ucar:httpservices)
BuildRequires:  mvn(edu.ucar:netcdf4)
BuildRequires:  mvn(net.sourceforge.jmatio:jmatio)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-csv)
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-math3)
BuildRequires:  mvn(org.apache.cxf:cxf-rt-frontend-jaxrs)
BuildRequires:  mvn(org.apache.cxf:cxf-rt-rs-client)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.scr.annotations)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpmime)
BuildRequires:  mvn(org.apache.james:apache-mime4j-core) >= 0.8.1
BuildRequires:  mvn(org.apache.james:apache-mime4j-dom) >= 0.8.1
BuildRequires:  mvn(org.apache.lucene:lucene-analyzers-common)
BuildRequires:  mvn(org.apache.lucene:lucene-analyzers-icu)
BuildRequires:  mvn(org.apache.lucene:lucene-core)
BuildRequires:  mvn(org.apache.lucene:lucene-memory)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.opennlp:opennlp-tools)
BuildRequires:  mvn(org.apache.pdfbox:pdfbox)
BuildRequires:  mvn(org.apache.pdfbox:pdfbox-tools)
BuildRequires:  mvn(org.apache.poi:poi) >= 3.17
BuildRequires:  mvn(org.apache.poi:poi-ooxml) >= 3.17
BuildRequires:  mvn(org.apache.poi:poi-ooxml-schemas) >= 3.17
BuildRequires:  mvn(org.apache.poi:poi-scratchpad) >= 3.17
BuildRequires:  mvn(org.bouncycastle:bcmail-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.ccil.cowan.tagsoup:tagsoup)
BuildRequires:  mvn(org.codelibs:jhighlight)
%if %{without vorbis_tika}
BuildRequires:  mvn(org.gagravarr:vorbis-java-core)
BuildRequires:  mvn(org.gagravarr:vorbis-java-tika)
%endif
BuildRequires:  mvn(org.osgi:org.osgi.compendium)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:jul-to-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-log4j12)
BuildRequires:  mvn(org.tukaani:xz)
BuildRequires:  mvn(org.xerial:sqlite-jdbc)

BuildArch: noarch
Source44: import.info

%description
The Apache Tika toolkit detects and extracts meta-data and
structured text content from various documents using existing
parser libraries.

%if %{without tika_parsers}
%if %{without tika_app}
%package app
Group: Development/Java
Summary: Apache Tika Application
# Explicit requires for javapackages-tools since tika-app script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description app
Apache Tika standalone application.
%endif

%package batch
Group: Development/Java
Summary: Apache Tika Batch

%description batch
Apache Tika Batch offers robust batch processing code
filesystem input -> filesystem output on a single machine.

%package java7
Group: Development/Java
Summary: Apache Tika Java-7 Components

%description java7
Java-7 reliant components, including FileTypeDetector
implementations.

%package parsers
Group: Development/Java
Summary: Apache Tika Parsers
Requires: apache-poi >= 3.17
Requires: apache-mime4j >= 0.8.1

%description parsers
Apache Tika Parsers implementation that matches the
type of the document, once it is known, using
Mime Type detection.

%package xmp
Group: Development/Java
Summary: Apache Tika XMP

%description xmp
Converts Tika metadata to XMP.
%endif

%package parent
Group: Development/Java
Summary: Apache Tika parent POM

%description parent
Apache Tika parent POM.

%package pom
Group: Development/Java
Summary: Apache Tika Aggregator POM

%description pom
Apache Tika Aggregator POM.

%package serialization
Group: Development/Java
Summary: Apache Tika serialization

%description serialization
Use GSON library support to serialize/deserialize
JSON Metadata objects.

%package translate
Group: Development/Java
Summary: Apache Tika translate

%description translate
This is the translate Apache Tika toolkit.
Translator implementations may depend on
web services.

%package eval
Group: Development/Java
Summary: Apache Tika eval
Requires: apache-poi >= 3.17

%description eval
Command line tool to assess the output of Tika or compare the output of
two different versions of Tika or other text extraction packages.

%package langdetect
Group: Development/Java
Summary: Apache Tika language detection

%description langdetect
Tika is able to help identify the language of a piece of text, which is
useful when extracting text from document formats which do not include
language information in their metadata.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q

%pom_disable_module %{name}-bundle
%pom_disable_module %{name}-example

# Unavailable deps for these modules
%pom_disable_module %{name}-dl
%pom_disable_module %{name}-nlp
%pom_disable_module %{name}-server

# Unavailable plugins
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin %{name}-core
%pom_remove_plugin org.codehaus.gmaven:groovy-maven-plugin %{name}-parsers

# Unnecessary plugins for RPM build
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin :forbiddenapis %{name}-parent
%pom_remove_plugin :maven-release-plugin %{name}-parent
%pom_remove_plugin :maven-shade-plugin tika-{server,eval,app,parent}
%pom_remove_plugin :maven-scr-plugin tika-{xmp,java7}

# Disable vorbis-java-tika support, cause circular dependency
%if %{with vorbis_tika}
%pom_remove_dep org.gagravarr: %{name}-parsers
%endif

%if %{with tika_parsers}
%pom_disable_module %{name}-parsers
%pom_disable_module %{name}-xmp
%else
%if %{with tika_app}
%pom_disable_module %{name}-app
%endif
%endif

# tika-translate
# https://gil.fedorapeople.org/microsoft-translator-java-api-0.6.2-1.fc19.src.rpm
%pom_remove_dep :microsoft-translator-java-api %{name}-translate
rm %{name}-translate/src/main/java/org/apache/tika/language/translate/MicrosoftTranslator.java \
 %{name}-translate/src/test/java/org/apache/tika/language/translate/MicrosoftTranslatorTest.java
sed -i '/MicrosoftTranslator/d' %{name}-translate/src/main/resources/META-INF/services/org.apache.tika.language.translate.Translator
rm %{name}-translate/src/main/resources/org/apache/tika/language/translate/translator.microsoft.properties
%pom_change_dep :junit ::4.11:test %{name}-translate

# Unavailable build dep com.googlecode.mp4parser:isoparser
# MP4 is non-free remove support for it
%pom_remove_dep com.googlecode.mp4parser:isoparser %{name}-parsers
rm -r tika-parsers/src/main/java/org/apache/tika/parser/mp4/ \
      tika-parsers/src/main/java/org/apache/tika/parser/pot/
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
%pom_remove_dep com.tdunning:json tika-parsers
rm -r tika-parsers/src/main/java/org/apache/tika/parser/{journal,recognition,captioning} \
      tika-parsers/src/main/java/org/apache/tika/parser/ner/{corenlp,nltk,grobid}
# Sentiment analysis not available in Fedora
%pom_remove_dep :sentiment-analysis-parser tika-parsers
rm -r tika-parsers/src/main/java/org/apache/tika/parser/sentiment
# Upstream pdfbox EOL'd the jempbox subproject
%pom_remove_dep org.apache.pdfbox:jempbox tika-parsers
rm -r tika-parsers/src/main/java/org/apache/tika/parser/image/xmp \
      tika-parsers/src/main/java/org/apache/tika/parser/pdf/PDFParser.java
%patch0
# No longer need CXF
%pom_remove_dep :cxf-rt-rs-client tika-parsers
# Various dep fixes for parsers
%pom_change_dep org.tallison:jmatio net.sourceforge.jmatio:jmatio tika-parsers
sed -i -e '/setAllowObjectDeserialization/d' tika-parsers/src/main/java/org/apache/tika/parser/mat/MatParser.java
%pom_change_dep :metadata-extractor ::2 tika-parsers

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

# Fix build against lucene 6.3+
%if 0%{?fedora} >= 29
sed -i -e 's/\(import org.apache\.lucene\.analysis.\)util\.FilteringTokenFilter/\1FilteringTokenFilter/' \
  tika-eval/src/main/java/org/apache/tika/eval/tokens/*FilterFactory.java
%endif

# ComparisonFailure: Date/Time Original for when the photo was taken, unspecified time zone expected:<2009-08-11T[09]:09:45> but was:<2009-08-11T[11]:09:45>
rm -r %{name}-parsers/src/test/java/org/apache/tika/parser/jpeg/JpegParserTest.java
# Fail on ARM builder TestTimedOutException: test timed out after 30000 milliseconds
rm -r %{name}-batch/src/test/java/org/apache/tika/batch/fs/BatchDriverTest.java

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
%jpackage_script org.apache.tika.cli.TikaCLI "" "" %{name}:opennlp:jwnl:jackcess-encrypt:jackcess:google-gson:commons-io:commons-logging:log4j12-1.2.17:metadata-extractor2-2:juniversalchardet:apache-commons-codec:boilerpipe:thredds:bea-stax-api:commons-compress:felix/org.apache.felix.scr.annotations:apache-mime4j/core:apache-mime4j/dom:pdfbox:poi/poi:poi/poi-scratchpad:poi/poi-ooxml:bcmail:bcprov:tagsoup:objectweb-asm/asm-all:rome:fontbox:vorbis-java:dom4j:xmlbeans:poi/poi-ooxml-schemas:xmpcore:slf4j/api:slf4j/log4j12:jdom:jdom2 %{name}-app true
%endif

%files -f .mfiles-%{name}-core
%doc CHANGES.txt HEADER.txt KEYS README.md
%doc --no-dereference LICENSE.txt NOTICE.txt

%if %{without tika_parsers}
%if %{without tika_app}
%files app -f .mfiles-%{name}-app
%{_bindir}/%{name}-app
%endif
%files batch -f .mfiles-%{name}-batch
%files java7 -f .mfiles-%{name}-java7
%files parsers -f .mfiles-%{name}-parsers
%files xmp -f .mfiles-%{name}-xmp
%endif

%files parent -f .mfiles-%{name}-parent
%doc --no-dereference LICENSE.txt NOTICE.txt

%files pom -f .mfiles-%{name}
%doc --no-dereference LICENSE.txt NOTICE.txt

%files serialization -f .mfiles-%{name}-serialization
%files translate -f .mfiles-%{name}-translate
%files eval -f .mfiles-%{name}-eval
%files langdetect -f .mfiles-%{name}-langdetect

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_4jpp8
- build with lucene7

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_0jpp8
- new version; build with old lucene 6.1

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_6jpp8
- new version

* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

