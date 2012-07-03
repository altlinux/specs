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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

Name:           htmlunit-core-js
Version:        2.8
Release:        alt1_3jpp6
Epoch:          0
Summary:        HtmlUnit adaptation of Mozilla Rhino Javascript engine for Java
License:        MPL 1.1
Group:          Development/Java
URL:            http://htmlunit.svn.sourceforge.net/
# svn -q export https://htmlunit.svn.sourceforge.net/svnroot/htmlunit/tags/core-js-2.8/ htmlunit-core-js-2.8 && tar cjf htmlunit-core-js-2.8.tar.bz2 htmlunit-core-js-2.8/
# Exported revision 6155.
Source0:        htmlunit-core-js-2.8.tar.bz2
Patch0:         htmlunit-core-js-build.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
BuildRequires: ant
BuildRequires: jpackage-utils
BuildRequires: junit4
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch: noarch
%endif
Source44: import.info

%description
HtmlUnit uses Rhino as its core JavaScript engine. HtmlUnit-core-js
is a fork of the Mozilla Rhino JavaScript engine where what is
important is to simulate browser's behavior.

%prep
%setup -q
%patch0 -p0 -b .sav0
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%build
export OPT_JAR_LIST=:
export CLASSPATH=
%{ant} -Djunit.jar=$(%{_bindir}/build-classpath junit4) jar-all

%install

%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/htmlunit-core-js-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap net.sourceforge.htmlunit htmlunit-core-js %{version} JPP %{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt MPL-1.1.html rhinoDiff.txt 
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root,) %{_libdir}/gcj/%{name}/%{name}-%{version}.jar.db
%attr(-,root,root,) %{_libdir}/gcj/%{name}/%{name}-%{version}.jar.so
%endif

%changelog
* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_3jpp6
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_2jpp6
- new version

