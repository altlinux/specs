BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.0.4
%define name jboss-ejb3-build
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

%define namedversion %{version}

Name:           jboss-ejb3-build
Version:        1.0.4
Release:        alt2_6jpp6
Epoch:          0
Summary:        JBoss EJB3 build pom
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/jbossas/projects/ejb3/tags/jboss-ejb3-build-1.0.4/ && tar cjf jboss-ejb3-build-1.0.4.tar.bz2 jboss-ejb3-build-1.0.4
Source0:        jboss-ejb3-build-1.0.4.tar.bz2
Patch0:         jboss-ejb3-build-pom.patch
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       jpackage-utils >= 0:1.7.3
BuildRequires:  jpackage-utils >= 0:1.7.3
Source44: import.info

%description
JBoss EJB3 build pom.

%prep
%setup -q 
%patch0

%build

%install

# pom
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss.ejb3 jboss-ejb3-build %{version} JPP %{name}

%files
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt2_6jpp6
- manually fixed patch0 to set correct version for maven3

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_6jpp6
- new jpp release

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_4jpp6
- new version

