BuildRequires: /proc
BuildRequires: jpackage-compat
# one of the sources is a zip file
BuildRequires: unzip
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

%define namedversion   1.3.1b

Name:           greenmail
Version:        1.3.1
Release:	alt2_3jpp6
Epoch:          0
Summary:        Email test server
Group:          Development/Java
License:        ASL 2.0
URL:            http://www.icegreen.com/greenmail/
Source0:        http://switch.dl.sourceforge.net/sourceforge/greenmail/greenmail-1.3.1b-src.zip
Source1:        %{name}-%{namedversion}.pom

BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant
BuildRequires: junit
BuildRequires: glassfish-javamail
BuildRequires: jaf_1_1_api
BuildRequires: slf4j

Requires: glassfish-javamail
Requires: jaf_1_1_api
Requires: slf4j

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
GreenMail is an open source, intuitive and easy-to-use test
suite of email servers for testing purposes.
Supports SMTP, POP3, IMAP with SSL socket support. 
GreenMail also provides a JBoss GreenMail Service.
GreenMail is the fist and only library that offers a test 
framework for both receiving and retrieving emails from Java. 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -c
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
pushd lib
ln -sf $(build-classpath slf4j/slf4j-api) slf4j-api-1.5.6.jar
ln -sf $(build-classpath slf4j/slf4j-simple) slf4j-simple-1.5.6.jar
ln -sf $(build-classpath glassfish-javamail-monolithic) mail.jar
ln -sf $(build-classpath jaf_1_1_api) activation.jar
ln -sf $(build-classpath junit) junit.jar
popd

%build
export OPT_JAR_LIST=:
export CLASSPATH=
%{ant} all

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 build/lib/%{name}-%{namedversion}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.icegreen %{name} %{namedversion} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt2_3jpp6
- fixed buid with new slf4j

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_3jpp6
- new version

