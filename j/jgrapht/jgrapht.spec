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


Name:           jgrapht
Version:        0.8.2
Release:        alt1_1jpp6
Epoch:          0
Summary:        Java graph library
License:        LGPLv2+
URL:            http://jgrapht.sourceforge.net/
Group:          Development/Java
Source0:        http://downloads.sourceforge.net/jgrapht/jgrapht-0.8.2.tar.gz
Patch0:         jgrapht-0.8.1-build.patch
Requires: jgraph
Requires: jpackage-utils
Requires: tggraphlayout
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: jgraph
BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: tggraphlayout
BuildRequires: xmlunit
BuildArch:      noarch
Source44: import.info

%description
JGraphT is a free Java graph library that provides mathematical graph-theory
objects and algorithms. JGraphT supports various types of graphs including:

    * directed and undirected graphs.
    * graphs with weighted / unweighted / labeled or any user-defined edges.
    * various edge multiplicity options, including: simple-graphs, multigraphs,
      pseudographs.
    * unmodifiable graphs - allow modules to provide "read-only" access to
      internal graphs.
    * listenable graphs - allow external listeners to track modification
      events.
    * subgraphs graphs that are auto-updating subgraph views on other graphs.
    * all compositions of above graphs.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p0 -b .sav0
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__rm} -r javadoc

%build
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/junit`"
export CLASSPATH=
%{ant} -Djunit.jar=$(build-classpath junit) \
       -Dxmlunit.jar=$(build-classpath xmlunit) \
       -Djgraph.jar=$(build-classpath jgraph) \
       -Dtouchgraph.jar=$(build-classpath tggraphlayout)

%install
%{__tar} xf jgrapht-%{version}-local.tar.gz

pushd jgrapht-%{version}-local

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__install} -p -m 0644 jgrapht.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

popd

%files
%doc jgrapht-%{version}-local/license-LGPL.txt jgrapht-%{version}-local/README.html
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.8.2-alt1_1jpp6
- new version

