Patch33: picocontainer2-alt-drop-site.patch
#BuildRequires: qdox16-poms
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

%define oname picocontainer

Name:           picocontainer2
Version:        2.4
Release:        alt4_2jpp6
Epoch:          0
Summary:        Dependency-injection container
Group:          Development/Java
License:        BSD
URL:            http://picocontainer.codehaus.org/
# svn export http://svn.codehaus.org/picocontainer/java/2.x/tags/picocontainer-2.4/
Source0:        picocontainer2-2.4.tar.gz
Source1:        picocontainer2-settings.xml
Source2:        picocontainer2-jpp-depmap.xml
Patch0:         %{name}-pom.patch
Patch1:         %{name}-gems-pom.patch
Patch99:        %{name}-distribution-temp-pom.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: jakarta-commons-logging
Requires: log4j
Requires: paranamer
Requires: proxytoys
Requires: simple-jndi

%if %with maven
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-shade
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: maven2-default-skin
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-plugin-cobertura
#BuildRequires:  liberation-fonts
BuildRequires: annotation_1_0_api
BuildRequires: picocontainer-site-resources
%else
BuildRequires: ant
BuildRequires: ant-junit
%endif
BuildRequires: cglib >= 0:2.1.3
BuildRequires: cobertura
BuildRequires: gnu-getopt
BuildRequires: apache-commons-parent
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-slide-webdavclient
BuildRequires: jetty5
BuildRequires: jmock2
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit >= 0:3.8.1
BuildRequires: log4j
BuildRequires: plexus-utils
BuildRequires: paranamer
BuildRequires: prefuse
BuildRequires: proxytoys
BuildRequires: servletapi5
BuildRequires: simple-jndi
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xpp3-minimal
BuildRequires: xstream >= 0:1.2.1
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
PicoContainer is a lightweight and highly embeddable container 
for components that honour Dependency Injection.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires: jakarta-commons-logging-javadoc
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n picocontainer-%{version}
%patch0 -b .sav0
%patch1 -b .sav1
%patch99 -b .sav99
%patch33 -p1
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
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e -s $MAVEN_SETTINGS \
        -Preporting,distribution \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.test.skip.exec=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc
#        install javadoc:aggregate

%else
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
pushd container
  export CLASSPATH=$(build-classpath jmock xstream)
  CLASSPATH=$CLASSPATH:target/classes:target/test-classes
  %{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
pushd tck
  export CLASSPATH=$(build-classpath jmock junit xstream)
  CLASSPATH=$CLASSPATH:../container/target/%{name}-%{version}.jar
  CLASSPATH=$CLASSPATH:target/classes:target/test-classes
  %{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
pushd gems
  export CLASSPATH=$(build-classpath commons-logging proxytoys prefuse jmock log4j xstream cglib-nodep xpp3-minimal)
  CLASSPATH=$CLASSPATH:../container/target/%{name}-%{version}.jar
  CLASSPATH=$CLASSPATH:../tck/target/%{name}-tck-%{version}.jar
  CLASSPATH=$CLASSPATH:target/classes:target/test-classes
  %{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
%endif

%install

#jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 tck/target/%{oname}-tck-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-tck-%{version}.jar
install -m 644 gems/target/%{oname}-gems-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-gems-%{version}.jar
install -m 644 container/target/%{oname}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

# create unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

%add_to_maven_depmap org.picocontainer picocontainer-parent %{version} JPP %{name}-parent
%add_to_maven_depmap org.picocontainer picocontainer-distribution %{version} JPP %{name}-distribution
%add_to_maven_depmap org.picocontainer picocontainer %{version} JPP %{name}
%add_to_maven_depmap org.picocontainer picocontainer-tck %{version} JPP %{name}-tck
%add_to_maven_depmap org.picocontainer picocontainer-gems %{version} JPP %{name}-gems

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
install -m 644 distribution/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-distribution.pom
install -m 644 container/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 tck/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-tck.pom
install -m 644 gems/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-gems.pom

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
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-gems-%{version}.jar
%{_javadir}/%{name}-gems.jar
%{_javadir}/%{name}-tck-%{version}.jar
%{_javadir}/%{name}-tck.jar
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
* Sun Jun 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt4_2jpp6
- build with maven-plugin-cobertura

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt3_2jpp6
- rebuild with bs maven-filtering

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt2_2jpp6
- fixed build with maven3

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_2jpp6
- new version

