BuildRequires: /proc
BuildRequires: jpackage-core
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

#def_with bootstrap
%bcond_with bootstrap


Name:           buildmagic
Version:        2.1.0
Release:        alt2_2jpp6
Epoch:          0
Summary:        JBoss buildmagic tasks module
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn export -q http://anonsvn.jboss.org/repos/labs/labs/jbossbuild/buildmagic/tags/buildmagic-2.1.0 && tar cjf buildmagic-2.1.0.tar.bz2 buildmagic-2.1.0
Source0:        buildmagic-2.1.0.tar.bz2
Patch0:         buildmagic-2.1.0-ivy-offline.patch
Provides:       %{name}-tasks = %{epoch}:%{version}-%{release}
#Requires: ant17 
Requires: bsf
Requires: jboss-common-core
BuildRequires: ant17 
BuildRequires: ant17-junit
BuildRequires: ant17-nodeps
BuildRequires: apache-ivy
BuildRequires: bsf
%if %without bootstrap
BuildRequires: buildmagic
%endif
BuildRequires: jboss-common-core
BuildRequires: jpackage-utils
BuildRequires: junit
BuildArch:      noarch
Source44: import.info

%description
Buildmagic tasks module of JBoss.

%prep
%setup -q
%patch0 -p1
%{_bindir}/find -type f -name "*.jar" | xargs -t %{__rm}
%{__rm} -r tools/ant
%{__rm} -r tools/apache-ivy
%{__rm} tasks/src/it/simple-external-build/module1/src/main/org/jboss/buildmagic/test/HelloModule1.java
%{__rm} tasks/src/it/simple-external-build/module2/src/main/org/jboss/buildmagic/test/HelloModule2.java
%{__rm} tasks/src/test/org/jboss/tools/buildmagic/task/ResolvePropertiesTestCase.java

# ant 1.8 support hack
for i in `find . -name buildmagic.ent`; do sed -i 's,fail unless="buildmagic.ant.compatible",fail if="never",' $i; done


%build
export OPT_JAR_LIST=$(%{__cat} %{_sysconfdir}/ant17.d/{junit,nodeps})
export CLASSPATH=$(build-classpath apache-ivy jboss-common-core)
%if %with bootstrap
pushd tasks
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
        -Divy.default.ivy.user.dir=$(pwd) \
        -Djavac.optimize=off \
        -Djavac.source=1.4 \
        -Djavac.target=1.5 \
        -Djavac.debug=off \
        -Djavac.depend=no \
        -Djavac.verbose=no \
        -Djavac.deprecation=on \
        -Djavac.include.ant.runtime=yes \
        -Djavac.include.java.runtime=no \
        -Djavac.fail.onerror=true \
        -Djavac.includes="**/*.java" \
        -Dsource.java=src \
        -Dsource.etc=src/etc \
        -Dsource.resources=src/resources \
        -Dsource.test=src/test \
        -Dbuild.classes=common/output/classes \
        -Dbuild.gen.classes=common/output/gen/classes \
        -Dbuild.gen-src=common/output/gen/classes \
        -Dbuild.etc=common/output/etc \
        -Dbuild.resources=common/output/resources \
        -Dbuild.lib=common/output/lib \
        -Dbuild.test=common/output/test \
        -Dbuild.reports=common/output/reports \
        -Dmodule.source=src \
        -Dmodule.output=common/output \
        -Dmodule.tools=tools \
        -Dmodule.thirdparty=thirdparty \
        -Dinit.disable=true \
        -Ddependency-manager.offline=true \
        -Dbuild.sysclasspath=first \
        output
popd
%endif

%if %with bootstrap
export CLASSPATH=${CLASSPATH}:$(pwd)/tasks/common/output/lib/buildmagic-tasks.jar
%else
export CLASSPATH=${CLASSPATH}:$(build-classpath buildmagic-tasks)
%endif
pushd build
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dant.version="`%{_bindir}/ant -version`" -Dbuild.sysclasspath=first -Divy.default.ivy.user.dir=$(pwd)
popd

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p tasks/output/lib/buildmagic-tasks.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-tasks-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-tasks-%{version}.jar
%{_javadir}/%{name}-tasks.jar

%changelog
* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt2_2jpp6
- build with ant17

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_2jpp6
- new jpp release

* Tue Mar 17 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_0.20030518.2jpp5
- first build (with bootstrap)

