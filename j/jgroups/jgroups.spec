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

%define reltag GA

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib
%bcond_without tests

%define namedversion %{version}.%{reltag}

%define repodir %{_javadir}/repository.jboss.com/jgroups/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           jgroups
Version:        2.6.10
Release:	alt1_4jpp6
Epoch:          1
Summary:        Toolkit for reliable multicast communication
License:        LGPLv2+
URL:            http://www.jgroups.org/
Group:          Development/Java
# cvs -Q -z3 -d:pserver:anonymous@javagroups.cvs.sourceforge.net:/cvsroot/javagroups export -r JGroups_2_6_10_GA -d JGroups-2.6.10.GA JGroups && tar cjf JGroups-2.6.10.GA.tar.bz2 JGroups-2.6.10.GA
Source0:        JGroups-2.6.10.GA.tar.bz2
Source1:        jgroups-component-info.xml
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jakarta-commons-logging
Requires: log4j
Requires: jaxp_parser_impl
Requires: jms
Requires: bsh
#Optional:      mx4j
BuildRequires: jpackage-utils
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: bsh
BuildRequires: jakarta-commons-logging
BuildRequires: jaxp_parser_impl
BuildRequires: jboss-jms-1.1-api
BuildRequires: junit
BuildRequires: log4j
BuildRequires: mx4j
BuildRequires: xalan-j2
BuildArch:      noarch
Source44: import.info

%description
JGroups is a toolkit for reliable multicast communication. (Note that
this doesn't necessarily mean IP Multicast, JGroups can also use
transports such as TCP). It can be used to create groups of processes
whose members can send messages to each other. The main features include

    * Group creation and deletion. Group members can be spread across
      LANs or WANs
    * Joining and leaving of groups
    * Membership detection and notification about joined/left/crashed members
    * Detection and removal of crashed members
    * Sending and receiving of member-to-group messages (point-to-multipoint)
    * Sending and receiving of member-to-member messages (point-to-point)

To use JGroups one needs:
 commons-logging.jar
 log4j.jar

To run JGroups you need to have an XML parser installed on your system.
If you use JDK 1.4 or higher, you can use the parser that is shipped with it.

If you want to use the JGroups JMS protocol ( org.jgroups.protocols.JMS ),
then you will also need to place jms.jar somewhere in your CLASSPATH. 

Place the JAR files somewhere in your CLASSPATH , and you're ready to start
using JGroups.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

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

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n JGroups-%{version}.%{reltag}

find . -type f -name .cvsignore | xargs -t rm
find . -type f -name "*.jar" | xargs -t rm

# this test requires bouncycastle
rm tests/junit/org/jgroups/protocols/ENCRYPTAsymmetricTest.java

pushd lib
ln -s $(build-classpath ant) .
ln -s $(build-classpath ant-launcher) .
ln -s $(build-classpath ant/ant-junit) .
#BUILD/JGroups-2.4.1.src/lib/bcprov-jdk14-117.jar.no
ln -s $(build-classpath bsh) .
ln -s $(build-classpath commons-logging) .
ln -s $(build-classpath jms) .
ln -s $(build-classpath junit) .
ln -s $(build-classpath log4j) .
ln -s $(build-classpath mx4j/mx4j-jmx) .
ln -s $(build-classpath xalan-j2) .
ln -s $(build-classpath xalan-j2-serializer) .
popd

%build
export CLASSPATH=
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/{junit,trax}`
%if %without tests
#%{ant} jar javadoc gossiprouter-service jgroups-service
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar javadoc gossip-service jgroups-service
%else
#%{ant} jar javadoc gossiprouter-service jgroups-service testreport
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar javadoc gossip-service jgroups-service
%endif

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p dist/jgroups-all.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
cp -p dist/jgroups-core.jar %{buildroot}%{_javadir}/%{name}-core-%{version}.jar
cp -p dist/jgroups-sources.jar %{buildroot}%{_javadir}/%{name}-sources-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

# pom
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p jgroups-pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap jgroups jgroups %{namedversion} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# services
mkdir -p %{buildroot}%{_datadir}/%{name}-%{version}
for sar in $(pwd)/dist/*.sar; do
    bsar=$(basename ${sar})
    mkdir -p %{buildroot}%{_datadir}/%{name}-%{version}/${bsar}
    pushd %{buildroot}%{_datadir}/%{name}-%{version}/${bsar}
    %{jar} xf ${sar}
    for jar in `find -type f -name "*.jar"`; do
        rm ${jar}
        bjar=$(basename ${jar})
        ln -s %{_javadir}/${bjar} ${bjar}
    done
    popd
done
ln -s %{name}-%{version} %{buildroot}%{_datadir}/%{name}

# docs
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr doc/* %{buildroot}%{_docdir}/%{name}-%{version}

%if %with repolib
mkdir -p %{buildroot}%{repodir}
mkdir -p %{buildroot}%{repodirlib}
cp -p %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}.%{reltag}-brew/g" %{buildroot}%{repodir}/component-info.xml
mkdir -p %{buildroot}%{repodirsrc}
cp -p %{SOURCE0} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/jgroups.jar
cp -p %{buildroot}%{_javadir}/%{name}-sources-%{version}.jar %{buildroot}%{repodirlib}/jgroups-sources.jar
cp -p jgroups-pom.xml %{buildroot}%{repodirlib}/jgroups.pom
%endif

%files
%doc CREDITS EULA INSTALL.html LICENSE README
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-core-%{version}.jar
%{_javadir}/%{name}-core.jar
%{_javadir}/%{name}-sources-%{version}.jar
%{_javadir}/%{name}-sources.jar
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}-%{version}/gossip-router.sar/
%dir %{_datadir}/%{name}-%{version}/jgroups-service.sar
%dir %{_datadir}/%{name}-%{version}/jgroups-service.sar/META-INF
%{_datadir}/%{name}-%{version}/jgroups-service.sar/META-INF/MANIFEST.MF
%{_datadir}/%{name}-%{version}/jgroups-service.sar/META-INF/jboss-service.xml
%{_datadir}/%{name}-%{version}/jgroups-service.sar/commons-logging.jar
%{_datadir}/%{name}-%{version}/jgroups-service.sar/jg-magic-map.xml
%{_datadir}/%{name}-%{version}/jgroups-service.sar/jgroups-core.jar
%{_datadir}/%{name}-%{version}/jgroups-service.sar/log4j.jar
%{_datadir}/%{name}-%{version}/jgroups-service.sar/stacks.xml
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.6.10-alt1_4jpp6
- new version

* Sat Sep 27 2008 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt2_1.SP4.1jpp5
- fixed build

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt1_1.SP4.1jpp5
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.9.2-alt1_3jpp1.7
- converted from JPackage by jppimport script

