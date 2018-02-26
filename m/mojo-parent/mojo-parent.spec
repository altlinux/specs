Packager: Igor Vlasenko <viy@altlinux.ru>
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

Name:           mojo-parent
Version:        20
Release:        alt1_2jpp6
Epoch:          0
Summary:        Codehaus Mojo Parent
License:        MIT
Group:          Development/Java
URL:            http://svn.codehaus.org/mojo/tags/mojo-parent-20
# svn -q export http://svn.codehaus.org/mojo/tags/mojo-parent-20/ && tar cjf mojo-parent-20.tar.bz2 mojo-parent-20
Source0:        mojo-parent-20.tar.bz2
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: maven2-plugin-antrun
Requires: maven2-plugin-assembly
Requires: maven2-plugin-checkstyle
Requires: maven2-plugin-clean
Requires: maven2-plugin-compiler
Requires: maven2-plugin-deploy
Requires: maven2-plugin-enforcer
Requires: maven2-plugin-install
Requires: maven2-plugin-invoker
Requires: maven2-plugin-jar
Requires: maven2-plugin-javadoc
Requires: maven2-plugin-pmd
Requires: maven2-plugin-source
Requires: maven-surefire-plugin
Requires: maven-release
Requires: maven2-plugin-jxr
Requires: maven2-plugin-project-info-reports
Requires: maven2-plugin-site
Requires: maven-surefire-report-maven-plugin
Requires: mojo-maven2-plugin-cobertura
Requires: mojo-maven2-plugin-taglist
BuildRequires: jpackage-utils
BuildArch:      noarch

%description
Codehaus Mojo Parent.

%prep
%setup -q

%build

%install

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.mojo mojo-parent %{version} JPP %{name}

%files
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_2jpp6
- new version

