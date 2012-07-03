BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# one of the sources is a zip file
BuildRequires: unzip
# Copyright (c) 2000-2011, JPackage Project
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

#def_with jdk6
%bcond_with jdk6
%bcond_without repolib

%define repoversion %{version}jboss.patch01-brew
%define repodir %{_javadir}/repository.jboss.com/jacorb/%{repoversion}
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define shortname jacorb

%define section devel

Name:           jacorb-jboss
Version:        2.3.1
Release:        alt2_8jpp6
Epoch:          0
Summary:        Free Java implementation of OMG's CORBA standard
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jacorb.org/
Source0:        http://www.jacorb.org/releases/2.3.1/jacorb-2.3.1-src.zip
Source1:        jacorb-jboss-component-info.xml
#Source2:       http://repository.jboss.com/jacorb/2.3.0jboss.patch3/resources/CSI.idl
#Source3:       http://repository.jboss.com/jacorb/2.3.0jboss.patch3/resources/CosTransactions.idl
Source4:        http://repository.jboss.com/jacorb/2.3.0jboss.patch3/resources/jacorb.properties
Source5:        http://repository.jboss.com/jacorb/2.3.0jboss.patch3/resources/orb.idl
Source6:        jacorb-repolib-README
Source7:        jacorb-idl-compiler.pom

Patch0:         jacorb-2.3.1-notification-build_xml.patch
Patch1:         jacorb-2.3.1-version.patch

# This patch resets the port of the primary address to zero when an
# IORInterceptor adds a TAG_CSI_SEC_MECH_LIST component with transport
# protection requirements (SSL), as it should be per the CSI v2 specification.
Patch7:         jacorb-2.3.1-primaddress_port.patch

# JBPAPP-1477 JacORB 2.3.0.jboss5 intermittently hangs during shutdown.
# Thread dump shows it waiting in RequestController.waitForShutdown(), 
# presumably beacause it believes there are outstanding requests still 
# in progress.
Patch9:         jacorb-2.3.0-CORBA_OBJECT_NOT_EXIST.patch

# This patch removes the OTS classes
Patch13:        jacorb-2.3.1-remove_ots_classes.patch

# read_boolean() now only adjusts positions if the chunk_end_pos == pos,
# no longer calling handle_chunking(). The problem with handle_chunking()
# is that it aligns the current position and this can cause CDRInputStream
# to "skip" valid boolean values, as those are not padded.
Patch14:        jacorb-2.3.1-read_boolean.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: antlr >= 0:2.7.2
BuildRequires: excalibur-avalon-logkit >= 0:1.2
BuildRequires: jakarta-commons-collections >= 0:2.0
BuildRequires: jakarta-commons-logging
BuildRequires: java-cup
BuildRequires: tanukiwrapper >= 0:3.1.0
BuildRequires: picocontainer >= 0:1.2
BuildRequires: slf4j >= 0:1.6.1
BuildRequires: xdoclet >= 0:1.2.3
BuildRequires: xjavadoc >= 0:1.1

Requires: antlr
Requires: excalibur-avalon-logkit
Requires: jakarta-commons-collections
Requires: jakarta-commons-logging
#Optional:       tanukiwrapper
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
#Optional:      picocontainer
Requires: slf4j >= 0:1.6.1
BuildArch:      noarch
Source44: import.info

%description
- high-performance, fully multithreaded ORB 
- IDL compiler, supports OMG IDL/Java language mapping 
  rev. 2.3, OBV 
- native IIOP, GIOP 1.2 and Bidirectional GIOP 
- POA (Portable Object Adapter) 
- AMI (Asynchronous Method Invocations) 
- ETF (Extensible Transport Framework) 
- POAMonitor, a GUI tools that lets you inspect your 
  object adapters (screenshot) 
- Dynamic Invocation Interface (DII) and Dynamic Skeleton 
  Interface (DSI) 
- Dynamic Management of Anys (DynAny) 
- Portable Interceptors (standard) 
- OMG Interoperable Naming Service 
- NameManager, a GUI browser for the name service 
  (requires Swing or JDK 1.2) (screenshot) 
- improved IIOP over SSL, includes KeyStoreManager 
- OMG Notification  and Event service 
- Transaction Service, Collection and Concurrency services 
- TradingService (supports trader links), an extension of 
  Mark Spruiell's free JTrader 
- CORBA 2.3 Code set support 
- Appligator, an IIOP proxy 
- Support for HTTP tunneling 
- Domain Manager, an object domain management service, 
  includes a domain browser GUI 
- Interface Repository 
- IRBrowser, a GUI front end for the Interface Repository
- Implementation Repository 
- Implementation Repository Manager, a GUI front end for 
  the Implementation Repository 
- IDL and Java source for all CORBA/COSS interfaces 
- examples and full source code included 
- 100%% pure Java, JDK 1.3 and 1.4 compatible, also cooperates 
  with Sun's JDK 1.2 classes (releases prior to 1.4 are 
  compatible with JDK 1.1) 

Note: To use the CORBA Notification Service add picocontainer.jar
      to the ClassPath (from the 'picocontainer' RPM).

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%package demo
Summary:        Usage examples for %{name}
Group:          Development/Documentation

%description demo
%{summary}.

%prep
%setup -q -n jacorb-%{version}
chmod -R go=u-w *
find . -name "*.jar" | xargs -t rm

%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch7 -p0 -b .sav7
%patch9 -p0 -b .sav9
%patch13 -p0 -b .sav13
%patch14 -p0 -b .sav14

# assume no filename contains spaces
# Uncomment this one for JDK 1.5  (not needed with Java4)
perl -p -i -e 's/edu(.)emory(.)mathcs(.)backport(.)java(.)util/java${1}util/' `grep edu.emory.mathcs.backport.java.util -lr *`

perl -p -i -e 's/maxmemory="256m"/maxmemory="512m"/' build.xml

pushd lib
ln -sf $(build-classpath antlr) .
ln -sf $(build-classpath excalibur/avalon-logkit) .
ln -sf $(build-classpath picocontainer) .
ln -sf $(build-classpath slf4j/slf4j-api) .
ln -sf $(build-classpath slf4j/slf4j-jdk14) .
ln -sf $(build-classpath tanukiwrapper) .
pushd build
ln -sf $(build-classpath commons-collections) .
ln -sf $(build-classpath commons-logging) .
ln -sf $(build-classpath java_cup) .
ln -sf $(build-classpath xdoclet/xdoclet) .
ln -sf $(build-classpath xdoclet/xdoclet-ejb-module) .
ln -sf $(build-classpath xdoclet/xdoclet-jboss-module) .
ln -sf $(build-classpath xdoclet/xdoclet-jmx-module) .
ln -sf $(build-classpath xdoclet/xdoclet-mx4j-module) .
ln -sf $(build-classpath xdoclet/xdoclet-web-module) .
ln -sf $(build-classpath xjavadoc) .
popd
popd
# Tests were not included with the 2.2.4 source zip
#pushd test/regression/lib
#ln -sf $(build-classpath easymock) .
#ln -sf $(build-classpath emma) .
#ln -sf $(build-classpath emma_ant) .
#ln -sf $(build-classpath junit) .
#popd

mkdir temp

%{__perl} -pi -e 's/\r$//g' \
  bin/NotifyService-Wrapper-MX4J.conf.template \
  bin/NamingService-Wrapper.conf \
  bin/NotifyService-Wrapper.conf \
  doc/CONTEXT_IDs \
  doc/jacorb.css \
  doc/Coding.txt \
  doc/REL_NOTES \
  doc/dds/TODOLIST.txt \
  doc/LICENSE \
  doc/dds/style.css

%build
export CLASSPATH=
export OPT_JAR_LIST=:
export ANT_OPTS="-Xms750m -Xmx1750m -Xss2m"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  all doc
for i in lib/*.jar ; do j=`basename $i` ; cp $i temp/${j/\.jar/_g.jar} ; done
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  realclean
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Ddebug=off all doc

%install

# remove DOS files
find . -name "*.exe" -exec rm {} \;
find . -name "*.bat" -exec rm {} \;

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 0644 lib/%{shortname}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{shortname}-%{version}.jar
%add_to_maven_depmap jacorb jacorb %{version} JPP/%{name} jacorb
install -p -m 0644 temp/%{shortname}_g.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{shortname}_g-%{version}.jar
%add_to_maven_depmap jacorb jacorb_g %{version} JPP/%{name} jacorb_g
install -p -m 0644 lib/idl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/idl-%{version}.jar
%add_to_maven_depmap jacorb idl %{version} JPP/%{name} idl
install -p -m 0644 temp/idl_g.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/idl_g-%{version}.jar
%add_to_maven_depmap jacorb idl_g %{version} JPP/%{name} idl_g

# resources
mkdir -p tmp/resources
cd tmp
install -p -m 0644 ../idl/omg/CSI.idl resources/
install -p -m 0644 ../idl/omg/CosTransactions.idl resources/
install -p -m 0644 %{SOURCE4} resources/
install -p -m 0644 %{SOURCE5} resources/
jar -cf %{name}-resources-%{version}.jar resources 
install -p -m 0644 %{name}-resources-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/resources-%{version}.jar
%add_to_maven_depmap jacorb resources %{version} JPP/%{name} resources
cd ..
rm -Rf tmp

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# FIXME: We need a pom for each artifact
# pom
mkdir -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-idl.pom

# bin, etc, idl
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin
cp -pr bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc
cp -pr etc/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/idl
cp -pr idl/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/idl

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/doc
cp -p index.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/doc
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/doc/api
%{__ln_s} %{_javadocdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/doc/api

# demo
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/demo

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}/
install -d -m 755 $RPM_BUILD_ROOT%{repodir}/resources/
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}/
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@VERSION@/%{repoversion}/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}/
install -p -m 0644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}/
install -p -m 0644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}/
install -p -m 0644 %{PATCH7} $RPM_BUILD_ROOT%{repodirsrc}/
install -p -m 0644 %{PATCH9} $RPM_BUILD_ROOT%{repodirsrc}/
install -p -m 0644 %{PATCH13} $RPM_BUILD_ROOT%{repodirsrc}/
install -p -m 0644 %{PATCH14} $RPM_BUILD_ROOT%{repodirsrc}/
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}/
install -p -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{repodirsrc}/README
#install -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/resources/
install -p -m 0644 idl/omg/CSI.idl $RPM_BUILD_ROOT%{repodir}/resources/
#install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{repodir}/resources/
install -p -m 0644 idl/omg/CosTransactions.idl $RPM_BUILD_ROOT%{repodir}/resources/
install -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{repodir}/resources/
install -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{repodir}/resources/
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/idl_g.jar $RPM_BUILD_ROOT%{repodirlib}/
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{shortname}_g.jar $RPM_BUILD_ROOT%{repodirlib}/
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{shortname}.jar $RPM_BUILD_ROOT%{repodirlib}/
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/idl.jar $RPM_BUILD_ROOT%{repodirlib}/
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirlib}/
%endif

# hack (2.3.1-5)
sed -i s,$RPM_BUILD_DIR/jacorb-%{version}/bin,%{_datadir}/%{name}-%{version}/bin,g %buildroot/usr/share/jacorb-jboss-2.3.1/bin/ntfy-wrapper
sed -i s,$RPM_BUILD_DIR/jacorb-%{version}/bin,%{_datadir}/%{name}-%{version}/bin,g %buildroot/usr/share/jacorb-jboss-2.3.1/bin/ns-wrapper

%files
%{_javadir}*/%{name}
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/bin
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/*
%{_datadir}/%{name}-%{version}/etc
%{_datadir}/%{name}-%{version}/idl
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}-%{version}/demo

%if %with repolib
%files repolib
%dir %{_javadir}*/
%exclude %dir %{_javadocdir}/
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt2_8jpp6
- built with java 6

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_8jpp6
- new jpp release

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_5jpp6
- new version

