BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.1.6
%define name jboss-ejb3
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

%define version_full %{version}

Name:           jboss-ejb3
Version:        1.1.6
Release:        alt1_2jpp6
Epoch:          0
Summary:        JBoss EJB3 Project POM
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/ejb3/
# svn -q export http://anonsvn.jboss.org/repos/jbossas/projects/ejb3/tags/jboss-ejb3-1.1.6/ && tar cjf jboss-ejb3-1.1.6.tar.bz2 jboss-ejb3-1.1.6
Source0:        jboss-ejb3-1.1.6.tar.bz2
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires:  jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
Defines the dependency chain configuration of the JBoss EJB3 Project.

%prep
%setup -q

%build

%install

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss.ejb3 jboss-ejb3 %{version_full} JPP %{name}

%files
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_2jpp6
- new jpp release

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_1jpp6
- new version

