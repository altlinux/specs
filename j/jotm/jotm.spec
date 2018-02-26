BuildRequires: /proc
BuildRequires: jpackage-compat
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


Name:		jotm
Summary:	JOTM : A Java Open Transaction Manager
Url:		http://jotm.objectweb.org/
Version:	2.0.11
Release:	alt2_3jpp6
Epoch:		0
License:	BSD-style
Group:		Development/Java
BuildArch:	noarch
Source0:	jotm-%{version}-src.tgz
Source1:	jotm-2.0.11.pom
Patch0:		jotm-2.0.11-build_xml.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:	ant >= 0:1.7.1
BuildRequires:	carol >= 0:2.0
BuildRequires:	howl-logger >= 0:0.1.8
BuildRequires:	j2ee_connector_1_5_api
BuildRequires:	apache-commons-cli
BuildRequires:	apache-commons-logging
BuildRequires:	jonathan-core >= 0:4.1
BuildRequires:	jonathan-jeremie >= 0:4.2.1
BuildRequires:	jta_1_0_1B_api
BuildRequires:	openorb-ots
BuildRequires:	log4j
BuildRequires:	kilim1
Requires:	carol >= 2.0
Requires:	howl-logger >= 0:0.1.8
Requires:	j2ee_connector_1_5_api
Requires:	apache-commons-cli
Requires:	apache-commons-logging
Requires:	jonathan-core >= 0:4.1
Requires:	jonathan-jeremie >= 0:4.2.1
Requires:	jta_1_0_1B_api
Requires:	openorb-ots
Requires:	log4j
Requires:	kilim1
Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info


%description
Today the JOTM team delivers to you a Java Open Source 
implementation of the JTA APIs. This implementation is 
fully functional and mature since it has been used for 
several years in the JOnAS application server project.
Tomorrow we aim at delivering adaptable software that 
can be used in a wide range of use cases involving 
transaction management. In particular we are currently 
looking at covering transaction models such as flat, 
CNT, ONT, BTP and transaction standards including JTA, 
JTS, OTS.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:	Examples for %{name}
Group:		Development/Documentation

%description demo
%{summary}.

%package manual
Summary:	Documents for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{name}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done
%patch0 -b .sav

%build
pushd externals
ln -sf $(build-classpath carol/ow_carol) carol.jar
ln -sf $(build-classpath howl-logger) howl.jar
ln -sf $(build-classpath commons-cli) commons-cli.jar
ln -sf $(build-classpath commons-logging) commons-logging.jar
ln -sf $(build-classpath j2ee_connector_1_5_api) connector-1_5.jar
ln -sf $(build-classpath jonathan-core) jonathan.jar
ln -sf $(build-classpath jonathan-jeremie) jeremie.jar
ln -sf $(build-classpath jta_1_0_1B_api) jta-spec1_0_1.jar
ln -sf $(build-classpath openorb-ots) jts1_0.jar
ln -sf $(build-classpath kilim1) kilim.jar
ln -sf $(build-classpath log4j) log4j.jar
popd
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 output/dist/lib/%{name}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar
install -m 644 output/dist/lib/%{name}_iiop_stubs.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/iiop-stubs-%{version}.jar
install -m 644 output/dist/lib/%{name}_jrmp_stubs.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jrmp-stubs-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/jdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# examples and configuration
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/examples
cp -pr output/dist/examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/examples
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf
cp -pr output/dist/conf/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr output/dist/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%doc output/dist/LICENSE.txt
%{_javadir}/%{name}
%{_datadir}/%{name}-%{version}/conf
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}/examples

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.11-alt2_3jpp6
- new jpp relase

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.11-alt2_2jpp5
- fixed build

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.11-alt1_2jpp5
- new jpp release

* Thu Nov 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.11-alt1_1jpp1.7
- converted from JPackage by jppimport script

