%def_without demo
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 2.0.05
%define name javahelp2
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


%global oname javahelp
%global namedversion %{version}

Name:           javahelp2
Version:        2.0.05
Release:        alt3_8jpp6
Epoch:          0
Summary:        JavaHelp
License:        LGPLv2 with the classpath exception
URL:            https://javahelp.dev.java.net/
Group:          Development/Java
#
# To get the source, build it from svn repository of 
# https://javahelp.dev.java.net/ 
# using following steps:
# svn checkout https://javahelp.dev.java.net/svn/javahelp/trunk javahelp --username guest -r 46
# cd javahelp
# ant -f javahelp_nbproject/build.xml release-source -Dversion=2.0.02_svn46
# the source file will be generated into 
# javahelp_nbproject/dist/javahelp2-src-2.0.02_svn46.zip
#
Source0:        %{name}-%{version}.tar.gz
# svn export -r 59 https://javahelp.dev.java.net/svn/javahelp/trunk javahelp2-2.0.05 --username guest
Source1:        %{name}-jhindexer.sh
Source2:        %{name}-jhsearch.sh
Source3:        %{oname}-%{version}.pom
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4
Requires:       jpackage-utils >= 0:1.7.4
Requires:       jsp_api >= 0:2.0
Requires:       servlet_api >= 0:2.4
BuildRequires:  jpackage-utils >= 0:1.7.4
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-nodeps
BuildRequires:  jsp_2_1_api
BuildRequires:  servlet_2_5_api
BuildArch:      noarch
Source44: import.info

%description
JavaHelp software is a full-featured, platform-independent, extensible
help system that enables developers and authors to incorporate online
help in applets, components, applications, operating systems, and
devices. Authors can also use the JavaHelp software to deliver online
documentation for the Web and corporate Intranet.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%if_with demo
%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
%endif #demo

%if_with demo
%description demo
Demonstrations and samples for %{name}.
%endif #demo

%prep
%setup -q 
# fix files perms
chmod -R go=u-w *

%{_bindir}/find -type f -name "*.bat" | %{_bindir}/xargs -t rm
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t rm

#
# This class provides native browser integration and would require
# JDIC project to be present. Currently there is no such jpackage.org
# package, so deleting the class. When JDIC package is created,
# add BuildProvides and remove the "rm" call.
#
rm jhMaster/JavaHelp/src/new/javax/help/plaf/basic/BasicNativeContentViewerUI.java

mkdir javahelp_nbproject/lib
ln -s %{_javadir}/jsp_2_1_api.jar javahelp_nbproject/lib/jsp-api.jar
ln -s %{_javadir}/servlet_2_5_api.jar javahelp_nbproject/lib/servlet-api.jar

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    -f javahelp_nbproject/build.xml \
    -Djdic-jar-present=true \
    -Djdic-zip-present=true \
    -Dservlet-jar-present=true \
    -Dtomcat-zip-present=true \
    release javadoc

%install

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
cp -p javahelp_nbproject/dist/lib/jh-client.jar %{buildroot}%{_javadir}/%{name}/jh-client-%{namedversion}.jar
cp -p javahelp_nbproject/dist/lib/jh.jar %{buildroot}%{_javadir}/%{name}/jh-%{namedversion}.jar
cp -p javahelp_nbproject/dist/lib/jhall.jar %{buildroot}%{_javadir}/%{name}/jhall-%{namedversion}.jar
cp -p javahelp_nbproject/dist/lib/jhbasic.jar %{buildroot}%{_javadir}/%{name}/jhbasic-%{namedversion}.jar
cp -p javahelp_nbproject/dist/lib/jsearch-client.jar %{buildroot}%{_javadir}/%{name}/jsearch-client-%{namedversion}.jar
cp -p javahelp_nbproject/dist/lib/jsearch-indexer.jar %{buildroot}%{_javadir}/%{name}/jsearch-indexer-%{namedversion}.jar
cp -p javahelp_nbproject/dist/lib/jsearch-misc.jar %{buildroot}%{_javadir}/%{name}/jsearch-misc-%{namedversion}.jar
cp -p javahelp_nbproject/dist/lib/jsearch.jar %{buildroot}%{_javadir}/%{name}/jsearch-%{namedversion}.jar
ln -s %{name}/jhall-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do ln -sf ${jar} ${jar/-%{namedversion}/}; done)
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{namedversion}*; do ln -sf ${jar} ${jar/-%{namedversion}/}; done)

# pom
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap javax.help %{oname} %{namedversion} JPP/%{name} jhall

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr javahelp_nbproject/dist/lib/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{_javadocdir}/%{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

# bin
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/jh2indexer
install -p -m 755 %{SOURCE2} %{buildroot}%{_bindir}/jh2search

# data
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr jhMaster/JavaHelp/doc/public-spec/dtd %{buildroot}%{_datadir}/%{name}
cp -pr jhMaster/JavaHelp/demos %{buildroot}%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/jhindexer.conf`
touch $RPM_BUILD_ROOT/etc/jhindexer.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/jhsearch.conf`
touch $RPM_BUILD_ROOT/etc/jhsearch.conf

%files
%doc jhMaster/JavaHelp/README jhMaster/JavaHelp/README.html jhMaster/JavaHelp/LICENSE.html
%attr(0755,root,root) %{_bindir}/*
%{_javadir}/%{name}-%{namedversion}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}/jh-%{version}.jar
%{_javadir}/%{name}/jh-client-%{version}.jar
%{_javadir}/%{name}/jh-client.jar
%{_javadir}/%{name}/jh.jar
%{_javadir}/%{name}/jhall-%{namedversion}.jar
%{_javadir}/%{name}/jhall.jar
%{_javadir}/%{name}/jhbasic-%{version}.jar
%{_javadir}/%{name}/jhbasic.jar
%{_javadir}/%{name}/jsearch-%{version}.jar
%{_javadir}/%{name}/jsearch-client-%{version}.jar
%{_javadir}/%{name}/jsearch-client.jar
%{_javadir}/%{name}/jsearch-indexer-%{version}.jar
%{_javadir}/%{name}/jsearch-indexer.jar
%{_javadir}/%{name}/jsearch-misc-%{version}.jar
%{_javadir}/%{name}/jsearch-misc.jar
%{_javadir}/%{name}/jsearch.jar
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/dtd
%{_datadir}/%{name}/dtd/favorites_2_0.dtd
%{_datadir}/%{name}/dtd/helpset_1_0.dtd
%{_datadir}/%{name}/dtd/helpset_2_0.dtd
%{_datadir}/%{name}/dtd/index_1_0.dtd
%{_datadir}/%{name}/dtd/index_2_0.dtd
%{_datadir}/%{name}/dtd/map_1_0.dtd
%{_datadir}/%{name}/dtd/map_2_0.dtd
%{_datadir}/%{name}/dtd/toc_1_0.dtd
%{_datadir}/%{name}/dtd/toc_2_0.dtd
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%config(noreplace,missingok) /etc/jhindexer.conf
%config(noreplace,missingok) /etc/jhsearch.conf

%files manual
%doc jhMaster/JavaHelp/doc/public-spec/*

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%if_with demo
%files demo
%{_datadir}/%{name}/demos
%endif #demo

%changelog
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

