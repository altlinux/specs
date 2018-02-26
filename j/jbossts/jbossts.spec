Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: geronimo-jta-1.1-api
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-core
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

%bcond_with bootstrap
# FIXME: (dwalluck): these features are broken
%bcond_with ws
%bcond_with jts

%bcond_with jdk6

%define _with_repolib 1
# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define reltag SP7
%define repodir %{_javadir}/repository.jboss.com/jboss/jbossts14/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

Name:           jbossts
Version:        4.2.3
Release:        alt3_1.SP7.4jpp5
Epoch:          1
Summary:        JBoss Transaction Service
License:        LGPLv2+
Group:          Development/Java
URL:		http://labs.jboss.com/jbosstm/
# svn export http://anonsvn.jboss.org/repos/labs/labs/jbosstm/tags/JBOSSTS_4_2_3_SP7/ JBOSSTS_4_2_3_SP7
# tar czf jbossts-4.2.3.SP7-src.tar.gz JBOSSTS_4_2_3_SP7
Source0:	jbossts-4.2.3.SP7-src.tar.gz
Source1:	jbossts-component-info.xml
Patch0:		jbossts-build.patch
Patch1:		jbossts-jfreechart.patch
Patch2:		jbossts-beamainthread.patch
Patch3:		jbossts-tests.patch
Patch4:         jbossts-jdk16.patch
BuildArch:	noarch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant17 >= 0:1.6
BuildRequires: ant17-nodeps
BuildRequires: ant17-junit
BuildRequires: ant17-trax
BuildRequires: junit
%if %with bootstrap
Requires: jboss4
Requires: jboss4-config-all
BuildRequires: jboss4
BuildRequires: jboss4-config-all
%else
Requires: jbossas
BuildRequires: jbossas
%endif
BuildRequires: mx4j
BuildRequires: jfreechart
BuildRequires: jcommon
BuildRequires: jta
BuildRequires: jakarta-commons-logging
BuildRequires: tanukiwrapper
BuildRequires: j2ee-connector
BuildRequires: concurrent
BuildRequires: log4j
BuildRequires: xerces-j2
%if %with jts
BuildRequires: antlr
BuildRequires: excalibur-avalon-logkit
BuildRequires: excalibur-avalon-framework-api
BuildRequires: excalibur-avalon-framework-impl
BuildRequires: jacorb
BuildRequires: picocontainer
%endif
%if %with ws
BuildRequires: bea-stax-api
BuildRequires: servletapi5
BuildRequires: saaj
BuildRequires: jaxrpc
BuildRequires: wstx
%endif
BuildRequires: xalan-j2
Requires: jpackage-utils >= 0:1.6

%description
Reliable Java and Web Services transaction management.
Includes Arjuna Transaction Service Suite (ArjunaTS) and
Arjuna's Web Services Transaction implementation, the market's only
implementation supporting both leading web services specifications
Web Services Transaction (WS-TX) and Web Services Composite Application
Framework (WS-CAF)

%if %{with_repolib}
%package repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:	         Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}

%prep
%setup -q -n JBOSSTS_4_2_3_SP7
chmod -R go=u-w *

# FIXME: remove classes12.jar which is Oracle's proprietary
# FIXME: Where do we get this Arjuna's TestingFramework.jar ?
# FIXME: Upgrade jfreechart used by JBossTS
find . -name "*.jar" \
       -not -name "classes12.jar" \
       -not -name "TestingFramework.jar" \
       -not -name "jfreechart-0.9.15.jar" \
       | xargs %{__rm}

pushd ext
build-jar-repository . jmxri
build-jar-repository . jndi
build-jar-repository . jta
build-jar-repository . jdbc-stdext
build-jar-repository . commons-logging
build-jar-repository . tanukiwrapper
build-jar-repository . j2ee-connector
build-jar-repository . concurrent
build-jar-repository . log4j
# FIXME the ones below were supposed to be under ArjunaCore/tsmx/lib/ext but
# there they are not found, so moved them here
build-jar-repository . jcommon
# FIXME Upgrade jfreechart used by JBossTS
#build-jar-repository . jfreechart
popd
pushd antbuildsystem/lib/ext
build-jar-repository . xerces-j2
popd
pushd common/lib/ext
build-jar-repository . xerces-j2
build-jar-repository . commons-logging
build-jar-repository . log4j
popd
#pushd ArjunaCore/tsmx/lib/ext
#build-jar-repository . jcommon
#build-jar-repository . jfreechart
#popd

%if %with jts
pushd ArjunaJTS/jacorb/lib
build-jar-repository . tanukiwrapper
build-jar-repository . antlr
build-jar-repository . excalibur/avalon-framework-api
build-jar-repository . excalibur/avalon-framework-impl
build-jar-repository . excalibur/avalon-logkit
build-jar-repository . jacorb
build-jar-repository . concurrent
build-jar-repository . picocontainer
popd
%endif

%patch0 -p0
#%patch1 -p0
%patch2 -p0
%patch3 -p1
%if %with jdk6
%patch4 -p1
%endif

%build
export CLASSPATH=
export OPT_JAR_LIST="ant17/ant17-nodeps ant17/ant17-junit junit ant17/ant17-trax xalan-j2 xalan-j2-serializer"
%if %with bootstrap
export JBOSS_HOME=%{_datadir}/jboss4
%else
export JBOSS_HOME=%{_datadir}/jbossas
%endif
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dant.library.dir=%{_javadir} \
	-Djavac.debug=true \
	jbossjta \
%if %with jts
	jbossjts
%endif


%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}/resources
install -p -m 0644 install/etc/jbossjta-properties.xml $RPM_BUILD_ROOT%{_javadir}/%{name}/resources
install -p -m 0644 install/lib/jbossjta.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbossjta-%{version}.jar
install -p -m 0644 install/lib/jbossjta-integration.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbossjta-integration-%{version}.jar
install -p -m 0644 install/lib/ext/%{name}-common.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-common-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr install/htdocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}/resources
	install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
        tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
        sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
	install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/jbossts/jbossts-common.jar $RPM_BUILD_ROOT%{repodirlib}
	cp -p $RPM_BUILD_ROOT%{_javadir}/jbossts/jbossjta-integration.jar $RPM_BUILD_ROOT%{repodirlib}
	cp -p $RPM_BUILD_ROOT%{_javadir}/jbossts/jbossjta.jar $RPM_BUILD_ROOT%{repodirlib}
	cp -p $RPM_BUILD_ROOT%{_javadir}/jbossts/resources/jbossjta-properties.xml $RPM_BUILD_ROOT%{repodir}/resources
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jbossjta-%{version}.jar
%{_javadir}/%{name}/jbossjta-integration-%{version}.jar
%{_javadir}/%{name}/jbossjta-integration.jar
%{_javadir}/%{name}/jbossjta.jar
%{_javadir}/%{name}/jbossts-common-%{version}.jar
%{_javadir}/%{name}/jbossts-common.jar
%dir %{_javadir}/%{name}/resources
%{_javadir}/%{name}/resources/jbossjta-properties.xml

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 1:4.2.3-alt3_1.SP7.4jpp5
- build with ant17

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 1:4.2.3-alt2_1.SP7.4jpp5
- selected java5 compiler explicitly

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 1:4.2.3-alt1_1.SP7.4jpp5
- new version

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 1:4.2.3-alt0.1jpp
- bootstrap for jbossas

