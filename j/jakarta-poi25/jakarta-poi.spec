Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define oldname jakarta-poi
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

%define base_name poi

Name:           jakarta-poi25
Version:        2.5.1
Release:        alt2_2jpp5
Epoch:          0
Summary:        Java API To Access Microsoft Format Files

Group:          Development/Java
License:        Apache Software License
URL:            http://jakarta.apache.org/poi/
Source0:        poi-src-2.5.1-final-20040804.tar.gz
#cvs -d :pserver:anoncvs@cvs.apache.org:/home/cvspublic  login
#cvs -z3 -d :pserver:anoncvs@cvs.apache.org:/home/cvspublic export -r HEAD jakarta-poi/src/scratchpad
Source1:	poi-scratchpad-unreleased-src-20050824.tar.gz

Patch0:         poi-build_xml.patch
BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: junit >= 0:3.8.1
BuildRequires: ant-trax >= 0:1.6
BuildRequires: jaxp_transform_impl
BuildRequires: ant-jdepend >= 0:1.6
BuildRequires: jdepend >= 0:2.6
BuildRequires: jakarta-commons-beanutils >= 0:1.6.1
BuildRequires: jakarta-commons-collections >= 0:2.1
BuildRequires: jakarta-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-logging >= 0:1.0.3
BuildRequires: log4j >= 0:1.2.8
BuildRequires: xalan-j2 >= 0:2.5.2
BuildRequires: xerces-j2 >= 0:2.6.0
Requires: jakarta-commons-beanutils >= 0:1.6.1
Requires: jakarta-commons-collections >= 0:2.1
Requires: jakarta-commons-lang >= 0:2.0
Requires: jakarta-commons-logging >= 0:1.0.3
Requires: log4j >= 0:1.2.8
Requires: xalan-j2 >= 0:2.5.2
Requires: xerces-j2 >= 0:2.6.0

%description
The POI project consists of APIs for manipulating 
various file formats based upon Microsoft's OLE 2 
Compound Document format using pure Java. In short, 
you can read and write MS Excel files using Java. 
Soon, you'll be able to read and write Word files 
using Java. POI is your Java Excel solution as well 
as your Java Word solution. However, we have a 
complete API for porting other OLE 2 Compound 
Document formats and welcome others to participate. 
OLE 2 Compound Document Format based files include 
most Microsoft Office files such as XLS and DOC as 
well as MFC serialization API based file formats. 


%package        javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{oldname}
Group:          Development/Documentation

%description    manual
%{summary}.


%prep
%setup -c -q -n %{base_name}
#find . -name "*.jar" -exec rm {} \;
find . -name "*.jar" -exec mv {} {}.no \;
gzip -dc %{SOURCE1} | tar xf -
rm -rf src/scratchpad/src/org/apache/poi/hslf/
rm -rf src/scratchpad/testcases/org/apache/poi/hslf/

%patch0 -b .sav

%build
export LANG=en_US.ISO8859-1
export OPT_JAR_LIST="ant/ant-junit junit ant/ant-jdepend jdepend jaxp_transform_impl ant/ant-trax"
export CLASSPATH=$(build-classpath \
commons-beanutils \
commons-collections \
commons-lang \
commons-logging \
log4j \
xalan-j2 \
xerces-j2)
export ANT_OPTS="-Xmx256m -Djava.awt.headless=true -Dbuild.sysclasspath=first -Ddisconnected=true"
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar #test

%install

install -dm 755 $RPM_BUILD_ROOT%{_javadir}
cp -p build/dist/%{base_name}-%{version}-final-*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
cp -p build/dist/%{base_name}-contrib-%{version}-final-*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib-%{version}.jar
cp -p build/dist/%{base_name}-scratchpad-%{version}-final-*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-scratchpad-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in %{name}*-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

#javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
cp -pr docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
ln -s %{oldname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{oldname} # ghost symlink
rm -rf docs/apidocs

#manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{oldname}-%{version} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/apidocs # ghost symlink

%post javadoc
rm -f %{_javadocdir}/%{oldname}
ln -s %{oldname}-%{version} %{_javadocdir}/%{oldname}


%files
%doc %{_docdir}/%{name}-%{version}/LICENSE
%dir %{_docdir}/%{name}-%{version}
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{oldname}-%{version}
%ghost %doc %{_javadocdir}/%{oldname}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt2_2jpp5
- fixed build with java 7

* Tue May 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_2jpp5
- compat version

