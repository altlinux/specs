BuildRequires: plexus-resources
BuildRequires: oro
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

%define gcj_support 0

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without          maven


Name:           pmd
Version:        4.2.5
Release:        alt3_2jpp6
Epoch:          0
Summary:        Scans Java source code and looks for potential problems
License:        BSD Style
Url:            http://pmd.sourceforge.net/
Group:          Development/Java
# svn export https://pmd.svn.sourceforge.net/svnroot/pmd/tags/pmd/pmd_release_4_2_5 pmd-4.2.5 && tar cjf pmd-4.2.5.tar.bz2 pmd-4.2.5
Source0:        pmd-4.2.5.tar.bz2
Source1:        pmd-4.2.5.pom
Source2:        %{name}-%{version}-jpp-depmap.xml
Source3:        %{name}-%{version}-settings.xml

Patch0:         pmd-4.2.5-pom.patch
Patch1:         pmd-ruby.patch
Patch2:         pmd-4.2.4-no-retroweaver.patch
Patch3:         pmd-4.2.4-no-classpath-in-manifest.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: ant >= 0:1.7.1
# FIXME: (dwalluck): Should be 1.1.1
Requires: jaxen >= 0:1.1
Requires: objectweb-asm >= 0:3.1
Requires: junit4 >= 0:4.4
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
BuildRequires: jaxen >= 0:1.1
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit4 >= 0:4.4
BuildRequires: objectweb-asm >= 0:3.1
%if %with maven
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-pmd
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-default-skin
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-jxr
BuildRequires: maven-surefire-maven-plugin
BuildRequires: apache-commons-parent
BuildRequires: fonts-ttf-liberation
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
PMD scans Java source code and looks for potential 
problems like:
+ Unused local variables 
+ Empty catch blocks 
+ Unused parameters 
+ Empty 'if' statements 
+ Duplicate import statements 
+ Unused private methods 
+ Classes which could be Singletons 
+ Short/long variable and method names 
PMD has plugins for JDeveloper, JEdit, JBuilder, 
NetBeans/Sun ONE Studio, IntelliJ IDEA, TextPad, 
Maven, Ant, Eclipse, Gel, and Emacs. 

%if %with maven
%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Documentation for %{name}.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1
%{_bindir}/find . -name "*.sh" | %{_bindir}/xargs -t %{__chmod} 0755
%{_bindir}/find . -name "*.jar" | xargs -t %{__rm}

%{__ln_s} $(build-classpath objectweb-asm/asm) lib/asm-3.0.jar
%if %with maven
cp %{SOURCE3} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
%endif

%build
export LANG=en_US.ISO8859-1
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2_SETTINGS \
        -Dmaven.test.failure.ignore=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc 
#	site

%else
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
export CLASSPATH=$(build-classpath \
backport-util-concurrent \
jaxen \
junit4 \
objectweb-asm \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
cd bin
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist javadoc
%endif

%install

# jar
install -d -m 755 %{buildroot}%{_javadir}
%if %with maven
install -p -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%else
install -p -m 644 lib/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%endif

(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/etc
%{__cp} -pr etc/* %{buildroot}%{_datadir}/%{name}-%{version}/etc

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/rulesets
%{__cp} -pr rulesets/* %{buildroot}%{_datadir}/%{name}-%{version}/rulesets
%{__ln_s} %{name}-%{version} %{buildroot}%{_datadir}/%{name}

# pom
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%if %with maven
%{__cp} -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
# FIXME: (dwalluck): breaks -bi --short-circuit
rm -rf target/site/apidocs
%else
%{__cp} -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%endif
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
%if %with maven
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
#%{__cp} -pr target/site/* %{buildroot}%{_docdir}/%{name}-%{version}/
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%{_datadir}/%{name}
%{_datadir}/%{name}-%{version}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%if %with maven
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%files javadoc
%doc %{_javadocdir}/*

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt3_2jpp6
- dropped velocity14

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt2_2jpp6
- fixed build with java 7

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt1_2jpp6
- new jpp release

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt1_1jpp5
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.2.4-alt1_2jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.9-alt1_2jpp5
- converted from JPackage by jppimport script

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_1jpp1.7
- converted from JPackage by jppimport script

