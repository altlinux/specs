BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 1.0.4
%define name sqljet
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

%bcond_without repolib

%if 0
%define reltag _redhat_1
%define namedreltag -redhat-1
%endif
%global namedversion %{version}%{?namedreltag}


Name:           sqljet
Version:        1.0.4
Release:        alt1_4_redhat_1jpp6
Epoch:          0
Summary:        Pure Java SQLite
Group:          Development/Java
License:        GPLv2
URL:            http://sqljet.com/
%if 0
svn export -r 1166 http://svn.sqljet.com/repos/sqljet/tags/1.0.4 sqljet-1.0.4 && tar cfj sqljet-1.0.4.tar.bz2 sqljet-1.0.4
%endif
Source0:        sqljet-%{version}.tar.bz2
Source2:        sqljet-browser.sh
Source3:        sqljet-browser.desktop
Source4:        sqljet-%{version}.pom
Patch0:         sqljet-javadoc.patch
Patch1:         sqljet-pom.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires:       antlr3
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7
BuildRequires:  antlr
BuildRequires:  antlr3
BuildRequires:  easymock2
BuildRequires:  netbeans-platform
BuildRequires:  junit4
BuildRequires:  desktop-file-utils
%if %with repolib
BuildRequires:  maven2-plugin-deploy
%endif
BuildArch:      noarch
Source44: import.info

%description
SQLJet is an independent pure Java implementation of a popular SQLite database
management system. SQLJet is a software library that provides API that enables
Java application to read and modify SQLite databases.

%package browser
Group:          Development/Java
Summary:        SQLJet database browser
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       netbeans-platform

%description browser
Utility for browsing SQLJet/SQLite databases.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

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
cp -p %{SOURCE4} sqljet-%{version}.pom
%patch0 -p1 -b .sav0
%if 0
%patch1 -p1 -b .sav1
%endif

find -type f \( -name '*.class' -o -name '*.jar' \) | xargs -t rm

pushd lib
ln -s %{_javadir}/antlr3.jar antlr-runtime-3.1.3.jar
popd
pushd sqljet-examples/browser/lib
ln -s %{_datadir}/netbeans/platform*/modules/org-netbeans-swing-outline.jar org-netbeans-swing-outline.jar
popd

%build
export CLASSPATH=$(build-classpath antlr3 antlr stringtemplate easymock2 junit4)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars osgi javadoc

%{jar} umf sqljet/osgi/MANIFEST.MF build/sqljet.jar

%if %with repolib
# repolib
export MAVEN_REPO_LOCAL=`pwd`/.m2/repository
export URL=file://`pwd`/maven2-brew
export MAVEN_OPTS=""
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  deploy:deploy-file -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DpomFile=sqljet-%{version}.pom -Dfile=build/sqljet.jar -DrepositoryId=jboss-releases-repository -Durl=${URL}
%endif

%install

mkdir -p %{buildroot}%{_javadir}
cp -p build/sqljet.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
cp -p build/sqljet-browser.jar %{buildroot}%{_javadir}/%{name}-browser-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do ln -sf ${jar} `echo $jar| sed "s|-%{namedversion}||g"`; done)

mkdir -p %{buildroot}%{_mavenpomdir}
cp -p sqljet-%{version}.pom %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap org.tmatesoft.sqljet sqljet %{namedversion} JPP %{name}

mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}-browser

desktop-file-install --vendor=jpackage --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
desktop-file-validate %{buildroot}%{_datadir}/applications/jpackage-sqljet-browser.desktop

%if %with repolib
# repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%{__cp} -pr maven2-brew/* %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%endif

%files
%doc CHANGES COPYING INSTALL README.txt
%{_javadir}*/%{name}.jar
%{_javadir}*/%{name}-%{namedversion}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files browser
%attr(0755,root,root) %{_bindir}/%{name}-browser
%{_javadir}*/%{name}-browser.jar
%{_javadir}*/%{name}-browser-%{namedversion}.jar
%{_datadir}/applications/jpackage-%{name}-browser.desktop

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*
%exclude %dir %{_javadocdir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_4_redhat_1jpp6
- new jpp relase

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp6
- new version

