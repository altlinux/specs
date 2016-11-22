# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Copyright (c) 2000-2005, JPackage Project
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

%global parent plexus
%global subname ant-factory

Name:           %{parent}-%{subname}
Version:        1.0
Release:        alt5_0.17.a2.2jpp8
Epoch:          0
Summary:        Plexus Ant component factory
# Email from copyright holder confirms license.
# See plexus-ant-factory_license_and_copyright.txt
License:        ASL 2.0
Group:          Development/Java
URL:            http://plexus.codehaus.org/
Source0:        %{name}-src.tar.bz2
# svn export http://svn.codehaus.org/plexus/tags/plexus-ant-factory-1.0-alpha-2.1/ plexus-ant-factory/
# tar cjf plexus-ant-factory-src.tar.bz2 plexus-ant-factory/
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  maven-local

BuildRequires:  ant
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-utils
BuildRequires:  plexus-component-factories-pom
Source44: import.info


%description
Ant component class creator for Plexus.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}
cp %{SOURCE1} LICENSE


%build
%mvn_file  : %{parent}/%{subname}
%mvn_build

%install
%mvn_install


%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files -f .mfiles
%doc LICENSE
%dir %{_javadir}/plexus

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.17.a2.2jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.16.a2.2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.13.a2.1jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.10.a2.1jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.8.a2.1.2jpp7
- rebuild with maven-local

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.8.a2.1.2jpp7
- fc update

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a2.1.1jpp6
- fixed build with new plexus-containers

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a2.1.1jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a1.4jpp5
- new jpackage release

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a1.2jpp1.7
- build with maven2

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a1.2jpp1.7
- converted from JPackage by jppimport script

