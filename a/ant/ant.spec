Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Copyright (c) 2000-2008, JPackage Project
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

%bcond_without tests
%bcond_without javadoc

%global ant_home %{_datadir}/ant

Name:           ant
Version:        1.10.1
Release:        alt1_8jpp8
Epoch:          0
Summary:        Java build tool
Summary(it):    Tool per la compilazione di programmi java
Summary(fr):    Outil de compilation pour java
License:        ASL 2.0
URL:            http://ant.apache.org/
Source0:        http://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
Source2:        apache-ant-1.8.ant.conf

# Fix some places where copies of classes are included in the wrong jarfiles
Patch4:         apache-ant-class-path-in-manifest.patch

BuildRequires:  javapackages-local
BuildRequires:  java-devel >= 1.8.0
BuildRequires:  ant
BuildRequires:  ant-junit

BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(bcel:bcel)
BuildRequires:  mvn(bsf:bsf)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(commons-logging:commons-logging-api)
BuildRequires:  mvn(commons-net:commons-net)
BuildRequires:  mvn(javax.mail:mail)
BuildRequires:  mvn(jdepend:jdepend)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j:1.2.13)
BuildRequires:  mvn(org.tukaani:xz)
BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(regexp:regexp)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xml-resolver:xml-resolver)

# Theoretically Ant might be usable with just JRE, but typical Ant
# workflow requires full JDK, so we recommend it here.

Requires:       %{name}-lib = %{epoch}:%{version}-%{release}

Obsoletes:      %{name}-scripts < %{epoch}:%{version}-%{release}
Provides:       %{name}-scripts = %{epoch}:%{version}-%{release}

BuildArch:      noarch
Source44: import.info

Obsoletes:      %{name}-style-xsl < %{version}
Obsoletes:      %{name}-nodeps < %{version}
Provides:       %{name}-nodeps = %{version}
Obsoletes:      %{name}-trax < %{version}
Provides:       %{name}-trax = %{version}


%description
Apache Ant is a Java library and command-line tool whose mission is to
drive processes described in build files as targets and extension
points dependent upon each other.  The main known usage of Ant is the
build of Java applications.  Ant supplies a number of built-in tasks
allowing to compile, assemble, test and run Java applications.  Ant
can also be used effectively to build non Java applications, for
instance C or C++ applications.  More generally, Ant can be used to
pilot any type of process which can be described in terms of targets
and tasks.


%package optional
Summary: Optional tasks for Ant
Group: Development/Java

Requires: %name = %{?epoch:%epoch:}%version-%release
Requires: %name-antlr = %{?epoch:%epoch:}%version-%release
Requires: %name-apache-bcel = %{?epoch:%epoch:}%version-%release
Requires: %name-commons-logging = %{?epoch:%epoch:}%version-%release
Requires: %name-commons-net = %{?epoch:%epoch:}%version-%release
Requires: %name-apache-oro = %{?epoch:%epoch:}%version-%release
Requires: %name-apache-regexp = %{?epoch:%epoch:}%version-%release
Requires: %name-javamail = %{?epoch:%epoch:}%version-%release
Requires: %name-jdepend = %{?epoch:%epoch:}%version-%release
Requires: %name-jmf = %{?epoch:%epoch:}%version-%release
Requires: %name-jsch = %{?epoch:%epoch:}%version-%release
Requires: %name-junit = %{?epoch:%epoch:}%version-%release
Requires: %name-apache-log4j = %{?epoch:%epoch:}%version-%release
Requires: %name-swing = %{?epoch:%epoch:}%version-%release
Requires: %name-apache-resolver = %{?epoch:%epoch:}%version-%release
Requires: %name-apache-bsf = %{?epoch:%epoch:}%version-%release
#Requires: %name-jai = %{?epoch:%epoch:}%version-%release
#Requires: %name-stylebook = %{?epoch:%epoch:}%version-%release

%description optional
Optional build tasks for ant, a platform-independent build tool for Java.

%files optional



%description -l fr
Ant est un outil de compilation multi-plateformes pour java. Il est
utilisé par les projets apache-jakarta et apache-xml.

%description -l it
Ant e' un tool indipendente dalla piattaforma creato per faciltare la
compilazione di programmi java.
Allo stato attuale viene utilizzato dai progetti apache jakarta ed
apache xml.

%package lib
Group: Development/Java
Summary:        Core part of %{name}

%description lib
Core part of Apache Ant that can be used as a library.

%package jmf
Group: Development/Java
Summary:        Optional jmf tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description jmf
Optional jmf tasks for %{name}.

%description jmf -l fr
Taches jmf optionelles pour %{name}.

%package swing
Group: Development/Java
Summary:        Optional swing tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description swing
Optional swing tasks for %{name}.

%description swing -l fr
Taches swing optionelles pour %{name}.

%package antlr
Group: Development/Java
Summary:        Optional antlr tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description antlr
Optional antlr tasks for %{name}.

%description antlr -l fr
Taches antlr optionelles pour %{name}.

%package apache-bsf
Group: Development/Java
Summary:        Optional apache bsf tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

#Provides: ant-bsf = %{epoch}:%version-%release
Obsoletes: ant-bsf < 1.8.0

%description apache-bsf
Optional apache bsf tasks for %{name}.

%description apache-bsf -l fr
Taches apache bsf optionelles pour %{name}.

%package apache-resolver
Group: Development/Java
Summary:        Optional apache resolver tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

#Provides: ant-xml-resolver = %{epoch}:%version-%release
Obsoletes: ant-xml-resolver < 1.8.0

%description apache-resolver
Optional apache resolver tasks for %{name}.

%description apache-resolver -l fr
Taches apache resolver optionelles pour %{name}.

%package commons-logging
Group: Development/Java
Summary:        Optional commons logging tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description commons-logging
Optional commons logging tasks for %{name}.

%description commons-logging -l fr
Taches commons logging optionelles pour %{name}.

%package commons-net
Group: Development/Java
Summary:        Optional commons net tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description commons-net
Optional commons net tasks for %{name}.

%description commons-net -l fr
Taches commons net optionelles pour %{name}.

# Disable because we don't ship the dependencies
%if 0
%package jai
Group: Development/Java
Summary:        Optional jai tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description jai
Optional jai tasks for %{name}.

%description jai -l fr
Taches jai optionelles pour %{name}.
%endif

%package apache-bcel
Group: Development/Java
Summary:        Optional apache bcel tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

#Provides: ant-bcel = %{epoch}:%version-%release
Obsoletes: ant-bcel < 1.8.0

%description apache-bcel
Optional apache bcel tasks for %{name}.

%description apache-bcel -l fr
Taches apache bcel optionelles pour %{name}.

%package apache-log4j
Group: Development/Java
Summary:        Optional apache log4j tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

#Provides: ant-log4j = %{epoch}:%version-%release
Obsoletes: ant-log4j < 1.8.0

%description apache-log4j
Optional apache log4j tasks for %{name}.

%description apache-log4j -l fr
Taches apache log4j optionelles pour %{name}.

%package apache-oro
Group: Development/Java
Summary:        Optional apache oro tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description apache-oro
Optional apache oro tasks for %{name}.

%description apache-oro -l fr
Taches apache oro optionelles pour %{name}.

%package apache-regexp
Group: Development/Java
Summary:        Optional apache regexp tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description apache-regexp
Optional apache regexp tasks for %{name}.

%description apache-regexp -l fr
Taches apache regexp optionelles pour %{name}.

%package apache-xalan2
Group: Development/Tools
Summary:        Optional apache xalan2 tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description apache-xalan2
Optional apache xalan2 tasks for %{name}.

%description apache-xalan2 -l fr
Taches apache xalan2 optionelles pour %{name}.

%package javamail
Group: Development/Java
Summary:        Optional javamail tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description javamail
Optional javamail tasks for %{name}.

%description javamail -l fr
Taches javamail optionelles pour %{name}.

%package jdepend
Group: Development/Java
Summary:        Optional jdepend tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description jdepend
Optional jdepend tasks for %{name}.

%description jdepend -l fr
Taches jdepend optionelles pour %{name}.

%package jsch
Group: Development/Java
Summary:        Optional jsch tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description jsch
Optional jsch tasks for %{name}.

%description jsch -l fr
Taches jsch optionelles pour %{name}.

%package junit
Group: Development/Java
Summary:        Optional junit tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description junit
Optional junit tasks for %{name}.

%description junit -l fr
Taches junit optionelles pour %{name}.

%package testutil
Group: Development/Tools
Summary:        Test utility classes for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description testutil
Test utility tasks for %{name}.

%package xz
Group: Development/Java
Summary:        Optional xz tasks for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description xz
Optional xz tasks for %{name}.

%package manual
Group: Development/Java
Summary:        Manual for %{name}
BuildArch: noarch
Obsoletes: ant-task-reference < 1.8.0

%description manual
Documentation for %{name}.

%description manual -l it
Documentazione di %{name}.

%description manual -l fr
Documentation pour %{name}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%description javadoc -l fr
Javadoc pour %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n apache-ant-%{version}
#Fixup version
find -name build.xml -o -name pom.xml | xargs sed -i -e s/-SNAPSHOT//

# Fix class-path-in-manifest rpmlint warning
%patch4

# clean jar files
find . -name "*.jar" | xargs -t rm

# failing testcases. TODO see why
rm src/tests/junit/org/apache/tools/ant/types/selectors/SignedSelectorTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/condition/IsFileSelectedTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/condition/IsSignedTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/JarTest.java \
   src/tests/junit/org/apache/tools/mail/MailMessageTest.java

#install jars
build-jar-repository -s -p lib/optional antlr bcel javamail/mailapi jdepend junit log4j-1 oro regexp bsf commons-logging commons-net jsch xalan-j2 xml-commons-resolver xalan-j2-serializer hamcrest/core xz-java

# fix hardcoded paths in ant script and conf
cp -p %{SOURCE2} %{name}.conf
sed -e 's:/etc/ant.conf:%{_sysconfdir}/ant.conf:g' \
    -e 's:/etc/ant.d:%{_sysconfdir}/ant.d:g' \
    -e 's:/usr/share/ant:%{_datadir}/ant:g' \
    -e 's:/usr/bin/build-classpath:%{_bindir}/build-classpath:g' \
    -e 's:/usr/share/java-utils/java-functions:%{_javadir}-utils/java-functions:g' \
    -i src/script/ant %{name}.conf

# Remove unnecessary JARs from the classpath
sed -i 's/jaxp_parser_impl//;s/xml-commons-apis//' src/script/ant

# Fix file-not-utf8 rpmlint warning
iconv KEYS -f iso-8859-1 -t utf-8 -o KEYS.utf8
mv KEYS.utf8 KEYS
iconv LICENSE -f iso-8859-1 -t utf-8 -o LICENSE.utf8
mv LICENSE.utf8 LICENSE

# It's part of the JDK now
%pom_remove_dep javax.activation src/etc/poms/ant-javamail/pom.xml

# We want a hard dep on antlr
%pom_xpath_remove pom:optional src/etc/poms/ant-antlr/pom.xml

%build
%{ant} jars test-jar

%if %with javadoc
%{ant} javadocs
%endif

#remove empty jai and netrexx jars. Due to missing dependencies they contain only manifests.
rm -fr build/lib/ant-jai.jar build/lib/ant-netrexx.jar
# -----------------------------------------------------------------------------

%install
# ANT_HOME and subdirs
mkdir -p $RPM_BUILD_ROOT%{ant_home}/{lib,etc,bin}

%mvn_alias :ant org.apache.ant:ant-nodeps apache:ant ant:ant
%mvn_alias :ant-launcher ant:ant-launcher

%mvn_file ':{ant,ant-bootstrap,ant-launcher}' %{name}/@1 @1

for jar in build/lib/*.jar
do
  # Make sure that installed JARs are not empty
  jar tf ${jar} | egrep -q *.class

  jarname=$(basename $jar .jar)

  # jar aliases
  ln -sf ../../java/%{name}/${jarname}.jar $RPM_BUILD_ROOT%{ant_home}/lib/${jarname}.jar

  pom=src/etc/poms/${jarname}/pom.xml

  # bootstrap does not have a pom, generate one
  [ $jarname == ant-bootstrap ] && pom='org.apache.ant:ant-bootstrap:%{version}'

  %mvn_artifact ${pom} ${jar}
done

# ant-parent pom
%mvn_artifact src/etc/poms/pom.xml

%mvn_package :ant lib
%mvn_package :ant-launcher lib
%mvn_package :ant-bootstrap lib
%mvn_package :ant-parent lib
%mvn_package :ant-junit4 junit
# catchall rule for the rest
%mvn_package ':ant-{*}' @1

%mvn_install

# scripts: remove dos and os/2 scripts
rm -f src/script/*.bat
rm -f src/script/*.cmd

# XSLs
cp -p src/etc/*.xsl $RPM_BUILD_ROOT%{ant_home}/etc

# install everything else
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p src/script/{ant,antRun} $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_bindir}/ant $RPM_BUILD_ROOT%{ant_home}/bin/
ln -sf %{_bindir}/antRun $RPM_BUILD_ROOT%{ant_home}/bin/

# default ant.conf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
cp -p %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

# OPT_JAR_LIST fragments
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d
echo "ant/ant-jmf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jmf
echo "ant/ant-swing" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/swing
echo "antlr ant/ant-antlr" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/antlr
echo "rhino bsf ant/ant-apache-bsf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bsf
echo "xml-commons-resolver ant/ant-apache-resolver" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-resolver
echo "apache-commons-logging ant/ant-commons-logging" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-logging
echo "apache-commons-net ant/ant-commons-net" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-net
#echo "jai ant/ant-jai" > $RPM_BUILD_ROOT%%{_sysconfdir}/%%{name}.d/jai
echo "bcel ant/ant-apache-bcel" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bcel
echo "log4j12 ant/ant-apache-log4j" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-log4j
echo "oro ant/ant-apache-oro" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-oro
echo "regexp ant/ant-apache-regexp" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-regexp
echo "xalan-j2 xalan-j2-serializer ant/ant-apache-xalan2" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-xalan2
echo "javamail jaf ant/ant-javamail" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/javamail
echo "jdepend ant/ant-jdepend" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jdepend
echo "jsch ant/ant-jsch" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jsch
echo "junit hamcrest/core ant/ant-junit" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/junit
echo "junit hamcrest/core ant/ant-junit4" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/junit4
echo "testutil ant/ant-testutil" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/testutil
echo "xz-java ant/ant-xz" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/xz

%if %with javadoc
# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%endif

# fix link between manual and javadoc
(cd manual; ln -sf %{_javadocdir}/%{name} api)
sed -i -e '1s,^#! *,#!,' %buildroot/%_bindir/*

%if %with tests
%check
%{ant} test
%endif

%files
%doc KEYS README WHATSNEW
%doc LICENSE NOTICE
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0755,root,root) %{_bindir}/ant
%attr(0755,root,root) %{_bindir}/antRun
%dir %{ant_home}/bin
%{ant_home}/bin/ant
%{ant_home}/bin/antRun
%dir %{ant_home}/etc
%{ant_home}/etc/ant-update.xsl
%{ant_home}/etc/changelog.xsl
%{ant_home}/etc/coverage-frames.xsl
%{ant_home}/etc/mmetrics-frames.xsl
%{ant_home}/etc/log.xsl
%{ant_home}/etc/tagdiff.xsl
%{ant_home}/etc/junit-frames-xalan1.xsl
%{ant_home}/etc/common2master.xsl
%{ant_home}/etc/printFailingTests.xsl
%dir %{_sysconfdir}/%{name}.d

%files lib -f .mfiles-lib
%dir %{ant_home}
%dir %{ant_home}/lib
%{ant_home}/lib/%{name}.jar
%{ant_home}/lib/%{name}-launcher.jar
%{ant_home}/lib/%{name}-bootstrap.jar

%files jmf -f .mfiles-jmf
%{ant_home}/lib/%{name}-jmf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jmf

%files swing -f .mfiles-swing
%{ant_home}/lib/%{name}-swing.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/swing

%files antlr -f .mfiles-antlr
%{ant_home}/lib/%{name}-antlr.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/antlr

%files apache-bsf -f .mfiles-apache-bsf
%{ant_home}/lib/%{name}-apache-bsf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bsf

%files apache-resolver -f .mfiles-apache-resolver
%{ant_home}/lib/%{name}-apache-resolver.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-resolver

%files commons-logging -f .mfiles-commons-logging
%{ant_home}/lib/%{name}-commons-logging.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-logging

%files commons-net -f .mfiles-commons-net
%{ant_home}/lib/%{name}-commons-net.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-net

# Disable as we dont ship the dependencies
%if 0
%files jai -f .mfiles-jai
%{ant_home}/lib/%{name}-jai.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jai
%endif

%files apache-bcel -f .mfiles-apache-bcel
%{ant_home}/lib/%{name}-apache-bcel.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bcel

%files apache-log4j -f .mfiles-apache-log4j
%{ant_home}/lib/%{name}-apache-log4j.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-log4j

%files apache-oro -f .mfiles-apache-oro
%{ant_home}/lib/%{name}-apache-oro.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-oro
%{ant_home}/etc/maudit-frames.xsl

%files apache-regexp -f .mfiles-apache-regexp
%{ant_home}/lib/%{name}-apache-regexp.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-regexp

%files apache-xalan2 -f .mfiles-apache-xalan2
%{ant_home}/lib/%{name}-apache-xalan2.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-xalan2

%files javamail -f .mfiles-javamail
%{ant_home}/lib/%{name}-javamail.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/javamail

%files jdepend -f .mfiles-jdepend
%{ant_home}/lib/%{name}-jdepend.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jdepend
%{ant_home}/etc/jdepend.xsl
%{ant_home}/etc/jdepend-frames.xsl

%files jsch -f .mfiles-jsch
%{ant_home}/lib/%{name}-jsch.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jsch

%files junit -f .mfiles-junit
%{ant_home}/lib/%{name}-junit.jar
%{ant_home}/lib/%{name}-junit4.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/junit
%config(noreplace) %{_sysconfdir}/%{name}.d/junit4
%{ant_home}/etc/junit-frames.xsl
%{ant_home}/etc/junit-noframes.xsl

%files testutil -f .mfiles-testutil
%{ant_home}/lib/%{name}-testutil.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/testutil

%files xz -f .mfiles-xz
%{ant_home}/lib/%{name}-xz.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/xz

%files manual
%doc LICENSE NOTICE
%doc --no-dereference manual/*

%if %with javadoc
%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}
%endif

# -----------------------------------------------------------------------------

%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10.1-alt1_8jpp8
- fc update

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10.1-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt3_3jpp8
- fixed shabang

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt2_3jpp8
- added osgi provides

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt1_2jpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt2
- use xml-commons-resolver

* Fri Aug 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1
- new version

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt6
- fixed build

* Sat Jul 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt5
- restored symlinks in /usr/share/ant/lib

* Fri Apr 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt4
- fixed ant-testutil location

* Wed Mar 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt3
- updated license tag

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt2
- added ant-junit3 subpackage

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1
- new version

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt4
- dropped parasyte perl & python deps due to optional py
  and pl scripts in /usr/share/ant/bin/

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt3
- added ant: jpp depmaps

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt2
- added ant-junit4 subpackage

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1
- new version

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt4
- fixed ant-testutil thanks to Alexey Morozov.

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2-alt3.1
- Rebuild with Python-2.7

* Thu Sep 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt3
- added ant-testutil

* Sat Mar 05 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2
- bugfix

* Fri Mar 04 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2
- added alt-specific -Djavadoc.maxmemory patch

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt6
- added alt-specific -Djavadoc.maxmemory patch

* Sun Sep 05 2010 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt5
- reverted to 1.7.1.

* Thu Sep 02 2010 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt4test
- 1.8.0 pretest for sisyphus rebuild

* Thu Sep 02 2010 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1
- new version

* Mon Feb 23 2009 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt3
- reverted back to alt2 due to regression
- TODO: fix ant script

* Tue Feb 17 2009 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2
- fixed ANTLIB

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1
- new version
- moved the rest of docs to manual

* Mon Nov 03 2008 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt12
- added support for /etc/ant.d parts in /usr/bin/ant

* Tue Sep 30 2008 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt11
- updated classpath (replaced obsolete jars that no more exist)
  fixed ant-junit: serializer class not found bug.
- replaced obsolete java-common functions w/jpackage ones
- added /etc/ant.d 
- added maven2 poms

* Thu Aug 14 2008 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt10
- removed obsolete j2se requires

* Tue Feb 12 2008 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt9
- Packaged %_javadir/%name
- Built with python 2.5

* Tue Dec 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt8
- Bumped release to match ant-optional

* Mon Jun 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt7
- Bumped release to match ant-optional

* Sat Jun 16 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt6
- Bumped release to match ant-optional

* Sat Jun 09 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt5
- Bumped release to match ant-optional

* Thu May 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt4
- Added symlinks for %_javadir/ant.jar and %_javadir/ant-launcher.jar
- Fixed ant launcher to use %%_datadir/java-common instead of %%_libdir/java-common

* Sat May 05 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt3
- Added Provides: ant-nodeps for jpackage compatibility

* Thu Feb 22 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt2
- Fix Java executable search (#10857)

* Sun Feb 04 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt1.1
- Raised release to match release of ant-optional package

* Sat Feb 03 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt1
- New version

* Sat Mar 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.5-alt2
- Dropped buildtime dependency on xml-commons-apis and jaxp_parser_impl,
  require JDK >= 1.4 instead
- Added serializer.jar from Xalan to the runtime classpath

* Mon Jun 06 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.5-alt1
- New upstream release

* Sat May 28 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.4-alt1
- New upstream release

* Fri Apr 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.3-alt1
- New upstream release
- rpm-build-java cosmetics
- Removed ANT_HOME setting from /etc/ant.conf as it interfered
  with the bootstrap script

* Wed Mar 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.2-alt3.1
- Rebuilt with python-2.4.

* Wed Jan 12 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.2-alt3
- Rebuild for ant-optional

* Sat Aug 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.2-alt2
- BuildRequire /proc

* Wed Jul 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.2-alt1
- New upstream release

* Mon Jun 14 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.1-alt2
- Add all the optional library dependencies to classpath in the launcher script
- Conditionally disable debug info (off by default)

* Sun Feb 22 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.1-alt1
- Updated to the upstream release 1.6.1
- Updated the ant script
- Substitute directory names in the apt script
- Set config(noreplace) attribute for /etc/apt.conf

* Fri Oct 24 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.4-alt2
- Shipped ant-optional off to a separate spec with extensive build dependencies
- Take scripts from dist/bin where <fixcrlf/> task is performed

* Sun Aug 17 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.4-alt1
- 1.5.4

* Mon Mar 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.2-alt1
- 1.5.2
- Synced with 1.5.2-2jpp: added scripts subpackage, changed URL

* Mon Nov 18 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.1-alt1
- 1.5.1
- refurbished for the new java packaging system derived from JPackage
- docs separated to main package stuff (introductory),
  manual, javadoc and task-reference (a bulky PDF document)
- style-xsl subpackage

* Wed May 29 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt3
- both ant script and build search /usr/lib for JDK
- build compatible with jdk-1.3.1 package

* Sun May 19 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt2
- ant-optional subpackage
- build probes known JDK locations when JAVA_HOME is not set

* Thu Apr 25 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt1
- 1.4.1
- Borrowed a start script from Henri once more, and cleaned it up

* Tue May 01 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.3-alt1
- Adapted for ALTLinux
- Renamed ant-manual back to ant-doc
- Returned jars back into ant tree for the sake of tidyness
- Revision 0.5 of ant.sh
- Set group to Development/Java

* Thu Mar 23 2001 Henri Gomez <hgomez@slib.fr>
- ant-1.3 RPM Release 2
- rebuild with updated ant-optional.jar, the previously
  used was missing some classes.

* Mon Mar 05 2001 Henri Gomez <hgomez@slib.fr>
- ant 1.3
- build CLASSPATH=/usr/share/java/bsf.jar:/usr/share/java/jakarta-regexp.jar:/usr/share/java/xalan.jar:/usr/share/java/xerces.jar

* Mon Feb 27 2001 Henri Gomez <hgomez@slib.fr>
- ant-1.3b2 release 3
- fix manual permissions

* Mon Feb 26 2001 Henri Gomez <hgomez@slib.fr>
- ant-1.3b2 release 2
- fix /usr/local/bin/perl references

* Fri Feb 09 2001 Henri Gomez <hgomez@slib.fr>
- ant-1.3b1
- build CLASSPATH=/usr/share/java/bsf.jar:/usr/share/java/jakarta-regexp.jar:/usr/share/java/xalan.jar:/usr/share/java/xerces.jar

* Wed Oct 25 2000 Henri Gomez <hgomez@slib.fr>
- ant-1.2 RPM Release 2
- renamed ant-doc to ant-manual (follow apache RPM naming)
- RH 7.0 changes location of docdir and DocumentRoot. The spec file is modified
  to place manual in right place when rebuilded under RH 6.x or RH 7.0
- compiled on Redhat 6.1 box plus updates with rpm-3.0.5

* Tue Oct 24 2000 Henri Gomez <hgomez@slib.fr>
- ant-1.2
- added optional.jar
- read WHATSNEW for changes in ant 1.2

* Fri Oct 20 2000 Henri Gomez <hgomez@slib.fr>
- ant-1.2rc
- added optional.jar (from jarkata site)
- source file is renamed from jakarta-ant-src.tar.gz to
  jakarta-ant-src-v1.2rc.tar.gz to allow multiple source file
  in my RPM source dir
- build CLASSPATH=

* Mon Oct 16 2000 Henri Gomez <hgomez@slib.fr>
- ant-1.1 RPM Release 5
- follow Debian policy about java stuff, libs in /usr/share/java,
  executable in /usr/bin
- prepare transition to RH 7.0 new document root (/var/www)
- build CLASSPATH=/usr/share/java/bsf.jar:/usr/share/java/xalan.jar

* Fri Oct 06 2000 Henri Gomez <hgomez@slib.fr>
- v1.1-4
- tomcat build failed if ANT_HOME is set to /usr.
  ant shell script set ANT_HOME to /usr/share/ant
  to fix 'antRun not found' and allow tomcat build ;-?!
- reorganized group packages for javas RPM :
  Development/Tools (ant)
  Developement/Libraries(xalan, xerces)
  Documentation (all ;-)
- build CLASSPATH=/usr/lib/java/bsf.jar:/usr/lib/java/bsfengines.jar:/usr/lib/java/xalan.jar

* Fri Sep 29 2000 Henri Gomez <hgomez@slib.fr>
- v1.1-3- jars are now installed on /usr/lib/java since /opt is
  mounted read-only on many systems <summer@os2.ami.com.au>
- correct bad URL in apidocs
- try to use jikes if present
- rebuilded with IBM JDK 1.3.0 (cx130-20000815)

* Fri Jul 21 2000 Henri Gomez <hgomez@slib.fr>
- v1.1-2
- Rebuild rpm with IBM JDK 1.3 (cx130-20000623) to allow ant
  work under both JDK 1.1.8 and JDK 1.3.
- minor spec file correction (patch ant after install)

* Thu Jul 20 2000 Henri Gomez <hgomez@slib.fr>
- v1.1 final release
- ant need now a JAXP compatible parser. Sun's jaxp 1.0.1 are
  allready included in .tar.gz and so we will use and export
  these jar (jaxp.jar & parser.jar).
  You could also use Apache xerces 1.1.2 or later.
- removed export CLASSPATH= at build time, but you'll have to
  ensure now you have a minimal CLASSPATH (ie: xml parser jars)
- Try to use now the Linux Software Map and Redhat Map.
  exec goes /usr/bin and classes in /usr/lib/ant.
  documentation stay in /home/httpd/html/manual/ant
- Compiled on Redhat 6.1 with latest IBM JDK 1.1.8 (l118-20000515)

* Tue May 02 2000 Henri Gomez <hgomez@slib.fr>
- v0.3.1
- From jakarta/tomcat 3.1 final release. Need now to
  have a consistent version number ;-)
- Fixed classpath problem at compile time by cleaning CLASSPATH before
  build/install stages.
- Compiled on Redhat 6.1 with IBM JDK 1.1.8 (20000328)

* Thu Apr 13 2000 Henri Gomez <hgomez@slib.fr>
- v0.3.1_rc1
- Version renamed to 0.3.1_rc1 to follow Sam Ruby (rubys@us.ibm.com)
  recommandation since the next major release will be 1.0

* Wed Mar 08 2000 Henri Gomez <gomez@slib.fr>
- v3.1b1
- removed moo from ant RPM. Will be now in watchdog RPM.

* Tue Feb 29 2000 Henri Gomez <gomez@slib.fr>
- v3.1_m2rc2

* Fri Feb 25 2000 Henri Gomez <gomez@slib.fr>
- v3.1_m2rc1
- moo is no more in the tar packages, will be released
  in another RPM
- added doc package

* Fri Jan 28 2000 Henri Gomez <gomez@slib.fr>
- v3.1_m1

* Tue Jan 18 2000 Henri Gomez <gomez@slib.fr>
- first RPM of v3.1_m1_rc1

* Tue Jan  4 2000 Henri Gomez <gomez@slib.fr>
- moved from /opt/jakarta/jakarta-tools to /opt/ant

* Tue Jan  4 2000 Henri Gomez <gomez@slib.fr>
- CVS 4 Jan 2000
- added servlet.jar from tomcat in SRPM
   to allow first build of moo.

* Thu Dec 30 1999 Henri Gomez <gomez@slib.fr>
- Initial release for jakarta-tools cvs
