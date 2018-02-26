Packager: Igor Vlasenko <viy@altlinux.ru>
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define repo    %{_javadir}/repository.jboss.com
%define repodir %{repo}/apache-xml-commons/1.3.04-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
#%%define resolverrepodir    %{repo}/apache-xml-commons-resolver/1.2-brew
#%%define resolverrepodirlib %{repodir}/lib
#%%define resolverrepodirsrc %{repodir}/src

%define resolverdir %{_sysconfdir}/java/resolver

# To get around having multiple versions of projects within the same srpm
%define apis_version_1_1 1.0.b2
%define apis_version_1_2 1.2.04

Name:           xml-commons
Version:        1.3.04
Release:        alt5_9jpp6
Summary:        Common code for XML projects
Epoch:          0
License:        ASL 2.0
URL:            http://xml.apache.org/commons/
# svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-1_0_b2/
Source0:        xml-commons-1.0.b2.tar.bz2
# svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-external-1_2_04/
Source1:        xml-commons-external-1.2.04.tar.bz2
# svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-external-1_3_04/
Source2:        xml-commons-external-1.3.04.tar.bz2
# svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-resolver-1_1_b1/
Source3:        xml-commons-resolver-1.1.b1.tar.bz2
Source4:        xml-commons.which10.script
Source5:        xml-commons.which11.script
Source6:        xml-commons-resolver10-resolver.1
Source7:        xml-commons-resolver10-resolver.sh
Source8:        xml-commons-resolver10-xparse.1
Source9:        xml-commons-resolver10-xparse.sh
Source10:       xml-commons-resolver10-xread.1
Source11:       xml-commons-resolver10-xread.sh
Source12:       xml-commons-resolver11-resolver.1
Source13:       xml-commons-resolver11-resolver.sh
Source14:       xml-commons-resolver11-xparse.1
Source15:       xml-commons-resolver11-xparse.sh
Source16:       xml-commons-resolver11-xread.1
Source17:       xml-commons-resolver11-xread.sh
Source18:       xml-commons-resolver12-resolver.1
Source19:       xml-commons-resolver12-resolver.sh
Source20:       xml-commons-resolver12-xparse.1
Source21:       xml-commons-resolver12-xparse.sh
Source22:       xml-commons-resolver12-xread.1
Source23:       xml-commons-resolver12-xread.sh
Source24:       %{name}-resolver-CatalogManager.properties
Source100:      xml-commons-component-info.xml
Source200:      http://mirrors.ibiblio.org/pub/mirrors/maven2/xml-apis/xml-apis/1.3.04/xml-apis-1.3.04.pom
Source201:      http://mirrors.ibiblio.org/pub/mirrors/maven2/xml-apis/xml-apis-ext/1.3.04/xml-apis-ext-1.3.04.pom
Patch0:         %{name}-external-1.3-build_xml.patch
Patch1:         %{name}-resolver-crosslink.patch
Patch2:         %{name}-resolver-1.1-build_xml.patch
Patch3:         %{name}-enum.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
BuildRequires: ant
BuildRequires: docbook-style-xsl
BuildRequires: xalan-j2
BuildRequires: jpackage-utils
Group:          Development/Java
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info
Source45: xml-commons-resolver-1.2.jar-OSGi-MANIFEST.MF
Source46: xml-commons-apis-1.4.01.jar-OSGi-MANIFEST.MF
Source47: xml-commons-apis-ext-1.4.01.jar-OSGi-MANIFEST.MF

%description
xml-commons is focused on common code and guidelines for xml projects.
It's first focus will be to organize and have common packaging for the
various externally-defined standards code relating to XML - things like
the DOM, SAX, and JAXP interfaces.
As the xml-commons community forms, we also hope to serve as a holding
area for other common xml-related utilities and code, and to help
promulgate common packaging, testing, documentation, and other
guidelines across all xml.apache.org subprojects.

%package jaxp-1.1-apis
Summary:        JAXP 1.1, DOM2, SAX2, SAX2-ext 1.0 apis
Group:          Development/Java
Provides:       jaxp = 1.1
Provides:       dom = 2
Provides:       sax = 2.0
Provides:       xslt = 1.0
Provides:       xml-commons-apis = %{epoch}:%{apis_version_1_1}-%{release}
Obsoletes:      xml-commons-apis <= 0:1.3.02-2jpp
Requires: jpackage-utils >= 0:1.6
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4

%description jaxp-1.1-apis
DOM 2 org.w3c.dom and SAX XML 2.0 org.xml.sax processor apis used 
by several pieces of Apache software. XSLT 1.0.
This version includes the JAXP 1.1 APIs -- Java API for XML 
Processing 1.1, i.e. javax.xml{.parsers,.transform}

%package jaxp-1.1-apis-javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}-jaxp-1.1-apis
Provides:       %{name}-apis-javadoc = %{epoch}:%{apis_version_1_1}-%{release}
Requires: jpackage-utils

%description jaxp-1.1-apis-javadoc
%{summary}.

%package jaxp-1.1-apis-manual
Group:          Development/Documentation
Summary:        Documents for %{name}-jaxp-1.1-apis

%description jaxp-1.1-apis-manual
%{summary}.

%package which10
Summary:        XmlWhich 1.0 utility from %{name}
Group:          Development/Java
Provides:       xml-commons-which = 0:1.0
Requires: jpackage-utils >= 0:1.6
Requires: jaxp_parser_impl
Requires: xml-commons-jaxp-1.1-apis = %{epoch}:%{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: ant >= 0:1.6
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4

%description which10
%{name}.

%package which10-javadoc
Summary:        Javadoc for %{name}-which10
Group:          Development/Documentation
Requires: jpackage-utils

%description which10-javadoc
Javadoc for %{name}-which.

%package resolver10
Summary:        XmlResolver 1.0 utility from %{name}
Group:          Development/Java
Provides:       xml-commons-resolver = 0:1.0
Requires: jpackage-utils >= 0:1.6
Requires: jaxp_parser_impl
Requires: xml-commons-jaxp-1.1-apis = %{epoch}:%{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4

%description resolver10
%{summary}.

%package resolver10-javadoc
Summary:        Javadoc for %{name}-resolver10
Group:          Development/Documentation
Requires: jpackage-utils

%description resolver10-javadoc
%{summary}.

%package resolver11
Summary:        XmlResolver 1.1 utility from %{name}
Group:          Development/Java
Provides:       xml-commons-resolver = 0:1.1
Requires: jpackage-utils >= 0:1.6
Requires: jaxp_parser_impl
Requires: xml-commons-jaxp-1.2-apis = %{epoch}:%{version}-%{release}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4

%description resolver11
%{summary}.

%package resolver11-javadoc
Summary:        Javadoc for %{name}-resolver11
Group:          Development/Documentation
Requires: jpackage-utils

%description resolver11-javadoc
%{summary}.

%package jaxp-1.2-apis
Summary:        JAXP 1.2, DOM 2, SAX 2.0.1, SAX2-ext 1.0 apis
Group:          Development/Java
Provides:       jaxp = 1.2
Provides:       dom = 2
Provides:       sax = 2.0.1
Provides:       xslt = 1.0
Provides:       xml-commons-apis = %{epoch}:%{apis_version_1_2}-%{release}
Obsoletes:      xml-commons-apis <= 0:1.3.02-2jpp
Requires: jpackage-utils >= 0:1.6
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4

%description jaxp-1.2-apis
DOM 2 org.w3c.dom and SAX XML 2.0 org.xml.sax processor apis used 
by several pieces of Apache software. XSLT 1.0.
This version includes the JAXP 1.2 APIs -- Java API for XML 
Processing 1.2, i.e. javax.xml{.parsers,.transform}

%package jaxp-1.2-apis-javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}-jaxp-1.2-apis
Provides:       %{name}-apis-javadoc = %{epoch}:%{apis_version_1_2}-%{release}
Requires: jpackage-utils

%description jaxp-1.2-apis-javadoc
%{summary}.

%package jaxp-1.2-apis-manual
Group:          Development/Documentation
Summary:        Documents for %{name}-jaxp-1.2-apis

%description jaxp-1.2-apis-manual
%{summary}.

%package jaxp-1.3-apis
Summary:        JAXP 1.3, DOM 2, SAX 2.0.1, SAX2-ext 1.0 apis
Group:          Development/Java
Provides:       jaxp = 1.3
Provides:       dom = 3
Provides:       sax = 2.0.2
Provides:       xslt = 1.0
Provides:       xml-commons-apis = %{epoch}:%{version}-%{release}
Obsoletes:      xml-commons-apis <= 0:1.3.02-2jpp
Requires: jpackage-utils >= 0:1.6
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
AutoReq: yes,noosgi

%description jaxp-1.3-apis
DOM 3 org.w3c.dom and SAX XML 2.0.2 (sax2r3) org.xml.sax
processor apis used by several pieces of Apache software.
Thi version includes the JAXP 1.3 APIs --
JSR 206, Java API for XML Processing 1.3, i.e.
javax.xml{.parsers,.transform,.validation,.datatype,.xtype}.

%package jaxp-1.3-apis-javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}-jaxp-1.3-apis
Provides:       %{name}-apis-javadoc = %{epoch}:%{version}-%{release}
Requires: jpackage-utils

%description jaxp-1.3-apis-javadoc
%{summary}.

%package jaxp-1.3-apis-manual
Group:          Development/Documentation
Summary:        Documents for %{name}-jaxp-1.3-apis

%description jaxp-1.3-apis-manual
%{summary}.

%package which11
Group:          Development/Java
Summary:        XmlWhich 1.1 from %{name}
Provides:       xml-commons-which = 0:1.1
Requires: jpackage-utils >= 0:1.6
Requires: jaxp_parser_impl
Requires: xml-commons-jaxp-1.3-apis = %{epoch}:%{version}-%{release}
Requires: ant >= 0:1.6
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4

%description which11
%{summary}.

%package which11-javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}-which11
Requires: jpackage-utils

%description which11-javadoc
%{summary}.

%package resolver12
Group:          Development/Java
Summary:        XmlResolver 1.2 from %{name}
Provides:       xml-commons-resolver = 0:1.2
Requires: jpackage-utils >= 0:1.6
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jaxp_parser_impl
Requires: xml-commons-jaxp-1.3-apis = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
AutoReq: yes,noosgi

%description resolver12
%{summary}.

%package resolver12-javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}-resolver12
Requires: jpackage-utils

%description resolver12-javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -T -c
%setup -q -T -D -a 0
%setup -q -T -D -a 1
%setup -q -T -D -a 2
%setup -q -T -D -a 3

%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
pushd xml-commons-external-1_3_*
%patch0 -b .sav
popd

for i in `egrep -rl 'enum( |\.)' *| egrep '\.java$'`; do
    %{__perl} -pi -e 's/enum([ \.])/enum1\1/g' $i
done

%build
pushd xml-commons-1_0_b2
pushd java
sed -e 's|call Resolver|call resolver|g' resolver.xml > tempf
sed -e 's|classname="org.apache.xml.resolver.Catalog"|fork="yes" classname="org.apache.xml.resolver.apps.resolver"|g' tempf > resolver.xml
sed -e 's|org.apache.xml.resolver.Catalog|org.apache.xml.resolver.apps.resolver|g' src/manifest.resolver > tempf
cp tempf src/manifest.resolver
rm tempf
popd
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars
popd
pushd xml-commons-resolver-1_1_b1
mkdir -p build/site/components/resolver
pushd java
sed -e 's|call Resolver|call resolver|g' resolver.xml > tempf
sed -e 's|classname="org.apache.xml.resolver.Catalog"|fork="yes" classname="org.apache.xml.resolver.apps.resolver"|g' tempf > resolver.xml
sed -e 's|org.apache.xml.resolver.Catalog|org.apache.xml.resolver.apps.resolver|g' src/manifest.resolver > tempf
cp tempf src/manifest.resolver
rm tempf
popd
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars javadocs
popd
pushd xml-commons-external-1_2_04
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f java/external/build.xml jar javadoc
popd
pushd xml-commons-external-1_3_*
pushd java
sed -e 's|call Resolver|call resolver|g' resolver.xml > tempf
sed -e 's|classname="org.apache.xml.resolver.Catalog"|fork="yes" classname="org.apache.xml.resolver.apps.resolver"|g' tempf > resolver.xml
sed -e 's|org.apache.xml.resolver.Catalog|org.apache.xml.resolver.apps.resolver|g' src/manifest.resolver > tempf
cp tempf src/manifest.resolver
rm tempf
popd
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars javadocs
popd

%install

# Jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
# JAXP11
install -m 644 xml-commons-1_0_b2/java/external/build/xml-apis.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.1-apis-%{version}.jar
# resolver10
install -m 644 xml-commons-1_0_b2/java/build/resolver.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-resolver10-%{version}.jar
# which10
install -m 644 xml-commons-1_0_b2/java/build/which.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-which10-%{version}.jar
# resolver11
install -m 644 xml-commons-resolver-1_1_b1/java/build/resolver.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-resolver11-%{version}.jar
# JAXP12
install -m 644 xml-commons-external-1_2_04/java/external/build/xml-apis.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.2-apis-%{version}.jar
# JAXP13
install -m 644 xml-commons-external-1_3_*/java/external/build/xml-apis.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.3-apis-%{version}.jar
# JAXP13 ext
install -m 644 xml-commons-external-1_3_*/java/external/build/xml-apis-ext.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.3-apis-ext-%{version}.jar
# resolver12
install -m 644 xml-commons-external-1_3_*/java/build/resolver.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-resolver12-%{version}.jar
# which11
install -m 644 xml-commons-external-1_3_*/java/build/which.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-which11-%{version}.jar

pushd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do
ln -sf ${jar} $(echo $jar | sed -e 's|-%{version}\.jar|.jar|');
done
ln -sf %{name}-jaxp-1.1-apis.jar jaxp11.jar
ln -sf %{name}-jaxp-1.2-apis.jar jaxp12.jar
ln -sf %{name}-jaxp-1.3-apis.jar jaxp13.jar
ln -sf %{name}-jaxp-1.3-apis.jar dom3.jar
popd

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE200} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-jaxp-1.3-apis.pom
%add_to_maven_depmap xml-apis xml-apis %{version} JPP %{name}-jaxp-1.3-apis
%{__ln_s} JPP-%{name}-jaxp-1.3-apis.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-apis.pom
%{__cp} -p %{SOURCE201} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-jaxp-1.3-apis-ext.pom
%add_to_maven_depmap xml-apis xml-apis-ext %{version} JPP %{name}-jaxp-1.3-apis-ext

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.1-apis-%{version}

# JAXP11
cp -pr xml-commons-1_0_b2/java/external/build/docs/javadoc/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.1-apis-%{version}
ln -s %{name}-jaxp-1.1-apis-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.1-apis
rm -rf xml-commons-1_0_b2/java/external/build/docs/javadoc

# resolver10
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver10-%{version}/org/apache/xml
cp -pr xml-commons-1_0_b2/java/build/docs/javadocs/org/apache/xml/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver10-%{version}/org/apache/xml
ln -s %{name}-resolver10-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver10

# resolver11
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver11-%{version}/
cp -pr xml-commons-resolver-1_1_b1/build/site/components/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver10-%{version}/
ln -s %{name}-resolver11-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver11

# which10
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which10-%{version}/org/apache/env
cp -pr xml-commons-1_0_b2/java/build/docs/javadocs/org/apache/env/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which10-%{version}/org/apache/env
ln -s %{name}-which10-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which10

# JAXP12
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.2-apis-%{version}
cp -pr xml-commons-external-1_2_04/java/external/build/docs/javadoc/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.2-apis-%{version}
ln -s %{name}-jaxp-1.2-apis-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.2-apis
rm -rf xml-commons-external-1_2_04/java/external/build/docs/javadoc

# JAXP13
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.3-apis-%{version}
cp -pr xml-commons-external-1_3_*/java/external/build/docs/javadoc/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.3-apis-%{version}
ln -s %{name}-jaxp-1.3-apis-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jaxp-1.3-apis
rm -rf xml-commons-external-1_3_*/java/external/build/docs/javadoc

# resolver12
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver12-%{version}
cp -pr xml-commons-external-1_3_*/java/build/apidocs/resolver/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver12-%{version}
ln -s %{name}-resolver12-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-resolver12

# which11
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which11-%{version}
cp -pr xml-commons-external-1_3_*/java/build/apidocs/which/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which11-%{version}
ln -s %{name}-which11-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-which11

# Scripts
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1

cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/xml-which10
cp -p %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/xml-which11

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE7} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-resolver10
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE9} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xread10
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE11} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xparse10

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE6} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-resolver10.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE8} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xread10.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE10} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xparse10.1

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE13} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-resolver11
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE15} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xread11
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE17} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xparse11

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE12} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-resolver11.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE14} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xread11.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE16} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xparse11.1

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE19} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-resolver12
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE21} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xread12
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE23} \
  > $RPM_BUILD_ROOT%{_bindir}/xml-xparse12

sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE18} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-resolver12.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE20} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xread12.1
sed -e 's|__RESOLVERDIR__|%{resolverdir}|' < %{SOURCE22} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/xml-xparse12.1

# Central CatalogManager.properties
install -d -m 755 $RPM_BUILD_ROOT%{resolverdir}
install -m 0644 %{SOURCE24} $RPM_BUILD_ROOT%{resolverdir}/CatalogManager.properties

# docs
# JAXP 1.1
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.1-apis-%{version}
install -m 0644 xml-commons-1_0_b2/java/external/LICENSE* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.1-apis-%{version}
install -m 0644 xml-commons-1_0_b2/java/external/README* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.1-apis-%{version}
# JAXP 1.2
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.2-apis-%{version}
install -m 0644 xml-commons-external-1_2_04/java/external/LICENSE* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.2-apis-%{version}
install -m 0644 xml-commons-external-1_2_04/java/external/README* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.2-apis-%{version}
# JAXP 1.3
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.3-apis-%{version}
install -m 0644 xml-commons-external-1_3_*/java/external/LICENSE* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.3-apis-%{version}
install -m 0644 xml-commons-external-1_3_*/java/external/README* $RPM_BUILD_ROOT%{_datadir}/%{name}-jaxp-1.3-apis-%{version}

# manuals
# JAXP 1.1
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.1-apis-%{version}
cp -pr xml-commons-1_0_b2/java/external/build/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.1-apis-%{version}
# JAXP 1.2
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.2-apis-%{version}
cp -pr xml-commons-external-1_2_04/java/external/build/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.2-apis-%{version}
# JAXP 1.3
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.3-apis-%{version}
cp -pr xml-commons-external-1_3_*/java/external/build/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-jaxp-1.3-apis-%{version}

# For Symlinks and alternatives
touch $RPM_BUILD_ROOT%{_javadir}/xml-commons-apis.jar
touch $RPM_BUILD_ROOT%{_javadir}/xml-commons-which.jar
touch $RPM_BUILD_ROOT%{_javadir}/xml-commons-resolver.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaxp.jar
touch $RPM_BUILD_ROOT%{_javadir}/dom3.jar
touch $RPM_BUILD_ROOT%{_javadir}/dom2.jar
touch $RPM_BUILD_ROOT%{_javadir}/dom.jar
touch $RPM_BUILD_ROOT%{_javadir}/sax2.jar
touch $RPM_BUILD_ROOT%{_javadir}/sax.jar
touch $RPM_BUILD_ROOT%{_bindir}/xml-which
touch $RPM_BUILD_ROOT%{_bindir}/xml-resolver
touch $RPM_BUILD_ROOT%{_bindir}/xml-xread
touch $RPM_BUILD_ROOT%{_bindir}/xml-xparse
#ln -s %{_sysconfdir}/alternatives/%{name}-apis-javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}-apis
%{__chmod} 755 $RPM_BUILD_ROOT%{_bindir}*

%{__perl} -pi -e 's/\r$//g' README.html KEYS

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -m 755 %{SOURCE100} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-jaxp-1.3-apis-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/xml-apis.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-resolver11-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/resolver.jar
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{repodirsrc}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-commons-apis_%{name}-jaxp-1.1-apis<<EOF
%{_javadir}/xml-commons-apis.jar	%{_javadir}/jaxp11.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_%{name}-jaxp-1.1-apis<<EOF
%{_javadir}/jaxp.jar	%{_javadir}/jaxp11.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/dom2_%{name}-jaxp-1.1-apis<<EOF
%{_javadir}/dom2.jar	%{_javadir}/jaxp11.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/dom_%{name}-jaxp-1.1-apis<<EOF
%{_javadir}/dom.jar	%{_javadir}/jaxp11.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/sax2_%{name}-jaxp-1.1-apis<<EOF
%{_javadir}/sax2.jar	%{_javadir}/jaxp11.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/sax_%{name}-jaxp-1.1-apis<<EOF
%{_javadir}/sax.jar	%{_javadir}/jaxp11.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xslt_%{name}-jaxp-1.1-apis<<EOF
%{_javadir}/xslt.jar	%{_javadir}/jaxp11.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-commons-apis-javadoc_%{name}-jaxp-1.1-apis-javadoc<<EOF
%{_javadocdir}/xml-commons-apis	%{_javadocdir}/%{name}-jaxp-1.1-apis/	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-which_%{name}-which10<<EOF
%{_bindir}/xml-which	%{_bindir}/xml-which10	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-commons-which_%{name}-which10<<EOF
%{_javadir}/xml-commons-which.jar	%{_javadir}/xml-commons-which10.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-resolver_%{name}-resolver10<<EOF
%{_bindir}/xml-resolver	%{_bindir}/xml-resolver10	10000
%{_javadir}/xml-commons-resolver.jar	%{_javadir}/xml-commons-resolver10.jar	%{_bindir}/xml-resolver10
%{_bindir}/xml-xread	%{_bindir}/xml-xread10	%{_bindir}/xml-resolver10
%{_bindir}/xml-xparse	%{_bindir}/xml-xparse10	%{_bindir}/xml-resolver10
%{_mandir}/man1/xml-resolver.1.bz2	%{_mandir}/man1/xml-resolver10.1.bz2	%{_bindir}/xml-resolver10
%{_mandir}/man1/xml-xread.1.bz2	%{_mandir}/man1/xml-xread10.1.bz2	%{_bindir}/xml-resolver10
%{_mandir}/man1/xml-xparse.1.bz2	%{_mandir}/man1/xml-xparse10.1.bz2	%{_bindir}/xml-resolver10
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-resolver_%{name}-resolver11<<EOF
%{_bindir}/xml-resolver	%{_bindir}/xml-resolver11	10100
%{_javadir}/xml-commons-resolver.jar	%{_javadir}/xml-commons-resolver11.jar	%{_bindir}/xml-resolver11
%{_bindir}/xml-xread	%{_bindir}/xml-xread11	%{_bindir}/xml-resolver11
%{_bindir}/xml-xparse	%{_bindir}/xml-xparse11	%{_bindir}/xml-resolver11
%{_mandir}/man1/xml-resolver.1.bz2	%{_mandir}/man1/xml-resolver11.1.bz2	%{_bindir}/xml-resolver11
%{_mandir}/man1/xml-xread.1.bz2	%{_mandir}/man1/xml-xread11.1.bz2	%{_bindir}/xml-resolver11
%{_mandir}/man1/xml-xparse.1.bz2	%{_mandir}/man1/xml-xparse11.1.bz2	%{_bindir}/xml-resolver11
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-commons-apis_%{name}-jaxp-1.2-apis<<EOF
%{_javadir}/xml-commons-apis.jar	%{_javadir}/jaxp12.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_%{name}-jaxp-1.2-apis<<EOF
%{_javadir}/jaxp.jar	%{_javadir}/jaxp12.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/dom2_%{name}-jaxp-1.2-apis<<EOF
%{_javadir}/dom2.jar	%{_javadir}/jaxp12.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/dom_%{name}-jaxp-1.2-apis<<EOF
%{_javadir}/dom.jar	%{_javadir}/jaxp12.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/sax2_%{name}-jaxp-1.2-apis<<EOF
%{_javadir}/sax2.jar	%{_javadir}/jaxp12.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/sax_%{name}-jaxp-1.2-apis<<EOF
%{_javadir}/sax.jar	%{_javadir}/jaxp12.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xslt_%{name}-jaxp-1.2-apis<<EOF
%{_javadir}/xslt.jar	%{_javadir}/jaxp12.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-commons-apis-javadoc_%{name}-jaxp-1.2-apis-javadoc<<EOF
%{_javadocdir}/xml-commons-apis	%{_javadocdir}/%{name}-jaxp-1.2-apis/	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-commons-apis_%{name}-jaxp-1.3-apis<<EOF
%{_javadir}/xml-commons-apis.jar	%{_javadir}/jaxp13.jar	10300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_%{name}-jaxp-1.3-apis<<EOF
%{_javadir}/jaxp.jar	%{_javadir}/jaxp13.jar	10300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/dom_%{name}-jaxp-1.3-apis<<EOF
%{_javadir}/dom.jar	%{_javadir}/jaxp13.jar	10300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/sax2_%{name}-jaxp-1.3-apis<<EOF
%{_javadir}/sax2.jar	%{_javadir}/jaxp13.jar	10300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/sax_%{name}-jaxp-1.3-apis<<EOF
%{_javadir}/sax.jar	%{_javadir}/jaxp13.jar	10300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xslt_%{name}-jaxp-1.3-apis<<EOF
%{_javadir}/xslt.jar	%{_javadir}/jaxp13.jar	10300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-commons-apis-javadoc_%{name}-jaxp-1.3-apis-javadoc<<EOF
%{_javadocdir}/xml-commons-apis	%{_javadocdir}/%{name}-jaxp-1.3-apis/	10300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-which_%{name}-which11<<EOF
%{_bindir}/xml-which	%{_bindir}/xml-which11	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-commons-which_%{name}-which11<<EOF
%{_javadir}/xml-commons-which.jar	%{_javadir}/xml-commons-which11.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-resolver_%{name}-resolver12<<EOF
%{_bindir}/xml-resolver	%{_bindir}/xml-resolver12	10200
%{_javadir}/xml-commons-resolver.jar	%{_javadir}/xml-commons-resolver12.jar	%{_bindir}/xml-resolver12
%{_bindir}/xml-xread	%{_bindir}/xml-xread12	%{_bindir}/xml-resolver12
%{_bindir}/xml-xparse	%{_bindir}/xml-xparse12	%{_bindir}/xml-resolver12
%{_mandir}/man1/xml-resolver.1.bz2	%{_mandir}/man1/xml-resolver12.1.bz2	%{_bindir}/xml-resolver12
%{_mandir}/man1/xml-xread.1.bz2	%{_mandir}/man1/xml-xread12.1.bz2	%{_bindir}/xml-resolver12
%{_mandir}/man1/xml-xparse.1.bz2	%{_mandir}/man1/xml-xparse12.1.bz2	%{_bindir}/xml-resolver12
EOF

# inject OSGi manifest xml-commons-resolver-1.2.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
zip -u %buildroot/usr/share/java/xml-commons-resolver12.jar META-INF/MANIFEST.MF

# inject OSGi manifest xml-commons-apis-1.4.01.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE46} META-INF/MANIFEST.MF
zip -u %buildroot/usr/share/java/xml-commons-jaxp-1.3-apis.jar META-INF/MANIFEST.MF

# inject OSGi manifest xml-commons-apis-ext-1.4.01.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE47} META-INF/MANIFEST.MF
zip -u %buildroot/usr/share/java/xml-commons-jaxp-1.3-apis-ext.jar META-INF/MANIFEST.MF

chmod 755 %buildroot%{_bindir}/*

# -----------------------------------------------------------------------------

%post jaxp-1.1-apis
##rm -f %{_javadir}/xml-commons-apis.jar
#rm -f %{_javadir}/jaxp11.jar
#ln -s %{name}-jaxp-1.1-apis.jar %{_javadir}/jaxp11.jar
:

%postun jaxp-1.1-apis
if [ "$1" = "0" ]; then
  :
  #rm -f %{_javadir}/jaxp11.jar
fi

%post jaxp-1.1-apis-javadoc
rm -f %{_javadocdir}/%{name}-jaxp-1.1-apis
ln -s %{name}-jaxp-1.1-apis-%{version} %{_javadocdir}/%{name}-jaxp-1.1-apis
:

%postun jaxp-1.1-apis-javadoc
if [ "$1" = "0" ]; then
  :
  rm -f %{_javadocdir}/%{name}-jaxp-1.1-apis
fi

%post which10-javadoc
rm -f %{_javadocdir}/%{name}-which10
ln -s %{name}-which10-%{version} %{_javadocdir}/%{name}-which10

%postun which10-javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}-which10
fi

%post resolver10-javadoc
rm -f %{_javadocdir}/%{name}-resolver10
ln -s %{name}-resolver10-%{version} %{_javadocdir}/%{name}-resolver10

%postun resolver10-javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}-resolver10
fi

%post resolver11-javadoc
rm -f %{_javadocdir}/%{name}-resolver11
ln -s %{name}-resolver11-%{version} %{_javadocdir}/%{name}-resolver11

%postun resolver11-javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}-resolver11
fi

%post jaxp-1.2-apis
#rm -f %{_javadir}/xml-commons-apis.jar
#rm -f %{_javadir}/jaxp12.jar
#ln -s %{name}-jaxp-1.2-apis.jar %{_javadir}/jaxp12.jar
:

%postun jaxp-1.2-apis
if [ "$1" = "0" ]; then
  :
  #rm -f %{_javadir}/jaxp12.jar
fi

%post jaxp-1.2-apis-javadoc
rm -f %{_javadocdir}/%{name}-jaxp-1.2-apis
ln -s %{name}-jaxp-1.2-apis-%{version} %{_javadocdir}/%{name}-jaxp-1.2-apis
:

%postun jaxp-1.2-apis-javadoc
if [ "$1" = "0" ]; then
  :
  rm -f %{_javadocdir}/%{name}-jaxp-1.2-apis
fi

%post jaxp-1.3-apis
#rm -f %{_javadir}/xml-commons-apis.jar
#rm -f %{_javadir}/jaxp13.jar
#ln -s %{name}-jaxp-1.3-apis.jar %{_javadir}/jaxp13.jar
:

%postun jaxp-1.3-apis
if [ "$1" = "0" ]; then
  :
  #rm -f %{_javadir}/jaxp13.jar
fi

%post jaxp-1.3-apis-javadoc
rm -f %{_javadocdir}/%{name}-jaxp-1.3-apis
ln -s %{name}-jaxp-1.3-apis-%{version} %{_javadocdir}/%{name}-jaxp-1.3-apis
:

%postun jaxp-1.3-apis-javadoc
if [ "$1" = "0" ]; then
  :
  rm -f %{_javadocdir}/%{name}-jaxp-1.3-apis
fi

%files 
%doc xml-commons-external-1_3_*/*.txt
%config(noreplace) %{resolverdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%endif
%{_mavendepmapfragdir}/%{name}

%files jaxp-1.1-apis
%_altdir/xslt_%{name}-jaxp-1.1-apis
%_altdir/sax_%{name}-jaxp-1.1-apis
%_altdir/sax2_%{name}-jaxp-1.1-apis
%_altdir/dom_%{name}-jaxp-1.1-apis
%_altdir/dom2_%{name}-jaxp-1.1-apis
%_altdir/jaxp_%{name}-jaxp-1.1-apis
%_altdir/xml-commons-apis_%{name}-jaxp-1.1-apis
# FIXME:
# xml-commons-jaxp-1.1-apis.noarch: W: file-not-utf8 /usr/share/xml-commons-jaxp-1.1-apis-1.3.03/LICENSE.dom-software.txt
# xml-commons-jaxp-1.1-apis.noarch: W: file-not-utf8 /usr/share/xml-commons-jaxp-1.1-apis-1.3.03/LICENSE.dom-documentation.txt
%doc %{_datadir}/%{name}-jaxp-1.1-apis-%{version}
%{_javadir}/%{name}-jaxp-1.1-apis*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-jaxp-1.1-apis*.jar.*
%endif
%exclude %{_javadir}/xml-commons-apis.jar
%{_javadir}/jaxp11.jar
%exclude %{_javadir}/jaxp.jar
%exclude %{_javadir}/dom2.jar
%exclude %{_javadir}/dom.jar
%exclude %{_javadir}/sax2.jar
%exclude %{_javadir}/sax.jar

%files jaxp-1.1-apis-javadoc
%_altdir/xml-commons-apis-javadoc_%{name}-jaxp-1.1-apis-javadoc
%{_javadocdir}/%{name}-jaxp-1.1-apis-%{version}
%{_javadocdir}/%{name}-jaxp-1.1-apis

%files jaxp-1.1-apis-manual
%doc %{_docdir}/%{name}-jaxp-1.1-apis-%{version}

%files which10
%_altdir/xml-commons-which_%{name}-which10
%_altdir/xml-which_%{name}-which10
%{_javadir}/%{name}-which10*.jar
%exclude %{_javadir}/xml-commons-which.jar
%attr(0755,root,root) %{_bindir}/xml-which10

%files which10-javadoc
%{_javadocdir}/%{name}-which10-%{version}
%{_javadocdir}/%{name}-which10

%files resolver10
%_altdir/xml-resolver_%{name}-resolver10
%{_javadir}/%{name}-resolver10*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-resolver10*.jar.*
%endif
%exclude %{_javadir}/xml-commons-resolver.jar
%attr(0755,root,root) %{_bindir}/xml-resolver10
%attr(0755,root,root) %{_bindir}/xml-xread10
%attr(0755,root,root) %{_bindir}/xml-xparse10
%{_mandir}/man1/xml-resolver10.1*
%{_mandir}/man1/xml-xread10.1*
%{_mandir}/man1/xml-xparse10.1*

%files resolver10-javadoc
%{_javadocdir}/%{name}-resolver10-%{version}
%{_javadocdir}/%{name}-resolver10

%files resolver11
%_altdir/xml-resolver_%{name}-resolver11
%{_javadir}/%{name}-resolver11*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-resolver11*.jar.*
%endif
%exclude %{_javadir}/xml-commons-resolver.jar
%attr(0755,root,root) %{_bindir}/xml-resolver11
%attr(0755,root,root) %{_bindir}/xml-xread11
%attr(0755,root,root) %{_bindir}/xml-xparse11
%{_mandir}/man1/xml-resolver11.1*
%{_mandir}/man1/xml-xread11.1*
%{_mandir}/man1/xml-xparse11.1*

%files resolver11-javadoc
%{_javadocdir}/%{name}-resolver11-%{version}
%{_javadocdir}/%{name}-resolver11

%files jaxp-1.2-apis
%_altdir/xslt_%{name}-jaxp-1.2-apis
%_altdir/sax_%{name}-jaxp-1.2-apis
%_altdir/sax2_%{name}-jaxp-1.2-apis
%_altdir/dom_%{name}-jaxp-1.2-apis
%_altdir/dom2_%{name}-jaxp-1.2-apis
%_altdir/jaxp_%{name}-jaxp-1.2-apis
%_altdir/xml-commons-apis_%{name}-jaxp-1.2-apis
%{_javadir}/%{name}-jaxp-1.2-apis*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-jaxp-1.2-apis*.jar.*
%endif
%doc %{_datadir}/%{name}-jaxp-1.2-apis-%{version}
%exclude %{_javadir}/xml-commons-apis.jar
%{_javadir}/jaxp12.jar
%exclude %{_javadir}/jaxp.jar
%exclude %{_javadir}/dom2.jar
%exclude %{_javadir}/dom.jar
%exclude %{_javadir}/sax2.jar
%exclude %{_javadir}/sax.jar

%files jaxp-1.2-apis-javadoc
%_altdir/xml-commons-apis-javadoc_%{name}-jaxp-1.2-apis-javadoc
%{_javadocdir}/%{name}-jaxp-1.2-apis-%{version}
%{_javadocdir}/%{name}-jaxp-1.2-apis

%files jaxp-1.2-apis-manual
%{_docdir}/%{name}-jaxp-1.2-apis-%{version}

%files jaxp-1.3-apis
%_altdir/xslt_%{name}-jaxp-1.3-apis
%_altdir/sax_%{name}-jaxp-1.3-apis
%_altdir/sax2_%{name}-jaxp-1.3-apis
%_altdir/dom_%{name}-jaxp-1.3-apis
%_altdir/jaxp_%{name}-jaxp-1.3-apis
%_altdir/xml-commons-apis_%{name}-jaxp-1.3-apis
%{_javadir}/%{name}-jaxp-1.3-apis-%{version}.jar
%{_javadir}/%{name}-jaxp-1.3-apis.jar
%{_javadir}/%{name}-jaxp-1.3-apis-ext-%{version}.jar
%{_javadir}/%{name}-jaxp-1.3-apis-ext.jar
%{_datadir}/maven2/poms/JPP-%{name}-apis.pom
%{_datadir}/maven2/poms/JPP-%{name}-jaxp-1.3-apis.pom
%{_datadir}/maven2/poms/JPP-%{name}-jaxp-1.3-apis-ext.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-jaxp-1.3-apis*.jar.*
%endif
%doc %{_datadir}/%{name}-jaxp-1.3-apis-%{version}
%exclude %{_javadir}/xml-commons-apis.jar
%{_javadir}/jaxp13.jar
%exclude %{_javadir}/jaxp.jar
%exclude %{_javadir}/dom3.jar
%exclude %{_javadir}/dom.jar
%exclude %{_javadir}/sax2.jar
%exclude %{_javadir}/sax.jar

%files jaxp-1.3-apis-javadoc
%_altdir/xml-commons-apis-javadoc_%{name}-jaxp-1.3-apis-javadoc
%{_javadocdir}/%{name}-jaxp-1.3-apis-%{version}
%{_javadocdir}/%{name}-jaxp-1.3-apis

%files jaxp-1.3-apis-manual
%{_docdir}/%{name}-jaxp-1.3-apis-%{version}

%files which11
%_altdir/xml-commons-which_%{name}-which11
%_altdir/xml-which_%{name}-which11
%{_javadir}/%{name}-which11*.jar
%exclude %{_javadir}/xml-commons-which.jar
%attr(0755,root,root) %{_bindir}/xml-which11

%files which11-javadoc
%{_javadocdir}/%{name}-which11-%{version}
%{_javadocdir}/%{name}-which11

%files resolver12
%_altdir/xml-resolver_%{name}-resolver12
%{_javadir}/%{name}-resolver12*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-resolver12*.jar.*
%endif
%exclude %{_javadir}/xml-commons-resolver.jar
%attr(0755,root,root) %{_bindir}/xml-resolver12
%attr(0755,root,root) %{_bindir}/xml-xread12
%attr(0755,root,root) %{_bindir}/xml-xparse12
%{_mandir}/man1/xml-resolver12.1*
%{_mandir}/man1/xml-xread12.1*
%{_mandir}/man1/xml-xparse12.1*

%files resolver12-javadoc
%{_javadocdir}/%{name}-resolver12-%{version}
%{_javadocdir}/%{name}-resolver12

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.04-alt5_9jpp6
- added  OSGi provides to jaxp-1.3-apis

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.04-alt4_5jpp5
- new jpp release

* Sat Jan 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3.04-alt4_4jpp5
- removed obsolete macroses from scripts

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.04-alt3_4jpp5
- build with target 1.4

* Mon Sep 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.04-alt2_4jpp5
- fixed alternatives

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.04-alt1_4jpp5
- converted from JPackage by jppimport script

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.03-alt3_11jpp1.7
- fixed alternatives

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.03-alt2_11jpp1.7
- updated to new jpackage release

* Mon Oct 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.03-alt2_10jpp1.7
- fixed regression in symlinks

* Thu Sep 27 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.03-alt1_10jpp1.7
- added fix (thanks to at@ for req.symlinks)

* Wed Apr 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.03-alt0.4_8jpp1.7
- converted from JPackage by jppimport script

* Fri Mar 10 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt0.4.b3
- Updated to the latest SVN snapshot
- Suspended xml-commons-apis as it's replaced with xml-commons-external
- Updated Patch0
- Patch1: emit code to run on J2SE 1.3

* Thu Jun 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt0.3.b3
- Packaged a CVS snapshot of Beta 3 which adds JAXP 1.3 APIs
- Updated Patch0

* Sat Jun 18 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt0.2.b2
- Use rpm-build-java macros
- Parameterized path substitutions in the which script
- Adapted to the new java-common location [bug #7017]

* Wed Sep 11 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt0.1.b2
- adaptations for ALT Linux
- ant build is made optional
- non-api javadoc is in fact common for which and resolver, made it
  common package
- more human-friendly descriptions and summaries here and there
- Included licenses for W3C stuff and added License tags accordingly

* Thu Jul 11 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.0-0.b2.1jpp
- 1.0.b2
- get tarball from xml.apache.org
- add macro section

* Fri Jan 18 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-0.b1.1jpp
- first jpp release
