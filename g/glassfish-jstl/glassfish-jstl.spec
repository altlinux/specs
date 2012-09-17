BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name glassfish-jstl
%define version 1.2.0
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
%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with jdk6
%bcond_without          jdk6
%bcond_with          repolib

%define jar_name jstl
%define jstlver 1.2

%define repodir %{_javadir}/repository.jboss.com/sun-jstl/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

Name:           glassfish-jstl 
Version:        1.2.0
Release:        alt2_10jpp6
Epoch:          0
Summary:        GlassFish JSTL
License:        CDDL 1.0
Group:          Development/Java
URL:            http://jstl.dev.java.net/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-component-info.xml
Source2:        CDDLv1.0.txt
Source3:        jstl-1.2.pom
Patch0:         %{name}-%{version}-ant-hack.patch
Patch1:         %{name}-jdk6.patch
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  servletapi6 >= 0:6.0.10
BuildRequires:  jboss-web jboss-el-2.2-api
Provides:       jstl = 0:%{jstlver}
BuildArch:      noarch
Source44: import.info

%description
JavaServer Pages Standard Tag Library.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jaf-javadoc = 0:%{jstlver}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n appserv-jstl 
%{_bindir}/iconv -f iso88591 -t utf8 < %{SOURCE2} > CDDLv1.0.txt
%patch0 -p1
%if %with jdk6
%patch1 -p1
%endif

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Djavaee.jar=$(build-classpath servletapi6 jspapi6 jboss-el-2.2-api jboss-web) release jar

%install

#jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/
install -p -m 0644 build/release/%{jar_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap jstl jstl %{version} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir}/
ln -sf %{name}-%{version}.jar %{name}.jar  )
touch  $RPM_BUILD_ROOT%{_javadir}/jstl.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml

install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/jstl.jar
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jstl_glassfish-jstl<<EOF
%{_javadir}/jstl.jar	%{_javadir}/%{name}.jar	10100
EOF

%files
%_altdir/jstl_glassfish-jstl
%doc CDDLv1.0.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%exclude %{_javadir}/%{jar_name}.jar
%{_datadir}/maven2/poms/JPP.%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_10jpp6
- jpp6 release + fresh jboss-web

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_7jpp5
- selected java5 compiler explicitly

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_7jpp5
- new version

