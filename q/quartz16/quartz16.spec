# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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

%define oname quartz

Summary:        Quartz Enterprise Job Scheduler
Name:           quartz16
Version:        1.6.5
Release:        alt1_2jpp6
Epoch:          0
License:        Apache Software License 2.0
URL:            http://www.opensymphony.com/quartz/
Group:          Development/Java
Source0:        https://quartz.dev.java.net/files/documents/1267/128858/quartz-1.6.5.zip
Source1:        %{oname}-%{version}-suppressions.xml
Source2:        %{oname}-%{version}.pom
Patch0:         %{oname}-%{version}-checkstyle-ant.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  junit
BuildRequires:  ejb_2_1_api
BuildRequires:  jaf_1_0_2_api
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-dbcp
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-modeler
BuildRequires:  apache-commons-pool
BuildRequires:  apache-commons-validator
BuildRequires:  jboss4-server
BuildRequires:  jboss4-jmx
BuildRequires:  jboss4-common
BuildRequires:  jboss4-system
BuildRequires:  javamail_1_3_1_api
BuildRequires:  jms_1_1_api
BuildRequires:  jta_1_0_1B_api
BuildRequires:  log4j
BuildRequires:  servlet_2_4_api
Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

Requires:  jaf_1_0_2_api
Requires:  apache-commons-beanutils
Requires:  apache-commons-collections
Requires:  apache-commons-dbcp
Requires:  apache-commons-digester
Requires:  apache-commons-logging
Requires:  apache-commons-modeler
Requires:  apache-commons-pool
Requires:  apache-commons-validator
Requires:  javamail_1_3_1_api
Requires:  jms_1_1_api
Requires:  jta_1_0_1B_api
Requires:  log4j
Requires:  servlet_2_4_api

BuildArch:      noarch
Source44: import.info

# nothing but examples
%add_findreq_skiplist %_datadir/%name-%version/bin/*
%add_findprov_skiplist %_datadir/%name-%version/bin/*

%description
Quartz is a job scheduling system that can be integrated with, or used 
along side virtually any J2EE or J2SE application. Quartz can be used 
to create simple or complex schedules for executing tens, hundreds, or 
even tens-of-thousands of jobs; jobs whose tasks are defined as standard 
Java components or EJBs. 

%package demo
Summary:        Examples for %{name}
Group:          Development/Documentation
Requires:       quartz16 = 0:%{version}

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
%setup -q -c -n %{name}-%{version}
cp %{SOURCE1} suppressions.xml
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
pushd lib
ln -sf $(build-classpath commons-beanutils) .
ln -sf $(build-classpath commons-collections) .
ln -sf $(build-classpath commons-dbcp) .
ln -sf $(build-classpath commons-digester) .
ln -sf $(build-classpath commons-logging) .
ln -sf $(build-classpath commons-modeler) .
ln -sf $(build-classpath commons-pool) .
ln -sf $(build-classpath ejb_2_1_api) .
ln -sf $(build-classpath jta_1_0_1B_api) .
ln -sf $(build-classpath servlet_2_4_api) .
ln -sf $(build-classpath junit) .
ln -sf $(build-classpath jaf_1_0_2_api) .
ln -sf $(build-classpath javamail_1_3_1_api) .
ln -sf $(build-classpath jms_1_1_api) .
ln -sf $(build-classpath log4j) .
ln -sf $(build-classpath commons-validator) .
ln -sf $(build-classpath jboss4/jboss-common) .
ln -sf $(build-classpath jboss4/jboss-jmx) .
ln -sf $(build-classpath jboss4/jboss-system) .
ln -sf $(build-classpath jboss4/jboss) .
popd

%patch0 -b .sav0

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/%{oname}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
cp -p build/%{oname}-all-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar
cp -p build/%{oname}-jboss-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-jboss-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf docs/api

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp readme.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp license.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name} # ghost symlink

%files
%{_docdir}/%{name}-%{version}/readme.txt
%{_docdir}/%{name}-%{version}/license.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}-%{version}
%{_datadir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.5-alt1_2jpp6
- new jpp relase

* Fri Jun 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.5-alt1_1jpp5
- new jpp release

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt4_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt3_1jpp5
- fixed repocop warnings

* Fri Oct 03 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt2_1jpp5
- converted from JPackage by jppimport script

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt1_1jpp5
- converted from JPackage by jppimport script

