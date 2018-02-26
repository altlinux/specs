Patch33: commons-parent-12-alt-no-commons-build-plugin.patch
Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define short_name commons-parent

Name:           apache-commons-parent
Version:        12
Release:        alt5_2jpp6
Epoch:          0
Summary:        Apache Commons Parent
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://svn.apache.org/repos/asf/commons/proper/commons-parent
# svn -q export http://svn.apache.org/repos/asf/commons/proper/commons-parent/tags/commons-parent-11 && tar cjf commons-parent-11.tar.bz2 commons-parent-11
Source0:        %{short_name}-%{version}.tar.bz2
Patch0:         apache-commons-parent-pom.patch
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
#Requires: commons-build-plugin >= 0:1.1
#Requires: felix-maven2 >= 0:1.0.2
# replced by
Requires: maven-plugin-bundle
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
BuildRequires: jpackage-utils >= 0:5.0.0
BuildArch:      noarch
Provides:       jakarta-commons-parent = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-commons-parent < %{epoch}:%{version}-%{release}
Source44: import.info

%description
Commons Parent.

%prep
%setup -q -n %{short_name}-%{version}
%patch0 -b .sav0
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
* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:12-alt5_2jpp6
- dropped commons-build-plugin dependency

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt4_2jpp6
- added maven-plugin-bundle as replacement for felix-maven

* Wed Sep 28 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt3_2jpp6
- removed felix-maven from requires

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt2_2jpp6
- removed mojo-maven2-plugin-* from requires

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:12-alt1_2jpp6
- new jpp release

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:12-alt1_1jpp6
- fixed init script

