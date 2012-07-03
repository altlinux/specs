Patch34: picocontainer-script-2.0-alt-jruby-pom.patch
Patch33: picocontainer-script-2.0-alt-kill-site.patch
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

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           picocontainer-script
Version:        2.0
Release:        alt4_1jpp6
Epoch:          0
Summary:        Scripting-layer for picocontainer
Group:          Development/Java
License:        BSD
URL:            http://picocontainer.codehaus.org/
Source0:        picocontainer-script-2.0.tar.gz
# svn export https://svn.codehaus.org/picocontainer/java/2.x/tags/picocontainer-script-2.0/
# tar czf picocontainer-script-2.0.tar.gz picocontainer-script-2.0/

Source1:        picocontainer-script-settings.xml
Source2:        picocontainer-script-jpp-depmap.xml
Patch0:         %{name}-distribution-temp-pom.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: picocontainer2 >= 0:2.4

%if %with maven
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-plugin-cobertura
BuildRequires: maven2-default-skin
#BuildRequires:  liberation-fonts
BuildRequires: apache-commons-parent
%else
BuildRequires: ant
BuildRequires: ant-junit
%endif
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: annotation_1_0_api
BuildRequires: groovy15
BuildRequires: jmock2
BuildRequires: jruby
BuildRequires: jython
BuildRequires: paranamer
BuildRequires: picocontainer2 >= 0:2.4
BuildRequires: picocontainer-site-resources
BuildRequires: xpp3-minimal
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
The main scope of PicoContainer Script to provide a scripting
layer on top of PicoContainer, adding the following features:
* Classloader (classpath) management,including programmable 
  permissions
* Class name based composition (via reflection)
* Meta-data and script language support:
  o XML
  o Beanshell
  o Groovy
  o JRuby
  o Jython (Python)
  o Rhino (Javascript)
It is important to stress that there is no "official" script
or meta-data language. We support multiple script languages 
to give the use the maximum flexibility in the choice that 
suits the task at hand. XML is of course the most widely 
used and mature meta-data markup, but lacks the programming 
features of some scripting languages, such as Groovy or 
JRuby with its builder syntax.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
%patch0 -b .sav0
%patch33 -b .sav33
%patch34 -b .sav34
cp -p %{SOURCE1} settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
%if %with maven
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
export MAVEN_SETTINGS=$(pwd)/settings.xml
mvn-jpp \
        -e -s $MAVEN_SETTINGS \
        -Preporting,distribution \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc
#        install javadoc:aggregate

%else
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
export CLASSPATH=$(build-classpath jmock xstream)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
%{ant} -Dbuild.sysclasspath=only jar javadoc
%endif

%install

#jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 script-core/target/%{name}-core-%{version}.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
install -m 644 script-bsh/target/%{name}-bsh-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-bsh-%{version}.jar
install -m 644 script-groovy/target/%{name}-groovy-%{version}.jar \
         $RPM_BUILD_ROOT%{_javadir}/%{name}-groovy-%{version}.jar
install -m 644 script-jruby/target/%{name}-jruby-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-jruby-%{version}.jar
install -m 644 script-jython/target/%{name}-jython-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-jython-%{version}.jar
install -m 644 script-rhino/target/%{name}-rhino-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-rhino-%{version}.jar
install -m 644 script-tck/target/%{name}-tck-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-tck-%{version}.jar
install -m 644 script-testmodel/target/%{name}-testmodel-%{version}.jar \
            $RPM_BUILD_ROOT%{_javadir}/%{name}-testmodel-%{version}.jar
# create unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

%add_to_maven_depmap org.picocontainer.script picocontainer-script %{version} JPP %{name}
%add_to_maven_depmap org.picocontainer.script picocontainer-script-core %{version} JPP %{name}-core
%add_to_maven_depmap org.picocontainer.script picocontainer-script-bsh %{version} JPP %{name}-bsh
%add_to_maven_depmap org.picocontainer.script picocontainer-script-groovy %{version} JPP %{name}-groovy
%add_to_maven_depmap org.picocontainer.script picocontainer-script-jruby %{version} JPP %{name}-jruby
%add_to_maven_depmap org.picocontainer.script picocontainer-script-jython %{version} JPP %{name}-jython
%add_to_maven_depmap org.picocontainer.script picocontainer-script-rhino %{version} JPP %{name}-rhino
%add_to_maven_depmap org.picocontainer.script picocontainer-script-tck %{version} JPP %{name}-tck
%add_to_maven_depmap org.picocontainer.script picocontainer-script-testmodel %{version} JPP %{name}-testmodel

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 script-core/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-core.pom
install -m 644 script-bsh/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-bsh.pom
install -m 644 script-groovy/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-groovy.pom
install -m 644 script-jruby/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-jruby.pom
install -m 644 script-jython/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-jython.pom
install -m 644 script-rhino/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-rhino.pom
install -m 644 script-tck/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-tck.pom
install -m 644 script-testmodel/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-testmodel.pom

#javadocs
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
#cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
%if %with maven
#install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr distribution/target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
#%doc %{_docdir}/%{name}-%{version}
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.db
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.so
%endif

%files javadoc
%{_javadocdir}/*

%changelog
* Sun Jun 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_1jpp6
- build with maven-plugin-cobertura

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_1jpp6
- fixed build with new jruby

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_1jpp6
- fixed build with maven3

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_1jpp6
- new version

