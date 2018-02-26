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

Name:           ehcache-parent
Version:        2.2
Release:        alt3_2jpp6
Epoch:          0
Summary:        Ehcache Parent
License:        ASL 2.0
Group:          Development/Java
URL:            http://svn.terracotta.org/svn/ehcache/trunk/pom.xml
Source0:        %{name}-%{version}.tar.bz2
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires:  jpackage-utils
BuildArch:      noarch
Source44: import.info
Provides: ehcache1-parent = %version
Obsoletes: ehcache1-parent < 2.0

%description
Ehcache is a widely used, pure Java, in-process, distributed cache.

%prep
%setup -q

%build

%install

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap net.sf.ehcache ehcache-parent %{version} JPP %{name}

%files
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt3_2jpp6
- new version

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_2jpp6
- resolved conflict with ehcache1

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_2jpp6
- fixed requires on modello plugin

