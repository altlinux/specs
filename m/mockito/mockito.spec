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

%bcond_without repolib
%bcond_without zip


%define ant JAVA_HOME=%{java_home} %{_bindir}/ant17

Name:           mockito
Version:        1.8.5
Release:        alt4_0.1jpp6
Epoch:          0
Summary:        Mock objects library for java
License:        MIT
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://mockito.googlecode.com/svn/tags/1.8.5 mockito-1.8.5 && tar cjf mockito-1.8.5.tar.bz2 mockito-1.8.5
Source0:        mockito-1.8.5.tar.bz2
Requires: junit4
Requires: hamcrest
Requires: objenesis
BuildRequires: ant17 >= 0:1.7.0
BuildRequires: ant17-junit >= 0:1.7.0
BuildRequires: ant17-trax >= 0:1.7.0
# FIXME
#BuildRequires:  aqute-bndlib >= 0:0.0.313
BuildRequires: hamcrest >= 0:1.1
# FIXME: >= 0:1.0
BuildRequires: jarjar
BuildRequires: jaxen >= 0:1.1.1
BuildRequires: junit4 >= 0:4.5
BuildRequires: maven-ant-tasks >= 0:2.0.9
BuildRequires: objectweb-asm >= 0:3.1
BuildRequires: objenesis >= 0:1.0
BuildRequires: pmd >= 0:4.1
# FIXME: needs cglib (repackaged) powermock-1.2.5 fest-1.1 sorcerer
BuildArch:      noarch
Source44: import.info

%description
Mock objects library for java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%if %with zip
%package zip
Summary:     Container for the zipped distribution of %{name}
Group:       Development/Java

%description zip
Container for the zipped distribution of %{name}.
%endif

%prep
%setup -q

%{__rm} ./cglib-and-asm/lib/ant-1.7.0.jar
%{__rm} ./lib/build/asm-3.1.jar
%{__rm} ./lib/build/jarjar-1.0.jar
%{__rm} ./lib/build/jaxen-1.1.1.jar
%{__rm} ./lib/build/maven-ant-tasks-2.0.9.jar
%{__rm} ./lib/build/pmd-4.1.jar

%if 0
%{__rm} ./lib/build/bnd-0.0.313.jar
%{__rm} ./lib/build/sorcerer.jar
%{__rm} ./lib/compile/com.springsource.org.junit-4.5.0.jar
%{__rm} ./lib/run/com.springsource.org.hamcrest.core-1.1.0.jar
%{__rm} ./lib/run/com.springsource.org.objenesis-1.0.0.jar
%{__rm} ./lib/sources/com.springsource.org.hamcrest.core-1.1.0-sources.jar
%{__rm} ./lib/sources/com.springsource.org.objenesis-1.0.0-sources.jar
%endif

%build
export CLASSPATH=$(build-classpath hamcrest/core jaxen jarjar junit4 maven-ant-tasks objectweb-asm/asm objenesis pmd)
export OPT_JAR_LIST=$(%{__cat} %{_sysconfdir}/ant17.d/{junit,trax})
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all

%install

%if %with repolib
export CLASSPATH=$(build-classpath maven-ant-tasks)
export OPT_JAR_LIST=:
%{ant} -Dmaven.repository.dir=%{buildroot}%{_javadir}/repository.jboss.com/maven2-brew release.maven
%endif

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/mockito-all-%{version}.jar %{buildroot}%{_javadir}/%{name}-all-%{version}.jar
%{__cp} -p target/mockito-all-%{version}-sources.jar %{buildroot}%{_javadir}/%{name}-all-sources-%{version}.jar
%{__cp} -p target/mockito-core-%{version}.jar %{buildroot}%{_javadir}/%{name}-core-%{version}.jar
%{__cp} -p target/mockito-core-%{version}-sources.jar %{buildroot}%{_javadir}/%{name}-core-sources-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p target/mockito-all.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-all.pom
%add_to_maven_depmap org.mockito mockito-all %{version} JPP %{name}-all
%{__cp} -p target/mockito-core.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-core.pom
%add_to_maven_depmap org.mockito mockito-core %{version} JPP %{name}-core

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with zip
%{__mkdir_p} %{buildroot}%{_javadir}/jbossas-fordev
%{__cp} -p target/mockito-%{version}.zip %{buildroot}%{_javadir}/jbossas-fordev/mockito-%{version}.zip
%endif

%files
%doc LICENSE NOTICE
%{_javadir}/%{name}-all-%{version}.jar
%{_javadir}/%{name}-all.jar
%{_javadir}/%{name}-all-sources-%{version}.jar
%{_javadir}/%{name}-all-sources.jar
%{_javadir}/%{name}-core-%{version}.jar
%{_javadir}/%{name}-core.jar
%{_javadir}/%{name}-core-sources-%{version}.jar
%{_javadir}/%{name}-core-sources.jar
%{_datadir}/maven2/poms/JPP-%{name}-all.pom
%{_datadir}/maven2/poms/JPP-%{name}-core.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%if %with zip
%files zip
%dir %{_javadir}
%dir %{_javadir}/jbossas-fordev
%{_javadir}/jbossas-fordev/mockito-%{version}.zip
%endif

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt4_0.1jpp6
- fixed build with new testng and xbean

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt3_0.1jpp6
- fixed build

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt2_0.1jpp6
- fixed build

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt1_0.1jpp6
- new version

