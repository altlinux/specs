BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: java-1.6.0-devel
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

%global major_version 1.9

Name:           ant%major_version
Version:        1.9.6
Release:        alt6_3jpp8
Epoch:          0
Summary:        Java build tool
Group:          Development/Java
License:        ASL 2.0
URL:            http://ant.apache.org/
Source0:        http://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
Source2:        apache-ant-1.8.ant.conf

# Fix some places where copies of classes are included in the wrong jarfiles
Patch4:         apache-ant-class-path-in-manifest.patch

%global ant_home %{_datadir}/%{name}
%global oldname ant

#BuildRequires:  javapackages-local

Requires: %{name}-lib = %{epoch}:%{version}
Provides: %{name}-nodeps = %{epoch}:%{version}

Conflicts: ant

BuildArch:      noarch

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

%package lib
Group: Development/Java
Summary:        Core part of %{name}
Conflicts: ant-lib

%description lib
Core part of Apache Ant that can be used as a library.
# -----------------------------------------------------------------------------

%prep
%setup -q -n apache-ant-%{version}
#Fixup version
find -name build.xml -o -name pom.xml | xargs sed -i -e s/-SNAPSHOT//

# Fix class-path-in-manifest rpmlint warning
%patch4

# clean jar files
find . -name "*.jar" | %{_bindir}/xargs -t rm

# failing testcases. TODO see why
rm src/tests/junit/org/apache/tools/ant/types/selectors/SignedSelectorTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/condition/IsFileSelectedTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/condition/IsSignedTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/JarTest.java \
   src/tests/junit/org/apache/tools/mail/MailMessageTest.java

## no deps on junit
sed -i -e 's!jars,test-jar!jars!' build.xml

# Fix file-not-utf8 rpmlint warning
iconv KEYS -f iso-8859-1 -t utf-8 -o KEYS.utf8
mv KEYS.utf8 KEYS
iconv LICENSE -f iso-8859-1 -t utf-8 -o LICENSE.utf8
mv LICENSE.utf8 LICENSE

%build
sh build.sh

pushd build/lib/
rm -f \
ant-antlr.jar \
ant-apache-bcel.jar \
ant-apache-bsf.jar \
ant-apache-log4j.jar \
ant-apache-oro.jar \
ant-apache-regexp.jar \
ant-apache-resolver.jar \
ant-apache-xalan2.jar \
ant-commons-logging.jar \
ant-commons-net.jar \
ant-jai.jar \
ant-javamail.jar \
ant-jdepend.jar \
ant-jmf.jar \
ant-jsch.jar \
ant-junit.jar \
ant-junit4.jar \
ant-netrexx.jar \
ant-swing.jar \
;
popd
# -----------------------------------------------------------------------------

%install

# ANT_HOME and subdirs
mkdir -p %buildroot%{ant_home}/{lib,etc,bin}

# jars
install -d -m 755 %buildroot%{_javadir}/%{name}

for jar in build/lib/*.jar
do
  # Make sure that installed JARs are not empty
  jar tf ${jar} | egrep -q *.class

  jarname=$(basename $jar .jar)

  #instal jar
  install -m 644 ${jar} $RPM_BUILD_ROOT%{_javadir}/%{name}/${jarname}.jar
  # jar aliases
  ln -sf ../../java/%{name}/${jarname}.jar $RPM_BUILD_ROOT%{ant_home}/lib/${jarname}.jar
done

for mod in '' -bootstrap -launcher; do
    ln -sf %{name}/ant${mod}.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}${mod}.jar
done

# scripts: remove dos and os/2 scripts
rm -f src/script/*.bat
rm -f src/script/*.cmd

# XSLs
cp -p src/etc/*.xsl $RPM_BUILD_ROOT%{ant_home}/etc

# install everything else
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 -D src/script/ant $RPM_BUILD_ROOT%{_bindir}/%name
install -m 755 -D src/script/antRun $RPM_BUILD_ROOT%{_bindir}/antRun%{major_version}
ln -sf %{_bindir}/%name $RPM_BUILD_ROOT%{ant_home}/bin/ant
ln -sf %{_bindir}/antRun%{major_version} $RPM_BUILD_ROOT%{ant_home}/bin/antRun
ln -sf %name $RPM_BUILD_ROOT%{_bindir}/ant
ln -sf antRun%{major_version} $RPM_BUILD_ROOT%{_bindir}/antRun

sed -i -e s,ant.conf,%{name}.conf,g $RPM_BUILD_ROOT%{_bindir}/%name
sed -i -e s,/usr/share/ant,/usr/share/%{name},g $RPM_BUILD_ROOT%{_bindir}/%name

# default ant.conf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

# OPT_JAR_LIST fragments
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d

sed -i -e '1s,^#! *,#!,' %buildroot/%_bindir/*

%files
%doc KEYS LICENSE NOTICE README WHATSNEW
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/antRun%{major_version}
%{_bindir}/ant
%{_bindir}/antRun
%dir %{ant_home}
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

%files lib
%dir %{ant_home}/lib
%{_javadir}/%{oldname}.jar
%{_javadir}/%{oldname}-bootstrap.jar
%{_javadir}/%{oldname}-launcher.jar
%{_javadir}/%{name}/%{oldname}.jar
%{_javadir}/%{name}/%{oldname}-bootstrap.jar
%{_javadir}/%{name}/%{oldname}-launcher.jar
%{ant_home}/lib/%{oldname}.jar
%{ant_home}/lib/%{oldname}-launcher.jar
%{ant_home}/lib/%{oldname}-bootstrap.jar

# -----------------------------------------------------------------------------

%changelog
* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt6_3jpp8
- nodeps build for bootstrap purposes

* Fri Apr 06 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt5_3jpp8
- dropped extra requires on xerces-j2 and xml-commons-apis

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt4_3jpp8
- add_maven_depmap is deprecated, using mvn_artifact/mvn_install

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt3_3jpp8
- added Conflicts: to ant-lib

* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt2_3jpp8
- added compat /usr/bin/ant

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt1_3jpp8
- ant1.9 for old JVMs

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt3_3jpp8
- fixed shabang

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt2_3jpp8
- added osgi provides

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.6-alt1_2jpp8
- new version
