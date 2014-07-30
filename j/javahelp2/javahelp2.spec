Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%def_without demo
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-compat
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
Release:	alt3_13jpp7
Summary:	JavaHelp is a full-featured, platform-independent, extensible help system 
License:	GPLv2 with exceptions
Url:		https://javahelp.dev.java.net/
Group:		Development/Java
# 
#
Source0:	https://javahelp.dev.java.net/files/documents/5985/59373/%{name}-src-%{version}.zip
Source1:	%{name}-jhindexer.sh
Source2:	%{name}-jhsearch.sh
BuildArch:	noarch
Requires:	jpackage-utils >= 0:1.5.32
BuildRequires:	jpackage-utils >= 0:1.5.32
BuildRequires:  jsp >= 0:2.0
BuildRequires:	ant ant-nodeps
BuildRequires:	servlet6
Source44: import.info

%description
JavaHelp software is a full-featured, platform-independent, extensible
help system that enables developers and authors to incorporate online
help in applets, components, applications, operating systems, and
devices. Authors can also use the JavaHelp software to deliver online
documentation for the Web and corporate Intranet.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
# fix files perms
chmod -R go=u-w *
# remove windows files
for file in `find . -type f -name .bat`; do rm -f $file; done

#
# This class provides native browser integration and would require
# JDIC project to be present. Currently there is no such jpackage.org
# package, so deleting the class. When JDIC package is created,
# add BuildProvides and remove the "rm" call.
#
rm jhMaster/JavaHelp/src/new/javax/help/plaf/basic/BasicNativeContentViewerUI.java

mkdir javahelp_nbproject/lib
ln -s %{_javadir}/jsp.jar javahelp_nbproject/lib/jsp-api.jar
ln -s %{_javadir}/servlet.jar javahelp_nbproject/lib/servlet-api.jar

%build
export CLASSPATH=$(build-classpath ant/ant-nodeps)
ant -f javahelp_nbproject/build.xml -Djdic-jar-present=true -Djdic-zip-present=true -Dservlet-jar-present=true -Dtomcat-zip-present=true release javadoc

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/jh2indexer
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/jh2search

install -m 644 javahelp_nbproject/dist/lib/jhall.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
#cp -pr jhMaster/JavaHelp/doc/public-spec/dtd $RPM_BUILD_ROOT%{_datadir}/%{name}
#cp -pr jhMaster/JavaHelp/demos $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr javahelp_nbproject/dist/lib/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
# create unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

mkdir -p $RPM_BUILD_ROOT`dirname /etc/jhindexer.conf`
touch $RPM_BUILD_ROOT/etc/jhindexer.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/jhsearch.conf`
touch $RPM_BUILD_ROOT/etc/jhsearch.conf

%files
%attr(0755,root,root) %{_bindir}/*
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%dir %{_datadir}/%{name}
%config(noreplace,missingok) /etc/jhindexer.conf
%config(noreplace,missingok) /etc/jhsearch.conf

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
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

