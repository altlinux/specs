Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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

%define gcj_support 0


Summary:        OpenSymphony Utilities
Name:           oscore
Version:        2.2.5
Release:        alt1_2jpp5
Epoch:          0
License:        Apache Software License modified
URL:            http://www.opensymphony.com/oscore/
Group:          Development/Java
Source0:        oscore-2.2.5.zip
Source1:        oscore-osbuild.xml
Patch0:         oscore-2.2.5-build_xml.patch
Patch1:         oscore-xalan-2.7.0-XalanXMLPrinterProvider.patch
Patch2:         oscore-osbuild.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: ant-nodeps
BuildRequires: ant-trax
BuildRequires: javacc3
BuildRequires: aelfred
BuildRequires: jalopy
BuildRequires: jalopy-ant
BuildRequires: jdom
BuildRequires: log4j
BuildRequires: jakarta-oro
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: junit >= 0:3.8.1
BuildRequires: mockobjects-jdk1.4-j2ee1.4
BuildRequires: mockobjects-alt-jdk1.4
BuildRequires: mockobjects
BuildRequires: velocity
BuildRequires: jakarta-commons-collections
BuildRequires: xdoclet
BuildRequires: xjavadoc
BuildRequires: jakarta-commons-logging
#BuildRequires:  crimson
BuildRequires: ejb_2_1_api
BuildRequires: javamail_1_3_1_api
BuildRequires: ognl
BuildRequires: servlet_2_3_api
BuildRequires: xalan-j2 >= 0:2.7.0


Requires: xml-commons-jaxp-1.3-apis
Requires: ognl
Requires: jakarta-commons-logging
Requires: log4j
Requires: xalan-j2
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
OSCore is a set of utility-classes that are common to 
the other components of OpenSymphony. Contains essential 
functionality for any J2EE application.

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
%setup -c -q -n %{name}
for j in $(find . -name "*.jar"); do
  mv $j $j.no
done
cp %{SOURCE1} osbuild.xml
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

%build
pushd lib/build
pushd jalopy
ln -sf $(build-classpath aelfred)
ln -sf $(build-classpath jalopy)
ln -sf $(build-classpath jalopy-ant)
ln -sf $(build-classpath jdom)
ln -sf $(build-classpath log4j)
ln -sf $(build-classpath oro)
ln -sf $(build-classpath xerces-j2)
ln -sf $(build-classpath xml-commons-apis)
popd
ln -sf $(build-classpath junit)
ln -sf $(build-classpath mockobjects-jdk1.4-j2ee1.4)
ln -sf $(build-classpath mockobjects-alt-jdk1.4)
ln -sf $(build-classpath mockobjects-jdk1.4)
ln -sf $(build-classpath mockobjects-core)
ln -sf $(build-classpath velocity)
pushd xdoclet
ln -sf $(build-classpath commons-collections)
ln -sf $(build-classpath xdoclet/xdoclet)
ln -sf $(build-classpath xdoclet/xdoclet-bea-module)
ln -sf $(build-classpath xdoclet/xdoclet-ejb-module)
ln -sf $(build-classpath xdoclet/xdoclet-jboss-module)
ln -sf $(build-classpath xdoclet/xdoclet-jmx-module)
ln -sf $(build-classpath xdoclet/xdoclet-macromedia-module)
ln -sf $(build-classpath xdoclet/xdoclet-orion-module)
ln -sf $(build-classpath xdoclet/xdoclet-web-module)
ln -sf $(build-classpath xjavadoc)
popd
popd
pushd lib/core
ln -sf $(build-classpath commons-logging)
#ln -sf $(build-classpath crimson)
ln -sf $(build-classpath ejb_2_1_api)
ln -sf $(build-classpath log4j)
ln -sf $(build-classpath javamail_1_3_1_api)
ln -sf $(build-classpath ognl)
ln -sf $(build-classpath servlet_2_3_api)
ln -sf $(build-classpath xalan-j2)
ln -sf $(build-classpath xalan-j2-serializer)
ln -sf $(build-classpath xerces-j2)
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis)
popd

echo package = com.opensymphony >> build.properties

export OPT_JAR_LIST="ant/ant-junit junit ant/ant-trax"
ant jar javadocs junit.report

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf dist/docs/api

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr dist/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Thu Jun 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.5-alt1_2jpp5
- new version

