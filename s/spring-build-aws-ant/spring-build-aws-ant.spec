BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 3.0.4
%define name spring-build-aws-ant
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with xmlgraphics
%bcond_with xmlgraphics


%define upstream_tag .RELEASE
%define upstream_version %{version}%{?upstream_tag}

Name:           spring-build-aws-ant
Summary:        Spring Build AWS Ant
Version:        3.0.4
Release:        alt1_1jpp6
Epoch:          0
License:        ASL 2.0
Group:          Development/Java
URL:            http://www.springframework.org/
# git clone git://git.springsource.org/spring-build/aws-ant.git
# mkdir spring-build-aws-ant-3.0.4.RELEASE
# cd aws-ant
# git archive 3.0.4.RELEASE | tar -x -C ../spring-build-aws-ant-3.0.4.RELEASE
# cd ..
# tar czf ../SOURCES/spring-build-aws-ant-3.0.4.RELEASE.tgz spring-build-aws-ant-3.0.4.RELEASE/

Source0:        %{name}-%{upstream_version}.tgz
Source1:        spring-build.tgz
Source2:        spring-build-aws-ant-local-repository.tgz
Source3:        http://repository.springsource.com/maven/bundles/release/org/springframework/build/org.springframework.build.aws.ant/3.0.4.RELEASE/org.springframework.build.aws.ant-3.0.4.RELEASE.pom
Patch0:         spring-build-standard-artifact.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1

BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-httpclient
BuildRequires:  apache-commons-logging
BuildRequires:  apache-ivy
BuildRequires:  ecj3
BuildRequires:  jets3t


Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
Spring is a layered Java/J2EE application framework, 
based on code published in Expert One-on-One J2EE 
Design and Development by Rod Johnson (Wrox, 2002). 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package devel
Summary:        Source jars for %{name}
Group:          Development/Java

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{upstream_version}
tar xzf %{SOURCE1}
tar xzf %{SOURCE2}
chmod -R go=u-w *

rm local-repository/org.apache.ant/com.springsource.org.apache.tools.ant/1.7.0/com.springsource.org.apache.tools.ant-1.7.0.jar
ln -sf $(build-classpath ant) local-repository/org.apache.ant/com.springsource.org.apache.tools.ant/1.7.0/com.springsource.org.apache.tools.ant-1.7.0.jar
rm local-repository/org.apache.commons/com.springsource.org.apache.commons.codec/1.3.0/com.springsource.org.apache.commons.codec-1.3.0.jar
ln -sf $(build-classpath commons-codec) local-repository/org.apache.commons/com.springsource.org.apache.commons.codec/1.3.0/com.springsource.org.apache.commons.codec-1.3.0.jar
rm local-repository/org.apache.commons/com.springsource.org.apache.commons.httpclient/3.1.0/com.springsource.org.apache.commons.httpclient-3.1.0.jar
ln -sf $(build-classpath commons-httpclient) local-repository/org.apache.commons/com.springsource.org.apache.commons.httpclient/3.1.0/com.springsource.org.apache.commons.httpclient-3.1.0.jar
rm local-repository/org.apache.commons/com.springsource.org.apache.commons.logging/1.1.1/com.springsource.org.apache.commons.logging-1.1.1.jar
ln -sf $(build-classpath commons-logging) local-repository/org.apache.commons/com.springsource.org.apache.commons.logging/1.1.1/com.springsource.org.apache.commons.logging-1.1.1.jar
rm local-repository/org.eclipse.jdt/com.springsource.org.eclipse.jdt.core.compiler.batch/3.3.0/com.springsource.org.eclipse.jdt.core.compiler.batch-3.3.0.jar
ln -sf $(build-classpath ecj3) local-repository/org.eclipse.jdt/com.springsource.org.eclipse.jdt.core.compiler.batch/3.3.0/com.springsource.org.eclipse.jdt.core.compiler.batch-3.3.0.jar
rm local-repository/org.jets3t/com.springsource.org.jets3t/0.6.1/com.springsource.org.jets3t-0.6.1.jar
ln -sf $(build-classpath jets3t/jets3t) local-repository/org.jets3t/com.springsource.org.jets3t/0.6.1/com.springsource.org.jets3t-0.6.1.jar
#rm local-repository/org.springframework.build/org.springframework.build.ant/1.1.0.RELEASE/org.springframework.build.ant-1.1.0.RELEASE.jar

%build
export CLASSPATH=
CLASSPATH="$CLASSPATH:../spring-build/lib/ivy/ivy.jar"
CLASSPATH="$CLASSPATH:../spring-build/lib/ivy/jets3t.jar"
CLASSPATH="$CLASSPATH:../spring-build/lib/ivy/commons-codec.jar"
CLASSPATH="$CLASSPATH:../spring-build/lib/ivy/commons-httpclient.jar"
CLASSPATH="$CLASSPATH:../spring-build/lib/ivy/commons-logging.jar"
CLASSPATH="$CLASSPATH:../spring-build/lib/ivy/org.springframework.build.aws.ivy.jar"


export ANT_OPTS="-Xmx768m -XX:MaxPermSize=128m"
export IVY_CACHE=$(pwd)/ivy-cache/repository
export IVY_LOCAL=$(pwd)/local-repository
cd org.springframework.build.aws.ant
%{ant} -Dlocal.repo.dir=${IVY_LOCAL} -Dtest.halt=false -Dbuild.sysclasspath=first -Djava.awt.headless=true jar javadoc-all

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/spring-build

install -m 644 org.springframework.build.aws.ant/target/artifacts/org.springframework.build.aws.ant.jar \
               $RPM_BUILD_ROOT%{_javadir}/spring-build/org.springframework.build.aws.ant-%{version}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc
install -m 644 org.springframework.build.aws.ant/target/artifacts/ivy.xml \
               $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/org.springframework.build.aws.ant-ivy.xml

mkdir -p $RPM_BUILD_ROOT%{_javadir}/spring-build-sources
install -m 644 org.springframework.build.aws.ant/target/artifacts/org.springframework.build.aws.ant-sources.jar \
               $RPM_BUILD_ROOT%{_javadir}/spring-build-sources/org.springframework.build.aws.ant-sources-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/spring-build && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/spring-build-sources && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%add_to_maven_depmap org.springframework.build org.springframework.build.aws.ant %{upstream_version} JPP/spring-build org.springframework.build.aws.ant

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.spring-build-org.springframework.build.aws.ant.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr org.springframework.build.aws.ant/target/javadoc-all/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%dir %{_javadir}/spring-build
%dir %{_javadir}/spring-build/*.jar
%dir %{_datadir}/%{name}-%{version}/etc
%{_datadir}/%{name}-%{version}/etc/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files devel
%dir %{_javadir}/spring-build-sources
%{_javadir}/spring-build-sources/*.jar

%changelog
* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt1_1jpp6
- new version

