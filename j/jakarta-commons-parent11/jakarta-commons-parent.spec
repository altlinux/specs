Patch33: commons-parent-11-alt-kill-commons-build-plugin.patch
%define oldname jakarta-commons-parent
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

%define short_name commons-parent

Name:           jakarta-commons-parent11
Version:        11
Release:	alt5_3jpp6
Epoch:          0
Summary:        Commons Parent
License:        LGPLv2+
Group:          Development/Java
URL:            http://svn.apache.org/repos/asf/commons/proper/commons-parent
# svn -q export http://svn.apache.org/repos/asf/commons/proper/commons-parent/tags/commons-parent-11 && tar cjf commons-parent-11.tar.bz2 commons-parent-11
Source0:        %{short_name}-%{version}.tar.bz2
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
#Requires: commons-build-plugin >= 0:1.1
#Requires: felix-maven2 >= 0:1.0.2
Requires: maven2-plugin-antrun
Requires: maven2-plugin-assembly
Requires: maven2-plugin-compiler
Requires: maven2-plugin-gpg
Requires: maven2-plugin-install
Requires: maven2-plugin-jar
Requires: maven2-plugin-javadoc
Requires: maven2-plugin-source
Requires: maven-surefire-plugin
Requires: maven-release
Requires: maven2-plugin-jxr
Requires: maven2-plugin-project-info-reports
Requires: maven2-plugin-site
Requires: maven-surefire-report-maven-plugin
#Requires: mojo-maven2-plugin-jdepend
#Requires: mojo-maven2-plugin-rat
BuildRequires: jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
Commons Parent.

%prep
%setup -q -n %{short_name}-%{version}
%patch33

%build

%install

%add_to_maven_depmap org.apache.commons commons-parent %{version} JPP %{name}

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

%files
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:11-alt5_3jpp6
- dropped commons-build-plugin dependency (patch33)

* Wed Sep 28 2011 Igor Vlasenko <viy@altlinux.ru> 0:11-alt4_3jpp6
- dropped felix maven req:

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:11-alt3_3jpp6
- compat build

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:11-alt2_3jpp6
- removed mojo-maven2-plugin-* deps

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:11-alt1_3jpp6
- added pom

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:11-alt1_1jpp5
- new version

