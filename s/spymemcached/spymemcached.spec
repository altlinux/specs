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


Name:           spymemcached
Version:        2.5
Release:        alt1_1jpp6
Epoch:          0
Summary:        Java client for memcached
License:        BSD
URL:            http://code.google.com/p/spymemcached
Group:          Development/Java
# git clone https://github.com/dustin/java-memcached-client.git
# cd java-memcached-client.git && git checkout 2.5
# cd .. && mv java-memcached-client.git spymemcached-2.5 && tar cjf spymemcached-2.5.tar.bz2 spymemcached-2.5
Source0:        spymemcached-2.5.tar.bz2
Source1:        spymemcached-manifest.mf
Source2:        http://bleu.west.spy.net/~dustin/m2repo/spy/memcached/2.5/memcached-2.5.pom
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
# FIXME: (dwalluck): really BuildRequires: apache-buildr
BuildRequires: jpackage-utils
%if 0
BuildRequires: junit4
%endif
BuildRequires: log4j
%if 0
BuildRequires: jmock
%endif
BuildArch:      noarch
Source44: import.info

%description
Java client for memcached.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%{__mkdir_p} classes
%{__mkdir_p} javadoc

%build
export OPT_JAR_LIST=:
%if 0
export CLASSPATH=$(%{_bindir}/build-classpath jmock junit4 log4j); javac `find -type f -name "*.java"`
%else
export CLASSPATH=$(%{_bindir}/build-classpath log4j)
%endif
pushd src/main
%{javac} -d ../../classes `%{_bindir}/find -type f -name "*.java"`
%{javadoc} -d ../../javadoc `%{_bindir}/find -type f -name "*.java"`
popd
pushd classes
%{jar} cfm ../memcached-%{version}.jar %{SOURCE1} *
popd

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p memcached-%{version}.jar %{buildroot}%{_javadir}/memcached-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-memcached.pom
%add_to_maven_depmap spy memcached %{version} JPP memcached

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/memcached-%{version}
%{__cp} -pr javadoc/* %{buildroot}%{_javadocdir}/memcached-%{version}
%{__ln_s} memcached-%{version} %{buildroot}%{_javadocdir}/memcached

%files
%doc LICENSE.txt
%{_javadir}*/memcached-%{version}.jar
%{_javadir}*/memcached.jar
%{_datadir}/maven2/poms/JPP-memcached.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/memcached-%{version}
%{_javadocdir}/memcached

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_1jpp6
- new version

