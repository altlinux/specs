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

%define _with_repolib 1
# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define reltag %{nil}
%define version_full %{version}

%define gcj_support 0


Name:           jbossbuild
Version:        1.1.6
Release:        alt1_1jpp6
Epoch:          0
Summary:        JBoss Build
License:        LGPLv2+
Group:          Development/Java
URL:            http://wiki.jboss.org/wiki/JBossBuild
# cvs -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r JBossBuild_1_1_6 -d jbossbuild-1.1.6 jbossbuild
# tar cjf jbossbuild-1.1.6.tar.bz2 jbossbuild-1.1.6
Source0:        jbossbuild-%{version_full}.tar.bz2
# Based on <https://jira.jboss.org/jira/secure/attachment/12317181/jboss-build-ant17.diff.gz>
# See <https://jira.jboss.org/jira/browse/JBBUILD-432>
Patch0:         jbossbuild-ant17.patch
Requires: junit
BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: junit
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
JBoss Build.

%prep
%setup -q -n jbossbuild-%{version_full}
find -type f -name '*.jar' | xargs -t %{__rm}
%patch0 -p1 -b .ant

%build
export CLASSPATH=$(build-classpath ant junit)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}/jboss
%{__cp} -a output/lib/jbossbuild.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%changelog
* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_1jpp6
- new version

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt1_1jpp5
- new version

