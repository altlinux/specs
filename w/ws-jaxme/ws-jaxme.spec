Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: docbook-dtds
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Copyright (c) 2000-2005, JPackage Project
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

%bcond_without  hsqldb

%global base_name jaxme

Name:           ws-jaxme
Version:        0.5.2
Release:        alt5_22jpp8
Epoch:          0
Summary:        Open source implementation of JAXB
License:        ASL 2.0
URL:            http://ws.apache.org/
# svn export http://svn.apache.org/repos/asf/webservices/archive/jaxme/tags/R0_5_2/ ws-jaxme-0.5.2
# tar czf ws-jaxme-0.5.2-src.tar.gz ws-jaxme-0.5.2
Source0:        ws-jaxme-0.5.2-src.tar.gz
Source1:        ws-jaxme-bind-MANIFEST.MF

Source2:        http://repo1.maven.org/maven2/org/apache/ws/jaxme/jaxme2/%{version}/jaxme2-%{version}.pom
Source3:        http://repo1.maven.org/maven2/org/apache/ws/jaxme/jaxme2-rt/%{version}/jaxme2-rt-%{version}.pom
Source4:        http://repo1.maven.org/maven2/org/apache/ws/jaxme/jaxmeapi/%{version}/jaxmeapi-%{version}.pom
Source5:        http://repo1.maven.org/maven2/org/apache/ws/jaxme/jaxmejs/%{version}/jaxmejs-%{version}.pom
Source6:        http://repo1.maven.org/maven2/org/apache/ws/jaxme/jaxmepm/%{version}/jaxmepm-%{version}.pom
Source7:        http://repo1.maven.org/maven2/org/apache/ws/jaxme/jaxmexs/%{version}/jaxmexs-%{version}.pom

# generated docs with forrest-0.5.1
Patch0:         ws-jaxme-docs_xml.patch
Patch1:         ws-jaxme-catalog.patch
Patch2:         ws-jaxme-system-dtd.patch
Patch3:         ws-jaxme-jdk16.patch
Patch4:         ws-jaxme-ant-scripts.patch
Patch5:         ws-jaxme-use-commons-codec.patch
# Remove xmldb-api, deprecated since f17
Patch6:         ws-jaxme-remove-xmldb.patch
Patch7:         ws-jaxme-0.5.2-class-version15.patch

BuildArch:      noarch
BuildRequires:  javapackages-local
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-apache-resolver
BuildRequires:  antlr-tool
BuildRequires:  apache-commons-codec
BuildRequires:  junit
%if %{with hsqldb}
BuildRequires:  hsqldb1
%endif
BuildRequires:  log4j12
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-dtds
Requires:       antlr-tool
Requires:       apache-commons-codec
Requires:       junit
%if %{with hsqldb}
Requires:       hsqldb1
%endif
Requires:       log4j12
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       jpackage-utils
Source44: import.info

%description
A Java/XML binding compiler takes as input a schema 
description (in most cases an XML schema, but it may 
be a DTD, a RelaxNG schema, a Java class inspected 
via reflection, or a database schema). The output is 
a set of Java classes:
* A Java bean class matching the schema description. 
  (If the schema was obtained via Java reflection, 
  the original Java bean class.)
* Read a conforming XML document and convert it into 
  the equivalent Java bean.
* Vice versa, marshal the Java bean back into the 
  original XML document.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Group: Development/Java
Summary:        Documents for %{name}
BuildArch: noarch

%description    manual
%{summary}.

%prep
%setup -q
find . -name "*.jar" -print -delete

%patch0 -p0
%patch1 -p0
%patch2 -p1
DOCBOOKX_DTD=`xmlcatalog %{_datadir}/sgml/docbook/xmlcatalog "-//OASIS//DTD DocBook XML V4.5//EN" 2>/dev/null`
sed -i 's|@DOCBOOKX_DTD@|$DOCBOOKX_DTD|' src/documentation/manual/jaxme2.xml
%patch3 -p1
%patch4 -b .sav
%patch5 -b .sav
%patch6 -p1
%patch7 -p1

sed -i 's/\r//' NOTICE

sed -i "s|log4j.jar|log4j12-1.2.17.jar|" ant/js.xml
sed -i "s|hsqldb.jar|hsqldb1-1.jar|" ant/js.xml ant/pm.xml

%if %{without hsqldb}
rm -r src/js/org/apache/ws/jaxme/sqls/hsqldb
%pom_xpath_remove 'target[@name="JS.generate"]/@depends' ant/js.xml
%endif

%build
export CLASSPATH=$(build-classpath antlr hsqldb1-1 commons-codec junit log4j12-1.2.17 xerces-j2 xalan-j2 xalan-j2-serializer)
ant all Docs.all \
-Dbuild.sysclasspath=first \
-Ddocbook.home=%{_datadir}/sgml/docbook \
-Ddocbookxsl.home=%{_datadir}/sgml/docbook/xsl-stylesheets

# Inject OSGi manifest
jar ufm dist/jaxmeapi-%{version}.jar %{SOURCE1}

%install
%mvn_file ':{*}' %{base_name}/@1 %{base_name}/ws-@1

for jar in jaxme2 jaxme2-rt jaxmeapi jaxmejs jaxmepm jaxmexs; do
   %mvn_artifact %{_sourcedir}/${jar}-%{version}.pom dist/${jar}-%{version}.jar
done

%mvn_install -J build/docs/src/documentation/content/apidocs

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%files manual
%doc LICENSE NOTICE
%doc build/docs/src/documentation/content/manual

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt5_22jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt5_19jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt5_16jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt5_15jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt5_14jpp8
- dropped dep on xmldb-api-sdk

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt4_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt4_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt4_8jpp7
- new release

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt4_6jpp7
- fixed build

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt3_6jpp7
- fixed deps

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt2_6jpp7
- fc release

* Fri May 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt2_1jpp5
- explicitly selected java5 compiler

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt1_1jpp5
- added OSGi provides

* Tue Oct 23 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.5.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Sun May 06 2007 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2
- added JPackage compatible symlinks

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 0.3.1-alt1
- Initial build for ALT Linux Sisyphus

