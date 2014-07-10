BuildRequires: /proc
BuildRequires: jpackage-compat
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



Name:           ecj3
Version:        3.7
Release:        alt3_1jpp6
Epoch:          1
Summary:        Eclipse Compiler for Java
Group:          Development/Java
License:        EPL
URL:            http://www.eclipse.org/
Source0:        http://mirrors.ibiblio.org/pub/mirrors/eclipse/eclipse/downloads/drops/R-3.7-201106131736/ecjsrc-3.7.jar
Source1:        core-3.7.pom
BuildRequires:  ant
BuildRequires:  jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
Eclipse Compiler for Java.

%prep
%setup -q -c

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 

%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p ecj.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%{__mkdir_p} %{buildroot}%{_mavenpomdir}/
%{__cp} -p %{SOURCE1} %{buildroot}%_mavenpomdir/JPP-%{name}.pom
%add_to_maven_depmap org.eclipse.jdt core %{version} JPP %{name}


%files
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.7-alt3_1jpp6
- fixed build

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.7-alt2_1jpp6
- fixed build with maven3

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.7-alt1_1jpp6
- new jpp relase

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.6-alt1_2jpp6
- new version

