Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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

%bcond_with jdk14


Name:           jbossretro
Version:        1.0.0
Release:	alt2_4jpp5
Epoch:          0
Summary:        JBoss Retro
License:        LGPLv2+
Group:          Development/Java
URL:            http://wiki.jboss.org/wiki/JBossRetro
# cvs -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r JBossRetro_1_0_0_GA jbossretro
# tar czf jbossretro-1.0.0.GA-src.tar.gz jbossretro
Source0:        jbossretro-1.0.0.GA-src.tar.gz
BuildArch:      noarch
Requires: jpackage-utils >= 0:1.6
Requires: backport-util-concurrent >= 0:2.1
Requires: javassist
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
%if %with jdk14
%endif
BuildRequires: buildmagic
BuildRequires: backport-util-concurrent >= 0:2.1
BuildRequires: javassist
BuildRequires: junit

%description
We want to develop software that can take of advantage of JDK5 
features while still being able to run the software in JDK1.4.

The Solution:

* Weave the classes such that the bytecode is 48.0 version compatible
* Replace invocations to JDK5 api with code that does the same thing.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}.GA-src
chmod -R go=u-w *
find -type f -name '*.jar' | xargs rm

#mkdir -p tools/lib
#pushd tools/lib
#ln -sf $(build-classpath jboss4/jboss4-buildmagic-tasks) buildmagic-tasks.jar
#popd

pushd thirdparty
#BUILD/jbossretro-1.0.0.GA-src/thirdparty/ant/lib:
pushd ant/lib
ln -sf $(build-classpath ant) .
popd

#BUILD/jbossretro-1.0.0.GA-src/thirdparty/concurrent/lib:
pushd concurrent/lib
ln -sf $(build-classpath backport-util-concurrent) jboss-backport-concurrent.jar
popd

#BUILD/jbossretro-1.0.0.GA-src/thirdparty/javassist/lib:
pushd javassist/lib
ln -sf $(build-classpath javassist) .
popd

#BUILD/jbossretro-1.0.0.GA-src/thirdparty/junit/lib:
pushd junit/lib
ln -sf $(build-classpath junit) .
popd

popd

mkdir -p output/api

%build
ant \
        -Djdk14.home=%{_jvmdir}/java-1.4.2 \
        -Djdk15.home=%{_jvmdir}/java-1.5.0 \
        dist
%if %with jdk14
export JAVA_HOME=%{_jvmdir}/java-1.4.2
ant \
        -Djdk14.home=%{_jvmdir}/java-1.4.2 \
        -Djdk15.home=%{_jvmdir}/java-1.5.0 \
        tests
%endif

(cd src/main; %{javadoc} -d ../../output/api `find -type f -name '*.java'`)

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}

install -p -m 0644 output/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -p -m 0644 output/lib/%{name}-rt.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-rt-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc *.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-rt-%{version}.jar
%{_javadir}/%{name}-rt.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt2_4jpp5
- selected java5 compiler explicitly

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_4jpp5
- new version

