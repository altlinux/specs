Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
# Copyright (c) 2000-2009, JPackage Project
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

%define jbossdir %{_var}/jboss

Summary:        Database statement interceptor for Java
Name:           p6spy
Version:        1.3
Release:        alt2_4jpp5
Epoch:          0
Group:          Databases
License:        P6Spy Software License
URL:            http://p6spy.sourceforge.net/
BuildArch:      noarch
Source0:        http://download.sourceforge.net/p6spy/p6spy-src.jar
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/p6spy/p6spy/1.3/p6spy-1.3.pom
Patch0:         %{name}-jboss3.patch
Patch1:         %{name}-javadoc-crosslink.patch
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: java-javadoc
BuildRequires: ant >= 0:1.6.5
BuildRequires: gnu-regexp
BuildRequires: log4j
#BuildRequires:  jdbc-stdext
BuildRequires: jboss4-common
BuildRequires: jboss4-jmx
BuildRequires: jboss4-system
BuildRequires: log4j-javadoc
BuildRequires: regexp
Requires: gnu-regexp
Requires: log4j
Requires: regexp
#Requires:       jdbc-stdext
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3


%description
P6Spy is an open source framework for applications that intercept and
optionally modify database statements.

%package        javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Manual for %{name}
Group:          Databases
BuildArch: noarch

%description    manual
%{summary}.


%prep
%setup -q -c
%patch0 -p0
%patch1 -p0
rm -rf javadocs documentation/Templates documentation/_notes
mkdir lib


%build
CLASSPATH=%(build-classpath regexp gnu.regexp log4j jdbc-stdext)
export CLASSPATH=$CLASSPATH:\
$(build-classpath jboss4/jboss-common):\
$(build-classpath jboss4/jboss-jmx):\
$(build-classpath jboss4/jboss-system)
# Tests would need a DB to test against :(
ant \
  -Dbuild.sysclasspath=last \
  -Dlog4j.javadoc=%{_javadocdir}/log4j \
  -Dj2se.javadoc=%{_javadocdir}/java \
  clean release


%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/p6spy.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# webapp
# TODO: dist/p6spy.war to tomcat/jboss+jetty webapps dir
# TODO: make %{_javadir}/p6spy.jar available in tomcat/jboss+jetty classpath


%files
%doc license.txt spy.properties
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc documentation/*


%changelog
* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_4jpp5
- selected java5 compiler explicitly

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_4jpp5
- new jpp release

* Sat Mar 08 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_3jpp1.7
- built with jboss4

* Mon Jul 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1
- converted from JPackage by jppimport script
- hacked from version _3jpp1.7 (added by hands jboss jars)

