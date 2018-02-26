BuildRequires: geronimo-jta-1.0.1B-api
%def_without board
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2012, JPackage Project
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


Name:           openorb
Version:        1.4.0
Release:        alt8_5jpp6
Epoch:          0
Summary:        Java CORBA Object Request Broker
License:        BSD
Group:          Development/Java
Source0:        http://downloads.sourceforge.net/openorb/ConcurrencyControlService-1.4.0-src.tgz
Source1:        http://downloads.sourceforge.net/openorb/EvaluatorUtility-1.4.0-src.tgz
Source2:        http://downloads.sourceforge.net/openorb/EventService-1.4.0-src.tgz
Source3:        http://downloads.sourceforge.net/openorb/InterfaceRepository-1.4.0-src.tgz
Source4:        http://downloads.sourceforge.net/openorb/ManagementBoard-1.4.0-src.tgz
Source5:        http://downloads.sourceforge.net/openorb/NamingService-1.4.0-src.tgz
Source6:        http://downloads.sourceforge.net/openorb/NotificationService-1.4.0-src.tgz
Source7:        http://downloads.sourceforge.net/openorb/OpenORB-1.4.0-src.tgz
Source8:        http://downloads.sourceforge.net/openorb/PersistentStateService-1.4.0-src.tgz
Source9:        http://downloads.sourceforge.net/openorb/PropertyService-1.4.0-src.tgz
Source10:       http://downloads.sourceforge.net/openorb/SSL-1.4.0-src.tgz
Source11:       http://downloads.sourceforge.net/openorb/TimeService-1.4.0-src.tgz
Source12:       http://downloads.sourceforge.net/openorb/Tools-1.4.0-src.tgz
Source13:       http://downloads.sourceforge.net/openorb/TradingService-1.4.0-src.tgz
Source14:       http://downloads.sourceforge.net/openorb/TransactionService-1.4.0-src.tgz
Source15:       openorb-1.4.0-poms.tar.gz

Patch0:         %{name}-OpenORB-build.patch
Patch1:         %{name}-TransactionService-build.patch
Patch2:         %{name}-TransactionService-ConnectionWrapper.patch
Patch3:         %{name}-TransactionService-XAVirtualConnection.patch
Patch4:         %{name}-NamingService-build.patch
Url:            http://openorb.sourceforge.net/
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  junit
BuildRequires:  excalibur-avalon-framework-api
BuildRequires:  excalibur-avalon-framework-impl
BuildRequires:  excalibur-avalon-logkit
BuildRequires:  checkstyle
BuildRequires:  excalibur-configuration
#BuildRequires:  fop
BuildRequires:  hsqldb
BuildRequires:  apache-commons-cli
BuildRequires:  javahelp2
BuildRequires:  jta_1_0_1B_api
#BuildRequires:  xalan-j2
#BuildRequires:  xerces-j2
#BuildRequires:  xml-commons-jaxp-1.3-apis
Requires:  excalibur-avalon-framework-api
Requires:  excalibur-avalon-framework-impl
Requires:  excalibur-avalon-logkit
Requires:  excalibur-configuration
Requires:  apache-commons-cli
Requires:  jta_1_0_1B_api
%if %{gcj_support}
BuildRequires:          java-gcj-compat-devel
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
OpenORB is a CORBA Object Request Broker fully developed in
Java. It fully complies with the CORBA 2.4.2 specification and 
provides a lot of features, services and extensions.


%package ccs
Group:          Development/Java
Summary:        %{name} Concurrency Control Service
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-ots = %{epoch}:%{version}-%{release}

%description ccs
%{summary}.

%package evaluator
Group:          Development/Java
Summary:        %{name} Evaluator Utility
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description evaluator
%{summary}.

%package event
Group:          Development/Java
Summary:        %{name} Event Service
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description event
%{summary}.

%package ir
Group:          Development/Java
Summary:        %{name} Interface Repository
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-ots = %{epoch}:%{version}-%{release}
Requires:       %{name}-pss = %{epoch}:%{version}-%{release}

%description ir
%{summary}.

%if_with board
%package board
Group:          Development/Java
Summary:        %{name} Management Board
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-ins = %{epoch}:%{version}-%{release}
Requires:       %{name}-tns = %{epoch}:%{version}-%{release}
Requires:       %{name}-evaluator = %{epoch}:%{version}-%{release}
Requires:       %{name}-pss = %{epoch}:%{version}-%{release}
Requires:       %{name}-ots = %{epoch}:%{version}-%{release}
Requires:       %{name}-ir = %{epoch}:%{version}-%{release}
Requires:       %{name}-notify = %{epoch}:%{version}-%{release}
Requires:       %{name}-trader = %{epoch}:%{version}-%{release}
Requires:       javahelp2
Requires:       jlfgr
%endif #board

%if_with board
%description board
%{summary}.
%endif #board

%package ins
Group:          Development/Java
Summary:        %{name} Interoperable Naming Service
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-pss = %{epoch}:%{version}-%{release}
Requires:       %{name}-ots = %{epoch}:%{version}-%{release}

%description ins
%{summary}.

%package tns
Group:          Development/Java
Summary:        %{name} Transient Service
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description tns
%{summary}.

%package notify
Group:          Development/Java
Summary:        %{name} Notification Service
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-ots = %{epoch}:%{version}-%{release}
Requires:       %{name}-pss = %{epoch}:%{version}-%{release}

%description notify
%{summary}.

%package pss
Group:          Development/Java
Summary:        %{name} Persistent State Service
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-ots = %{epoch}:%{version}-%{release}

%description pss
%{summary}.

%package property
Group:          Development/Java
Summary:        %{name} Property Service
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description property
%{summary}.

%package ssl
Group:          Development/Java
Summary:        %{name} SSL
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description ssl
%{summary}.

%package time
Group:          Development/Java
Summary:        %{name} Time Service
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-event = %{epoch}:%{version}-%{release}

%description time
%{summary}.

%package trader
Group:          Development/Java
Summary:        %{name} Trading Service
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-pss = %{epoch}:%{version}-%{release}

%description trader
%{summary}.

%package ots
Group:          Development/Java
Summary:        %{name} Transaction Service
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description ots
%{summary}.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -c
gzip -dc %{SOURCE0} | tar xf -
gzip -dc %{SOURCE1} | tar xf -
gzip -dc %{SOURCE2} | tar xf -
gzip -dc %{SOURCE3} | tar xf -
gzip -dc %{SOURCE4} | tar xf -
gzip -dc %{SOURCE5} | tar xf -
gzip -dc %{SOURCE6} | tar xf -
gzip -dc %{SOURCE7} | tar xf -
gzip -dc %{SOURCE8} | tar xf -
gzip -dc %{SOURCE9} | tar xf -
gzip -dc %{SOURCE10} | tar xf -
gzip -dc %{SOURCE11} | tar xf -
gzip -dc %{SOURCE12} | tar xf -
gzip -dc %{SOURCE13} | tar xf -
gzip -dc %{SOURCE14} | tar xf -
# poms
gzip -dc %{SOURCE15} | tar xf -
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
# remove all binary libs
find . -name "*.jar" | xargs rm

%build
export CLASSPATH=
ln -sf $(build-classpath javahelp2) tools/lib/ext
#BUILD/openorb-1.4.0/tools/lib/ext/avalon-framework.jar.no
ln -sf $(build-classpath excalibur/avalon-framework-api) tools/lib/ext
ln -sf $(build-classpath excalibur/avalon-framework-impl) tools/lib/ext
#BUILD/openorb-1.4.0/tools/lib/ext/build/ant.jar.no
ln -sf $(build-classpath ant) tools/lib/ext/build
#BUILD/openorb-1.4.0/tools/lib/ext/build/ant-launcher.jar.no
ln -sf $(build-classpath ant-launcher) tools/lib/ext/build
#BUILD/openorb-1.4.0/tools/lib/ext/build/batik.jar.no
#
#BUILD/openorb-1.4.0/tools/lib/ext/build/checkstyle-all.jar.no
ln -sf $(build-classpath checkstyle) tools/lib/ext/build
#BUILD/openorb-1.4.0/tools/lib/ext/build/fop.jar.no
ln -sf $(build-classpath fop) tools/lib/ext/build
#BUILD/openorb-1.4.0/tools/lib/ext/build/jfor.jar.no
#
#BUILD/openorb-1.4.0/tools/lib/ext/build/jimi.jar.no
#
#BUILD/openorb-1.4.0/tools/lib/ext/build/junit.jar.no
ln -sf $(build-classpath junit) tools/lib/ext/build
#BUILD/openorb-1.4.0/tools/lib/ext/build/xalan.jar.no
ln -sf $(build-classpath xalan-j2) tools/lib/ext/build/xalan.jar
ln -sf $(build-classpath xalan-j2-serializer) tools/lib/ext/build
#BUILD/openorb-1.4.0/tools/lib/ext/commons-cli.jar.no
ln -sf $(build-classpath commons-cli) tools/lib/ext
#BUILD/openorb-1.4.0/tools/lib/ext/excalibur-configuration.jar.no
ln -sf $(build-classpath excalibur/excalibur-configuration) tools/lib/ext
#BUILD/openorb-1.4.0/tools/lib/ext/hsqldb.jar.no
ln -sf $(build-classpath hsqldb) tools/lib/ext
#BUILD/openorb-1.4.0/tools/lib/ext/logkit.jar.no
ln -sf $(build-classpath excalibur/avalon-logkit) tools/lib/ext/logkit.jar
#BUILD/openorb-1.4.0/tools/lib/ext/xercesImpl.jar.no
ln -sf $(build-classpath xerces-j2) tools/lib/ext/xercesImpl.jar
#BUILD/openorb-1.4.0/tools/lib/ext/xml-apis.jar.no
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) tools/lib/ext/xml-apis.jar
#BUILD/openorb-1.4.0/tools/lib/launcher.jar.no
#
#BUILD/openorb-1.4.0/tools/lib/openorb_native.jar.no
#
#BUILD/openorb-1.4.0/tools/lib/tools_test-1.4.0.jar.no
#
#BUILD/openorb-1.4.0/TransactionService/lib/ext/jdbc.jar.no
#
#BUILD/openorb-1.4.0/TransactionService/lib/ext/jta_1.0.1.jar.no
ln -sf $(build-classpath jta_1_0_1B_api) tools/lib/ext/jta_1.0.1.jar
#BUILD/openorb-1.4.0/TransactionService/lib/ext/savepoint.jar.no
#
export CLASSPATH=$(build-classpath xalan-j2)
pushd OpenORB
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd TransactionService
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd PersistentStateService
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd NamingService
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd ConcurrencyControlService
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd EventService
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd NotificationService
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd PropertyService
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd TimeService
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd TradingService
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd EvaluatorUtility
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd InterfaceRepository
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd ManagementBoard
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -buildfile src/build.xml \
    jar doc
popd
pushd SSL
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -DVERSION_MAJOR=1 \
    -DVERSION_MINOR=4 \
    -DVERSION_MINOR_CHANGE=0 \
    -Djhall-jar=$(build-classpath javahelp2) \
    -buildfile src/build.xml \
    jar doc
popd

%install
# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
# with compat symlink
install -m 644 OpenORB/lib/%{name}_orb-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/orb-%{version}.jar
ln -sf %{name}/orb-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap %{name} %{name}-orb %{version} JPP/%{name} orb
install -m 644 OpenORB/lib/%{name}_orb_tools-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/orb-tools-%{version}.jar
ln -sf %{name}/orb-tools-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tools-%{version}.jar
%add_to_maven_depmap %{name} %{name}-orb-tools %{version} JPP/%{name} orb-tools
install -m 644 OpenORB/lib/endorsed/%{name}_orb_omg-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/orb-omg-%{version}.jar
ln -sf %{name}/orb-omg-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-omg-%{version}.jar
%add_to_maven_depmap %{name} %{name}-orb-omg %{version} JPP/%{name} orb-omg
install -m 644 tools/lib/tools-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/tools-%{version}.jar
ln -sf %{name}/tools-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/tools-%{name}-%{version}.jar
%add_to_maven_depmap %{name} %{name}-tools %{version} JPP/%{name} tools

# new, without compat symlink
install -m 644 ConcurrencyControlService/lib/%{name}_ccs-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ccs-%{version}.jar
%add_to_maven_depmap %{name} %{name}-ccs %{version} JPP/%{name} ccs
install -m 644 EvaluatorUtility/lib/%{name}_evaluator-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/evaluator-%{version}.jar
%add_to_maven_depmap %{name} %{name}-evaluator %{version} JPP/%{name} evaluator
install -m 644 EventService/lib/%{name}_event-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/event-%{version}.jar
%add_to_maven_depmap %{name} %{name}-event %{version} JPP/%{name} event
install -m 644 InterfaceRepository/lib/%{name}_ir-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ir-%{version}.jar
%add_to_maven_depmap %{name} %{name}-ir %{version} JPP/%{name} ir
install -m 644 ManagementBoard/lib/%{name}_board-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/board-%{version}.jar
%add_to_maven_depmap %{name} %{name}-board %{version} JPP/%{name} board
install -m 644 NamingService/lib/%{name}_ins-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ins-%{version}.jar
%add_to_maven_depmap %{name} %{name}-ins %{version} JPP/%{name} ins
install -m 644 NamingService/lib/%{name}_tns-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/tns-%{version}.jar
%add_to_maven_depmap %{name} %{name}-tns %{version} JPP/%{name} tns
install -m 644 NotificationService/lib/%{name}_notify-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/notify-%{version}.jar
%add_to_maven_depmap %{name} %{name}-notify %{version} JPP/%{name} notify
install -m 644 PersistentStateService/lib/%{name}_pss-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/pss-%{version}.jar
%add_to_maven_depmap %{name} %{name}-pss %{version} JPP/%{name} pss
install -m 644 PropertyService/lib/%{name}_property-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/property-%{version}.jar
%add_to_maven_depmap %{name} %{name}-property %{version} JPP/%{name} property
install -m 644 SSL/lib/%{name}_ssl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ssl-%{version}.jar
%add_to_maven_depmap %{name} %{name}-ssl %{version} JPP/%{name} ssl
install -m 644 TimeService/lib/%{name}_time-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/time-%{version}.jar
%add_to_maven_depmap %{name} %{name}-time %{version} JPP/%{name} time
install -m 644 TradingService/lib/%{name}_trader-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/trader-%{version}.jar
%add_to_maven_depmap %{name} %{name}-trader %{version} JPP/%{name} trader

# with compat symlink
install -m 644 TransactionService/lib/%{name}_ots-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ots-%{version}.jar
ln -sf %{name}/ots-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-ots-%{version}.jar
%add_to_maven_depmap %{name} %{name}-ots %{version} JPP/%{name} ots

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} ${jar/-%{version}/}; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} ${jar/-%{version}/}; done)

# poms provisional
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{name}-board-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-board.pom
install -m 644 %{name}-ccs-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ccs.pom
install -m 644 %{name}-evaluator-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-evaluator.pom
install -m 644 %{name}-event-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-event.pom
install -m 644 %{name}-ins-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ins.pom
install -m 644 %{name}-ir-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ir.pom
install -m 644 %{name}-notify-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-notify.pom
install -m 644 %{name}-orb-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-orb.pom
install -m 644 %{name}-orb-omg-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-orb-omg.pom
install -m 644 %{name}-orb-tools-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-orb-tools.pom
install -m 644 %{name}-ots-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ots.pom
install -m 644 %{name}-property-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-property.pom
install -m 644 %{name}-pss-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-pss.pom
install -m 644 %{name}-ssl-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ssl.pom
install -m 644 %{name}-time-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-time.pom
install -m 644 %{name}-tns-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tns.pom
install -m 644 %{name}-tools-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tools.pom
install -m 644 %{name}-trader-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-trader.pom


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/OpenORB/omg
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/OpenORB/test
cp -pr OpenORB/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/OpenORB
cp -pr OpenORB/doc/javadoc-omg/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/OpenORB/omg
cp -pr OpenORB/doc/javadoc-test/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/OpenORB/test

for module in ConcurrencyControlService \
              EvaluatorUtility \
              EventService \
              InterfaceRepository \
              ManagementBoard \
              NamingService \
              NotificationService \
              PersistentStateService \
              PropertyService \
              SSL \
              TimeService \
              TradingService \
              TransactionService \
              ; do
    install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/$module
    cp -pr $module/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/$module
done

ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p OpenORB/LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p OpenORB/README $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
for module in OpenORB \
              ConcurrencyControlService \
              EvaluatorUtility \
              EventService \
              InterfaceRepository \
              ManagementBoard \
              NamingService \
              NotificationService \
              PersistentStateService \
              PropertyService \
              SSL \
              TimeService \
              TradingService \
              TransactionService \
              ; do
    install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$module
    [ -f $module/doc/*.html ] && cp -p $module/doc/*.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$module
    [ -d $module/doc/html_img ] && cp -pr $module/doc/html_img $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$module
done

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%doc %{_docdir}/%{name}-%{version}/README
%dir %{_javadir}/%{name}
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}-tools*.jar
%{_javadir}/tools-%{name}*.jar
%{_javadir}/%{name}-omg*.jar
%{_javadir}/%{name}/orb-%{version}.jar
%{_javadir}/%{name}/orb.jar
%{_javadir}/%{name}/orb-tools-%{version}.jar
%{_javadir}/%{name}/orb-tools.jar
%{_javadir}/%{name}/orb-omg-%{version}.jar
%{_javadir}/%{name}/orb-omg.jar
%{_javadir}/%{name}/tools-%{version}.jar
%{_javadir}/%{name}/tools.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{name}-tools-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{name}-omg-%{version}.jar.*
%{_libdir}/gcj/%{name}/tools-%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files ccs
%{_javadir}/%{name}/ccs*.jar

%files evaluator
%{_javadir}/%{name}/evaluator*.jar

%files event
%{_javadir}/%{name}/event*.jar

%files ir
%{_javadir}/%{name}/ir*.jar

%if_with board
%files board
%{_javadir}/%{name}/board*.jar
%endif #board

%files ins
%{_javadir}/%{name}/ins*.jar

%files tns
%{_javadir}/%{name}/tns*.jar

%files notify
%{_javadir}/%{name}/notify*.jar

%files pss
%{_javadir}/%{name}/pss*.jar

%files property
%{_javadir}/%{name}/property*.jar

%files ssl
%{_javadir}/%{name}/ssl*.jar

%files time
%{_javadir}/%{name}/time*.jar

%files trader
%{_javadir}/%{name}/trader*.jar

%files ots
%{_javadir}/%{name}-ots*.jar
%{_javadir}/%{name}/ots*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt8_5jpp6
- built with java 6 due to abstract getParentLogger

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt7_5jpp6
- converted from JPackage by jppimport script

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt7_4jpp5
- fixed build

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt6_4jpp5
- selected java5 compiler explicitly

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt5_4jpp5
- rebuild with xmlgraphics-fop

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt4_4jpp5
- disabled openorb-board

* Sun Oct 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_4jpp5
- jpackage 5.0

* Tue Nov 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_2jpp1.7
- require new commons-cli

* Sun Oct 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

