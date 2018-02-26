Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2005, JPackage Project
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

%define sname		jrunit

Summary:	JBoss JRunit
URL:		http://labs.jboss.com/portal/index.html?ctrl:id=page.default.info&project=jrunit
Source0:	jboss-jrunit-1.0-b2-src.tar.gz
#cvs -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r HEAD jrunit
# 2006/04/25
Patch0:		jboss-jrunit-build_xml.patch
Patch1:		jboss-jrunit-project_properties.patch
Patch2:		jboss-jrunit-TestDriver.patch
Patch3:		jboss-jrunit-DatabaseTestProperties.patch

Name:		jboss-jrunit
Version:	1.0
Release:	alt4_0.b2.2jpp5
Epoch:		0
License:	LGPL
Group:		Development/Java
BuildArch:	noarch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-logging
BuildRequires: concurrent
BuildRequires: hsqldb
BuildRequires: servletapi5
BuildRequires: jcommon
BuildRequires: jfreechart
BuildRequires: jgroups
BuildRequires: junit
BuildRequires: log4j
Requires: jpackage-utils >= 0:1.6
Requires: concurrent
Requires: jakarta-commons-logging
Requires: jgroups
Requires: junit
Requires: log4j

%description
JBoss JRunit is a project to aid in adding benchmarking to 
JUnit based test cases as well as providing a framework 
extension to JUnit to allow for distributed client/server 
based tests. It is important to note that JBoss JRunit is 
not a replacement for the popular test framework JUnit, but 
an extention to it allowing for more enterprise focused features.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}

%package demo
Summary:        Usage examples for %{name}
Group:          Development/Documentation

%description demo
%{summary}

%prep
%setup -q -n %{sname}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
mkdir -p db

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav

%build
pushd lib
#BUILD/jrunit/lib/ant.jar.no
ln -sf $(build-classpath ant) .
#BUILD/jrunit/lib/commons-logging.jar.no
ln -sf $(build-classpath commons-logging) .
#BUILD/jrunit/lib/concurrent.jar.no
ln -sf $(build-classpath concurrent) .
#BUILD/jrunit/lib/hsqldb.jar.no
ln -sf $(build-classpath hsqldb) .
#BUILD/jrunit/lib/javax.servlet.jar.no
ln -sf $(build-classpath servletapi5) javax.servlet.jar
#BUILD/jrunit/lib/jgroups.jar.no
ln -sf $(build-classpath jgroups) .
#mv jgroups.jar.no jgroups.jar
#BUILD/jrunit/lib/junit.jar.no
ln -sf $(build-classpath junit) .
#BUILD/jrunit/lib/log4j.jar.no
ln -sf $(build-classpath log4j) .
#
#tst#mkdir endorsed
#tst#pushd endorsed
#tst#ln -sf $(build-classpath xalan-j2-serializer) .
#tst#ln -sf $(build-classpath xalan-j2) .
#tst#ln -sf $(build-classpath xerces-j2) .
#tst#ln -sf $(build-classpath xml-commons-apis) .
#tst#popd
popd
pushd weblib
#BUILD/jrunit/weblib/commons-beanutils.jar.no
ln -sf $(build-classpath commons-beanutils) .
#BUILD/jrunit/weblib/commons-logging-api.jar.no
ln -sf $(build-classpath commons-logging-api) .
#BUILD/jrunit/weblib/commons-logging.jar.no
ln -sf $(build-classpath commons-logging) .
#BUILD/jrunit/weblib/jcommon-1.0.0-rc1.jar.no
ln -sf $(build-classpath jcommon) .
#BUILD/jrunit/weblib/jfreechart-1.0.0-rc1.jar.no
ln -sf $(build-classpath jfreechart) .
popd

#tst#ant -Djava-endorsed.dirs=$(pwd)/lib/endorsed distribution web-app javadocs run-tests
export ANT_OPTS="-Xmx256m"
export OPT_JAR_LIST="ant/ant-junit junit xalan-j2-serializer"
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 distribution web-app javadocs

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 output/jar/jrunit.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -p -m 0644 output/war/jrunit-report.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# demo
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples
cp -pr src/samples/*   $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/*
%{_datadir}/%{name}-%{version}/*.war

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}/samples

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.b2.2jpp5
- built with java 6 due to com.sun.image.codec.jpeg

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b2.2jpp5
- new version

* Mon Oct 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.dev.3jpp1.7
- disabled tests

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.dev.3jpp1.7
- converted from JPackage by jppimport script

