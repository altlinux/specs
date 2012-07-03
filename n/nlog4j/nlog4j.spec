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



Summary:        Log4j-replacement with native SLF4J API support
Name:           nlog4j
Version:        1.2.25
Release:        alt1_1jpp5
Epoch:		0
Group:          Development/Java
License:        X11 License
URL:            http://www.slf4j.org/nlog4j/
BuildArch:      noarch
Source0:        http://www.slf4j.org/dist/nlog4j-1.2.25.tar.gz
Source1:        http://repo1.maven.org/maven2/org/slf4j/nlog4j/1.2.25/nlog4j-1.2.25.pom
Patch0:         nlog4j-1.2.21-jmx-Agent.patch

BuildRequires: ant >= 0:1.6.5
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: junit
BuildRequires: geronimo-javamail-1.3.1-api
BuildRequires: geronimo-jaf-1.0.2-api
BuildRequires: geronimo-jms-1.1-api
BuildRequires: mx4j
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
NLOG4J is a production-quality log4j-replacement with direct 
SLF4J API support. NLOG4J is maintained by Ceki Gulcu the founder 
of the log4j project. In a nutshell, NLOG4J can be considered as 
a drop-in replacement for log4j version 1.2.9. 

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

%patch0 -b .orig

%build
export OPT_JAR_LIST="ant/ant-junit junit"
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
ant -Dversion=%{version} -Dbuild.compiler=modern \
    -Djavamail.jar=$(build-classpath geronimo-javamail-1.3.1-api) \
    -Dactivation.jar=$(build-classpath geronimo-jaf-1.0.2-api) \
    -Djms.jar=$(build-classpath geronimo-jms-1.1-api) \
    -Djmx.jar=$(build-classpath mx4j/mx4j) \
    -Djmx-extra.jar=$(build-classpath mx4j/mx4j-tools) \
	nlog4j.jar javadoc

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
pushd $RPM_BUILD_ROOT%{_javadir}
   ln -fs %{name}-%{version}.jar %{name}.jar
popd

%add_to_maven_depmap org.slf4j %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/

%files
%doc LICENSE.txt
%{_javadir}/*
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.25-alt1_1jpp5
- new jpp release

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.21-alt1_1jpp1.7
- converted from JPackage by jppimport script

