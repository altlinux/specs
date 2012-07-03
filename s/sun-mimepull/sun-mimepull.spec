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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/org/jvnet/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


Name:           sun-mimepull
Version:        1.2
Release:        alt4_2jpp6
Epoch:          0
Summary:        MIME Pull
License:        CDDL
Group:          Development/Java
URL:            https://mimepull.dev.java.net/
# svn -q export https://mimepull.dev.java.net/svn/mimepull/tags/mimepull-1.2 --username guest sun-mimepull-1.2
Source0:        sun-mimepull-%{version}.tar.gz
Source1:        sun-mimepull-settings.xml
Source2:        sun-mimepull-component-info.xml
Patch0:         sun-mimepull-pom.patch
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4
Requires: jaf_1_1_api
Requires: stax_1_0_api
Requires: stax-ex
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
BuildRequires: jaf_1_1_api
BuildRequires: stax_1_0_api
BuildRequires: stax-ex
BuildRequires: wstx
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
This provides a streaming API to access attachments parts in 
a MIME message. Often times, a large MIME message cannot be 
loaded into memory. Hence the whole message or attachment 
parts are written to a file system and access to the 
attachment parts is provided using those files.
But in some cases, the attachment parts can be accessed by 
applications in a streaming fashion, provided: - The parts 
are accessed orderly (as they appear in the stream) - The 
parts are accessed only once. In such situations, the parts 
need not be written to file system (however large message 
it is !)
MIME message parsing is done using pull-parsing, much similar
to StAX in XML world. The MIMEParts are constructed lazily, 
and parsing is triggered by applications while reading the 
attachment parts. MIMEConfig provides various configuration 
options to control parsing and storing MIME parts. It is 
also possible to read MIME parts in any order and multiple 
times, but doing so may create attachment parts on the file 
system.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q 
%patch0 -p0
cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

mv LICENSE LICENSE.org
%{_bindir}/iconv -f iso8859-1 -t utf8 -o LICENSE LICENSE.org

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
mkdir -p $MAVEN_REPO_LOCAL
export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s $M2_SETTINGS \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/mimepull-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap org.jvnet mimepull %{version} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir} && ln -s %{name}-%{version}.jar %{name}.jar)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/mimepull.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_2jpp6
- added repolib

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_1jpp5
- fixes for java6 support

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_1jpp5
- fixed docdir ownership

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp5
- converted from JPackage by jppimport script

