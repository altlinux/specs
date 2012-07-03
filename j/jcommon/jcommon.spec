Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%def_with repolib
%bcond_with repolib

%define repodir %{_javadir}/repository.jboss.com/jcommon/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           jcommon
Version:        1.0.16
Release:	alt2_2jpp6
Epoch:          0
Summary:        Common library
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jfree.org/jcommon/index.html
Source0:        http://downloads.sourceforge.net/project/jfreechart/3.%%%%20JCommon/1.0.16/jcommon-1.0.16.tar.gz
Source1:        %%{name}-component-info.xml
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/jfree/jcommon/1.0.16/jcommon-1.0.16.pom
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: ant
BuildRequires: junit
BuildRequires: jpackage-utils >= 0:1.7.3
BuildArch:      noarch
Source44: import.info

%description
Collection of classes used by Object Refinery Projects,
for example, jfreechart.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package test
Summary:        Test tasks for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: junit

%description test
All test tasks for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%description javadoc -l fr
Javadoc pour %{name}.

%prep
%setup -q
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%build
export CLASSPATH=$(%{_bindir}/build-classpath junit)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f ant/build.xml -Dbuildstable=true -Dproject.outdir=. -Dbasedir=. compile compile-junit-tests javadoc

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p jcommon-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -p lib/%{name}-%{version}-junit.jar %{buildroot}%{_javadir}/%{name}-junit-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap jfree jcommon %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{buildroot}%{_javadir}/jcommon.jar %{buildroot}%{repodirlib}
%endif

%files
%doc licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files test
%{_javadir}/%{name}-junit-%{version}.jar
%{_javadir}/%{name}-junit.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.16-alt2_2jpp6
- enabled repolib

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.16-alt1_2jpp6
- added pom

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.12-alt2_3jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.12-alt1_2jpp5
- converted from JPackage by jppimport script

* Fri Jun 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Tue Apr 26 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.0.0-alt0.1pre2
- First build for ALTLinux
