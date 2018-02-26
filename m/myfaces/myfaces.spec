Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: struts-taglib struts-tiles
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


Summary:        JSF Implementation
Name:           myfaces
Version:        1.1.0
Release:        alt3_3jpp5
Epoch:          0
License:        Apache Software License 2.0
URL:            http://myfaces.apache.org/
Group:          Development/Java
Source0:        myfaces-1.1.0-src.tar.gz
# svn export https://svn.apache.org/repos/asf/myfaces/release/tags/1_1_0

Patch0:         myfaces-1.1.0-build_xml.patch
BuildRequires: ant >= 0:1.6 ant-junit >= 0:1.6 jpackage-utils >= 0:1.5
BuildRequires: junit
BuildRequires: asm
BuildRequires: cglib
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-el10
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-validator
BuildRequires: jsp
BuildRequires: easymock-classextension
BuildRequires: easymock
BuildRequires: oro
BuildRequires: jakarta-taglibs-standard
BuildRequires: portlet-1.0-api
BuildRequires: servletapi5
BuildRequires: struts
BuildRequires: tlddoc
BuildRequires: xdoclet
BuildRequires: xjavadoc
BuildRequires: xml-commons-apis
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-codec
Requires: jakarta-commons-collections
Requires: jakarta-commons-digester
Requires: jakarta-commons-el10
Requires: jakarta-commons-fileupload
Requires: jakarta-commons-logging
Requires: jakarta-commons-validator
Requires: jsp
Requires: portlet-1.0-api
Requires: servletapi5
Requires: struts
Requires: xml-commons-apis
BuildArch:      noarch

%description
JavaServer(tm) Faces is a new and upcoming web application framework 
that accomplishes the MVC paradigm. It is comparable to the 
well-known Struts Framework but has features and concepts that 
are beyond those of Struts; especially the component orientation. 
Look at Sun's JavaServer(tm) Page to learn more about the Java 
Specification Request 127  and to download the specification. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation

%description demo
%{summary}.

%prep
%setup -q -n %{name}-%{version}-src
# remove all binary libs
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done

%patch0 -b .sav

%build
mkdir -p build/dist/temp
mkdir lib
pushd lib
ln -sf $(build-classpath asm/asm) .
ln -sf $(build-classpath cglib) .
ln -sf $(build-classpath commons-beanutils) .
ln -sf $(build-classpath commons-codec) .
ln -sf $(build-classpath commons-collections) .
ln -sf $(build-classpath commons-digester) .
ln -sf $(build-classpath commons-el10) commons-el.jar
ln -sf $(build-classpath commons-fileupload) .
ln -sf $(build-classpath commons-logging) .
ln -sf $(build-classpath commons-validator) .
ln -sf $(build-classpath easymock-classextension) .
ln -sf $(build-classpath easymock) .
ln -sf $(build-classpath oro) jakarta-oro.jar
ln -sf $(build-classpath jsp) jsp.jar
ln -sf $(build-classpath taglibs-core) jstl.jar
ln -sf $(build-classpath junit) .
ln -sf $(build-classpath portlet-1.0-api) portlet-api.jar
ln -sf $(build-classpath servletapi5) servlet-api.jar
ln -sf $(build-classpath struts) .
ln -sf $(build-classpath struts-taglib) .
ln -sf $(build-classpath struts-tiles) .
ln -sf $(build-classpath tlddoc) .
ln -sf $(build-classpath xdoclet/xdoclet) .
ln -sf $(build-classpath xjavadoc) .
popd

cd build
export CLASSPATH=$(build-classpath struts-tiles)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Dskip.sandbox=true dist-all

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}

cp -p api/build/dist/%{name}-api.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jsf-api-%{version}.jar
cp -p build/dist/%{name}-all.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-all-%{version}.jar
cp -p impl/build/dist/%{name}-impl.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-impl-%{version}.jar
cp -p tomahawk/build/dist/tomahawk.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/tomahawk-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tomahawk
cp -pr api/build/temp/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
cp -pr impl/build/temp/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
cp -pr tomahawk/build/temp/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tomahawk
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p api/build/LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}/*.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt3_3jpp5
- fixed build

* Fri May 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt2_3jpp5
- fixed build

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_3jpp5
- fixed repocop warnings

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

