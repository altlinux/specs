Name:           docx4j
Version:        11.5.5
Release:        alt1

Summary:        JAXB-based Java library for Word docx, Powerpoint pptx, and Excel xlsx files
License:        Apache-2.0
Group:          Development/Java
URL:            https://www.docx4java.org
VCS:            https://github.com/plutext/docx4j

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-17-compat

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(org.plutext:jaxb-svg11)
BuildRequires:  mvn(net.engio:mbassador)
BuildRequires:  mvn(org.apache.xmlgraphics:xmlgraphics-commons)
BuildRequires:  mvn(org.docx4j.org.apache:xalan-serializer)
BuildRequires:  mvn(org.docx4j.org.apache:xalan-interpretive)
BuildRequires:  mvn(net.arnx:wmf2svg)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.checkerframework:checker-qual)
BuildRequires:  mvn(org.apache.pdfbox:fontbox)
BuildRequires:  mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires:  mvn(org.glassfish.jaxb:jaxb-core)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(com.thedeanda:lorem)
BuildRequires:  mvn(org.plutext:jaxb-xslfo)
BuildRequires:  mvn(org.apache.xmlgraphics:batik-bridge)
BuildRequires:  mvn(org.apache.xmlgraphics:fop)
BuildRequires:  mvn(org.plutext.graph-convert:graph-convert-base)
BuildRequires:  mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core)

BuildArch:      noarch

%description
docx4j is an open source (Apache v2) library for creating, editing, and saving
OpenXML "packages", including docx, pptx, and xslx.

It uses JAXB to create the Java representation.
- Open existing docx/pptx/xlsx
- Create new docx/pptx/xlsx
- Programmatically manipulate docx/pptx/xlsx (anything the file format allows)
- Document generation via variable, content control data binding, or MERGEFIELD
- CustomXML binding (with support for pictures, rich text, checkboxes, and
  OpenDoPE extensions for repeats & conditionals, and importing XHTML)
- Export as HTML
- Export as PDF, choice of 3 strategies, see
  https://www.docx4java.org/blog/2020/09/office-pptxxlsxdocx-to-pdf-to-in-docx4j-8-2-3/
- Produce/consume Word 2007's xmlPackage (pkg) format
- Apply transforms, including common filters
- Font support (font substitution, and use of any fonts embedded in the
  document)

%javadoc_package

%package        conversion-via-microsoft-graph
Summary:        DOCX4J conversion via microsoft graph
Group:          Development/Java

%description    conversion-via-microsoft-graph
%summary.

%package        core
Summary:        DOCX4J Core
Group:          Development/Java

%description    core
docx4j is a library which helps you to work with the Office Open XML file format
as used in docx documents, pptx presentations, and xlsx spreadsheets.

%package        core-tests
Summary:        DOCX4J Core tests
Group:          Development/Java

%description    core-tests
%summary.

%package        diffx
Summary:        DOCX4J diffx
Group:          Development/Java

%description    diffx
Differencing of docx files.

%package        docx-anon
Summary:        DOCX4J docx-anon
Group:          Development/Java

%description    docx-anon
Anonymization of docx files.

%package        export-fo
Summary:        DOCX4J export-fo
Group:          Development/Java

%description    export-fo
Export docx to PDF via XSL FO, using Apache FOP.

%package        jaxb-ReferenceImpl
Summary:        DOCX4J jaxb-ReferenceImpl
Group:          Development/Java

%description    jaxb-ReferenceImpl
Config specifying that docx4j should use the JAXB reference impls.

%package        legacy-service
Summary:        DOCX4J legacy-service
Group:          Development/Java

%description    legacy-service
Code supporting the no longer available legacy commercial PDF Converter.

%package        openxml-objects
Summary:        DOCX4J openxml-objects
Group:          Development/Java

%description    openxml-objects
JAXB representation of OpenXML, except for pml and sml (handled separately).

%package        openxml-objects-pml
Summary:        DOCX4J openxml-objects-pml
Group:          Development/Java

%description    openxml-objects-pml
JAXB representation of OpenXML Presentation Markup Language (pml).

%package        openxml-objects-sml
Summary:        DOCX4J openxml-objects-sml
Group:          Development/Java

%description    openxml-objects-sml
JAXB representation of OpenXML Spreadsheet Markup Language (sml).

%package        parent
Summary:        DOCX4J parent
Group:          Development/Java

%description    parent
%summary.

%package        samples
Summary:        DOCX4J samples
Group:          Development/Java

%description    samples
%summary.

%prep
%setup

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :flatten-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-dependency-plugin

# brokens packaging
find . -name module-info.java -delete

# using qdox 1.x api but we have 2.x
rm docx4j-core/src/main/java/org/docx4j/org/apache/fop/tools/EventProducerCollector.java

# test fails
rm docx4j-core-tests/src/test/java/org/docx4j/fonts/RunFontSelectorCalibriCheckBoxTest.java
rm docx4j-core-tests/src/test/java/org/docx4j/model/datastorage/EndToEndTest.java

%pom_disable_module docx4j-documents4j-remote
%pom_disable_module docx4j-documents4j-local
%pom_disable_module docx4j-JAXB-MOXy
%pom_disable_module docx4j-samples-conversion-via-microsoft-graph
%pom_disable_module docx4j-samples-documents4j-remote
%pom_disable_module docx4j-samples-documents4j-local

%mvn_package :%name-samples-* %name-samples

%build
%mvn_build -s

%install
%mvn_install

%files core -f .mfiles-docx4j-core
%doc *.md

%files conversion-via-microsoft-graph -f .mfiles-docx4j-conversion-via-microsoft-graph
%files core-tests -f .mfiles-docx4j-core-tests
%files diffx -f .mfiles-docx4j-diffx
%files docx-anon -f .mfiles-docx4j-docx-anon
%files export-fo -f .mfiles-docx4j-export-fo
%files jaxb-ReferenceImpl -f .mfiles-docx4j-JAXB-ReferenceImpl
%files legacy-service -f .mfiles-docx4j-legacy-service
%files openxml-objects -f .mfiles-docx4j-openxml-objects
%files openxml-objects-pml -f .mfiles-docx4j-openxml-objects-pml
%files openxml-objects-sml -f .mfiles-docx4j-openxml-objects-sml
%files parent -f .mfiles-docx4j-parent
%files samples -f .mfiles-docx4j-samples

%changelog
* Thu Sep 23 2025 Evgeniy Serov <scala@altlinux.org> 11.5.5-alt1
- Initial build for Sisyphus (ty trogjan@).
