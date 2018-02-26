Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

#def_with manifest_only
%bcond_with manifest_only
#def_with gcj_support
%bcond_with gcj_support
#def_with bootstrap
%bcond_with bootstrap
%bcond_without repolib

%if %with bootstrap
%define build_javadoc        0
%else
%define build_javadoc        1
%endif

%define repodir %{_javadir}/repository.jboss.com/org/apache/ant/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define ant_home %{_datadir}/ant17

%define major_version 1.7
%define cvs_version 1.7.1

Name:           ant17
Version:        1.7.1
Release:        alt3_13jpp6
Epoch:          0
Summary:        Ant build tool for java
Summary(it):    Tool per la compilazione di programmi java
Summary(fr):    Outil de compilation pour java
License:        ASL 2.0
URL:            http://ant.apache.org/
Group:          Development/Java
Source0:        http://www.apache.org/dist/ant/source/apache-ant-%{cvs_version}-src.tar.bz2
Source2:        apache-ant-%{major_version}.ant.conf
Source1:        http://repo1.maven.org/maven2/org/apache/ant/ant/1.7.1/ant-1.7.1.pom
Source3:        http://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.7.1/ant-launcher-1.7.1.pom
Source4:        http://repo1.maven.org/maven2/org/apache/ant/ant-netrexx/1.7.1/ant-netrexx-1.7.1.pom
Source5:        http://repo1.maven.org/maven2/org/apache/ant/ant-starteam/1.7.1/ant-starteam-1.7.1.pom
Source6:        http://repo1.maven.org/maven2/org/apache/ant/ant-stylebook/1.7.1/ant-stylebook-1.7.1.pom
Source7:        http://repo1.maven.org/maven2/org/apache/ant/ant-weblogic/1.7.1/ant-weblogic-1.7.1.pom
Source8:        http://repo1.maven.org/maven2/org/apache/ant/ant-antlr/1.7.1/ant-antlr-1.7.1.pom
Source9:        http://repo1.maven.org/maven2/org/apache/ant/ant-apache-bsf/1.7.1/ant-apache-bsf-1.7.1.pom
Source10:       http://repo1.maven.org/maven2/org/apache/ant/ant-apache-resolver/1.7.1/ant-apache-resolver-1.7.1.pom
Source11:       http://repo1.maven.org/maven2/org/apache/ant/ant-commons-logging/1.7.1/ant-commons-logging-1.7.1.pom
Source12:       http://repo1.maven.org/maven2/org/apache/ant/ant-commons-net/1.7.1/ant-commons-net-1.7.1.pom
#Source13:      http://repo1.maven.org/maven2/org/apache/ant/ant-jai/1.7.1/ant-jai-1.7.1.pom
Source14:       http://repo1.maven.org/maven2/org/apache/ant/ant-apache-bcel/1.7.1/ant-apache-bcel-1.7.1.pom
Source15:       http://repo1.maven.org/maven2/org/apache/ant/ant-apache-log4j/1.7.1/ant-apache-log4j-1.7.1.pom
Source16:       http://repo1.maven.org/maven2/org/apache/ant/ant-apache-oro/1.7.1/ant-apache-oro-1.7.1.pom
Source17:       http://repo1.maven.org/maven2/org/apache/ant/ant-apache-regexp/1.7.1/ant-apache-regexp-1.7.1.pom
Source18:       http://repo1.maven.org/maven2/org/apache/ant/ant-javamail/1.7.1/ant-javamail-1.7.1.pom
Source19:       http://repo1.maven.org/maven2/org/apache/ant/ant-jdepend/1.7.1/ant-jdepend-1.7.1.pom
Source20:       http://repo1.maven.org/maven2/org/apache/ant/ant-jmf/1.7.1/ant-jmf-1.7.1.pom
Source21:       http://repo1.maven.org/maven2/org/apache/ant/ant-jsch/1.7.1/ant-jsch-1.7.1.pom
Source22:       http://repo1.maven.org/maven2/org/apache/ant/ant-junit/1.7.1/ant-junit-1.7.1.pom
Source23:       http://repo1.maven.org/maven2/org/apache/ant/ant-nodeps/1.7.1/ant-nodeps-1.7.1.pom
Source24:       http://repo1.maven.org/maven2/org/apache/ant/ant-swing/1.7.1/ant-swing-1.7.1.pom
Source25:       http://repo1.maven.org/maven2/org/apache/ant/ant-trax/1.7.1/ant-trax-1.7.1.pom
Source26:       http://repo1.maven.org/maven2/org/apache/ant/ant-parent/1.7.1/ant-parent-1.7.1.pom
Source27:       %{name}-component-info.xml
Source33:       http://repo1.maven.org/maven2/org/apache/ant/ant-testutil/1.7.1/ant-testutil-1.7.1.pom

# Fix some places where copies of classes are included in the wrong jarfiles
Patch0:         apache-ant-jars.patch
Patch1:         apache-ant-bz163689.patch
Patch2:         apache-ant-gnu-classpath.patch
Patch3:         apache-ant-no-test-jar.patch
#  Patch for #43114: ensuring that package-info.class is created/touched when
#  package-info.java is compiled.
Patch4:         apache-ant-bug43114.patch
Patch5:         apache-ant-script.patch
BuildRequires: jpackage-utils
BuildRequires: jaxp_transform_impl
%if %without bootstrap
BuildRequires: ant
BuildRequires: junit
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xerces-j2
%endif

Requires: jpackage-utils
%if %without bootstrap
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif
Obsoletes:      ant-optional < %{epoch}:%{version}-%{release}
Provides:       ant-optional = %{epoch}:%{version}-%{release}
Obsoletes:      ant-optional-full < %{epoch}:%{version}-%{release}
Provides:       ant-optional-full = %{epoch}:%{version}-%{release}
# Allow subpackages not in RHEL to be installed from JPackage
Provides:       %{name} = %{epoch}:%{version}-%{release}
# RHUG
Obsoletes:      ant-devel < %{epoch}:%{version}-%{release}
Provides:       ant-devel = %{epoch}:%{version}-%{release}
# Mandriva
Conflicts: j2sdk-ant
# RHEL3 and FC2
Obsoletes:      %{name}-libs < %{epoch}:%{version}-%{release}
Provides:       %{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-core < %{epoch}:%{version}-%{release}
Provides:       %{name}-core = %{epoch}:%{version}-%{release}
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif

Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info
Patch33: apache-ant-1.7.1-alt-commons-net2.0.patch

%description
Ant is a platform-independent build tool for java. It's used by apache
jakarta and xml projects.

%description -l fr
Ant est un outil de compilation multi-plateformes pour java. Il est
utilisA© par les projets apache-jakarta et apache-xml.

%description -l it
Ant e' un tool indipendente dalla piattaforma creato per faciltare la
compilazione di programmi java.
Allo stato attuale viene utilizzato dai progetti apache jakarta ed
apache xml.

%package jmf
Summary:        Optional jmf tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides:       ant-jmf = %{epoch}:%{version}-%{release}

%description jmf
Optional jmf tasks for %{name}.

%description jmf -l fr
Taches jmf optionelles pour %{name}.

%package nodeps
Summary:        Optional tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides:       ant-nodeps = %{epoch}:%{version}-%{release}

%description nodeps
Optional tasks for %{name}.

%description nodeps -l fr
Taches optionelles pour %{name}.

%package swing
Summary:        Optional swing tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides:       ant-swing = %{epoch}:%{version}-%{release}

%description swing
Optional swing tasks for %{name}.

%description swing -l fr
Taches swing optionelles pour %{name}.

%package trax
Summary:        Optional trax tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jaxp_transform_impl
Provides:       ant-trax = %{epoch}:%{version}-%{release}
# The ant-xalan jar has been merged into the ant-trax one
Obsoletes:      ant-xalan2 < %{epoch}:%{version}-%{release}
Provides:       ant-xalan2 = %{epoch}:%{version}-%{release}

%description trax
Optional trax tasks for %{name}.

%description trax -l fr
Taches trax optionelles pour %{name}.

%if %without bootstrap
%if %with manifest_only
%package manifest-only
Summary:        Manifest-only jars for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides:       %{name}-icontract = %{epoch}:%{version}-%{release}
Provides:       %{name}-netrexx = %{epoch}:%{version}-%{release}
Provides:       %{name}-starteam = %{epoch}:%{version}-%{release}
Provides:       %{name}-stylebook = %{epoch}:%{version}-%{release}
Provides:       %{name}-vaj = %{epoch}:%{version}-%{release}
Provides:       %{name}-weblogic = %{epoch}:%{version}-%{release}
Provides:       %{name}-xalan1 = %{epoch}:%{version}-%{release}
Provides:       %{name}-xslp = %{epoch}:%{version}-%{release}

%description  manifest-only
Manifest-only jars for %{name}.
%endif

%package antlr
Summary:        Optional antlr tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: antlr
BuildRequires: antlr
Provides:       ant-antlr = %{epoch}:%{version}-%{release}

%description antlr
Optional antlr tasks for %{name}.

%description antlr -l fr
Taches antlr optionelles pour %{name}.

%package apache-bsf
Summary:        Optional apache bsf tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: bsf
BuildRequires: bsf
Provides:       ant-apache-bsf = %{epoch}:%{version}-%{release}

%description apache-bsf
Optional apache bsf tasks for %{name}.

%description apache-bsf -l fr
Taches apache bsf optionelles pour %{name}.

%package apache-resolver
Summary:        Optional apache resolver tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: xml-commons-resolver12
BuildRequires: xml-commons-resolver12
Provides:       ant-apache-resolver = %{epoch}:%{version}-%{release}

%description apache-resolver
Optional apache resolver tasks for %{name}.

%description apache-resolver -l fr
Taches apache resolver optionelles pour %{name}.

%package commons-logging
Summary:        Optional commons logging tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jakarta-commons-logging
BuildRequires: jakarta-commons-logging
Provides:       ant-commons-logging = %{epoch}:%{version}-%{release}

%description commons-logging
Optional commons logging tasks for %{name}.

%description commons-logging -l fr
Taches commons logging optionelles pour %{name}.

%package commons-net
Summary:        Optional commons net tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jakarta-commons-net
BuildRequires: jakarta-commons-net
Provides:       ant-commons-net = %{epoch}:%{version}-%{release}

%description commons-net
Optional commons net tasks for %{name}.

%description commons-net -l fr
Taches commons net optionelles pour %{name}.

# Disable because we don't ship the dependencies
%if 0
%package jai
Summary:        Optional jai tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jai
BuildRequires: jai
Provides:       ant-jai = %{epoch}:%{version}-%{release}

%description jai
Optional jai tasks for %{name}.

%description jai -l fr
Taches jai optionelles pour %{name}.
%endif

%package apache-bcel
Summary:        Optional apache bcel tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: bcel
BuildRequires: bcel
Provides:       ant-apache-bcel = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-bcel = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-bcel < %{epoch}:%{version}-%{release}

%description apache-bcel
Optional apache bcel tasks for %{name}.

%description apache-bcel -l fr
Taches apache bcel optionelles pour %{name}.

%package apache-log4j
Summary:        Optional apache log4j tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: log4j
BuildRequires: log4j
Provides:       ant-apache-log4j = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-log4j = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-log4j < %{epoch}:%{version}-%{release}

%description apache-log4j
Optional apache log4j tasks for %{name}.

%description apache-log4j -l fr
Taches apache log4j optionelles pour %{name}.

%package apache-oro
Summary:        Optional apache oro tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: oro
BuildRequires: oro
Provides:       ant-apache-oro = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-oro = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-oro < %{epoch}:%{version}-%{release}

%description apache-oro
Optional apache oro tasks for %{name}.

%description apache-oro -l fr
Taches apache oro optionelles pour %{name}.

%package apache-regexp
Summary:        Optional apache regexp tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: regexp
BuildRequires: regexp
Provides:       ant-apache-regexp = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-regexp = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-regexp < %{epoch}:%{version}-%{release}

%description apache-regexp
Optional apache regexp tasks for %{name}.

%description apache-regexp -l fr
Taches apache regexp optionelles pour %{name}.

%package javamail
Summary:        Optional javamail tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: javamail 
Requires: jaf 
BuildRequires: javamail 
BuildRequires: jaf 
Provides:       ant-javamail = %{epoch}:%{version}-%{release}

%description javamail
Optional javamail tasks for %{name}.

%description javamail -l fr
Taches javamail optionelles pour %{name}.

%package jdepend
Summary:        Optional jdepend tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jdepend
BuildRequires: jdepend
Provides:       ant-jdepend = %{epoch}:%{version}-%{release}

%description jdepend
Optional jdepend tasks for %{name}.

%description jdepend -l fr
Taches jdepend optionelles pour %{name}.

%package jsch
Summary:        Optional jsch tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jsch
BuildRequires: jsch
Provides:       ant-jsch = %{epoch}:%{version}-%{release}

%description jsch
Optional jsch tasks for %{name}.

%description jsch -l fr
Taches jsch optionelles pour %{name}.

%package junit
Summary:        Optional junit tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: junit
Provides:       ant-junit = %{epoch}:%{version}-%{release}

%description junit
Optional junit tasks for %{name}.

%description junit -l fr
Taches junit optionelles pour %{name}.

%package scripts
Summary:        Additional scripts for %{name}
Group:          Development/Java
AutoReqProv:    no
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{_bindir}/perl
Requires: %{_bindir}/python

%description scripts
Additional Perl and Python scripts for %{name}.

%description scripts -l fr
Scripts additionels pour %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%description manual -l it
Documentazione di %{name}.

%description manual -l fr
Documentation pour %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%description javadoc -l fr
Javadoc pour %{name}.
%endif

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

# -----------------------------------------------------------------------------

%prep
%setup -q -n apache-ant-%{cvs_version}

# Fix some places where copies of classes are included in the wrong jarfiles
%patch0 -p1

# Disable the style and xmlvalidate tasks on ppc64 and s390x (#163689).
%ifarch ppc64 s390x
%patch1 -p1
%endif

# Update ant to work with recent versions of GNU Classpath
%patch2 -p1

# When bootstrapping, we don't have junit
%patch3 -p1

#  Patch for #43114: ensuring that package-info.class is created/touched when
#  package-info.java is compiled.
%patch4 -p1

%patch5 -p1

# clean jar files
find . -name "*.jar" | %{_bindir}/xargs -t rm
%patch33 -p1

# -----------------------------------------------------------------------------

%build
export OPT_JAR_LIST=:
%if %without bootstrap
export CLASSPATH=$(build-classpath xerces-j2 xml-commons-jaxp-1.3-apis antlr bcel jaf javamail/mailapi jdepend junit log4j oro regexp bsf commons-logging commons-net jsch xml-commons-resolver12)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars test-jar
%if %{build_javadoc}
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 javadocs
%endif
%else
#export JAVA_HOME=%{java_home}
export CLASSPATH=$JAVA_HOME/lib/tools.jar
sh ./build.sh --noconfig jars test-jar
%endif

# -----------------------------------------------------------------------------

%install

# ANT_HOME and subdirs
mkdir -p $RPM_BUILD_ROOT%{ant_home}/{lib,etc}

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 build/lib/ant.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 build/lib/ant-bootstrap.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-bootstrap-%{version}.jar
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.ant %{name} %{version} JPP %{name}
install -m 644 build/lib/ant-launcher.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-launcher-%{version}.jar
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-launcher.pom
%add_to_maven_depmap org.apache.ant %{name}-launcher %{version} JPP %{name}-launcher
install -m 644 build/lib/ant-testutil.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-testutil-%{version}.jar
install -m 644 %{SOURCE33} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-testutil.pom
%add_to_maven_depmap org.apache.ant %{name}-testutil %{version} JPP %{name}-testutil

install -m 644 build/lib/ant-jmf.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jmf-%{version}.jar
install -m 644 %{SOURCE20} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jmf.pom
%add_to_maven_depmap org.apache.ant %{name}-jmf %{version} JPP/%{name} %{name}-jmf
install -m 644 build/lib/ant-nodeps.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-nodeps-%{version}.jar
install -m 644 %{SOURCE23} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-nodeps.pom
%add_to_maven_depmap org.apache.ant %{name}-nodeps %{version} JPP/%{name} %{name}-nodeps
install -m 644 build/lib/ant-swing.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-swing-%{version}.jar
install -m 644 %{SOURCE24} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-swing.pom
%add_to_maven_depmap org.apache.ant %{name}-swing %{version} JPP/%{name} %{name}-swing
install -m 644 build/lib/ant-trax.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-trax-%{version}.jar
install -m 644 %{SOURCE25} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-trax.pom
%add_to_maven_depmap org.apache.ant %{name}-trax %{version} JPP/%{name} %{name}-trax

# optional jars
%if %without bootstrap
%if %with manifest_only
install -m 644 build/lib/ant-icontract.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-icontract-%{version}.jar
install -m 644 build/lib/ant-netrexx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-netrexx-%{version}.jar
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-netrexx.pom
%add_to_maven_depmap org.apache.ant %{name}-netrexx %{version} JPP/%{name} %{name}-netrexx
install -m 644 build/lib/ant-starteam.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-starteam-%{version}.jar
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-starteam.pom
%add_to_maven_depmap org.apache.ant %{name}-starteam %{version} JPP/%{name} %{name}-starteam
install -m 644 build/lib/ant-stylebook.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-stylebook-%{version}.jar
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-stylebook.pom
%add_to_maven_depmap org.apache.ant %{name}-stylebook %{version} JPP/%{name} %{name}-stylebook
install -m 644 build/lib/ant-vaj.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-vaj-%{version}.jar
install -m 644 build/lib/ant-weblogic.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-weblogic-%{version}.jar
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-weblogic.pom
%add_to_maven_depmap org.apache.ant %{name}-weblogic %{version} JPP/%{name} %{name}-weblogic
install -m 644 build/lib/ant-xalan1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-xalan1-%{version}.jar
install -m 644 build/lib/ant-xslp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-xslp-%{version}.jar
%endif
install -m 644 build/lib/ant-antlr.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-antlr-%{version}.jar
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-antlr.pom
%add_to_maven_depmap org.apache.ant %{name}-antlr %{version} JPP/%{name} %{name}-antlr
install -m 644 build/lib/ant-apache-bsf.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-bsf-%{version}.jar
install -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-bsf.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-bsf %{version} JPP/%{name} %{name}-apache-bsf
install -m 644 build/lib/ant-apache-resolver.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-resolver-%{version}.jar
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-resolver.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-resolver %{version} JPP/%{name} %{name}-apache-resolver
install -m 644 build/lib/ant-commons-logging.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-commons-logging-%{version}.jar
install -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-commons-logging.pom
%add_to_maven_depmap org.apache.ant %{name}-commons-logging %{version} JPP/%{name} %{name}-commons-logging
install -m 644 build/lib/ant-commons-net.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-commons-net-%{version}.jar
install -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-commons-net.pom
%add_to_maven_depmap org.apache.ant %{name}-commons-net %{version} JPP/%{name} %{name}-commons-net
#install -m 644 build/lib/ant-jai.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jai-%{version}.jar
#install -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jai.pom
#%add_to_maven_depmap org.apache.ant %{name}-jai %{version} JPP/%{name} %{name}-jai
install -m 644 build/lib/ant-apache-bcel.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-bcel-%{version}.jar
install -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-bcel.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-bcel %{version} JPP/%{name} %{name}-apache-bcel
install -m 644 build/lib/ant-apache-log4j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-log4j-%{version}.jar
install -m 644 %{SOURCE15} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-log4j.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-log4j %{version} JPP/%{name} %{name}-apache-log4j
install -m 644 build/lib/ant-apache-oro.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-oro-%{version}.jar
install -m 644 %{SOURCE16} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-oro.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-oro %{version} JPP/%{name} %{name}-apache-oro
install -m 644 build/lib/ant-apache-regexp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-regexp-%{version}.jar
install -m 644 %{SOURCE17} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-regexp.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-regexp %{version} JPP/%{name} %{name}-apache-regexp
ln -sf %{name}-apache-bcel.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-bcel.jar
ln -sf %{name}-apache-log4j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-log4j.jar
ln -sf %{name}-apache-oro.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-oro.jar
ln -sf %{name}-apache-regexp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-regexp.jar
install -m 644 build/lib/ant-javamail.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-javamail-%{version}.jar
install -m 644 %{SOURCE18} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-javamail.pom
%add_to_maven_depmap org.apache.ant %{name}-javamail %{version} JPP/%{name} %{name}-javamail
install -m 644 build/lib/ant-jdepend.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jdepend-%{version}.jar
install -m 644 %{SOURCE19} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jdepend.pom
%add_to_maven_depmap org.apache.ant %{name}-jdepend %{version} JPP/%{name} %{name}-jdepend
install -m 644 build/lib/ant-jsch.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jsch-%{version}.jar
install -m 644 %{SOURCE21} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jsch.pom
%add_to_maven_depmap org.apache.ant %{name}-jsch %{version} JPP/%{name} %{name}-jsch
install -m 644 build/lib/ant-junit.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-junit-%{version}.jar
install -m 644 %{SOURCE22} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-junit.pom
%add_to_maven_depmap org.apache.ant %{name}-junit %{version} JPP/%{name} %{name}-junit
install -m 644 %{SOURCE26} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%add_to_maven_depmap org.apache.ant %{name}-parent %{version} JPP %{name}-parent
%endif

# jar aliases
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# scripts: remove dos and os/2 scripts
rm -f src/script/*.bat
rm -f src/script/*.cmd

# XSLs
cp -p src/etc/*.xsl $RPM_BUILD_ROOT%{ant_home}/etc

# install everything else
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p src/script/ant $RPM_BUILD_ROOT%{_bindir}/ant17
cp -p src/script/antRun $RPM_BUILD_ROOT%{_bindir}/ant17Run
cp -p src/script/complete-ant-cmd.pl $RPM_BUILD_ROOT%{_bindir}/complete-ant17-cmd.pl
cp -p src/script/runant.pl $RPM_BUILD_ROOT%{_bindir}/runant17.pl
cp -p src/script/runant.py $RPM_BUILD_ROOT%{_bindir}/runant17.py

# default ant.conf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

# OPT_JAR_LIST fragments
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d
echo "ant17/ant17-jmf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jmf
echo "ant17/ant17-nodeps" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/nodeps
echo "ant17/ant17-swing" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/swing
echo "jaxp_transform_impl ant17/ant17-trax xalan-j2-serializer" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/trax
%if %without bootstrap
echo "antlr ant17/ant17-antlr" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/antlr
echo "bsf ant17/ant17-apache-bsf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bsf
echo "xml-commons-resolver12 ant17/ant17-apache-resolver" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-resolver
echo "jakarta-commons-logging ant17/ant17-commons-logging" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-logging
echo "jakarta-commons-net ant17/ant17-commons-net" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-net
#echo "jai ant17/ant17-jai" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jai
echo "bcel ant17/ant17-apache-bcel" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bcel
echo "log4j ant17/ant17-apache-log4j" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-log4j
echo "oro ant17/ant17-apache-oro" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-oro
echo "regexp ant17/ant17-apache-regexp" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-regexp
echo "javamail jaf ant17/ant17-javamail" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/javamail
echo "jdepend ant17/ant17-jdepend" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jdepend
echo "jsch ant17/ant17-jsch" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jsch
echo "junit ant17/ant17-junit" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/junit
%endif

%if %{build_javadoc}
# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%endif

# fix link between manual and javadoc
(cd docs/manual; ln -sf %{_javadocdir}/%{name}-%{version} api)

%if %with bootstrap
find $RPM_BUILD_ROOT%{_datadir}/ant/etc -type f -name "*.xsl" \
                                                 -a ! -name ant-update.xsl \
                                                 -a ! -name changelog.xsl \
                                                 -a ! -name coverage-frames.xsl \
                                                 -a ! -name junit-frames-xalan1.xsl \
                                                 -a ! -name log.xsl \
                                                 -a ! -name mmetrics-frames.xsl \
                                                 -a ! -name tagdiff.xsl \
                                                 | xargs -t rm
%endif

# -----------------------------------------------------------------------------

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE27} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE3} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE4} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE5} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE6} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE7} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE8} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE9} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE10} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE11} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE12} %{buildroot}%{repodirsrc}
#%%{__install} -p -m 644 %{SOURCE13} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE14} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE15} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE16} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE17} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE18} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE19} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE20} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE21} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE22} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE23} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE24} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE25} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE26} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH2} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH3} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH4} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH5} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/ant.jar
%{__cp} -p %{buildroot}%{_javadir}/%{name}-launcher-%{version}.jar %{buildroot}%{repodirlib}/ant-launcher.jar
%if %without bootstrap
%{__cp} -p %{buildroot}%{_javadir}/%{name}/%{name}-junit-%{version}.jar %{buildroot}%{repodirlib}/ant-junit.jar
%endif
%endif

# -----------------------------------------------------------------------------

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc KEYS LICENSE NOTICE README WHATSNEW
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0755,root,root) %{_bindir}/ant17
%attr(0755,root,root) %{_bindir}/ant17Run
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}-launcher.jar
%{_javadir}/%{name}-launcher-%{version}.jar
%{_javadir}/%{name}-bootstrap.jar
%{_javadir}/%{name}-bootstrap-%{version}.jar
%{_javadir}/%{name}-testutil.jar
%{_javadir}/%{name}-testutil-%{version}.jar
%dir %{_javadir}/%{name}
%dir %{ant_home}
%dir %{ant_home}/etc
%{ant_home}/etc/ant-update.xsl
%{ant_home}/etc/changelog.xsl
%{ant_home}/etc/log.xsl
%{ant_home}/etc/tagdiff.xsl
%{ant_home}/etc/junit-frames-xalan1.xsl
%if %without bootstrap
%{ant_home}/etc/common2master.xsl
%endif
%dir %{ant_home}/lib
%dir %{_sysconfdir}/%{name}.d
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/ant17-%{version}.jar.*
%{_libdir}/gcj/%{name}/ant17-launcher-%{version}.jar.*
%endif

%files jmf
%{_javadir}/%{name}/%{name}-jmf.jar
%{_javadir}/%{name}/%{name}-jmf-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jmf
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-jmf-%{version}.jar.*
%endif

%files nodeps
%{_javadir}/%{name}/%{name}-nodeps.jar
%{_javadir}/%{name}/%{name}-nodeps-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/nodeps
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-nodeps-%{version}.jar.*
%endif

%files swing
%{_javadir}/%{name}/%{name}-swing.jar
%{_javadir}/%{name}/%{name}-swing-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/swing
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-swing-%{version}.jar.*
%endif

%files trax
%{_javadir}/%{name}/%{name}-trax.jar
%{_javadir}/%{name}/%{name}-trax-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/trax
%{ant_home}/etc/mmetrics-frames.xsl
%{ant_home}/etc/coverage-frames.xsl
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-trax-%{version}.jar.*
%endif

%if %without bootstrap
%if %with manifest_only
%files manifest-only
%{_javadir}/%{name}/ant17-icontract-%{version}.jar
%{_javadir}/%{name}/ant17-icontract.jar
%{_javadir}/%{name}/ant17-netrexx-%{version}.jar
%{_javadir}/%{name}/ant17-netrexx.jar
%{_javadir}/%{name}/ant17-starteam-%{version}.jar
%{_javadir}/%{name}/ant17-starteam.jar
%{_javadir}/%{name}/ant17-stylebook-%{version}.jar
%{_javadir}/%{name}/ant17-stylebook.jar
%{_javadir}/%{name}/ant17-vaj-%{version}.jar
%{_javadir}/%{name}/ant17-vaj.jar
%{_javadir}/%{name}/ant17-weblogic-%{version}.jar
%{_javadir}/%{name}/ant17-weblogic.jar
%{_javadir}/%{name}/ant17-xalan1-%{version}.jar
%{_javadir}/%{name}/ant17-xalan1.jar
%{_javadir}/%{name}/ant17-xslp-%{version}.jar
%{_javadir}/%{name}/ant17-xslp.jar
%endif

%files antlr
%{_javadir}/%{name}/%{name}-antlr.jar
%{_javadir}/%{name}/%{name}-antlr-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/antlr
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-antlr-%{version}.jar.*
%endif

%files apache-bsf
%{_javadir}/%{name}/%{name}-apache-bsf.jar
%{_javadir}/%{name}/%{name}-apache-bsf-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bsf
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-apache-bsf-%{version}.jar.*
%endif

%files apache-resolver
%{_javadir}/%{name}/%{name}-apache-resolver.jar
%{_javadir}/%{name}/%{name}-apache-resolver-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-resolver
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-apache-resolver-%{version}.jar.*
%endif

%files commons-logging
%{_javadir}/%{name}/%{name}-commons-logging.jar
%{_javadir}/%{name}/%{name}-commons-logging-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-logging
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-commons-logging-%{version}.jar.*
%endif

%files commons-net
%{_javadir}/%{name}/%{name}-commons-net.jar
%{_javadir}/%{name}/%{name}-commons-net-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-net
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-commons-net-%{version}.jar.*
%endif

# Disable as we dont ship the dependencies
%if 0
%files jai
%{_javadir}/%{name}/%{name}-jai.jar
%{_javadir}/%{name}/%{name}-jai-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jai
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-jai-%{version}.jar.*
%endif
%endif

%files apache-bcel
%{_javadir}/%{name}/%{name}-apache-bcel.jar
%{_javadir}/%{name}/%{name}-apache-bcel-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-bcel.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bcel
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-apache-bcel-%{version}.jar.*
%endif

%files apache-log4j
%{_javadir}/%{name}/%{name}-apache-log4j.jar
%{_javadir}/%{name}/%{name}-apache-log4j-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-log4j.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-log4j
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-apache-log4j-%{version}.jar.*
%endif

%files apache-oro
%{_javadir}/%{name}/%{name}-apache-oro.jar
%{_javadir}/%{name}/%{name}-apache-oro-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-oro.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-oro
%{ant_home}/etc/maudit-frames.xsl
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-apache-oro-%{version}.jar.*
%endif

%files apache-regexp
%{_javadir}/%{name}/%{name}-apache-regexp.jar
%{_javadir}/%{name}/%{name}-apache-regexp-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-regexp.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-regexp
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-apache-regexp-%{version}.jar.*
%endif

%files javamail
%{_javadir}/%{name}/%{name}-javamail.jar
%{_javadir}/%{name}/%{name}-javamail-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/javamail
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-javamail-%{version}.jar.*
%endif

%files jdepend
%{_javadir}/%{name}/%{name}-jdepend.jar
%{_javadir}/%{name}/%{name}-jdepend-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jdepend
%{ant_home}/etc/jdepend.xsl
%{ant_home}/etc/jdepend-frames.xsl
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-jdepend-%{version}.jar.*
%endif

%files jsch
%{_javadir}/%{name}/%{name}-jsch.jar
%{_javadir}/%{name}/%{name}-jsch-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jsch
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-jsch-%{version}.jar.*
%endif

%files junit
%{_javadir}/%{name}/%{name}-junit.jar
%{_javadir}/%{name}/%{name}-junit-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/junit
%{ant_home}/etc/junit-frames.xsl
%{ant_home}/etc/junit-noframes.xsl
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ant17-junit-%{version}.jar.*
%endif

%files scripts
#%defattr(0755,root,root,0755)
%{_bindir}/*.pl
%{_bindir}/*.py*

%files manual
%doc --no-dereference docs/*

%if %{build_javadoc}
%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%endif
%endif

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

# -----------------------------------------------------------------------------

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt3_13jpp6
- built with java 6 due to abstract getParentLogger

* Sun Dec 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt2_13jpp6
- fixed build with new commons-net

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_13jpp6
- compat version for future ant upgrade to 1.8.x

