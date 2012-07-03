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


Name:           tggraphlayout
Version:        1.22
Release:        alt1_1jpp6
Epoch:          0
Summary:        Set of interfaces for graph visualization
License:        ASL 2.0
Group:          Development/Java
URL:            http://touchgraph.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/touchgraph/TGGL_122_jre11.zip
Requires: jpackage-utils
BuildRequires: jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
TouchGraph provides a set of interfaces for graph visualization using
force-based layout and focus+context techniques.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n TGGraphLayout
%{__mkdir_p} build
%{__mkdir_p} javadoc

%build
export CLASSPATH=
%{__mkdir_p} build
%{javac} -d build `%{_bindir}/find -name "*.java"`
pushd build
%{jar} cf %{name}.jar `%{_bindir}/find -name "*.class"`
popd
%{javadoc} -d javadoc `%{_bindir}/find -name "*.java"`

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__install} -p -m 0644 build/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/TGGraphLayout-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/TGGraphLayout-%{version}
%{__ln_s} TGGraphLayout-%{version} %{buildroot}%{_javadocdir}/TGGraphLayout

%files
%doc TG-APACHE-LICENSE.txt TGGL\ ReleaseNotes.txt TGGraphLayout.html 
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/TGGraphLayout-%{version}.jar
%{_javadir}/TGGraphLayout.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/TGGraphLayout-%{version}
%{_javadocdir}/TGGraphLayout

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.22-alt1_1jpp6
- new version

