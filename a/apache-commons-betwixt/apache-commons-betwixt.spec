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

%define base_name betwixt
%define short_name commons-betwixt

Name:           apache-%{short_name}
Version:        0.9
Release:        alt1_0.r830480.5jpp6
Epoch:          0
Summary:        Java bean to XML mapping library
Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://commons.apache.org/betwixt/
Source0:        commons-betwixt-0.9-src.tar.gz
# svn export -r 830480 http://svn.apache.org/repos/asf/commons/proper/betwixt/trunk commons-betwixt-0.9-src
# tar czf ../SOURCES/commons-betwixt-0.9-src.tar.gz commons-betwixt-0.9-src/
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        apache-commons-digester-component-info.xml

%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-beanutils
%if %with maven
BuildRequires: apache-commons-parent >= 0:12
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
Requires: jakarta-commons-logging
Requires: jakarta-commons-digester
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:1.0-1
Provides:       jakarta-%{short_name}0 = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}0 < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Source44: import.info

%description
The Betwixt library provides an XML introspection mechanism for
mapping beans to XML in a flexible way. It is implemented using an
XMLIntrospector and XMLBeanInfo classes which are similar to the
standard Introspector and BeanInfo from the Java Beans specification.
Betwixt provides a way of turning beans into XML as well as
automatically generating digester rules in a way that can be
customized on a per type manner in the same way that the BeanInfo
mechanism can be used to customize the default introspection on a java
object.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}0-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}0-repolib < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-repolib < %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires: java-javadoc
BuildRequires: jakarta-commons-collections-javadoc
BuildRequires: jakarta-commons-logging-javadoc
BuildRequires: jakarta-commons-digester-javadoc
BuildRequires: jakarta-commons-beanutils-javadoc
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}0-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}0-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%{__perl} -pi -e 's/\r$//g' LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

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
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL}"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        install javadoc:javadoc

%else

export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath apache-commons-logging-api \
apache-commons-logging apache-commons-digester apache-commons-collections \
apache-commons-beanutils \
)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dnoget=true \
  -Dbuild.sysclasspath=first \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Dcollections.javadoc=%{_javadocdir}/apache-commons-collections \
  -Dlogging.javadoc=%{_javadocdir}/apache-commons-logging \
  -Ddigester.javadoc=%{_javadocdir}/apache-commons-digester \
  -Dbeanutils.javadoc=%{_javadocdir}/apache-commons-beanutils \
  test dist
%endif

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%if %with maven
install -m 644 target/%{short_name}-%{version}-SNAPSHOT.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%else
install -m 644 dist/%{short_name}-%{version}-SNAPSHOT.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%endif
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in apache-*; do ln -sf ${jar} $(echo $jar | sed -e 's/apache-/jakarta-/'); done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in apache-*; do ln -sf ${jar} $(echo $jar | sed -e 's/apache-//'); done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} $(echo $jar | sed -e 's/-%{version}//'); done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{name}

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr RELEASE-NOTES.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %with repolib
%{__install} -d -m 0755 %{buildroot}%{repodir}
%{__install} -d -m 0755 %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 0755 %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%doc %{_docdir}/%{name}-%{version}/RELEASE-NOTES.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/*

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_0.r830480.5jpp6
- new version

