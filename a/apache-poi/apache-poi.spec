Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ rpm-build-java swig unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global reldate 20160924

Name:          apache-poi
Version:       3.15
Release:       alt1_1jpp8
Summary:       The Java API for Microsoft Documents
# ASLv2 + GPLv3 src/resources/scratchpad/org/apache/poi/hdgf/chunks_parse_cmds.tbl
# https://bugzilla.redhat.com/show_bug.cgi?id=1146670#c13
License:       ASL 2.0 and (CC-BY and CC-BY-SA and W3C) and GPLv3
URL:           http://poi.apache.org/
Source0:       http://archive.apache.org/dist/poi/release/src/poi-src-%{version}%{?reldate:-}%{?reldate}.tar.gz
# Creative Commons license 4.0 (Attribution-ShareAlike)
# These two zip files renamed after download for deficiencies in fedpkg
#Source1:       http://www.ecma-international.org/publications/files/ECMA-ST/Office%20Open%20XML%201st%20edition%20Part%204%20%28PDF%29.zip
#Source2:       http://www.ecma-international.org/publications/files/ECMA-ST/Office%20Open%20XML%201st%20edition%20Part%202%20%28PDF%29.zip
Source1:       Office_Open_XML_1st_edition_Part_4__PDF_.zip
Source2:       Office_Open_XML_1st_edition_Part_2__PDF_.zip
# Creative Commons Attribution 3.0 License
Source3:       http://dublincore.org/schemas/xmls/qdc/2003/04/02/dc.xsd
Source4:       http://dublincore.org/schemas/xmls/qdc/2003/04/02/dcterms.xsd
Source5:       http://dublincore.org/schemas/xmls/qdc/2003/04/02/dcmitype.xsd
# W3C
Source6:       http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd
# http://www.etsi.org/index.php/terms-of-use
# see https://bz.apache.org/bugzilla/show_bug.cgi?id=57862
Source7:       http://uri.etsi.org/01903/v1.3.2/XAdES.xsd
Source8:       http://uri.etsi.org/01903/v1.4.1/XAdESv141.xsd

Source9:       http://repo2.maven.org/maven2/org/apache/poi/poi/%{version}/poi-%{version}.pom
Source10:      http://repo2.maven.org/maven2/org/apache/poi/poi-examples/%{version}/poi-examples-%{version}.pom
Source11:      http://repo2.maven.org/maven2/org/apache/poi/poi-excelant/%{version}/poi-excelant-%{version}.pom
Source12:      http://repo2.maven.org/maven2/org/apache/poi/poi-ooxml/%{version}/poi-ooxml-%{version}.pom
Source13:      http://repo2.maven.org/maven2/org/apache/poi/poi-ooxml-schemas/%{version}/poi-ooxml-schemas-%{version}.pom
Source14:      http://repo2.maven.org/maven2/org/apache/poi/poi-scratchpad/%{version}/poi-scratchpad-%{version}.pom

# Force compile of xsds if disconnected
Patch1:        apache-poi-3.14-compile-xsds.patch
# Disable javadoc doclint
Patch2:        apache-poi-3.14-build.patch

BuildArch:     noarch

BuildRequires: jacoco
BuildRequires: javapackages-local
BuildRequires: apache-commons-collections4 >= 4.1
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-logging
BuildRequires: mvn(com.github.virtuald:curvesapi)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.santuario:xmlsec) >= 2.0.1
BuildRequires: mvn(org.apache.xmlbeans:xmlbeans)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.ow2.asm:asm-all)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(rhino:js)

#Fonts for testing
BuildRequires: fontconfig fonts-ttf-liberation fonts-ttf-liberation

Obsoletes:     %{name}-manual <= %{version}-%{release}
Source44: import.info

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

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n poi-%{version}
%patch1
%patch2

find -name '*.class' -delete
find -name '*.jar' -delete

mkdir lib ooxml-lib
build-jar-repository -s -p lib ant commons-collections4 commons-codec commons-logging hamcrest/core junit bcprov bcpkix xmlsec slf4j/slf4j-api log4j-1.2.17
build-jar-repository -s -p ooxml-lib dom4j xmlbeans/xbean curvesapi

#Unpack the XMLSchema
pushd ooxml-lib
unzip "%SOURCE1" OfficeOpenXML-XMLSchema.zip
unzip "%SOURCE2" OpenPackagingConventions-XMLSchema.zip
cp -p %SOURCE3 .
cp -p %SOURCE4 .
cp -p %SOURCE5 .
cp -p %SOURCE6 .
cp -p %SOURCE7 .
cp -p %SOURCE8 .
popd

# Customize pom file
cp -p %SOURCE11 .
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId ='ant']" "
<scope>provided</scope>" poi-excelant-%{version}.pom

%mvn_file org.apache.poi:poi poi/%{name} poi/poi
for m in examples excelant ooxml ooxml-schemas scratchpad;do
%mvn_file org.apache.poi:poi-${m} poi/%{name}-${m} poi/poi-${m}
done

# These tests fails on arm builders
rm src/ooxml/testcases/org/apache/poi/xssf/usermodel/TestXSSFSheet.java \
 src/ooxml/testcases/org/apache/poi/xssf/usermodel/TestXSSFSheetMergeRegions.java
sed -i '/TestXSSFSheet/d' src/ooxml/testcases/org/apache/poi/xssf/usermodel/AllXSSFUsermodelTests.java

%build
cat > build.properties <<'EOF'
main.ant.jar=lib/ant.jar
main.commons-collections4.jar=lib/commons-collections4.jar
main.commons-codec.jar=lib/commons-codec.jar
main.commons-logging.jar=lib/commons-logging.jar
main.log4j.jar=lib/log4j-1.2.17.jar
main.junit.jar=lib/junit.jar
main.hamcrest.jar=lib/hamcrest_core.jar
ooxml.dom4j.jar=ooxml-lib/dom4j.jar
ooxml.curvesapi.jar=ooxml-lib/curvesapi.jar
ooxml.xmlbeans23.jar=ooxml-lib/xmlbeans_xbean.jar
ooxml.xmlbeans26.jar=ooxml-lib/xmlbeans_xbean.jar
dsig.xmlsec.jar=lib/xmlsec.jar
dsig.bouncycastle-prov.jar=lib/bcprov.jar
dsig.bouncycastle-pkix.jar=lib/bcpkix.jar
dsig.sl4j-api.jar=lib/slf4j_slf4j-api.jar
disconnected=1
DSTAMP=%{reldate}
EOF

export ANT_OPTS="-Xmx768m"
ant -propertyfile build.properties compile-ooxml-xsds jar javadocs

%install
for m in poi poi-excelant poi-examples poi-ooxml poi-ooxml-schemas poi-scratchpad ; do
%mvn_artifact $RPM_SOURCE_DIR/${m}-%{version}.pom build/dist/maven/$m/${m}-%{version}.jar
done

%mvn_install -J build/tmp/site/build/site/apidocs

%check
# To enable 8-bit character tests
export LANG=en_US.UTF-8
# Ignore test failures for now
ant -propertyfile build.properties test || :

%files -f .mfiles
%doc KEYS
%doc LICENSE NOTICE
 
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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

