BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2011, JPackage Project
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

Name:           simple-jndi
Version:        0.11.4.1
Release:        alt2_2jpp6
Summary:        Simple JNDI

Group:          Development/Java
License:        BSD style
URL:            http://www.osjava.org/simple-jndi

Source0:        http://dist.osjava.org/releases/official/simple-jndi/simple-jndi-0.11.4.1-src.tar.gz
Source1:        http://repo1.maven.org/maven2/simple-jndi/simple-jndi/0.11.4.1/simple-jndi-0.11.4.1.pom

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  junit
BuildRequires:  apache-commons-parent
BuildRequires:  apache-commons-dbcp
BuildRequires:  apache-commons-pool

Requires:  apache-commons-dbcp
Requires:  apache-commons-pool

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
Simple-JNDI is intended to solve two problems. The first is
that of finding a container independent way of opening a 
database connection, the second is to find a good way of 
specifying application configurations.
1. Unit tests or prototype code often need to emulate the 
   environment within which the code is expected to run. 
   A very common one is to get an object of type 
   javax.sql.DataSource from JNDI so a java.sql.Connection 
   to your database of choice may be opened.
2. Applications need configuration; a JNDI implementation 
   makes a handy location for configuration values. Either 
   as a globally available system, or via IoC through the 
   use of some kind of JNDI configuration facade (see gj-config).
A solution: simple implementation of JNDI. It is entirely 
library based, so no server instances are started, and it 
sits upon Java .properties files, XML files or Windows-style 
.ini files, so it is easy to use and simple to understand.
The files may be either on the file system or in the classpath. 

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dlibdir=lib \
    -Dcommons-pool.jar=file://$(build-classpath commons-pool) \
    -Dcommons-dbcp.jar=file://$(build-classpath commons-dbcp) \
     jar javadoc

%install
%__rm -rf %{buildroot}

# jar
%__install -d -m 755 %{buildroot}%{_javadir}
%__install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
install -m 644 %{SOURCE1} \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

%__install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt2_2jpp6
- built with java 6 due to abstract getParentLogger

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt1_2jpp6
- new jpp relase

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.4.1-alt1_1jpp6
- new version

