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


Name:           biojava
Version:        1.7.1
Release:        alt1_1jpp6
Epoch:          0
Summary:        Java framework for processing biological data
License:        LGPLv2+
Group:          Development/Java
URL:            http://biojava.org/
Source0:        http://www.biojava.org/download/bj171/src/biojava-1.7.1-src.jar
Patch0:         biojava-1.7-javadoc.patch
Requires: bytecode
Requires: jakarta-commons-cli
Requires: commons-collections
Requires: commons-dbcp
Requires: commons-pool
Requires: hsqldb
Requires: jgrapht
Requires: jpackage-utils
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: bytecode
BuildRequires: jakarta-commons-cli
BuildRequires: commons-collections >= 0:2.1
BuildRequires: commons-dbcp >= 0:1.1
BuildRequires: commons-pool >= 0:1.1
BuildRequires: hsqldb
BuildRequires: java-javadoc
BuildRequires: jgrapht
BuildRequires: jpackage-utils
BuildRequires: junit4 >= 0:4.4
BuildArch:      noarch
Source44: import.info

%description
BioJava is an open-source project dedicated to providing a Java framework for
processing biological data. It provides analytical and statistical routines,
parsers for common file formats and allows the manipulation of sequences and 3D
structures. The goal of the biojava project is to facilitate rapid application
development for bioinformatics. 

%package apps
Summary:        Apps for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description apps
Apps for %{name}.

%package demos
Summary:        Demos for %{name}
Group:          Development/Documentation
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demos
Demos for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package apps-javadoc
Summary:        Javadoc for %{name}-apps
Group:          Development/Documentation

%description apps-javadoc
Javadoc for %{name}-apps.

%package demos-javadoc
Summary:        Javadoc for %{name}-demos
Group:          Development/Documentation

%description demos-javadoc
Javadoc for %{name}-demos.

%prep
%setup -q -c
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}

pushd biojava-%{version}-src
%patch0 -p0 -b .sav0
%{__ln_s} $(build-classpath bytecode) bytecode.jar
%{__ln_s} $(build-classpath commons-cli) commons-cli.jar
%{__ln_s} $(build-classpath commons-collections) commons-collections-2.1.jar
%{__ln_s} $(build-classpath commons-dbcp) commons-dbcp-1.1.jar
%{__ln_s} $(build-classpath commons-pool) commons-pool-1.1.jar
%{__ln_s} $(build-classpath hsqldb) hsqldb.jar
%{__ln_s} $(build-classpath jgrapht) jgrapht-jdk1.5.jar
%{__ln_s} $(build-classpath junit4) junit-4.4.jar
popd

%build
pushd biojava-%{version}-src
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
export CLASSPATH=
%{ant} dist
popd

%install

pushd biojava-%{version}-src/dist/biojava-%{version}
# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__install} -p -m 0644 biojava-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__install} -p -m 0644 apps-%{version}.jar %{buildroot}%{_javadir}/%{name}-apps-%{version}.jar
%{__install} -p -m 0644 demos-%{version}.jar %{buildroot}%{_javadir}/%{name}-demos-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr doc/biojava/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-apps-%{version}
%{__cp} -pr doc/apps/* %{buildroot}%{_javadocdir}/%{name}-apps-%{version}
%{__ln_s} %{name}-apps-%{version} %{buildroot}%{_javadocdir}/%{name}-apps
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-demos-%{version}
%{__cp} -pr doc/demos/* %{buildroot}%{_javadocdir}/%{name}-demos-%{version}
%{__ln_s} %{name}-demos-%{version} %{buildroot}%{_javadocdir}/%{name}-demos
popd

%files
%doc
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files apps
%{_javadir}/%{name}-apps-%{version}.jar
%{_javadir}/%{name}-apps.jar

%files demos
%{_javadir}/%{name}-demos-%{version}.jar
%{_javadir}/%{name}-demos.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files apps-javadoc
%{_javadocdir}/%{name}-apps-%{version}
%{_javadocdir}/%{name}-apps

%files demos-javadoc
%{_javadocdir}/%{name}-demos-%{version}
%{_javadocdir}/%{name}-demos

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_1jpp6
- new version

