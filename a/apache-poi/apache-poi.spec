%define _unpackaged_files_terminate_build 1
%global reldate 20261019

Name: apache-poi
Version: 6.0.0
Release: alt1

Summary: The Java API for Microsoft Documents
License: Apache-2.0 and MIT
Group: Development/Java
URL: https://poi.apache.org/
VCS: https://github.com/apache/poi.git

Source0: %name-src-%version-%reldate.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: maven-local
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.apache.commons:commons-collections4)
BuildRequires: mvn(org.apache.commons:commons-math3)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(com.zaxxer:SparseBitSet)
BuildRequires: mvn(com.github.virtuald:curvesapi)
BuildRequires: mvn(org.apache.xmlbeans:xmlbeans)
BuildRequires: mvn(org.apache.xmlbeans:xmlbeans:pom:)
BuildRequires: mvn(org.apache.logging.log4j:log4j-bom:pom:)
BuildRequires: mvn(org.apache.logging.log4j:log4j-api)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.pdfbox:pdfbox)
BuildRequires: mvn(de.rototor.pdfbox:graphics2d)
BuildRequires: mvn(org.apache.xmlgraphics:batik-svggen)
BuildRequires: mvn(org.apache.xmlgraphics:batik-svgrasterizer)
BuildRequires: mvn(org.apache.xmlgraphics:batik-codec)
BuildRequires: mvn(org.apache.xmlgraphics:batik-bridge)
BuildRequires: mvn(org.apache.xmlgraphics:batik-script)
BuildRequires: mvn(org.apache.santuario:xmlsec)
BuildRequires: mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires: mvn(jakarta.activation:jakarta.activation-api)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk18on)
BuildRequires: mvn(org.bouncycastle:bcutil-jdk18on)
BuildRequires: mvn(org.slf4j:slf4j-api:2)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-junitlauncher)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.xmlunit:xmlunit-core)
BuildRequires: mvn(org.reflections:reflections)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.apache.commons:commons-csv)
BuildRequires: mvn(net.bytebuddy:byte-buddy)
BuildRequires: mvn(net.bytebuddy:byte-buddy-agent)

#Fonts for testing
BuildRequires: fontconfig
BuildRequires: fonts-ttf-liberation

%package ooxml
Summary: Apache POI OOXML module
Group: Development/Java

%description ooxml
Apache POI module for Office Open XML documents.

%package ooxml-full
Summary: Apache POI full OOXML schemas module
Group: Development/Java

%description ooxml-full
Full XML schema definitions for Apache POI Office Open XML support.

%package ooxml-lite
Summary: Apache POI compact OOXML schemas module
Group: Development/Java

%description ooxml-lite
Compact XML schema definitions for Apache POI Office Open XML support.

%package ooxml-lite-agent
Summary: Apache POI OOXML lite instrumentation agent
Group: Development/Java

%description ooxml-lite-agent
Instrumentation agent used by the Apache POI compact OOXML schemas module.

%package scratchpad
Summary: Apache POI additional document format support module
Group: Development/Java

%description scratchpad
Additional document format support from Apache POI.

%package excelant
Summary: Apache POI Excel Ant tasks module
Group: Development/Java

%description excelant
Apache POI Ant tasks for processing Excel documents.

%package examples
Summary: Apache POI examples module
Group: Development/Java

%description examples
Examples for the Apache POI APIs.

%description
The Apache POI Project's mission is to create and maintain Java APIs for
manipulating various file formats based upon the Office Open XML standards
(OOXML) and Microsoft's OLE 2 Compound Document format (OLE2). In short, you
can read and write MS Excel files using Java. In addition, you can read and
write MS Word and MS PowerPoint files using Java. Apache POI is your Java
Excel solution (for Excel 97-2008). We have a complete API for porting other
OOXML and OLE2 formats and welcome others to participate.

OLE2 files include most Microsoft Office files such as XLS, DOC, and PPT as
well as MFC serialization API based file formats. The project provides APIs
for the OLE2 Filesystem (POIFS) and OLE2 Document Properties (HPSF).

Office OpenXML Format is the new standards based XML file format found in
Microsoft Office 2007 and 2008. This includes XLSX, DOCX and PPTX. The
project provides a low level API to support the Open Packaging Conventions
using openxml4j.

For each MS Office application there exists a component module that attempts
to provide a common high level Java API to both OLE2 and OOXML document
formats. This is most developed for Excel workbooks (SS=HSSF+XSSF). Work is
progressing for Word documents (HWPF+XWPF) and PowerPoint presentations
(HSLF+XSLF).

The project has recently added support for Outlook (HSMF). Microsoft opened
the specifications to this format in October 2007. We would welcome
contributions.

There are also projects for Visio (HDGF) and Publisher (HPBF).

%prep
%setup -q -n %name-src-%version-%reldate
# Leave address space for JDK native memory in 32-bit Hasher.
if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i 's/-Xmx3G/-Xmx1g/' gradle.properties
    printf '%%s\n' 'org.gradle.workers.max=2' >> gradle.properties
    sed -i 's/maxHeapSize = "2g"/maxHeapSize = "1g"/' build.gradle
    sed -i "s/maxHeapSize = '3g'/maxHeapSize = '1280m'/" \
        poi-integration/build.gradle
    sed -i 's/-Xmx2G/-Xmx1g/' \
        poi-ooxml-full/build.gradle poi-ooxml-lite/build.gradle
fi

%build
%gradle_publish

%install
%mvn_package org.apache.poi:poi
%mvn_package org.apache.poi:poi-ooxml ooxml
%mvn_package org.apache.poi:poi-ooxml-full ooxml-full
%mvn_package org.apache.poi:poi-ooxml-lite ooxml-lite
%mvn_package org.apache.poi:poi-ooxml-lite-agent ooxml-lite-agent
%mvn_package org.apache.poi:poi-scratchpad scratchpad
%mvn_package org.apache.poi:poi-excelant excelant
%mvn_package org.apache.poi:poi-examples examples
%gradle_register --artifacts=poi-
%gradle_install

%check
%gradle_check -Dmaven.repo.local="$PWD/.m2/repository"

%files -f .mfiles
%doc legal/LICENSE legal/NOTICE

%files ooxml -f .mfiles-ooxml

%files ooxml-full -f .mfiles-ooxml-full

%files ooxml-lite -f .mfiles-ooxml-lite

%files ooxml-lite-agent -f .mfiles-ooxml-lite-agent

%files scratchpad -f .mfiles-scratchpad

%files excelant -f .mfiles-excelant

%files examples -f .mfiles-examples

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 6.0.0-alt1
- New version.
- Build with xgradle and system dependencies.
- Split published modules into RPM subpackages.
- Build on i586.
- Fix FTBFS: Run integration tests serially.

* Wed Sep 09 2026 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt3
- FTBFS: built with Gradle 9.7.1.

* Mon Jan 12 2026 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt2
- Packaged xmvn metainfo files.

* Sun Jul 06 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- new version
- build with java 21

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.17-alt1_4jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.17-alt1_2jpp8
- fc29 update

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.17-alt1_1jpp8
- java update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.15-alt1_2jpp8
- java update

* Mon Nov 20 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.15-alt1_1jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.14-alt1_4jpp8
- new version

* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.13-alt1_2jpp8
- new version

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.12-alt1_2jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt2_4jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt2_3jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt1_3jpp7
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_1jpp6
- new version

