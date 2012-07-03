#BuildRequires: velocity
BuildRequires: mojo-maven2-plugin-jdepend mojo-maven2-plugin-rat
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without maven
#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-%{base_name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define base_name vfs
%define short_name commons-%{base_name}

Name:           apache-commons-vfs
Version:        2.0
Release:        alt2_0.r834424.5jpp6
Epoch:          0
Summary:        Apache Commons Virtual Filesystem
License:        ASL 2.0
Url:            http://common.apache.org/vfs/
Group:          Development/Java
Source0:        commons-vfs-2.0-src.tar.gz
# svn export -r 834424 http://svn.apache.org/repos/asf/commons/proper/vfs/trunk commons-vfs-2.0-src
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
Patch0:         %{name}-pom.patch
Patch1:         %{name}-SmbFileObject.patch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: fonts-ttf-liberation
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
BuildRequires: junit
%if %with maven
BuildRequires: apache-commons-parent >= 0:12
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-default-skin
BuildRequires: maven-jxr
%endif
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-compress
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-net
BuildRequires: jackrabbit >= 0:1.5.7
BuildRequires: jaf_1_1_api
BuildRequires: javamail_1_4_api
BuildRequires: jcifs
BuildRequires: jdepend
BuildRequires: jdom
BuildRequires: jsch
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: apache-commons-codec
Requires: apache-commons-collections
Requires: apache-commons-compress
Requires: jakarta-commons-httpclient
Requires: jakarta-commons-logging
Requires: jakarta-commons-net
Requires: jackrabbit >= 0:1.5.7
Requires: jaf_1_1_api
Requires: javamail_1_4_api
Requires: jcifs
Requires: jdom
Requires: jsch
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Source44: import.info

%description
Commons VFS provides a single API for accessing various 
different file systems. It presents a uniform view of the 
files from various different sources, such as the files on 
local disk, on an HTTP server, or inside a Zip archive.
Some of the features of Commons VFS are:
* A single consistent API for accessing files of different 
  types.
* Support for numerous file system types.
* Caching of file information. Caches information in-JVM, 
  and optionally can cache remote file information on the 
  local file system.
* Event delivery.
* Support for logical file systems made up of files from 
  various different file systems.
* Utilities for integrating Commons VFS into applications, 
  such as a VFS-aware ClassLoader and URLStreamHandlerFactory.
* A set of VFS-enabled Ant tasks.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-manual < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-manual < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -b .sav0
%patch1 -b .sav1
%{__perl} -pi \
    -e 's/\r$//g;' \
  PROPOSAL.html LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%if %with maven
cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%endif

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
%if %with maven
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -Dmaven.test.failure.ignore=true"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        install

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        javadoc:javadoc site

%else
export CLASSPATH=$(build-classpath commons-collections commons-httpclient commons-logging commons-net jaf_1_1_api javamail_1_4_api jcifs jdom jsch junit slide/jakarta-slide-webdavlib):`pwd`/target/commons-vfs-%{version}.jar:`pwd`/target/test-classes
export OPT_JAR_LIST="junit ant/ant-junit"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    -Dmaven.build.dir=`pwd`/target \
    -Dmaven.build.outputDir=`pwd`/target \
    -Dmaven.mode.offline=true \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.repo.remote=file:%{_datadir}/maven/repository \
    -Dmaven.javadoc.source=1.4 \
    -Dmaven.home.local=$(pwd)/.maven \
    -Dmaven.test.skip=true \
    -Dmaven.test.error.ignore=true \
    package javadoc 
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 core/target/%{short_name}-%{version}-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap commons-vfs commons-vfs %{version} JPP commons-vfs
install -m 644 examples/target/%{short_name}-examples-%{version}-SNAPSHOT.jar \
                   $RPM_BUILD_ROOT%{_javadir}/%{name}-examples-%{version}.jar
%add_to_maven_depmap commons-vfs commons-vfs-examples %{version} JPP commons-vfs-examples
install -m 644 sandbox/target/%{short_name}-sandbox-%{version}-SNAPSHOT.jar \
                   $RPM_BUILD_ROOT%{_javadir}/%{name}-sandbox-%{version}.jar
%add_to_maven_depmap commons-vfs commons-vfs-sandbox %{version} JPP commons-vfs-sandbox
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar
ln -s %{name}-examples-%{version}.jar %{buildroot}%{_javadir}/%{name}-examples.jar
ln -s %{name}-examples-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-examples-%{version}.jar
ln -s %{name}-examples-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-examples.jar
ln -s %{name}-examples-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-examples-%{version}.jar
ln -s %{name}-examples-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-examples.jar
ln -s %{name}-sandbox-%{version}.jar %{buildroot}%{_javadir}/%{name}-sandbox.jar
ln -s %{name}-sandbox-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-sandbox-%{version}.jar
ln -s %{name}-sandbox-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-sandbox.jar
ln -s %{name}-sandbox-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-sandbox-%{version}.jar
ln -s %{name}-sandbox-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-sandbox.jar

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-project.pom
%add_to_maven_depmap commons-vfs commons-vfs-project %{version} JPP %{name}-project
%{__cp} -p core/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap commons-vfs commons-vfs %{version} JPP %{name}
%{__cp} -p examples/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-examples.pom
%add_to_maven_depmap commons-vfs commons-vfs-examples %{version} JPP %{name}-examples
%{__cp} -p sandbox/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-sandbox.pom
%add_to_maven_depmap commons-vfs commons-vfs-sandbox %{version} JPP %{name}-sandbox

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
# FIXME: (dwalluck): breaks --short-circuit
rm -rf target/site/apidocs
%else
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf target/site/apidocs
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %with maven
## manual
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
find $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} -name "*.sav" -exec rm {} \;
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__install} -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
#%{__install} -p -m 0644 %{PATCH0} %{buildroot}%{repodirsrc}/
%{__install} -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}/
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{repodirsrc}/
%{__install} -m 0644 %{SOURCE2} %{buildroot}%{repodirsrc}/
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc *.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/*

%if %with maven
%files manual
%{_docdir}/%{name}-%{version}
%endif

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_0.r834424.5jpp6
- fixed build with maven3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_0.r834424.5jpp6
- new version

