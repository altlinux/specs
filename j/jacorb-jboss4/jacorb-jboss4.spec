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


Summary:	Free Java implementation of OMG's CORBA standard
URL:		http://www.jacorb.org/
Source0:	http://www.jacorb.org/releases/2.2/JacORB_2_2-full.tar.gz
Source1:	jacorb-2.2-jboss-4.0.1-SSLPolicy.idl
Source2:	jacorb-2.2-jboss-4.0.1-SSLPolicyFactory.java
Source3:	jacorb-2.2-jboss-4.0.1-SSLPolicyImpl.java
Patch0:         jacorb-2.2-jboss-4.0.1.patch
Patch1:         jacorb-2.2-java5-common.patch
Patch2:         jacorb-2.2-java5-RequestController.patch
Patch3:         jacorb-2.2-java5-build.patch

Name:		jacorb-jboss4
Version:	2.2
Release:	alt1_6jpp5
Epoch:		0
License:	LGPL
Group:		Development/Java
BuildArch:	noarch
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: antlr
BuildRequires: concurrent
BuildRequires: tanukiwrapper
BuildRequires: excalibur-avalon-framework-api
BuildRequires: excalibur-avalon-framework-impl
BuildRequires: excalibur-avalon-logkit
Requires: jpackage-utils >= 0:1.7.3
Requires: concurrent
Requires: tanukiwrapper
Requires: excalibur-avalon-framework-api
Requires: excalibur-avalon-framework-impl
Requires: excalibur-avalon-logkit
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

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description manual
%{summary}

%package demo
Summary:        Usage examples for %{name}
Group:          Development/Documentation

%description demo
%{summary}

%prep
%setup -q -n JacORB_2_2
chmod -R go=u-w *
find . -name "*.jar" -exec rm -f {} \;
cp %{SOURCE1} idl/jacorb/SSLPolicy.idl
cp %{SOURCE2} src/org/jacorb/security/ssl/SSLPolicyFactory.java
cp %{SOURCE3} src/org/jacorb/security/ssl/SSLPolicyImpl.java

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3

%build
export ANT_OPTS=" -Xmx256m "
export CLASSPATH=$(build-classpath \
antlr \
concurrent \
tanukiwrapper \
excalibur/avalon-framework-api \
excalibur/avalon-framework-impl \
excalibur/avalon-logkit
)
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=first all doc

%install

# remove DOS files
find . -name "*.exe" -exec rm {} \;
find . -name "*.bat" -exec rm {} \;

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 0644 lib/jacorb.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar
install -p -m 0644 lib/idl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/idl-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# bin, etc, idl
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin
cp -pr bin/*   $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc
cp -pr etc/*   $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/idl
cp -pr idl/*   $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/idl

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf doc/api

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/doc
cp index.html   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/*   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/doc

# demo
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/demo

pushd $RPM_BUILD_ROOT/usr/share/%name-%version/bin
chmod 644 *.conf
for i in *.template; do
    cat $i | sed -e 's,@@@JACORB_HOME@@@,/usr/share/%name-%version/bin,' > `echo $i | sed -e 's,.template$,,'`
done
popd

%files
%{_javadir}/*
%{_docdir}/%{name}-%{version}/doc/LICENSE
%dir %{_datadir}/%{name}-%{version}/bin
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/*
%{_datadir}/%{name}-%{version}/etc
%{_datadir}/%{name}-%{version}/idl
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}/doc
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}-%{version}/demo

%changelog
* Wed May 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_6jpp5
- repocop fixes

* Mon Nov 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_5jpp5
- java 5 fixes

* Mon Oct 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_5jpp1.7
- converted from JPackage by jppimport script

