BuildRequires: maven2-plugin-resources maven2-plugin-plugin
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

#def_with bootstrap
%bcond_with                bootstrap
%define gcj_support        %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

Name:           jflex
Version:        1.4.3
Release:        alt5_1jpp6
Epoch:          0
Summary:        Lexical Analyzer Generator for Java
License:        GPLv2+
Group:          Development/Java
URL:            http://www.jflex.de/
Source0:        jflex-1.4.3.tar.gz
# svn export http://jflex.svn.sourceforge.net/svnroot/jflex/tags/release_1_4_3/ jflex-1.4.3
# tar czf jflex-1.4.3.tar.gz jflex-1.4.3/
Source1:        jflex.script
Source2:        jflex-settings.xml
Source3:        jflex-1.4.3.pom
Patch0:         jflex-bootwith-1.4.2.patch

Requires: java-cup
Requires: jpackage-utils
BuildRequires: ant
BuildRequires: java-cup
%if %without bootstrap
BuildRequires: jflex
%endif
BuildRequires: junit

BuildRequires: maven2 >= 2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven-plugin-tools
BuildRequires: apache-commons-parent
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
JFlex is a lexical analyzer generator for Java written in Java. It is 
also a rewrite of the very useful tool JLex which was developed by 
Elliot Berk at Princeton University. As Vern Paxson states for his C/C++ 
tool flex: they do not share any code though.

Design goals The main design goals of JFlex are:

    * Full unicode support
    * Fast generated scanners
    * Fast scanner generation
    * Convenient specification syntax
    * Platform independence
    * JLex compatibility

%package maven-plugin
Group:          Development/Java
Summary:        Maven2 plugin for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}

%description maven-plugin
%{summary}.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
cp -p %{SOURCE2} settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

%if %without bootstrap
export CLASSPATH=$(build-classpath java-cup junit jflex)
export OPT_JAR_LIST=:
pushd jflex/src
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  realclean
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jflex
popd
# patch if bootstrapping with jflex-1.4.2
# %patch0 -b .sav0
%endif

%build
export LANG=en_US.ISO8859-1
pushd jflex/src
%if %without bootstrap
export CLASSPATH=$(build-classpath java-cup junit jflex)
%else
export CLASSPATH=$(build-classpath java-cup junit)
%endif
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar
%{__mkdir_p} ../dist/docs/api
%{javadoc} -d ../dist/docs/api `find . -type f -name "*.java"`
popd

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p  $MAVEN_REPO_LOCAL/JPP
cp jflex/lib/JFlex.jar $MAVEN_REPO_LOCAL/JPP/jflex.jar
mkdir -p $MAVEN_REPO_LOCAL/de/jflex/jflex/%{version}/
cp jflex/lib/JFlex.jar $MAVEN_REPO_LOCAL/de/jflex/jflex/%{version}/jflex-%{version}.jar

pushd maven-jflex-plugin

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ../settings.xml \
	-Dmaven.repo.local=$MAVEN_REPO_LOCAL \
	-Dmaven.test.skip=true \
        install javadoc:javadoc

#       -Dmaven2.jpp.depmap.file=%{SOURCE4} \
#       -Dmaven.test.failure.ignore=true \

popd

%install

# jar
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -a jflex/lib/JFlex.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -a maven-jflex-plugin/target/maven-jflex-plugin-%{version}.jar %{buildroot}%{_javadir}/maven-jflex-plugin-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# compatibility symlink
(cd %{buildroot}%{_javadir} && %{__ln_s} jflex.jar JFlex.jar)

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP-jflex.pom
%add_to_maven_depmap de.jflex %{name} %{version} JPP %{name}
install -m 644 maven-jflex-plugin/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-maven-jflex-plugin.pom
%add_to_maven_depmap de.jflex maven-jflex-plugin %{version} JPP maven-jflex-plugin

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -a jflex/dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%__subst 's,java_cup,java-cup,' $RPM_BUILD_ROOT/%_bindir/jflex

%files
%doc jflex/COPYRIGHT jflex/doc jflex/examples jflex/src/README jflex/src/changelog
%attr(0755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/JFlex.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files maven-plugin
%{_javadir}/maven-%{name}-plugin-%{version}.jar
%{_javadir}/maven-%{name}-plugin.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt5_1jpp6
- fixed build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt4_1jpp6
- fixed build with java 7

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt3_1jpp6
- added maven2-plugin-resources dep

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt2_1jpp6
- new version (full build)

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt1_1jpp6
- new version (bootstrap build)

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_3jpp5
- new jpp release

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_1jpp5
- fixed classpath

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_1jpp5
- jpp5 build

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.5-alt1_2jpp1.7
- converted from JPackage by jppimport script

