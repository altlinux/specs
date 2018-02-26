Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define oname   subethasmtp

Name:           subethasmtp1
Version:        1.2.1
Release:        alt1_2jpp6
Epoch:          0
Summary:        A multithreaded standalone SMTP mail server implementation

Group:          Development/Java
License:        Apache License 2.0
URL:            http://subethasmtp.tigris.org
Source0:        subethasmtp-1.2.1-src.tar.gz
# svn export http://subethasmtp.googlecode.com/svn/tags/1.2.1 subethasmtp-1.2.1-src
Patch0:         subethasmtp-1.2.1-build.patch

BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
BuildRequires: jakarta-commons-logging
BuildRequires: glassfish-javamail
BuildRequires: jaf_1_1_api
BuildRequires: junit4
BuildRequires: retroweaver
BuildRequires: slf4j

Requires: jakarta-commons-logging
Requires: javamail_1_4_api
Requires: jaf_1_1_api
Requires: slf4j

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
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
%setup -q -n %{oname}-%{version}-src
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0

%build
#ant smtp-jar junit javadoc
export CLASSPATH=$(build-classpath commons-logging glassfish-javamail)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first \
 -Dretroweaver.home=%{_javadir} \
 -Dretroweaver.version=2.0.2 \
 smtp-jar \
 smtp-jdk1.4-jar \
 wiser-jar \
 wiser-jdk1.4-jar \
 javadoc \
 junit \


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/subetha-smtp.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-smtp-%{version}.jar
install -m 644 build/subetha-wiser.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-wiser-%{version}.jar
install -m 644 build/subetha-smtp-jdk1.4.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-smtp-java14-%{version}.jar
install -m 644 build/subetha-wiser-jdk14.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-wiser-java14-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.subethamail subethasmtp-parent %{version} JPP %{name}
install -m 644 wiser/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-wiser.pom
%add_to_maven_depmap org.subethamail subethasmtp-wiser %{version} JPP %{name}-wiser
%add_to_maven_depmap org.subethamail subethasmtp-wiser-java14 %{version} JPP %{name}-wiser-java14
install -m 644 smtp/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-smtp.pom
%add_to_maven_depmap org.subethamail subethasmtp-smtp %{version} JPP %{name}-smtp
%add_to_maven_depmap org.subethamail subethasmtp-smtp-java14 %{version} JPP %{name}-smtp-java14

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_2jpp6
- new version

