# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 1.0.0
%define name jboss-profiler
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/jboss/profiler/jvmti/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define reltag CR5

Name:           jboss-profiler
Version:        1.0.0
Release:        alt2_0.1.CR5.6jpp6
Epoch:          0
Summary:        Log based profiler using JVMPI and JVMTI
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com/portal/jbossprofiler
# cvs -z3 -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r JBPROFILER_CR5 -d jboss-profiler-1.0.0.CR5 jboss-profiler && tar cjf jboss-profiler-1.0.0.CR5.tar.bz2 jboss-profiler-1.0.0.CR5
Source0:        jboss-profiler-1.0.0.CR5.tar.bz2
Source1:        http://repository.jboss.org/maven2/jboss/profiler/jvmti/jboss-profiler-jvmti/1.0.0.CR5/jboss-profiler-jvmti-1.0.0.CR5.pom
Source2:        jboss-profiler-jvmti-component-info.xml
Patch0:         jboss-profiler-ChartView.patch
Patch1:         jboss-profiler-ServletUpload.patch
Patch2:         jboss-profiler-ServletUploadFile.patch
Patch3:         jboss-profiler-GraphApplet.patch
Patch4:         jboss-profiler-GraphMemoryApplet.patch
Patch5:         jboss-profiler-project_properties.patch
Patch6:         jboss-profiler-jfreechart-StandardPieToolTipGenerator.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       jpackage-utils >= 0:1.7.3
Requires:       jboss-common-core
Requires:       jboss-common-logging-spi
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit
BuildRequires:  ant-nodeps
BuildRequires:  jboss-aop2
BuildRequires:  jboss-common-core
BuildRequires:  jboss-common-logging-spi
BuildRequires:  gnu-trove
BuildRequires:  struts
BuildRequires:  servlet_2_5_api
BuildRequires:  jakarta-commons-beanutils
BuildRequires:  jakarta-commons-fileupload
BuildRequires:  jakarta-poi
BuildRequires:  jcommon
BuildRequires:  jfreechart
BuildRequires:  jgraph
BuildRequires:  junit
BuildArch:      noarch
Source44: import.info

%description
JBoss Profiler is a log based profiler using JVMPI and JVMTI. 
It uses an agent written in C that captures events from the
JVM and logs them to disk. A web application running on JBoss
or another machine can be used to analyze these logs through a
web browser.

Using log files is especially useful for server application
analysis. Creating profiling snapshots without the need of a
front-end near the JVM means the data can be analyzed#
remotely.

Imagine if your application server slows down and you don't know
why. Why should you have to install a complex tool environment or
have to send data through an open port, breaking firewall rules
between the profiler front-end and the JVMPI/JVMTI JBoss Profiler
can be easily run though your web browser instead.

NOTE: You may have to add a few things on the classpath for running the
profiler console (jgraph, jfreechart, jcommon...).
The AS should provide what is needed for the data # collection during run-time.

%package webapps
Summary:        WARs, SARs, Applet for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description webapps
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}

%if %with repolib
%package jvmti-repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description jvmti-repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n jboss-profiler-%{version}.%{reltag}
chmod -R go=u-w *
# Clean up jars
find . -name "*.jar" | xargs -t %{__rm}

# FIXME should not be needed if an export is used
find . -depth -type d -name CVS -exec rm -r {} \;

%{__perl} -pi -e 's/\r$//g' docs/wiki/JBossProfilerDocumentation.wiki docs/Tutorials/readme.txt

%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
%patch4 -p0 -b .sav4
%patch5 -p0 -b .sav5
%patch6 -p1 -b .sav6

pushd java/libs/aop
ln -s $(build-classpath jboss-aop2/jboss-aop) .
ln -s $(build-classpath jboss-common-logging-spi) .
ln -s $(build-classpath jboss-common-core) .
ln -s $(build-classpath gnu-trove) .
popd
pushd java/libs/web
ln -s $(build-classpath struts) .
ln -s $(build-classpath servlet_2_5_api) .
ln -s $(build-classpath commons-fileupload) .
ln -s $(build-classpath commons-beanutils) .
ln -s $(build-classpath poi) .
ln -s $(build-classpath jfreechart) .
ln -s $(build-classpath jcommon) .
popd
pushd java/libs/appletsLibs
ln -s $(build-classpath jgraph) .
popd

%build
export CLASSPATH=
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/{junit,nodeps}`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
        compile \
        jar \
        war \
        console \
        jboss-mbean \
        javah-full \
        javah-lite \
        antProfiler \
        appletjar

%install

# jar
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -p -m 0644 build/antProfiler.jar %{buildroot}%{_javadir}/%{name}/antProfiler-%{version}.jar
install -p -m 0644 build/jar/jboss-profilerEngine.jar %{buildroot}%{_javadir}/%{name}/jboss-profilerEngine-%{version}.jar
install -p -m 0644 build/jboss-profiler-jvmti.jar %{buildroot}%{_javadir}/%{name}/jboss-profiler-jvmti-%{version}.jar
install -p -m 0644 build/profilerConsole.jar %{buildroot}%{_javadir}/%{name}/profilerConsole-%{version}.jar
install -p -m 0644 build/profilerSynchronizer.jar %{buildroot}%{_javadir}/%{name}/profilerSynchronizer-%{version}.jar
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.jboss-profiler-jvmti.pom
%add_to_maven_depmap jboss.profiler.jvmti jboss-profiler-jvmti %{namedversion} JPP %{name}/jboss-profiler-jvmti

# webapps
install -d -m 0755 %{buildroot}%{_datadir}/%{name}-%{version}
install -p -m 0644 build/aop-monitoring.war %{buildroot}%{_datadir}/%{name}-%{version}
install -p -m 0644 build/applet/graphApplet.jar %{buildroot}%{_datadir}/%{name}-%{version}
install -p -m 0644 build/jboss-profiler-jvmti.sar %{buildroot}%{_datadir}/%{name}-%{version}
install -p -m 0644 build/jboss-profiler-noAOP.sar %{buildroot}%{_datadir}/%{name}-%{version}
install -p -m 0644 build/jboss-profiler.war %{buildroot}%{_datadir}/%{name}-%{version}

# manual
install -d -m 0755 %{buildroot}%{_docdir}/%{name}-%{version}
mv "docs/JBossProfiler - JVMTI.doc" "docs/JBossProfiler-JVMTI.doc"
mv "docs/JBoss Profiler ARM.doc" "docs/JBossProfilerARM.doc"
cp -pr docs/* %{buildroot}%{_docdir}/%{name}-%{version}

%if %with repolib
install -d -m 755 %{buildroot}%{repodir}
install -d -m 755 %{buildroot}%{repodirlib}
install -p -m 644 %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}.%{reltag}-brew/g" %{buildroot}%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
install -d -m 755 %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
install -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
install -p -m 644 %{PATCH1} %{buildroot}%{repodirsrc}
install -p -m 644 %{PATCH2} %{buildroot}%{repodirsrc}
install -p -m 644 %{PATCH3} %{buildroot}%{repodirsrc}
install -p -m 644 %{PATCH4} %{buildroot}%{repodirsrc}
install -p -m 644 %{PATCH5} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}/jboss-profiler-jvmti.jar %{buildroot}%{repodirlib}/jboss-profiler-jvmti.jar
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/antProfiler-%{version}.jar
%{_javadir}/%{name}/antProfiler.jar
%{_javadir}/%{name}/jboss-profiler-jvmti-%{version}.jar
%{_javadir}/%{name}/jboss-profiler-jvmti.jar
%{_javadir}/%{name}/jboss-profilerEngine-%{version}.jar
%{_javadir}/%{name}/jboss-profilerEngine.jar
%{_javadir}/%{name}/profilerConsole-%{version}.jar
%{_javadir}/%{name}/profilerConsole.jar
%{_javadir}/%{name}/profilerSynchronizer-%{version}.jar
%{_javadir}/%{name}/profilerSynchronizer.jar
%{_datadir}/maven2/poms/JPP.%{name}.jboss-profiler-jvmti.pom
%{_mavendepmapfragdir}/%{name}

%files webapps
%{_datadir}/%{name}-%{version}

%files manual
%{_docdir}/%{name}-%{version}

%if %with repolib
%files jvmti-repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt2_0.1.CR5.6jpp6
- built with java 6 due to com.sun.image.codec.jpeg

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_0.1.CR5.6jpp6
- new jpp release

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_0.1.CR5.5jpp6
- new jpp release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.1.CR5.2jpp5
- new version

