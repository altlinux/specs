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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with jdk6
%bcond_with jdk6

%define milestone M3


Name:           axion
Version:        1.0
Release:        alt5_0.M3.6jpp6
Epoch:          0
Summary:        Axion RDBMS 
License:        BSD
Group:          Development/Java
URL:            http://axion.tigris.org/
# cvs -q -d :pserver:guest@cvs.tigris.org:/cvs export -D20080415 -d axion-20080415 axion && tar cjf axion-20080415.tar.bz2 axion-20080415
Source0:        axion-20080415.tar.bz2
Source1:        http://repo1.maven.org/maven2/axion/axion/1.0-M3-dev/axion-1.0-M3-dev.pom

Requires: apache-commons-codec >= 0:1.1
Requires: apache-commons-collections >= 0:2.1
Requires: apache-commons-primitives >= 0:1.0
Requires: apache-commons-logging >= 0:1.0
Requires: javacc
Requires: jpackage-utils
Requires: regexp >= 0:1.2
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-nodeps
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: javacc >= 0:3.1
BuildRequires: apache-commons-codec >= 0:1.1
BuildRequires: apache-commons-collections >= 0:2.1
BuildRequires: apache-commons-primitives >= 0:1.0
BuildRequires: apache-commons-logging >= 0:1.0
BuildRequires: regexp >= 0:1.2
BuildArch:      noarch
Source44: import.info

%description
Axion is a small, fast, open source relational 
database system (RDBMS) supporting SQL and JDBC 
written in and for the Java programming language.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n axion-20080415

%build
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/{nodeps,junit}` javacc"
export CLASSPATH=$(build-classpath \
commons-codec \
commons-collections \
commons-primitives \
commons-logging \
regexp \
)
CLASSPATH=$CLASSPATH:bin/classes:bin/test/classes
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djavacc.home=%{_javadir} -Dbuild.sysclasspath=only jar doc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p bin/axion-%{version}-%{milestone}-dev.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)


# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap axion axion %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr bin/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%{_javadir}/*
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.M3.6jpp6
- built with java 6 due to abstract getParentLogger

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.M3.6jpp6
- fixed pom dep on javacc3

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.M3.5jpp6
- fixed build with commons-primitives

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.M3.4jpp6
- added pom

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.M3.4jpp6
- new jpackage release

* Sun May 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.M3.cvs040914.5jpp5
- explicitly selected java5 as default

* Thu Apr 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.M3.cvs040914.5jpp5
- new jpp release

* Mon Nov 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.M3.2jpp5
- java5 fixes

* Mon Oct 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.M3.2jpp1.7
- converted from JPackage by jppimport script

