BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

%bcond_with maven
#def_with gcj_support
%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define svn_tag 1_3

Name:           picocontainer
Version:        1.3
Release:        alt5_5jpp6
Epoch:          0
Summary:        Dependency-injection container
Group:          Development/Java
License:        BSD
URL:            http://picocontainer.codehaus.org/
# svn export http://svn.codehaus.org/picocontainer/java/1.x/picocontainer/tags/picocontainer-1_3/ picocontainer-1.3
Source0:        picocontainer-1.3.tar.gz
Source1:        picocontainer-settings.xml
Source2:        picocontainer-1.3-jpp-depmap.xml
#Source3:        picocontainer-site.xml
Source4:        picocontainer-build.xml
Source5:        picocontainer-container-build.xml
Source6:        picocontainer-distribution-build.xml
Source7:        picocontainer-gems-build.xml
Source8:        picocontainer-tck-build.xml
Patch0:         %{name}-%{version}-pom_xml.patch
Patch1:         %{name}-%{version}-CommonsLoggingTracingContainerDecorator-java2.patch
Patch2:         %{name}-%{version}-Log4jTracingContainerDecorator-java2.patch
Patch3:         %{name}-%{version}-CommonsLoggingTracingContainerDecoratorTestCase-java2.patch
Patch4:         %{name}-%{version}-Log4jTracingContainerDecoratorTestCase-java2.patch
Patch5:         %{name}-%{version}-distribution-pom_xml.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires:       proxytoys
Requires:       apache-commons-logging
Requires:       log4j

%if %with maven
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-dependency
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-project-info-reports
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-site
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-release
BuildRequires:  mojo-maven2-plugin-cobertura >= 0:16-2
BuildRequires:  maven2-default-skin
BuildRequires:  fonts-ttf-liberation
%else
BuildRequires:  ant
BuildRequires:  ant-junit
%endif
BuildRequires:  cglib >= 0:2.1.3
BuildRequires:  cobertura
BuildRequires:  gnu-getopt
BuildRequires:  apache-commons-parent
BuildRequires:  apache-commons-logging
BuildRequires:  jakarta-slide-webdavclient
BuildRequires:  jetty5
BuildRequires:  jmock
BuildRequires:  jpackage-utils >= 0:5.0.0
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  log4j
BuildRequires:  plexus-utils
BuildRequires:  prefuse
BuildRequires:  proxytoys
BuildRequires:  servletapi5
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  xpp3-minimal
BuildRequires:  xstream >= 0:1.2.1
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
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
BuildRequires:  apache-commons-logging-javadoc
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
cp -p %{SOURCE1} settings.xml
mkdir -p src/site
#cp -p %{SOURCE3} src/site/site.xml
cp -p %{SOURCE4} build.xml
cp -p %{SOURCE5} container/build.xml
cp -p %{SOURCE6} distribution/build.xml
cp -p %{SOURCE7} gems/build.xml
cp -p %{SOURCE8} tck/build.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export LANG=en_US.ISO8859-1
%if %with maven
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install 
#	javadoc:javadoc
%else
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
pushd container
  export CLASSPATH=$(build-classpath jmock xstream)
  CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
pushd tck
  export CLASSPATH=$(build-classpath jmock junit xstream)
  CLASSPATH=$CLASSPATH:../container/target/%{name}-%{version}.jar
  CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
pushd gems
  export CLASSPATH=$(build-classpath commons-logging proxytoys prefuse jmock log4j xstream cglib-nodep xpp3-minimal)
  CLASSPATH=$CLASSPATH:../container/target/%{name}-%{version}.jar
  CLASSPATH=$CLASSPATH:../tck/target/%{name}-tck-%{version}.jar
  CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
%endif

%install

#jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 tck/target/%{name}-tck-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-tck-%{version}.jar
install -m 644 gems/target/%{name}-gems-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-gems-%{version}.jar
install -m 644 container/target/%{name}-%{version}.jar \
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
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tck
cp -pr tck/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tck
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/gems
cp -pr gems/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/gems
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/container
cp -pr container/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/container
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
%if %with maven
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr distribution/target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
#doc %{_docdir}/%{name}-%{version}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/picocontainer-gems-%{version}.jar
%{_javadir}/picocontainer-gems.jar
%{_javadir}/picocontainer-tck-%{version}.jar
%{_javadir}/picocontainer-tck.jar
%{_datadir}/maven2/poms/JPP-picocontainer-distribution.pom
%{_datadir}/maven2/poms/JPP-picocontainer-gems.pom
%{_datadir}/maven2/poms/JPP-picocontainer-parent.pom
%{_datadir}/maven2/poms/JPP-picocontainer-tck.pom
%{_datadir}/maven2/poms/JPP-picocontainer.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.db
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.so
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt5_5jpp6
- dropped extra build dependencies

* Mon May 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt4_5jpp6
- fixed build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_5jpp6
- fixed build with java 7

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_5jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_4jpp5
- new jpp release

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp5
- fixed build

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp1.7
- added dependency on new excalibur

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp1.7
- converted from JPackage by jppimport script

