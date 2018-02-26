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

#def_with bootstrap
%bcond_with bootstrap
%bcond_without repolib
#def_with tests
%bcond_with tests

# If you don't want to run the unit tests
# give rpmbuild option '--without tests'
# (dwalluck) This option is required for bootstrapping
%if %with bootstrap
#def_with tests
%bcond_with tests
%endif

%define reltag GA
%define repodir %{_javadir}/repository.jboss.com/jboss/serialization/%{namedversion}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define namedversion %{version}.%{reltag}

Name:           jboss-serialization
Version:        1.0.3
Release:        alt1_8jpp6
Epoch:          0
Summary:        JBoss Serialization
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com/portal/index.html?ctrl:id=page.default.info&project=serialization
# cvs -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r JBSER_1_0_3_GA jboss-serialization
# mv jboss-serialization jboss-serialization-1.0.3.GA-src
# tar czf jboss-serialization-1.0.3.GA-src.tar.gz jboss-serialization-1.0.3.GA-src
Source0:        jboss-serialization-1.0.3.GA-src.tar.gz
Source1:        jboss-serialization-component-info.xml
Source2:        http://repository.jboss.org/nexus/content/groups/public-jboss/jboss/jboss-serialization/1.0.3.GA/jboss-serialization-1.0.3.GA.pom
Patch0:         jboss-serialization-build_xml.patch
Patch1:         jboss-serialization-ProxySerializationTestCase.patch
Patch2:         jboss-serialization-MockHibernateSession.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
Requires: log4j
Requires: gnu-trove
BuildRequires: ant >= 0:1.6
BuildRequires: asm
BuildRequires: cglib
BuildRequires: concurrent
BuildRequires: gnu-trove
BuildRequires: hibernate3
BuildRequires: jakarta-commons-logging
BuildRequires: javassist
BuildRequires: jpackage-utils
BuildRequires: jboss-common-core
BuildRequires: jboss-aop2
BuildRequires: jboss-jrunit
BuildRequires: jboss-profiler
%if %with tests
BuildRequires: ant-junit
BuildRequires: jboss5-libs
BuildRequires: jboss-common-logging-log4j
BuildRequires: jboss-remoting
%endif
BuildRequires: jcommon
BuildRequires: jfreechart
BuildRequires: jgroups >= 0:2.2.9.2
BuildRequires: joda-time
BuildArch:      noarch
Source44: import.info

%description
We (java developers) have accepted over the years 
java.io.ObjectInputStream and java.io.ObjectOutputStream 
being slow when dealing with writeObject operations.
We then started using Externalizable objects as a faster 
approach for serialization, but even that way was slow when 
using writeObject operations inside externalizable classes.
Recently we discovered that most of the problems in 
JavaSerialization are related to static synchronized caching, 
what causes CPU spikes and also diminishes scaling capabilities.
With JBossSerialization we have done internal benchmarks and we 
have realized at least 2 times faster serialization with this 
library. These benchmarks are commited into our CVS repository 
(as testcases) and they are publicly available.
The main feature in JBossSerialization besides performance, is 
Smart Cloning. Smart cloning is the capability of the reuse of 
final fields among different class loaders doing exactly what 
serialization does, without the need of convert every field into 
a byteArray. This approach is at least 10 times faster than using 
serialization over a byte array.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:                Development/Java

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
%{summary}.

%prep
%setup -q -n %{name}-%{namedversion}-src
%{_bindir}/find -type f -name '*.jar' | %{_bindir}/xargs -t %{__rm}
%patch0 -p0
# Patch1 is needed if newer Hibernate versions are used
%patch1 -p0
%patch2 -p0

pushd libs
ln -s $(build-classpath asm/asm-attrs) .
ln -s $(build-classpath asm/asm) .
ln -s $(build-classpath cglib) cglib-2.1_2jboss.jar
ln -s $(build-classpath commons-logging) .
ln -s $(build-classpath concurrent) .
%if %with tests
# FIXME a jboss-serialization test is using a class 
# org.hibernate.engine.query.NativeSQLQuerySpecification that has been
# removed from Hibernate 3.2.4 (existed in 3.2.0)
ln -s $(build-classpath hibernate3-core) hibernate3.jar
# (dwalluck): removing the test case
%{__rm} ../tests/org/jboss/serial/hibernatesession/MockHibernateSession.java
%{__rm} ../tests/org/jboss/serial/hibernatesession/ProxySerializationTestCase.java
%endif
pushd javassist/lib
ln -s $(build-classpath javassist) .
popd
pushd jboss/aop/lib
ln -s $(build-classpath jboss-aop2/jboss-aop) .
#ln -s $(build-classpath jboss-aop/jboss-aop-jdk50-client) .
#ln -s $(build-classpath jboss-aop/jboss-aop-jdk50) .
#ln -s $(build-classpath jboss-aop/jdk14-pluggable-instrumentor) .
#ln -s $(build-classpath jboss-aop/jrockit-pluggable-instrumentor) .
ln -s $(build-classpath jboss-aop2/pluggable-instrumentor) .
popd
ln -s $(build-classpath jboss-common-core) jboss-common.jar
ln -s $(build-classpath jboss-profiler/jboss-profiler-jvmti) .
%if %with tests
ln -s $(build-classpath jboss5-libs/server-client) jboss-client.jar
ln -s $(build-classpath jboss5-libs/server-client) jboss-j2ee.jar
ln -s $(build-classpath jboss-remoting) .
%endif
ln -s $(build-classpath jcommon) .
ln -s $(build-classpath jfreechart) .
ln -s $(build-classpath jgroups) .
ln -s $(build-classpath joda-time) joda-time-1.2.1.jar
ln -s $(build-classpath jboss-jrunit) jrunit.jar
ln -s $(build-classpath junit) .
ln -s $(build-classpath log4j) .
ln -s $(build-classpath jboss-profiler/profilerConsole) .
ln -s $(build-classpath gnu-trove) trove.jar
popd

%build
%if %with tests
export CLASSPATH=$(build-classpath jboss-common-logging-log4j log4j)
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/junit`
export ANT_OPTS="-Djava.net.preferIPv4Stack=true"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadocs run-tests
%else
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadocs
%endif

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 build/jar/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom 
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap jboss jboss-serialization %{namedversion} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{namedversion}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-serialization.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-serialization.jar
%endif

%files
%doc docs/readme.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt1_8jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt1_5jpp5
- rebuild with default profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.3-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Oct 23 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_0.rc2.3jpp1.7
- converted from JPackage by jppimport script

