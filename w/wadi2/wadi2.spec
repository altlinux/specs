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

%define gcj_support 0


Name:           wadi2
Version:        2.1.1
Release:        alt2_1jpp6
Epoch:          0
License:        ASL 2.0
Summary:        WADI Application Distribution Infrastructure
Group:          Development/Java
URL:            http://wadi.codehaus.org/
# svn -q export http://svn.codehaus.org/wadi/tags/2.1.1/ wadi-2.1.1 && tar cjf wadi-2.1.1.tar.bz2 wadi-2.1.1
Source0:        wadi-2.1.1.tar.bz2
Source1:        wadi-2.0-M10-settings.xml
Source2:        wadi-2.0-M10-jpp-depmap.xml
Patch0:         wadi-2.1.1-pom.patch
Patch1:         wadi-2.0-tribes-pom.patch
Patch2:         wadi-2.0-M10-webapp-pom.patch
Patch3:         wadi-2.0-group-TestVMCluster.patch
Patch4:         wadi-2.0-core-AbstractServiceSpaceTestCase.patch
Patch5:         wadi-2.0-M10-core-BasicServiceSpaceRegistryTest.patch
Patch6:         wadi-2.0-M10-core-GetServiceSpaceInfosTest.patch
Patch7:         wadi-2.0-M10-core-LocalPartitionInsertIMToPMActionTest.patch
Patch8:         wadi-2.0-core-BasicServiceSpaceTest.patch
Patch9:         wadi-2.0-M10-core-VersionAwarePartitionFacadeTest.patch
Patch10:        wadi-2.0-M10-core-BasicServiceInvokerTest.patch
Patch11:        wadi-2.0-M10-core-BasicServiceRegistryTest.patch
Patch12:        wadi-2.1.1-core-LockingRehydrationImmoterTest.patch
Patch13:        wadi-2.0-M10-core-ReplicaAwareContextualiserTest.patch
Patch14:        wadi-2.0-M10-core-LocalPartitionMoveIMToPMActionTest.patch
Patch15:        wadi-2.0-M10-core-LocalPartitionEvacuateIMToPMActionTest.patch
Patch16:        wadi-2.0-M10-core-BasicClassIndexerTest.patch
Patch17:        wadi-2.0-M10-core-BasicPartitionRepopulateTaskTest.patch
Patch18:        wadi-2.0-M10-core-SimplePartitionManagerSmokeTest.patch
Patch19:        wadi-2.0-M10-aop-CopyStateVisitorTest.patch
Patch20:        wadi-2.0-M10-aop-ValueUpdaterInfoTest.patch
Patch21:        wadi-2.0-M10-aop-BasicInstanceTrackerTest.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-clean
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-war
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: mojo-maven2-plugin-aspectj
BuildRequires: mojo-maven2-plugin-jspc
BuildRequires: mojo-maven2-jspc-compiler-tomcat5

BuildRequires: rmock

BuildRequires: cglib
BuildRequires: concurrent
BuildRequires: derby
BuildRequires: groovy11
BuildRequires: jakarta-commons-el
BuildRequires: jakarta-slide-webdavclient >= 0:2.1
BuildRequires: jgroups
BuildRequires: mx4j
BuildRequires: spring-mock
BuildRequires: tomcat5-jasper
BuildRequires: tomcat6
BuildRequires: tomcat6-lib


%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
WADI is an acronym of 
'WADI Application Distribution Infrastructure'. 
WADI started life as a solution to the problems surrounding
the distribution of state in clustered web tiers. It has 
evolved into a more generalised distributed state and service
framework.  WADI's aim is to resolve many of the problems of
dealing with state in a cluster. This involves technologies
such as: 
WADI Core: 
- Vertically - a distributed 'space' with pluggable/stackable
  paging and persistance mechanisms (e.g. File and Database) 
- Horizontally - A scalable, highly available, self-partitioning,
  self-healing clustering substrate 
- Providing transparent migration of State to Invocation but
  also migration of Invocation to State 
- Pluggable in-memory replication strategies for HA state 
WADI AOP: 
- An AOP extension providing the fine-grained replication of
  state, i.e. object instances. Thanks to AOP, field updates
  and method executions are tracked and replayed on state replicas. 
WADI Web: 
- A resolution to application vs container space concurrency
  issues surrounding HttpSessions 
- Pluggable HttpSession serialisation strategies - per-session,
  per-attribute 
- HttpRequest relocation (by redirection and proxying) 
- HttpSession replication 

WADI currently supports the following J2EE containers and
application servers: 
Jetty-6.x 
Geronimo-2.x/Jetty 
Geronimo-2.1/Tomcat 
Geronimo-2.1/OpenEJB 

#%package webapp
#Summary:        WebApp Module from %{name}
#Group:          Development/Libraries/Java
#Requires:       %{name} = %{epoch}:%{version}-%{release}
#
#%description webapp
#%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n wadi-%{version}
cp -p %{SOURCE1} settings.xml
# XXX: test can fail/hang
rm wadi-core/src/test/java/org/codehaus/wadi/evacuation/TestInVMEvacuation.java
# XXX: Recognition of file "/builddir/build/BUILDROOT/wadi2-2.1.1-1.jpp6.x86_64/usr/share/doc/wadi2-2.1.1/topologies.gnumeric" failed: mode 100644 zlib: invalid literal/lengths setempty (gzip compressed data, from Unix, last modified: Wed Jul  7 13:53:16 2004)
find -type f -name topologies.gnumeric | xargs -t rm
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
%patch15 -b .sav15
%patch16 -b .sav16
%patch17 -b .sav17
%patch18 -b .sav18
%patch19 -b .sav19
%patch20 -b .sav20
%patch21 -b .sav21

cp -pr wadi-webapp/src/webapp wadi-webapp/src/main

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP


sed -i -e '/relativePath/d' wadi-aop/pom.xml wadi-group/pom.xml

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}

export SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dmaven.test.failure.ignore=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        install javadoc:javadoc

#pushd wadi-webapp
#    mvn-jpp \
#        -e \
#        -s $SETTINGS \
#        -DtoolsJar=$JAVA_HOME/lib/tools.jar \
#        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
#        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
#        compiler:compile install
#popd

%install

install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
# jars
install -d -m 755 %{buildroot}%{_javadir}/%{name}

%add_to_maven_depmap org.codehaus.wadi wadi %{version} JPP/%{name} wadi
install -p -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-wadi.pom

install -p -m 644 wadi-aop/target/wadi-aop-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/aop-%{version}.jar
%add_to_maven_depmap org.codehaus.wadi wadi-aop %{version} JPP/%{name} aop
install -p -m 644 wadi-aop/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-aop.pom

install -p -m 644 wadi-core/target/wadi-core-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/core-%{version}.jar
%add_to_maven_depmap org.codehaus.wadi wadi-core %{version} JPP/%{name} core
install -p -m 644 wadi-core/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-core.pom

install -p -m 644 wadi-group/target/wadi-group-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/group-%{version}.jar
%add_to_maven_depmap org.codehaus.wadi wadi-group %{version} JPP/%{name} group
install -p -m 644 wadi-group/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-group.pom

install -p -m 644 wadi-jgroups/target/wadi-jgroups-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/jgroups-%{version}.jar
%add_to_maven_depmap org.codehaus.wadi wadi-jgroups %{version} JPP/%{name} jgroups
install -p -m 644 wadi-jgroups/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jgroups.pom

install -p -m 644 wadi-tribes/target/wadi-tribes-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/tribes-%{version}.jar
%add_to_maven_depmap org.codehaus.wadi wadi-tribes %{version} JPP/%{name} tribes
install -p -m 644 wadi-tribes/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-tribes.pom


(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

#install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}
#install -p -m 644 wadi-webapp/target/wadi-webapp-%{version}.war \
#   %{buildroot}%{_datadir}/%{name}-%{version}/webapp-%{version}.war
#(cd %{buildroot}%{_datadir}/%{name}-%{version} && for war in *-%{version}.war; do ln -sf ${war} `echo $war| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
for m in aop core group jgroups tribes; do 
    install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}/${m}
    cp -pr wadi-${m}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/${m}
done
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr doc/* %{buildroot}%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/aop-%{version}.jar
%{_javadir}/%{name}/aop.jar
%{_javadir}/%{name}/core-%{version}.jar
%{_javadir}/%{name}/core.jar
%{_javadir}/%{name}/group-%{version}.jar
%{_javadir}/%{name}/group.jar
%{_javadir}/%{name}/jgroups-%{version}.jar
%{_javadir}/%{name}/jgroups.jar
%{_javadir}/%{name}/tribes-%{version}.jar
%{_javadir}/%{name}/tribes.jar
%{_datadir}/maven2/poms/JPP.%{name}-aop.pom
%{_datadir}/maven2/poms/JPP.%{name}-core.pom
%{_datadir}/maven2/poms/JPP.%{name}-group.pom
%{_datadir}/maven2/poms/JPP.%{name}-jgroups.pom
%{_datadir}/maven2/poms/JPP.%{name}-tribes.pom
%{_datadir}/maven2/poms/JPP.%{name}-wadi.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*-%{version}.jar.*
%endif

#%files webapp
#%defattr(0644,root,root,0755)
#%{_datadir}/%{name}-%{version}/webapp*.war

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_1jpp6
- fixed build

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_1jpp6
- jpp 6.0 relese

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_0.M10.1jpp5
- explicit selection of java5 compiler

* Wed May 20 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_0.M10.1jpp5
- new version

