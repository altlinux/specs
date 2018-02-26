BuildRequires: geronimo-jta-1.0.1B-api
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

#def_with bootstrap
%bcond_with bootstrap
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/quartz/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           quartz
Epoch:          0
Version:        1.5.2
Release:	alt2_6jpp6
Summary:        Quartz Enterprise Job Scheduler
License:        ASL 2.0
URL:            http://www.opensymphony.com/quartz/
Group:          Development/Java
Source0:        %{name}-%{version}.zip
Source1:        quartz-component-info.xml
Patch0:         %{name}-%{version}-build_xml.patch
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: ant >= 0:1.6
BuildRequires: junit
BuildRequires: ejb_2_1_api
BuildRequires: jaf
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-validator
BuildRequires: jakarta-commons-dbcp
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-pool
%if %with bootstrap
BuildRequires: jboss4-server
BuildRequires: jboss4-jmx
BuildRequires: jboss4-common
BuildRequires: jboss4-system
%else
BuildRequires: jbossas
%endif
BuildRequires: javamail
BuildRequires: jta
BuildRequires: log4j
BuildRequires: mx4j
BuildRequires: servletapi5
Requires: jaf
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-digester
Requires: jakarta-commons-logging
Requires: jakarta-commons-pool
#Optional:  javamail
Requires: log4j
Requires: servletapi5

BuildArch:      noarch
Source44: import.info
BuildRequires: dos2unix

%description
Quartz is a job scheduling system that can be integrated with, or used 
along side virtually any J2EE or J2SE application. Quartz can be used 
to create simple or complex schedules for executing tens, hundreds, or 
even tens-of-thousands of jobs; jobs whose tasks are defined as standard 
Java components or EJBs. 

Note: If you want Quartz to be able to send e-mail then add javamail.jar to
your ClassPath.

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package demo
Summary:        Examples for %{name}
Group:          Development/Documentation
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Examples for %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Manual for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
find . -type f -name "*.jar" | xargs rm
perl -pi -e 's/\r$//g' docs/dbTables/*.sql docs/xml/job_scheduling_data_1_5.dtd
perl -pi -e 's/\r/\n/g' docs/dbTables/tables_db2.sql
# 
#sed -e 's+lib\.jboss-common\.jar=.*$+lib\.jboss-common\.jar=/usr/share/java/jboss4/jboss-common\.jar+' \
#        -e 's+lib\.jboss-jmx\.jar=.*$+lib\.jboss-jmx\.jar=/usr/share/java/jboss4/jboss-jmx\.jar+' \
#        -e 's+lib\.jboss-system\.jar=.*$+lib\.jboss-system\.jar=/usr/share/java/jboss4/jboss-system\.jar+' \
#        -e 's+lib\.jboss\.jar=.*$+lib\.jboss\.jar=/usr/share/java/jboss4/jboss\.jar+' \
#        build.properties > build.properties.mod
#cp build.properties.mod build.properties
#rm build.properties.mod
pushd lib
#ln -s $(find-jar oracle-jdbc-thin) classes12.zip
#ln -s $(find-jar servletapi5) servlet.jar
#ln -s $(find-jar commons-dbcp) commons-dbcp-1.1.jar
#ln -s $(find-jar jta) jta.jar 
#ln -s $(find-jar mx4j/mx4j-jmx) jmx.jar 
#ln -s $(find-jar ejb_2_1_api) ejb.jar 
#ln -s $(find-jar commons-beanutils) commons-beanutils.jar
#ln -s $(find-jar commons-digester) commons-digester.jar
#ln -s $(find-jar jdbc-stdext) jdbc2_0-stdext.jar 
#ln -s $(find-jar jaf) activation.jar 
#ln -s $(find-jar javamail) javamail.jar 
#ln -s $(find-jar commons-collections) commons-collections.jar
#ln -s $(find-jar commons-logging) commons-logging.jar 
#ln -s $(find-jar commons-pool) commons-pool-1.1.jar
#ln -s $(find-jar log4j) log4j.jar
#ln -s $(find-jar junit) junit.jar

#commons-beanutils.jar (1.7.0)
#- buildtime, runtime, optional
ln -s $(find-jar commons-beanutils) .
#commons-collections-3.1.jar (3.1)
#- runtime, required 
ln -s $(find-jar commons-collections) .
#commons-dbcp-1.2.1.jar (1.2.1)
#- runtime, optional
ln -s $(find-jar commons-dbcp) .
#commons-digester-1.7.jar (1.7)
#- buildtime, runtime, optional
ln -s $(find-jar commons-digester) .
#commons-logging.jar (1.0.4)
#- runtime, required
ln -s $(find-jar commons-logging) .
#commons-pool-1.2.jar (1.2)
#- runtime, optional
ln -s $(find-jar commons-pool) .
#jdbc2_0-stdext.jar
#- Standard JDBC APIs
#- runtime, required
ln -s $(find-jar jdbc-stdext) .
#ejb.jar (2.0)
#- Enterprise Java Beans API
#- buildtime, runtime, optional
ln -s $(find-jar ejb_2_1_api) .
#jta.jar
#- Standard JTA API
#- runtime, optional
ln -s $(find-jar jta) .
#servlet.jar (2.3)
#- Servlet API (2.3)
#- buildtime, runtime, optional
# XXX: can use 2.4 for build
ln -s $(find-jar servletapi5) .
#junit.jar (3.8.1)
#- JUnit test framework
#- buildtime
ln -s $(find-jar junit) .
#activation.jar (1.1)
#- Javax Activation framework
ln -s $(find-jar jaf) .
#mail.jar (1.3.3)
#- Javax Mail api
ln -s $(find-jar javamail) .
#log4j-1.2.11.jar (1.2.11)
#- Log4j Logging Framework 
#- runtime, optional
ln -s $(find-jar log4j) .
#commons-validator-1.1.4.jar (1.1.4)
#- Commons Validation Framework
#- runtime, optional
ln -s $(find-jar commons-validator) .

%if %with bootstrap
ln -s $(find-jar jboss4/jboss-common) .
ln -s $(find-jar jboss4/jboss-jmx) .
ln -s $(find-jar jboss4/jboss-system) .
ln -s $(find-jar jboss4/jboss) .
%else
ln -s $(build-classpath jbossas/jbossall-client) .
ln -s $(build-classpath jbossas/jboss-jmx) .
ln -s $(build-classpath jbossas/jboss-system) .
ln -s $(build-classpath jbossas/jboss) .
%endif
popd

%patch0 -b .sav
mkdir opensymphony
cp osbuild.xml opensymphony
cp EMPTY.MF opensymphony

%{__perl} -pi -e 's/\r$//g' readme.txt license.txt \
  `find . -name '*.sh' -o -name '*.css' -o -name '*.xml*' -o -name package-list`

find . -name '*.sh' | xargs %{__chmod} 0755

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
cp -p build/%{name}-all-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# FIXME: (dwalluck) This breaks -bi --short-circuit
rm -rf docs/api

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/quartz.jar $RPM_BUILD_ROOT%{repodirlib}/quartz.jar
%if 0
cp -p $RPM_BUILD_ROOT%{_javadir}/quartz-all.jar $RPM_BUILD_ROOT%{repodirlib}/quartz-all.jar
%endif
%endif

find $RPM_BUILD_ROOT -name '*.sh' -print0 | xargs -0 dos2unix
grep -r -m 1 -l -Z '^#!/bin/sh' $RPM_BUILD_ROOT%_bindir | xargs -0 dos2unix
find $RPM_BUILD_ROOT%_datadir/%name-%version/ -name "*.sh" -print0 | xargs -0 chmod 755

%files
%doc readme.txt license.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}-all.jar
%{_javadir}/%{name}-all-%{version}.jar

%files demo
%{_datadir}/%{name}-%{version}
%{_datadir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_6jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_4jpp5
- new jpp release

* Mon Oct 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_3jpp5
- full build

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Oct 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

