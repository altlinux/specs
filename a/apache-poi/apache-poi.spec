Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global reldate 20120326
%global rcver %{nil}

Name:           apache-poi
Version:        3.8
Release:        alt2_3jpp7
Summary:        The Java API for Microsoft Documents

Group:          Development/Java
License:        ASL 2.0
URL:            http://poi.apache.org/
Source0:        http://www.apache.org/dist/poi/release/src/poi-src-%{version}-%{reldate}.tar.gz
#Source0:        http://www.apache.org/dist/poi/dev/src/poi-src-%{version}%{?rcver}-%{reldate}.tar.gz
Source1:        http://www.ecma-international.org/publications/files/ECMA-ST/Office%%20Open%%20XML%%201st%%20edition%%20Part%%204%%20(PDF).zip
Source2:        http://repo2.maven.org/maven2/org/apache/poi/poi/%{version}/poi-%{version}.pom
#Force compile of xsds if disconnected
Patch1:         %{name}-3.7-compile-xsds.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=799078
Patch2:         apache-poi-CVE-2012-0213.patch
# https://issues.apache.org/bugzilla/show_bug.cgi?id=53369
# Patch to fix build with JDK 1.7
Patch3:         apache-poi-jdk17.patch
BuildArch:      noarch
ExcludeArch:    ppc64

BuildRequires:  jpackage-utils
BuildRequires:  ant-junit
BuildRequires:  dom4j
BuildRequires:  apache-commons-logging
BuildRequires:  junit
#Fonts for testing
BuildRequires:  fontconfig fonts-ttf-liberation fonts-ttf-liberation
BuildRequires:  log4j
BuildRequires:  xmlbeans

Requires:       jpackage-utils
Requires:       dom4j
Requires:       apache-commons-logging
Requires:       log4j
Requires:       xmlbeans
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
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%package manual
Summary:        Manual for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Requires:       %{name}-javadoc = %{?epoch:%epoch:}%{version}-%{release}
BuildArch: noarch

%description manual
The manual for %{name}.


%prep
%setup -q -n poi-%{version}%{?rcver}
%patch1 -p1 -b .compile-xsds
%patch2 -p0 -b .CVE-2012-0213
%patch3 -p1 -b .jdk17
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
mkdir lib ooxml-lib
build-jar-repository -s -p lib ant commons-codec commons-logging junit log4j
build-jar-repository -s -p ooxml-lib dom4j xmlbeans/xbean
#Unpack the XMLSchema
pushd ooxml-lib
unzip "%SOURCE1" OfficeOpenXML-XMLSchema.zip
popd


%build
cat > build.properties <<'EOF'
main.ant.jar=lib/ant.jar
main.commons-codec.jar=lib/commons-codec.jar
main.commons-logging.jar=lib/commons-logging.jar
main.log4j.jar=lib/log4j.jar
main.junit.jar=lib/junit.jar
ooxml.dom4j.jar=ooxml-lib/dom4j.jar
ooxml.xmlbeans.jar=ooxml-lib/xmlbeans_xbean.jar
disconnected=1
DSTAMP=%{reldate}
EOF
export ANT_OPTS="-Xmx768m"
ant -propertyfile build.properties compile-ooxml-xsds jar


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}/poi
for jar in poi poi-examples poi-ooxml poi-ooxml-schemas poi-scratchpad
do
  cp -p build/dist/${jar}-%{version}%{?rcver}-%{reldate}.jar   \
        $RPM_BUILD_ROOT%{_javadir}/poi/apache-${jar}.jar
  ln -s apache-${jar}.jar $RPM_BUILD_ROOT%{_javadir}/poi/${jar}.jar
done
#pom
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp -p %SOURCE2 $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-poi.pom
%add_to_maven_depmap org.apache.poi poi %{version}%{?rcver}-%{reldate} JPP/poi poi

#javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -pr docs/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}
#Don't copy for manual
rm -rf docs/apidocs 

#manual - Link to javadoc location
ln -s ../../javadoc/%{name} docs/apidocs


%check
ant -propertyfile build.properties test


%files
%doc KEYS LICENSE NOTICE
%{_javadir}/poi/
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/JPP-poi.pom

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%files manual
%doc --no-dereference LICENSE docs/*


%changelog
* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt2_3jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt1_3jpp7
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_1jpp6
- new version

