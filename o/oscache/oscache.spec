Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: servletapi4
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


Summary:        High performance J2EE caching solution
Name:           oscache
Version:        2.4.1
Release:        alt2_1jpp5
Epoch:          0
License:        ASL 2.0
Group:          Development/Java
URL:            http://www.opensymphony.com/oscache/
# svn export http://svn.opensymphony.com/svn/oscache/tags/v2_4_1 oscache-2.4.1
# tar cjf oscache-2.4.1.tar.bz2 oscache-2.4.1
Source0:        oscache-2.4.1.tar.bz2
Source1:        oscache-2.4.1-osbuild.xml
Source2:	oscache-2.4.1-ivyconf.xml
Source3:	oscache-2.4.1-ivy.xml
Patch0:		oscache-2.4.1-no-clover.patch
Patch1:		oscache-2.4.1-no-groboutils.patch
Requires: jakarta-commons-logging
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit
BuildRequires: junit >= 0:3.8.2
BuildRequires: apache-ivy
BuildRequires: ant-trax
BuildRequires: junitperf >= 0:1.9.1
BuildRequires: hibernate3 >= 0:3.2.4
BuildRequires: httpunit >= 0:1.6
BuildRequires: jms >= 0:1.1
BuildRequires: servlet >= 0:2.3
BuildRequires: jakarta-commons-logging >= 0:1.1
BuildRequires: jgroups >= 0:2.2.8
BuildArch:      noarch

%description
OSCache solves fundamental problems for dynamic websites:
+ Caching Dynamic Content - Dynamic content must often be 
executed in some form each request, but sometimes that 
content doesn't change every request. Caching the whole 
page does not help because sections of the page change 
every request. OSCache solves this problem by providing 
a means to cache sections of JSP pages. 
+ Caching Binary Content - Generated images and PDFs can 
be very costly in terms of server load. OSCache solves 
this problem through a Servlet 2.3 CachingFilter which 
can cache any URI (such as an entire page or a generated 
image/PDF) 
+ Error Tolerance - If one error occurs somewhere on your 
dynamic page, chances are the whole page will be returned 
as an error, even if 95%% of the page executed correctly. 
OSCache solves this problem by allowing you to serve the 
cached content in the event of an error, and then 
reporting the error appropriately. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q
# FIXME: (dwalluck): remove the dependency on GroboUtils (we don't have it)
rm src/test/java/com/opensymphony/oscache/base/TestConcurrency2.java
# Archive is clean
#find . -name "*.[jw]ar" | xargs rm

cp -p %{SOURCE1} osbuild.xml
cp -p %{SOURCE2} ivyconf.xml
cp -p %{SOURCE3} ivy.xml

cp -p trunk/ivyconf.properties ivyconf.properties
touch EMPTY.MF

%patch0 -p1
%patch1 -p1

sed -i -e s,fr.jayasoft.ivy,org.apache.ivy,g build.xml osbuild.xml

%build

    export CLASSPATH=$(build-classpath apache-ivy ant/ant-junit junit ant/ant-trax)
export CLASSPATH=
export OPT_JAR_LIST="apache-ivy ant/ant-junit junit ant/ant-trax"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dskip.tests=true -Dcommon.build=osbuild.xml jar
# docs example-war 

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
#mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
## FIXME: (dwalluck) breaks --short-circuit
#rm -rf dist/docs/api

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr dist/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -p dist/oscache-example.war $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%doc LICENSE.txt
%{_javadir}/*

#files javadoc
#%{_javadocdir}/%{name}-%{version}
#%{_javadocdir}/%{name}

#files manual
#%doc %{_docdir}/%{name}-%{version}

# -----------------------------------------------------------------------------

%changelog
* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_1jpp5
- fixed build

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_1jpp5
- new version

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_2jpp1.7
- converted from JPackage by jppimport script

