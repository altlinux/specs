BuildRequires: geronimo-corba-1.0-apis geronimo-j2ee-connector-1.5-api
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define javadir         %{_datadir}/java
%define javadocdir      %{_datadir}/javadoc

Summary:                An Open Source implementation of the Java Transaction Service
Name:                   tyrex
Version:                1.0.3
Release:                alt6_2jpp6
Epoch:                  0
Group:                  Development/Java
License:                BSD-like
Url:                    http://tyrex.sourceforge.net
BuildArch:              noarch
BuildRequires:          jpackage-utils >= 0:1.7.5
BuildRequires:          ant >= 0:1.7.1
BuildRequires:          ant-trax
BuildRequires:          avalon-framework
BuildRequires:          avalon-logkit
BuildRequires:          castor0
BuildRequires:          j2ee-connector
BuildRequires:          javamail
BuildRequires:          jta_1_0_1B_api
BuildRequires:          gfv2corba
BuildRequires:          junit
BuildRequires:          ldapsdk
BuildRequires:          log4j
BuildRequires:          openorb >= 0:1.4.0-3jpp
BuildRequires:          openorb-tns
BuildRequires:          xalan-j2
BuildRequires:          xalan-j2-xsltc
BuildRequires:          xerces-j2
BuildRequires:          xml-commons-apis
Source0:                http://prdownloads.sourceforge.net/tyrex/%{name}-%{version}-src.tgz
Source1:                tyrex-1.0.3.pom
Patch0:                 tyrex-1.0.3-build.patch
Patch1:                 tyrex-1.0.3-Current.patch
Patch2:                 tyrex-1.0.3-OTSTest.patch
Patch3:                 tyrex-1.0.3-ConnectionPool.patch
Patch4:                 tyrex-1.0.3-ClientConnection.patch
Patch5:                 tyrex-1.0.3-XAConnectionImpl.patch
Patch6:                 tyrex-1.0.3-EnabledDataSource.patch
Patch7:                 tyrex-1.0.3-TyrexStatementImpl.patch
Patch8:                 tyrex-1.0.3-TyrexPreparedStatementImpl.patch
Patch9:                 tyrex-1.0.3-TyrexCallableStatementImpl.patch
Patch10:                tyrex-1.0.3-TyrexResultSetImpl.patch
Patch11:                tyrex-1.0.3-TyrexDatabaseMetaDataImpl.patch
Patch12:                tyrex-1.0.3-TestConnectionImpl.patch
Patch13:                tyrex-1.0.3-TestResultSetImpl.patch
Patch14:                tyrex-1.0.3-TestStatementImpl.patch
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
Tyrex is a J2EE service provider for both Servlet
and EJB container, JMS providers and generic connectors. 
It provides services for security and authentication,
local and distributed transactions, resource configuration
and pooling, and TP monitoring. 
- Full support for JTA and OTS transactions APIs 
- Support for local and distributed transactions 
- JAAS-based authentication, LDAP login module 
- Configurable transaction processing monitor 
- JDBC pooling and automatic JDBC resource enlistment 
- JCA connection manager 
- XML based configuration 
- JNDI environment naming context 
- Transaction context propagation over IIOP 
- Can be used as a stand alone OTS server 

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
%setup -q
# remove external jars
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
for j in $(find src -name "*.java" -exec grep -l 'assert *(' {} \;); do
    sed -i -e 's:assert *(:assertTrue(:' $j
done
for j in $(find src -name "*.java" -exec grep -l '\.PI\.' {} \;); do
    sed -i -e 's:\.PI\.:\.orb\.pi\.:g' $j
done
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -b .sav9
%patch10 -b .sav10
%patch11 -b .sav11
%patch12 -b .sav12
%patch13 -b .sav13
%patch14 -b .sav14

%build
export OPT_JAR_LIST="ant/ant-trax"
export CLASSPATH=$(build-classpath \
castor0 \
commons-logging \
avalon-framework \
avalon-logkit \
geronimo-corba-1.0-apis \
geronimo-javamail-1.3.1-api \
geronimo-j2ee-connector-1.5-api \
gfv2corba/omgapi \
jta_1_0_1B_api \
junit \
log4j \
openorb/orb \
openorb/orb-omg \
openorb/orb-tools \
openorb/tns \
openorb/tools \
)
CLASSPATH=$CLASSPATH:build/classes:build/tests

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=only -f src/build.xml all-iiop doc javadoc

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
install -m 644 dist/%{name}-%{version}-iiop.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-iiop-%{version}.jar
install -m 644 dist/%{name}-%{version}-iiop-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-iiop-tests-%{version}.jar
install -m 644 dist/%{name}-%{version}-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tests-%{version}.jar
install -m 644 dist/%{name}-%{version}-tests-unit.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tests-unit-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/schema
install -m 644 build/schema/* \
        $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/schema

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -prf build/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf build/doc/javadoc

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -prf build/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%doc %{_docdir}/%{name}-%{version}/license.txt
%{_javadir}/*.jar
%{_datadir}/%{name}-%{version}
%{_datadir}/maven2
%{_mavendepmapfragdir}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt6_2jpp6
- fixed build

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt5_2jpp6
- converted from JPackage by jppimport script

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt5_1jpp5
- fixed build

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt4_1jpp5
- fixed build

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt3_1jpp5
- selected java5 compiler explicitly

* Sun Aug 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt2_1jpp5
- fixed build

* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt1_1jpp5
- full build

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt0.1jpp
maven 2.0.7 bootstrap

