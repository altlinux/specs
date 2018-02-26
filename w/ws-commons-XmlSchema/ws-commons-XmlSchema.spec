Patch33: ws-commons-XmlSchema-1.4.7-alt-kill-site.patch
BuildRequires: maven-dependency-plugin maven2-default-skin
#BuildRequires: mojo-maven2-plugin-jdepend 
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 1.4.7
%define name ws-commons-XmlSchema
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

%define gcj_support 0

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/org/apache/ws/commons/schema/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define short_name XmlSchema


Name:           ws-commons-XmlSchema
Version:        1.4.7
Release:        alt2_1jpp6
Epoch:          0
Summary:        XmlSchema Object Model
License:        Apache Software License 2.0
Url:            http://ws.apache.org/commons/XmlSchema/
Group:          Development/Java
# svn export http://svn.apache.org/repos/asf/webservices/commons/tags/XmlSchema/XmlSchema-1.4.7/
Source0:        %{name}-%{version}-src.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        http://www.w3.org/XML/2004/xml-schema-test-suite/xmlschema2002-01-16/xsts-2002-01-16.tar.gz
Source4:	%{name}-component-info.xml
Source5:        XmlSchema-1.4.7-MANIFEST.MF

Patch0:         XmlSchema-1.4.7-disable-bundle-pom-xml.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  junit >= 0:3.8.2
BuildRequires:  xmlunit
%if %{with_maven}
BuildRequires:  maven2 >= 2.0.8
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-one
BuildRequires:  maven2-plugin-resources
BuildRequires:	maven2-plugin-remote-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-release
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:	maven-doxia-sitetools
BuildRequires:	maven-surefire-provider-junit
BuildRequires:  apache-commons-parent
BuildRequires:  plexus-velocity

%endif
BuildRequires:  geronimo-qname-1.1-api
BuildRequires:  ws-commons-java5
Requires:  jpackage-utils >= 0:1.7.5
Requires:  geronimo-qname-1.1-api
Requires:  ws-commons-java5
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
XMLSchema is a lightweight schema object model that can be 
used to manipulate and generate XML schema representations. 
It has very few external dependancies and can be easily 
integrated into an existing project.

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
%setup -q -n %{short_name}-%{version}
%patch0 -p0

# 1.4.5 don't have MANIFEST.MF!!!
mkdir -p src/main/resources/META-INF/
cp %{SOURCE5} src/main/resources/META-INF/MANIFEST.MF

cp %{SOURCE1} settings.xml
%if ! %{with_maven}
mkdir -p build
pushd build
gzip -dc %{SOURCE3} | tar xf -
popd
%endif

%patch33

%build
%if %{with_maven}
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven.test.failure.ignore=true \
        package javadoc:javadoc
%else
mkdir -p build/lib
build-jar-repository -s -p build/lib \
xmlunit-1.0 \

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc
%endif


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%if %{with_maven}
install -m 644 target/%{short_name}-%{version}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%else
install -m 644 build/lib/%{short_name}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%endif
%add_to_maven_depmap org.apache.ws.commons.schema %{short_name} %{version} JPP %{name}

# create unprefixed and unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}-%{version}.jar %{name}.jar
)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %{with_maven}
#cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr build/apidoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink


%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE4} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml

%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE3} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{name}.jar
%endif

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.7-alt2_1jpp6
- fixed build with maven3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.7-alt1_1jpp6
- new jpp relase

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.5-alt1_2jpp6
- new jpp release

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_1jpp5
- new version

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

