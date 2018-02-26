Packager: Igor Vlasenko <viy@altlinux.ru>
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

%def_with jdk6
%bcond_with jdk6

#def_with bootstrap
%bcond_with bootstrap

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jboss/cache/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

# If you want to built without jdk15 support, 
# give rpmbuild option '--without jdk15'
%define without_jdk15 %{?_without_jdk15:1}%{!?_without_jdk15:0}
%define with_jdk15 %{!?_without_jdk15:1}%{?_without_jdk15:0}

# If you want to built with unit tests, give rpmbuild option '--with tests'
%define with_tests %{?_with_tests:1}%{!?_with_tests:0}
%define without_tests %{!?_with_tests:1}%{?_with_tests:0}


%define reltag  SP9

Name:           jboss-cache
Version:        1.4.1
Release:        alt3_4.SP9.6jpp6
Epoch:          0
Summary:        JBoss Cache
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn export http://anonsvn.jboss.org/repos/jbosscache/core/tags/1.4.1.SP9/ JBossCache-1.4.1.SP9-src
# tar czf JBossCache-1.4.1.SP9-src.tar.gz JBossCache-1.4.1.SP9-src
Source0:        JBossCache-1.4.1.SP9-src.tar.gz
Source1:        jboss-cache-README.txt
Source2:	jboss-cache-component-info.xml

# FIXME must adjust this patch to force IPv4 to be used on Linux
Patch1:		jboss-cache-1.3.0.2-build_xml.patch
Patch2:		jboss-cache-GlobalTransactionTest.patch

# tool requires
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant
BuildRequires: ant-javamail
BuildRequires: ant-junit
BuildRequires: ant-nodeps
BuildRequires: ant-trax
#BuildRequires: ant-xslp
BuildRequires: bsf
BuildRequires: junit
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xml-commons-resolver
%if  %{with_jdk15}
%else
%endif

# other requires
BuildRequires: bsh2 >= 0:2.0-0.b4
BuildRequires: berkeleydb
BuildRequires: concurrent
BuildRequires: dom4j
BuildRequires: derby
BuildRequires: gnu.trove
BuildRequires: jakarta-commons-logging
BuildRequires: javassist
BuildRequires: jboss-aop
BuildRequires: jboss-jrunit
BuildRequires: jboss-serialization
%if %with bootstrap
BuildRequires: jboss4-common
BuildRequires: jboss4-j2ee
BuildRequires: jboss4-jmx
BuildRequires: jboss4-server
BuildRequires: jboss4-system
%else
BuildRequires: jboss-common
BuildRequires: jbossas
%endif
BuildRequires: jdbm
BuildRequires: jcommon
BuildRequires: jfreechart
BuildRequires: jgroups
BuildRequires: log4j
BuildRequires: qdox >= 0:1.5
Requires: berkeleydb
Requires: concurrent
Requires: jakarta-commons-logging
Requires: jboss-aop
Requires: jboss-common
%if %with bootstrap
Requires: jboss4-common
Requires: jboss4-j2ee
Requires: jboss4-jmx
Requires: jboss4-server
Requires: jboss4-system
%else
Requires: jboss-common
Requires: jbossas
%endif
Requires: jgroups
Requires: xml-commons-jaxp-1.3-apis
BuildArch:      noarch
Source44: import.info
Patch33: jboss-cache-1.4.1-alt-berkeleydb-3.0.12.patch

%description
JBoss Cache is a product designed to cache frequently accessed 
Java objects in order to dramatically improve the performance 
of e-business applications. By eliminating unnecessary database 
access, JBoss Cache decreases network traffic and increases the 
scalability of applications.
JBoss Cache provides two caching APIs to suit your needs. The 
JBossCache API offers a traditional, tree-structured node-based 
cache and the JBossCacheAOP API, which builds on the JBossCache 
API, provides the ability to perform fine-grained replication 
of Java objects, resulting in maximum performance benefits. 


%if %{with_repolib}
%package repolib
Summary:	Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires: java-javadoc
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.

%prep
%setup -q -n JBossCache-1.4.1.%{reltag}-src
find . -type f -name "*.jar" | xargs -t rm
# FIXME must adjust this patch to force IPv4 to be used on Linux
#%%patch1 -b .sav
%patch2 -b .sav

pushd ant-dist/lib
#BUILD/JBossCache-1.3.0.1-src/ant-dist/lib/ant.jar.no
ln -sf $(build-classpath ant) .
#BUILD/JBossCache-1.3.0.1-src/ant-dist/lib/ant-junit.jar.no
ln -sf $(build-classpath ant/ant-junit) .
#BUILD/JBossCache-1.3.0.1-src/ant-dist/lib/ant-launcher.jar.no
ln -sf $(build-classpath ant-launcher) .
#BUILD/JBossCache-1.3.0.1-src/ant-dist/lib/ant-nodeps.jar.no
ln -sf $(build-classpath ant/ant-nodeps) .
#BUILD/JBossCache-1.3.0.1-src/ant-dist/lib/ant-trax.jar.no
ln -sf $(build-classpath ant/ant-trax) .
#BUILD/JBossCache-1.3.0.1-src/ant-dist/lib/ant-xslp.jar.no
#ln -sf $(build-classpath ant/ant-xslp) .
#BUILD/JBossCache-1.3.0.1-src/ant-dist/lib/bsf.jar.no
ln -sf $(build-classpath bsf) .
#BUILD/JBossCache-1.3.0.1-src/ant-dist/lib/junit.jar.no
ln -sf $(build-classpath junit) .
#BUILD/JBossCache-1.3.0.1-src/ant-dist/lib/pretty.jar.no
#
#BUILD/JBossCache-1.3.0.1-src/ant-dist/lib/resolver.jar.no
ln -sf $(build-classpath xml-commons-resolver) resolver.jar
popd
pushd lib-50
#BUILD/JBossCache-1.3.0.1-src/lib-50/jboss-aop-jdk50.jar.no
#
popd
pushd lib
#BUILD/JBossCache-1.3.0.1-src/lib/bsh-2.0b4.jar.no
ln -sf $(build-classpath bsh2/bsh-core) .
ln -sf $(build-classpath bsh2/bsh-util) .
#BUILD/JBossCache-1.3.0.1-src/lib/commons-logging.jar.no
ln -sf $(build-classpath commons-logging) .
#BUILD/JBossCache-1.3.0.1-src/lib/concurrent.jar.no
ln -sf $(build-classpath concurrent) .
#
ln -sf $(build-classpath dom4j) .
#BUILD/JBossCache-1.3.0.1-src/lib/derby.jar.no
ln -sf $(build-classpath derby/derby) .
#BUILD/JBossCache-1.3.0.1-src/lib/javassist.jar.no
ln -sf $(build-classpath javassist) .
#BUILD/JBossCache-1.3.0.1-src/lib/jboss-aop.jar.no
ln -sf $(build-classpath jboss-aop/jboss-aop) .
#BUILD/JBossCache-1.3.0.1-src/lib/jboss-j2ee.jar.no
%if %with bootstrap
ln -sf $(build-classpath jboss4/jboss-common) .
ln -sf $(build-classpath jboss4/jboss-j2ee) .
ln -sf $(build-classpath jboss4/jboss-jmx) .
ln -sf $(build-classpath jboss4/jboss-minimal) .
ln -sf $(build-classpath jboss4/jboss-system) .
%else
#BUILD/JBossCache-1.3.0.1-src/lib/jboss-common.jar.no
ln -sf $(build-classpath jboss-common/jboss-common) .
#BUILD/JBossCache-1.3.0.1-src/lib/jboss-j2ee.jar.no
ln -sf $(build-classpath jbossas/jboss-j2ee) .
#BUILD/JBossCache-1.3.0.1-src/lib/jboss-jmx.jar.no
ln -sf $(build-classpath jbossas/jboss-jmx) .
#BUILD/JBossCache-1.3.0.1-src/lib/jboss-minimal.jar.no
ln -sf $(build-classpath jbossas/jboss-minimal) .
#BUILD/JBossCache-1.3.0.1-src/lib/jboss-system.jar.no
ln -sf $(build-classpath jbossas/jboss-system) .
%endif
#BUILD/JBossCache-1.3.0.1-src/lib/jboss-serialization.jar.no
ln -sf $(build-classpath jboss-serialization) .
#BUILD/JBossCache-1.3.0.1-src/lib/jdbm-1.0.jar.no
ln -sf $(build-classpath jdbm) .
#BUILD/JBossCache-1.3.0.1-src/lib/jcommon-1.0.0-rc1.jar.no
ln -sf $(build-classpath jcommon) .
#BUILD/JBossCache-1.3.0.1-src/lib/jfreechart-1.0.0-rc1.jar.no
ln -sf $(build-classpath jfreechart) .
#BUILD/JBossCache-1.3.0.1-src/lib/jgroups.jar.no
ln -sf $(build-classpath jgroups) .
#BUILD/JBossCache-1.3.0.1-src/lib/jrunit.jar.no
ln -sf $(build-classpath jboss-jrunit) jrunit.jar
#BUILD/JBossCache-1.3.0.1-src/lib/junit.jar.no
ln -sf $(build-classpath junit) .
#BUILD/JBossCache-1.3.0.1-src/lib/log4j.jar.no
ln -sf $(build-classpath log4j) .
#BUILD/JBossCache-1.3.0.1-src/lib/qdox.jar.no
ln -sf $(build-classpath qdox) .
#BUILD/JBossCache-1.3.0.1-src/lib/trove.jar.no
ln -sf $(build-classpath gnu.trove) trove.jar
pushd sleepycat
#BUILD/JBossCache-1.3.0.1-src/lib/sleepycat/je.jar.no
ln -sf $(build-classpath berkeleydb) je.jar
popd
popd
%patch33 -p1

%build
BUILD_ID=`date -u +%Y%m%d%H%M`_%{version}-%{release}

#FIXME:
%if %with jdk6
rm tests/functional/org/jboss/cache/loader/DataSourceIntegrationTest.java
%endif

export CLASSPATH=
export OPT_JAR_LIST=:

%if %{with_tests}
export ANT_OPTS="-Djava.net.preferIPv4Stack=true"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
	-Djunit.timeout.performance=90000 \
	-Djunit.timeout=750000 \
	jar javadocs unittests
%else
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadocs
%endif

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

# jars
install -m 644 dist/lib/jboss-cache.jar $RPM_BUILD_ROOT%{_javadir}/jboss-cache-%{version}.jar
%if %{with_jdk15}
install -m 644 dist/lib-50/jboss-cache-jdk50.jar $RPM_BUILD_ROOT%{_javadir}/jboss-cache-jdk50-%{version}.jar
%endif

# create all versionless symlinks
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# -----------------------------------------------------------------------------
# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
        tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
        sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/README.txt
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	install -p -m 0644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-cache-jdk50.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%{_javadir}/jboss-cache-%{version}.jar
%{_javadir}/jboss-cache.jar
%if %{with_jdk15}
%{_javadir}/jboss-cache-jdk50-%{version}.jar
%{_javadir}/jboss-cache-jdk50.jar
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

# -----------------------------------------------------------------------------

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Oct 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt3_4.SP9.6jpp6
- fixed build w/new berkeleydb

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt3_4.SP9.6jpp5
- selected java5 compiler explicitly

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_4.SP9.6jpp5
- full build

* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_4.SP9.6jpp5
- new bootstrap version

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0.2-alt1_1jpp5
- fixed build w/java5

* Tue Dec 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

