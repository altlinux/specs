Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define namedversion 4.0.0.GA

Name:           jboss-dtf
Version:        4.0.0
Release:	alt2_3jpp6
Epoch:          0
Summary:        Java distributed testing framework
Group:          Development/Java
License:        LGPLv2+
URL:            http://jargs.sourceforge.net/
# svn export http://anonsvn.jboss.org/repos/dtf/tags/DTF_4_0_0_GA/ jboss-dtf-4.0.0
Source0:        jboss-dtf-4.0.0.tar.gz
Patch0:         jboss-dtf-build.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: ant
Requires: itext
Requires: jaf_1_1_api
Requires: jakarta-commons-fileupload
Requires: javamail_1_4_api
Requires: jdom
Requires: junit
Requires: log4j
Requires: servlet_2_5_api
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant
BuildRequires: junit
BuildRequires: glassfish-javamail
BuildRequires: itext
BuildRequires: jaf_1_1_api
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-io
BuildRequires: jdom
BuildRequires: log4j
BuildRequires: mysql-connector-java
BuildRequires: servlet_2_5_api
BuildArch:      noarch

%description
JBoss distributed testing framework.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0
#BUILD/jboss-dtf-4.0.0/lib/activation.jar.no
ln -sf $(build-classpath jaf_1_1_api) lib/activation.jar
#BUILD/jboss-dtf-4.0.0/lib/ant.jar.no
ln -sf $(build-classpath ant) lib/ant.jar
#BUILD/jboss-dtf-4.0.0/lib/ant-launcher.jar.no
ln -sf $(build-classpath ant-launcher) lib/ant-launcher.jar
#BUILD/jboss-dtf-4.0.0/lib/commons-fileupload-1.2.1.jar.no
ln -sf $(build-classpath commons-fileupload) lib/commons-fileupload-1.2.1.jar
#BUILD/jboss-dtf-4.0.0/lib/commons-io-1.3.2.jar.no
ln -sf $(build-classpath commons-io) lib/commons-io-1.3.2.jar
#BUILD/jboss-dtf-4.0.0/lib/fscontext.jar.no

#BUILD/jboss-dtf-4.0.0/lib/iText-2.0.8.jar.no
ln -sf $(build-classpath itext) lib/iText-2.0.8.jar
#BUILD/jboss-dtf-4.0.0/lib/jdom.jar.no
ln -sf $(build-classpath jdom) lib/jdom.jar
#BUILD/jboss-dtf-4.0.0/lib/junit.jar.no
ln -sf $(build-classpath junit) lib/junit.jar
#BUILD/jboss-dtf-4.0.0/lib/log4j-1.2.15.jar.no
ln -sf $(build-classpath log4j) lib/log4j-1.2.15.jar
#BUILD/jboss-dtf-4.0.0/lib/mailapi.jar.no
ln -sf $(build-classpath glassfish-javamail/mailapi) lib/mailapi.jar
#BUILD/jboss-dtf-4.0.0/lib/mysql-connector-java-5.1.6-bin.jar.no
ln -sf $(build-classpath mysql-connector-java) lib/mysql-connector-java-5.1.6-bin.jar
#BUILD/jboss-dtf-4.0.0/lib/providerutil.jar.no

#BUILD/jboss-dtf-4.0.0/lib/servlet-2_5-api.jar.no
ln -sf $(build-classpath servlet_2_5_api) lib/servlet-2_5-api.jar
#BUILD/jboss-dtf-4.0.0/lib/smtp.jar.no
ln -sf $(build-classpath glassfish-javamail/smtp) lib/smtp.jar

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist create-javadocs

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 dist/lib/TestingFramework.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/TestingFramework-%{version}.jar
install -m 644 dist/lib/DTFTools.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/DTFTools-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -m 644 dist/dtf.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/DTFTools-%{version}.jar
%{_javadir}/%{name}/DTFTools.jar
%{_javadir}/%{name}/TestingFramework-%{version}.jar
%{_javadir}/%{name}/TestingFramework.jar
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/dtf.war

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.0.0-alt2_3jpp6
- built with java 6 due to com.sun.image.codec.jpeg

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.0-alt1_3jpp6
- new version

