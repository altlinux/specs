Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define base_name poi
%define namedversion 3.6-20091214

Name:           apache-%{base_name}
Version:        3.6
Release:        alt1_1jpp6
Epoch:          0
Summary:        Java API To Access Microsoft Format Files

Group:          Development/Java
License:        Apache Software License
URL:            http://jakarta.apache.org/poi/
Source0:        http://www.apache.org/dist/poi/release/src/poi-src-3.6-20091214.tar.gz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/poi/poi/3.6/poi-3.6.pom
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/poi/poi-contrib/3.6/poi-contrib-3.6.pom
Source3:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/poi/poi-scratchpad/3.6/poi-scratchpad-3.6.pom
Source4:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/poi/poi-examples/3.6/poi-examples-3.6.pom
Source5:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/poi/poi-ooxml-schemas/3.6/poi-ooxml-schemas-3.6.pom
Source6:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/poi/poi-ooxml/3.6/poi-ooxml-3.6.pom
Source7:        OfficeOpenXML-XMLSchema.zip
# extract it from http://www.ecma-international.org/publications/files/ECMA-ST/Office%20Open%20XML%201st%20edition%20Part%204%20(PDF).zip
Patch0:         apache-poi-build.patch
BuildArch:      noarch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
BuildRequires: junit >= 0:3.8.1
BuildRequires: ant-trax
BuildRequires: jakarta-commons-logging >= 0:1.1
BuildRequires: log4j >= 0:1.2.13
BuildRequires: xmlbeans
Requires: jakarta-commons-logging >= 0:1.1
Requires: log4j >= 0:1.2.13
Requires: xmlbeans
BuildRequires: dom4j geronimo-stax-1.0-api

%description
The Apache POI Project's mission is to create and maintain 
Java APIs for manipulating various file formats based upon 
the Office Open XML standards (OOXML) and Microsoft's OLE 2 
Compound Document format (OLE2). In short, you can read and 
write MS Excel files using Java. In addition, you can read 
and write MS Word and MS PowerPoint files using Java. 
Apache POI is your Java Excel solution (for Excel 97-2008). 
We have a complete API for porting other OOXML and OLE2 
formats and welcome others to participate.

OLE2 files include most Microsoft Office files such as XLS,
DOC, and PPT as well as MFC serialization API based file 
formats. The project provides APIs for the OLE2 Filesystem 
(POIFS) and OLE2 Document Properties (HPSF).

Office OpenXML Format is the new standards based XML file 
format found in Microsoft Office 2007 and 2008. This 
includes XLSX, DOCX and PPTX. The project provides a low 
level API to support the Open Packaging Conventions using 
openxml4j.

For each MS Office application there exists a component 
module that attempts to provide a common high level Java 
api to both OLE2 and OOXML document formats. This is most 
developed for Excel workbooks (SS=HSSF+XSSF). Work is 
progressing for Word documents (HWPF+XWPF) and PowerPoint 
presentations (HSLF+XSLF).

The project has recently added support for Outlook (HSMF). 
Microsoft opened the specifications to this format in 
October 2007. We would welcome contributions.

There are also projects for Visio (HDGF) and Publisher (HPBF).

As a general policy we collaborate as much as possible with 
other projects to provide this functionality. Examples 
include: Cocoon for which there are serializers for HSSF; 
Open Office.org with whom we collaborate in documenting the 
XLS format; and Lucene for which we provide format 
interpretors. When practical, we donate components directly 
to those projects for POI-enabling them. 


%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.


%prep
%setup -q -n poi-%{version}
find . -name "*.jar" -exec mv {} {}.no \;
%patch0 -b .orig
mkdir lib
build-jar-repository -s -p lib \
commons-logging \
junit \
log4j 

mkdir ooxml-lib
build-jar-repository -s -p ooxml-lib \
dom4j \
geronimo-stax-1.0-api \
xmlbeans/xbean

cp %{SOURCE7} ooxml-lib

%build
export LANG=en_US.UTF-8

export ANT_OPTS="-Xmx256m -Djava.awt.headless=true -Ddisconnected=true"
ant -Dhalt.on.test.failure=false compile-ooxml-xsds jar test

%install

install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{base_name}
cp -p build/dist/%{base_name}-%{version}*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}/%{name}-%{version}.jar
cp -p build/dist/%{base_name}-contrib-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}/%{name}-contrib-%{version}.jar
cp -p build/dist/%{base_name}-examples-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}/%{name}-examples-%{version}.jar
cp -p build/dist/%{base_name}-ooxml-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}/%{name}-ooxml-%{version}.jar
cp -p build/dist/%{base_name}-ooxml-schemas-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}/%{name}-ooxml-schemas-%{version}.jar
cp -p build/dist/%{base_name}-scratchpad-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}/%{name}-scratchpad-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{base_name} && for jar in %{name}*-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|apache-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{base_name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.poi %{base_name} %{version} JPP/%{base_name} %{base_name}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-contrib.pom
%add_to_maven_depmap org.apache.poi %{base_name}-contrib %{version} JPP/%{base_name} %{base_name}-contrib
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-scratchpad.pom
%add_to_maven_depmap org.apache.poi %{base_name}-scratchpad %{version} JPP/%{base_name} %{base_name}-scratchpad
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-examples.pom
%add_to_maven_depmap org.apache.poi %{base_name}-examples %{version} JPP/%{base_name} %{base_name}-examples
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-ooxml-schemas.pom
%add_to_maven_depmap org.apache.poi %{base_name}-ooxml-schemas %{version} JPP/%{base_name} %{base_name}-ooxml-schemas
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-ooxml.pom
%add_to_maven_depmap org.apache.poi %{base_name}-ooxml %{version} JPP/%{base_name} %{base_name}-ooxml

#javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf docs/apidocs

#manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/apidocs # ghost symlink

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE
%dir %{_javadir}/%{base_name}
%{_javadir}/%{base_name}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_1jpp6
- new version

