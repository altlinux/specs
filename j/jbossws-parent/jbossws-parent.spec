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
#

%define version_maj 1
%define version_min 0
%define version_rev 2
%define version_tag GA
%define version_full %{version_maj}.%{version_min}.%{version_rev}.%{version_tag}
 
Name:           jbossws-parent
Version:        %{version_maj}.%{version_min}.%{version_rev}
Release:	alt2_4jpp6
Epoch:          0
Summary:        JBoss Web Services (parent)
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com/jbossws/
# svn export http://anonsvn.jboss.org/repos/jbossws/maven/parent/tags/jbossws-parent-1.0.2.GA/ jbossws-parent-1.0.2
# tar cjf jbossws-parent-1.0.2.tar.bz2 jbossws-parent-1.0.2
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-pom.patch

Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       maven-surefire-report-maven-plugin
Requires:       maven2
Requires:       maven2-plugin-compiler
Requires:       maven2-plugin-jar
Requires:       maven2-plugin-source
Requires:       maven-plugin-build-helper
BuildRequires:  jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
JBossWS Parent.

%prep
%setup -q
%patch0

%build

%install

%add_to_maven_depmap org.jboss.ws jbossws-parent %{version_full} JPP %{name}

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

%files
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_4jpp6
- use maven-plugin-build-helper

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_4jpp6
- new jpp release

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_3jpp6
- new jpp release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_1jpp5
- new jpp release

