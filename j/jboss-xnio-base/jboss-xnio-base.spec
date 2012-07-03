Packager: Igor Vlasenko <viy@altlinux.ru>
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
%define namedversion %{version}.%{reltag}

Name:           jboss-xnio-base
Version:        1.2.0
Release:        alt1_2jpp6
Epoch:          0
Summary:        XNIO low level IO layer
Group:          Development/Java
License:        LGPLv2+
URL:            http://jboss.org/xnio/
# svn export http://anonsvn.jboss.org/repos/xnio/xnio-base/tags/1.2.0.GA/ jboss-xnio-base-1.2.0.GA
Source0:        jboss-xnio-base-1.2.0.GA.tar.gz
Source1:        http://repository.jboss.com/maven2/org/jboss/xnio/xnio-api/1.2.0.GA/xnio-api-1.2.0.GA.pom
Source2:        http://repository.jboss.com/maven2/org/jboss/xnio/xnio-nio/1.2.0.GA/xnio-nio-1.2.0.GA.pom
Patch0:         jboss-xnio-base-build.patch
Patch1:         jboss-xnio-base-build-properties.patch
Patch2:         jboss-xnio-base-policy.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: jaxb_2_1_api
Requires: jboss-common-core
Requires: jboss-microcontainer2
Requires: jbossxb2
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: junit
BuildRequires: jaxb_2_1_api
BuildRequires: jboss-common-core
BuildRequires: jboss-microcontainer2
BuildRequires: jbossxb2
BuildArch:      noarch

%description
XNIO is a simplified low-level I/O layer which can be used 
anywhere you are using NIO today. It frees you from the 
hassle of dealing with Selectors and the lack of NIO support 
for multicast sockets and non-socket I/O such as serial 
ports, while still maintaining all the capabilities present 
in NIO. Also, XNIO vastly simplifies implementation of 
channels, opening the door to supporting higer-level 
transport concepts (like SSL or virtual channels) with the 
same simple API.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

mkdir -p .jboss/repository/sun-jaxb/2.0.5/lib/
cp -p $(build-classpath jaxb_2_1_api) .jboss/repository/sun-jaxb/2.0.5/lib/jaxb-api.jar

mkdir -p .jboss/repository/jboss-common-core/2.2.0.GA/lib/
cp $(build-classpath jboss-common-core) .jboss/repository/jboss-common-core/2.2.0.GA/lib/jboss-common-core-2.2.0.GA.jar

mkdir -p .jboss/repository/jboss-microcontainer/2.0.0.Beta11/lib/
cp $(build-classpath jboss-microcontainer2/jboss-kernel) .jboss/repository/jboss-microcontainer/2.0.0.Beta11/lib/jboss-kernel.jar

mkdir -p .jboss/repository/jbossxb/2.0.0.CR5/lib/
cp $(build-classpath jbossxb2) .jboss/repository/jbossxb/2.0.0.CR5/lib/jboss-xml-binding.jar

mkdir -p .jboss/repository/junit/3.8.1/lib/
cp $(build-classpath junit) .jboss/repository/junit/3.8.1/lib/junit.jar

%build
export CLASSPATH=
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/junit`
%{ant} all jar test javadoc

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}/jboss-xnio
install -p -m 644 xnio-api.jar %{buildroot}%{_javadir}/jboss-xnio/xnio-api-%{version}.jar
install -p -m 644 xnio-nio.jar %{buildroot}%{_javadir}/jboss-xnio/xnio-nio-%{version}.jar
(cd %{buildroot}%{_javadir}/jboss-xnio && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr docs/target/main/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.jboss-xnio-xnio-api.pom
%add_to_maven_depmap org.jboss.xnio xnio-api %{namedversion} JPP/jboss-xnio xnio-api
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP.jboss-xnio-xnio-nio.pom
%add_to_maven_depmap org.jboss.xnio xnio-nio %{namedversion} JPP/jboss-xnio xnio-nio

%files
%dir %{_javadir}/jboss-xnio
%{_javadir}/jboss-xnio/xnio-api-%{version}.jar
%{_javadir}/jboss-xnio/xnio-api.jar
%{_javadir}/jboss-xnio/xnio-nio-%{version}.jar
%{_javadir}/jboss-xnio/xnio-nio.jar
%{_datadir}/maven2/poms/JPP.jboss-xnio-xnio-api.pom
%{_datadir}/maven2/poms/JPP.jboss-xnio-xnio-nio.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_2jpp6
- new version

