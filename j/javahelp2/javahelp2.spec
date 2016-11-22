Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%def_without demo
%filter_from_requires /^.usr.bin.run/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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

Name:		javahelp2
Version:	2.0.05
Release:	alt3_19jpp8
Summary:	JavaHelp is a full-featured, platform-independent, extensible help system 
License:	GPLv2 with exceptions
Url:		https://javahelp.java.net/
Source0:	https://javahelp.dev.java.net/files/documents/5985/59373/%{name}-src-%{version}.zip
Source1:	%{name}-jhindexer.sh
Source2:	%{name}-jhsearch.sh
BuildArch:	noarch

BuildRequires:	javapackages-local

BuildRequires:	ant
BuildRequires:	tomcat-servlet-3.1-api
BuildRequires:	tomcat-jsp-2.3-api
Source44: import.info


%description
JavaHelp software is a full-featured, platform-independent, extensible
help system that enables developers and authors to incorporate online
help in applets, components, applications, operating systems, and
devices. Authors can also use the JavaHelp software to deliver online
documentation for the Web and corporate Intranet.

%package javadoc
Group: Development/Java
Summary:	Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
# fix files perms
chmod -R go=u-w *
# remove windows files
find . -name "*.bat" -delete
#
# This class provides native browser integration and would require
# JDIC project to be present. Currently there is no such jpackage.org
# package, so deleting the class. When JDIC package is created,
# add BuildProvides and remove the "rm" call.
#
rm jhMaster/JavaHelp/src/new/javax/help/plaf/basic/BasicNativeContentViewerUI.java

mkdir javahelp_nbproject/lib
ln -s %{_javadir}/tomcat-jsp-api.jar javahelp_nbproject/lib/jsp-api.jar
ln -s %{_javadir}/tomcat-servlet-api.jar javahelp_nbproject/lib/servlet-api.jar

%build

ant -f javahelp_nbproject/build.xml \
 -Djavac.source=1.6 -Djavac.target=1.6 \
 -Djdic-jar-present=true -Djdic-zip-present=true \
 -Dservlet-jar-present=true -Dtomcat-zip-present=true \
 -Djavadoc.additionalparam="-Xdoclint:none" \
 release javadoc

%install
# see https://svn.java.net/svn/javahelp~svn/trunk/jhMaster/jhall.pom
%mvn_file javax.help:javahelp %{name}
%mvn_artifact javax.help:javahelp:%{version} javahelp_nbproject/dist/lib/jhall.jar
%mvn_install -J javahelp_nbproject/dist/lib/javadoc

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
#cp -pr jhMaster/JavaHelp/doc/public-spec/dtd $RPM_BUILD_ROOT%%{_datadir}/%%{name}
#cp -pr jhMaster/JavaHelp/demos $RPM_BUILD_ROOT%%{_datadir}/%%{name}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/jh2indexer
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/jh2search

mkdir -p $RPM_BUILD_ROOT`dirname /etc/jhindexer.conf`
touch $RPM_BUILD_ROOT/etc/jhindexer.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/jhsearch.conf`
touch $RPM_BUILD_ROOT/etc/jhsearch.conf

%files -f .mfiles
%{_bindir}/*
%dir %{_datadir}/%{name}
%config(noreplace,missingok) /etc/jhindexer.conf
%config(noreplace,missingok) /etc/jhsearch.conf

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.05-alt3_19jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.05-alt3_18jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.05-alt3_15jpp7
- new release

* Wed Jul 30 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.05-alt3_13jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.0.05-alt3_12jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.05-alt3_8jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.05-alt3_2jpp5
- fixes for java6 support

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.05-alt2_2jpp5
- new jpp release

* Fri Oct 03 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.05-alt2_1jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.05-alt1_1jpp5
- converted from JPackage by jppimport script

