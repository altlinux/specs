BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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
%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}} 
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without jdk6
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/jacorb/%{version}jboss.patch6-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define shortname jacorb


Name:           jacorb
Version:        2.3.0
Release:	alt2_20jpp6
Epoch:          0
Summary:        Free Java implementation of OMG's CORBA standard
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jacorb.org/
Source0:        http://www.jacorb.org/releases/2.3.0/JacORB-2.3.0-src.zip
Source1:        jacorb-jboss-component-info.xml
Source4:        http://repository.jboss.com/jacorb/2.3.0jboss.patch3/resources/jacorb.properties
Source5:        http://repository.jboss.com/jacorb/2.3.0jboss.patch3/resources/orb.idl
Source6:        jacorb-repolib-README
Source7:        jacorb-idl-compiler.pom
Patch0:         jacorb-2.3.0-notification-build_xml.patch
Patch1:         jacorb-2.3.0-version.patch
# The size of a chunk should not include any bytes of padding that might have
# been added after the chunk for alignment purposes. This patch allows JacORB 
# to interoperate with the ORB in Sun's JDK 1.5 with chunking of custom RMI
# valuetypes enabled (jacorb.interop.chunk_custom_rmi_valuetypes=on), as it 
# should be per the CORBA spec. 
Patch2:         jacorb-2.3.0-chunk_size.patch
# In handle_chunking: change to distinguish a null value tag from
# a chunk size tag (the latter must be positive).
# In read_untyped_value and readChunkSizeTag: changes for correctness (to 
# ensure that chunk_end_pos is set to -1 if we are not within a chunk) and 
# for clarity.
Patch3:         jacorb-2.3.0-null_value_tag.patch
# Fix for bug #782 in JacORB's bugzilla system:
# The creation of an SSLServerSocket fails when JacORB 2.3.0 uses the JSSE
# included in Sun's JDK 1.4 and later releases. The problem is in the wrapper
# class JSSEUtil, which causes an IllegalAccessException to be thrown.
Patch4:         jacorb-2.3.0-JSSE.patch
# Fix for bug #783 in JacORB's bugzilla system:
# Server throws CORBA.INTERNAL (ArrayIndexOutOfBoundsException) when a client
# uses an IOR with a component tagged with TAG_CSI_SEC_MECH_LIST. When the 
# current implementation of the method 
# org.jacorb.orb.iiop.IIOPProfile.getTLSPortFromCSIComponent finds an IOR
# component that is tagged with TAG_CSI_SEC_MECH_LIST and has a non-empty list
# of security mechanisms, it assumes that the first mechanism listed has a 
# transport component tagged with TAG_TLS_SEC_TRANS. It tries to access the 
# data of the presumed TLS_SEC_TRANS component, without first checking the 
# component's tag. If this tag is TAG_NULL_TAG rather than TAG_TLS_SEC_TRANS, 
# then an ArrayIndexOutOfBoundsException occurs.
Patch5:         jacorb-2.3.0-IIOP.patch
# Fix for NPE on shutdown
Patch6:         jacorb-2.3.0-IIOP_Shutdown.patch
# This patch resets the port of the primary address to zero when an
# IORInterceptor adds a TAG_CSI_SEC_MECH_LIST component with transport
# protection requirements (SSL), as it should be per the CSI v2 specification.
Patch7:         jacorb-2.3.0-primaddress_port.patch
# The SSL profile check is unnecessary and incorrect, as it should also check
# for the presence of the TAG_TLS_SEC_TRANS tag in the IIOPProfile.
# By not doing so, it causes JacORB not to open SSL connections when the
# server-side IORs contain only the TAG_TLS_SEC_TRANS tag. We can just
# eliminate this verification since the remaining method body already performs
# the necessary checks correctly.
Patch8:         jacorb-2.3.0-ssl_verification.patch
Patch9:         jacorb-2.3.0-manifest-classpath.patch
Patch10:        jacorb-jdk6.patch
Patch11:        jacorb-2.3.0-javadoc-maxmemory.patch
# JBPAPP-1477 JacORB 2.3.0.jboss5 intermittently hangs during shutdown.
# Thread dump shows it waiting in RequestController.waitForShutdown(),
# presumably beacause it believes there are outstanding requests still
# in progress.
Patch12:         jacorb-2.3.0-CORBA_OBJECT_NOT_EXIST.patch
# This patch removes the OTS classes
Patch13:        jacorb-2.3.0-remove_ots_classes.patch
# read_boolean() now only adjusts positions if the chunk_end_pos == pos,
# no longer calling handle_chunking(). The problem with handle_chunking()
# is that it aligns the current position and this can cause CDRInputStream
# to "skip" valid boolean values, as those are not padded.
Patch14:        jacorb-2.3.0-read_boolean.patch

Requires: antlr
Requires: concurrent
Requires: excalibur-avalon-framework-api
Requires: excalibur-avalon-framework-impl
Requires: excalibur-avalon-logkit
Requires: jakarta-commons-collections
Requires: jakarta-commons-logging
#Optional:      tanukiwrapper
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
#Optional:      picocontainer
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: antlr
BuildRequires: concurrent
BuildRequires: excalibur-avalon-framework-api
BuildRequires: excalibur-avalon-framework-impl
BuildRequires: excalibur-avalon-logkit
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-logging
BuildRequires: tanukiwrapper
BuildRequires: picocontainer
BuildRequires: xdoclet
BuildRequires: xjavadoc
BuildArch:      noarch
Source44: import.info
%add_findreq_skiplist /usr/share/%{name}-*

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
%setup -q -n JacORB
%{__chmod} -R go=u-w *
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -p1 -b .sav9
%if %with jdk6
%patch10 -p1 -b .sav10
%endif
%patch11 -p1 -b .sav11
%patch12 -b .sav12
%if 0
%patch13 -b .sav13
%endif
%patch14 -b .sav14

# assume no filename contains spaces
# Uncomment this one for JDK 1.5  (not needed with Java4)
perl -p -i -e 's/edu(.)emory(.)mathcs(.)backport(.)java(.)util/java${1}util/' `grep edu.emory.mathcs.backport.java.util -lr *`

pushd lib
%{__ln_s} $(build-classpath antlr) .
%{__ln_s} $(build-classpath excalibur/avalon-framework-api) .
%{__ln_s} $(build-classpath excalibur/avalon-framework-impl) .
%{__ln_s} $(build-classpath excalibur/avalon-logkit) .
%{__ln_s} $(build-classpath picocontainer) .
%{__ln_s} $(build-classpath tanukiwrapper) .
pushd build
%{__ln_s} $(build-classpath commons-collections) .
%{__ln_s} $(build-classpath commons-logging) .
%{__ln_s} $(build-classpath xdoclet/xdoclet) .
%{__ln_s} $(build-classpath xdoclet/xdoclet-ejb-module) .
%{__ln_s} $(build-classpath xdoclet/xdoclet-jboss-module) .
%{__ln_s} $(build-classpath xdoclet/xdoclet-jmx-module) .
%{__ln_s} $(build-classpath xdoclet/xdoclet-mx4j-module) .
%{__ln_s} $(build-classpath xdoclet/xdoclet-web-module) .
%{__ln_s} $(build-classpath xjavadoc) .
popd
popd
# Tests were not included with the 2.2.4 source zip
#pushd test/regression/lib
#%{__ln_s} $(build-classpath easymock) .
#%{__ln_s} $(build-classpath emma) .
#%{__ln_s} $(build-classpath emma_ant) .
#%{__ln_s} $(build-classpath junit) .
#popd

%{__mkdir_p} temp

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

# remove DOS files
%{_bindir}/find -name "*.bat" | %{_bindir}/xargs -t %{__rm}
%{_bindir}/find -name "*.exe" | %{_bindir}/xargs -t %{__rm}
%__subst 's,avalon-framework-[0-9\.]\+,avalon-framework-*,' etc/common-xdoclet.xml

%build
export ANT_OPTS=" -Xmx256m "
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all doc
for i in lib/*.jar ; do j=`basename $i`; %{__cp} -p ${i} temp/${j/\.jar/_g.jar} ; done
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 realclean
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Ddebug=off all doc

%install

# jar
%{__mkdir_p} %{buildroot}%{_javadir}/%{name}
%{__cp} -p lib/jacorb.jar %{buildroot}%{_javadir}/%{name}/%{shortname}-%{version}.jar
%{__cp} -p temp/jacorb_g.jar %{buildroot}%{_javadir}/%{name}/%{shortname}_g-%{version}.jar
%{__cp} -p lib/idl.jar %{buildroot}%{_javadir}/%{name}/idl-%{version}.jar
%{__cp} -p temp/idl_g.jar %{buildroot}%{_javadir}/%{name}/idl_g-%{version}.jar

# resources
%{__mkdir_p} tmp/resources
pushd tmp
%{__cp} -p ../idl/omg/CSI.idl resources/
%{__cp} -p ../idl/omg/CosTransactions.idl resources/
%{__cp} -p %{SOURCE4} resources/
%{__cp} -p %{SOURCE5} resources/
%{jar} -cf %{name}-resources-%{version}.jar resources
%{__cp} -p %{name}-resources-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/resources-%{version}.jar
%add_to_maven_depmap jacorb resources %{version} JPP/%{name} resources
popd
%{__rm} -r tmp

(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE7} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-idl.pom
%add_to_maven_depmap org.jacorb jacorb-idl-compiler %{version} JPP/%{name} idl

# bin, etc, idl
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}-%{version}/bin
%{__cp} -pr bin/* %{buildroot}%{_datadir}/%{name}-%{version}/bin
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}-%{version}/etc
%{__cp} -pr etc/* %{buildroot}%{_datadir}/%{name}-%{version}/etc
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}-%{version}/idl
%{__cp} -pr idl/* %{buildroot}%{_datadir}/%{name}-%{version}/idl

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr doc/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}/doc
%{__cp} -p index.html %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -pr doc/* %{buildroot}%{_docdir}/%{name}-%{version}/doc
%{__rm} -r %{buildroot}%{_docdir}/%{name}-%{version}/doc/api
%{__ln_s} %{_javadocdir}/%{name}-%{version} %{buildroot}%{_docdir}/%{name}-%{version}/doc/api

# demo
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}-%{version}/demo

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}/
%{__mkdir_p} %{buildroot}%{repodir}/resources/
%{__mkdir_p} %{buildroot}%{repodirlib}/
%{__cp} -p %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@VERSION@/%{version}jboss.patch6-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH1} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH2} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH3} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH4} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH5} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH6} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH7} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH8} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH10} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH11} %{buildroot}%{repodirsrc}/
%{__cp} -p %{PATCH12} %{buildroot}%{repodirsrc}/
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}/
%{__cp} -p %{SOURCE6} %{buildroot}%{repodirsrc}/README
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirlib}/
%{__cp} -p idl/omg/CSI.idl %{buildroot}%{repodir}/resources/CSI.idl
%{__cp} -p idl/omg/CosTransactions.idl %{buildroot}%{repodir}/resources/CosTransactions.idl
%{__cp} -p %{SOURCE4} %{buildroot}%{repodir}/resources/jacorb.properties
%{__cp} -p %{SOURCE5} %{buildroot}%{repodir}/resources/orb.idl
%{__cp} -p %{buildroot}%{_javadir}/%{name}/idl_g.jar %{buildroot}%{repodirlib}/idl_g.jar
%{__cp} -p %{buildroot}%{_javadir}/%{name}/%{shortname}_g.jar %{buildroot}%{repodirlib}/jacorb_g.jar
%{__cp} -p %{buildroot}%{_javadir}/%{name}/%{shortname}.jar %{buildroot}%{repodirlib}/jacorb.jar
%{__cp} -p %{buildroot}%{_javadir}/%{name}/idl.jar %{buildroot}%{repodirlib}/idl.jar
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-idl.pom %{buildroot}%{repodirlib}/idl.pom
%endif

pushd $RPM_BUILD_ROOT/usr/share/%name-%version/bin
chmod 644 *.conf
for i in *.template; do
    cat $i | sed -e 's,@@@JACORB_HOME@@@,/usr/share/%name-%version/bin,' > `echo $i | sed -e 's,.template$,,'`
done
popd

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/idl-%{version}.jar
%{_javadir}/%{name}/idl.jar
%{_javadir}/%{name}/idl_g-%{version}.jar
%{_javadir}/%{name}/idl_g.jar
%{_javadir}/%{name}/jacorb-%{version}.jar
%{_javadir}/%{name}/jacorb.jar
%{_javadir}/%{name}/jacorb_g-%{version}.jar
%{_javadir}/%{name}/jacorb_g.jar
%{_javadir}/%{name}/resources-%{version}.jar
%{_javadir}/%{name}/resources.jar
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/bin
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/*
%{_datadir}/%{name}-%{version}/etc
%{_datadir}/%{name}-%{version}/idl
%{_datadir}/maven2/poms/JPP.%{name}-idl.pom
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
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt2_20jpp6
- built with java 6

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_20jpp6
- new jpp release

* Thu May 13 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_19jpp5
- jpp6 import

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_17jpp5
- new jpp release

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_11jpp5
- new version

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2.4-alt3_3jpp1.7
- rebuild with backport-util-concurrent 3

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.4-alt2_3jpp1.7
branch 4.0 compatible build

* Mon Oct 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.4-alt1_3jpp1.7
- converted from JPackage by jppimport script

