BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define oname   subethasmtp

Name:           subethasmtp2
Version:        2.1
Release:	alt3_3jpp6
Epoch:          0
Summary:        Multithreaded standalone SMTP mail server implementation
Group:          Development/Java
License:        ASL 2.0
URL:            http://subethasmtp.tigris.org
Source0:        subethasmtp-2.1.tar.gz
# svn export http://subethasmtp.googlecode.com/svn/tags/2.1/ subethasmtp-2.1
Source1:        http://repo1.maven.org/maven2/org/subethamail/subethasmtp/2.1.0/subethasmtp-2.1.0.pom

BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: glassfish-javamail
BuildRequires: jaf_1_1_api
BuildRequires: junit4
BuildRequires: mina11
BuildRequires: mina11-filter-ssl
BuildRequires: mina11-integration-jmx

BuildRequires: slf4j

Requires: glassfish-javamail
Requires: jaf_1_1_api
Requires: mina11
Requires: mina11-filter-ssl
Requires: mina11-integration-jmx
Requires: slf4j

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
A multithreaded standalone SMTP mail server 
implementation.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{oname}-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
pushd lib
ln -sf $(build-classpath slf4j/slf4j-api) slf4j-api-1.4.3.jar
ln -sf $(build-classpath slf4j/slf4j-jdk14) slf4j-jdk14-1.4.3.jar
ln -sf $(build-classpath junit) junit.jar
ln -sf $(build-classpath glassfish-javamail-monolithic) mail.jar
ln -sf $(build-classpath jaf_1_1_api) activation.jar
ln -sf $(build-classpath mina11/core) mina-core-1.1.7.jar
ln -sf $(build-classpath mina11/filter-ssl) mina-filter-ssl-1.1.7.jar
ln -sf $(build-classpath mina11/integration-jmx) mina-integration-jmx-1.1.7.jar
popd

%build
export LANG=en_US.ISO8859-1
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
export CLASSPATH=
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 smtp-jar junit javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 target/smtp/subethasmtp.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.subethamail subethasmtp 2.1.0 JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_3jpp6
- fixed build with java 7

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_3jpp6
- fixed buid with new slf4j

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_3jpp6
- new version

