BuildRequires: maven2-plugin-javadoc maven2-plugin-source maven-shared-archiver asm maven2-plugin-resources
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

Name:           fest
Version:        1.0.2
Release:        alt2_2jpp6
Epoch:          0
Summary:        Fixtures for Easy Software Testing
License:        ASL 2.0
Group:          Development/Java
URL:            http://fest.easytesting.org
# svn export http://svn.codehaus.org/fest/trunk/fest/ fest-1.0.2 && tar cjf fest-1.0.2.tar.bz2 fest-1.0.2
# Exported revision 1169.
Source0:        fest-1.0.2.tar.bz2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        http://svn.codehaus.org/fest/trunk/fest-assembly/src/main/resources/assembly.xml
Patch0:         fest-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: apache-commons-parent
Requires: fest-assembly >= 0:1.0
Requires: jpackage-utils
Requires: junit4 >= 0:4.7
Requires: maven-surefire-report-maven-plugin
Requires: maven2
Requires: maven2-plugin-assembly
Requires: maven2-plugin-changes
Requires: maven2-plugin-compiler
Requires: maven2-plugin-dependency
Requires: maven2-plugin-javadoc
Requires: maven2-plugin-project-info-reports
Requires: maven2-plugin-resources
Requires: maven2-plugin-site
Requires: maven2-plugin-source
Requires: maven-surefire-plugin
Requires: mojo-maven2-plugin-findbugs
Requires: mojo-maven2-plugin-javancss
Requires: mojo-maven2-plugin-jdepend
BuildRequires: apache-commons-parent
BuildRequires: fest-assembly >= 0:1.0
BuildRequires: jpackage-utils
BuildRequires: junit4 >= 0:4.7
BuildRequires: maven-surefire-report-maven-plugin
BuildRequires: maven2
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-changes
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-deploy
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: mojo-maven2-plugin-findbugs
BuildRequires: mojo-maven2-plugin-javancss
BuildRequires: mojo-maven2-plugin-jdepend
BuildArch:      noarch
Source44: import.info

%description
Fixtures for Easy Software Testing.

%prep
%setup -q
%patch0 -p0 -b .sav0
%{__cp} -p %{SOURCE3} .

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -DaltDeploymentRepository=oss-releases::default::file://$(pwd)/maven2-brew \
        -Dmaven.test.skip=true \
        -DskipAssembly=true \
        install \
        javadoc:aggregate \
%if 0
        site
%endif

%install

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

%add_to_maven_depmap org.easytesting fest %{version} JPP %{name}

%files
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_2jpp6
- built with patched assembly plugin

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp6
- new version

