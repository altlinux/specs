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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/trove/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define section devel
%define old_name gnu.trove
%define short_name trove

Name:           gnu-%{short_name}
Version:        1.0.2
Release:	alt1_9jpp6
Epoch:          0
Summary:        High performance collections for Java
License:        LGPLv2+
URL:            http://trove4j.sourceforge.net/
Group:          Development/Java
Source0:        trove-1.0.2.tar.gz
Source1:        trove-build.xml
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/trove/trove/1.0.2/trove-1.0.2.pom
Source3:        gnu-trove-component-info.xml
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: junit
Obsoletes:      %{old_name} < %{epoch}:%{version}-%{release}
Provides:       %{old_name} = %{epoch}:%{version}-%{release}
BuildArch:      noarch
Source44: import.info

%description
The GNU Trove library has two objectives: 

Provide "free" (as in "free speech" and "free beer"), 
fast, lightweight implementations of the java.util 
Collections API. These implementations are designed 
to be pluggable replacements for their JDK equivalents. 

Whenever possible, provide the same collections support 
for primitive types. This gap in the JDK is often 
addressed by using the "wrapper" classes 
(java.lang.Integer, java.lang.Float, etc.) with 
Object-based collections. For most applications, however, 
collections which store primitives directly will require 
less space and yield significant performance gains. 

%if %with repolib
%package repolib
Summary:      Artifacts to be uploaded to a repository library
Group:        Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Obsoletes:      %{old_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{old_name}-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%{__cp} -p %{SOURCE1} build.xml

%build
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-%{version}.jar
%{__ln_s} %{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{old_name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap trove trove %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/trove.jar %{buildroot}%{repodirlib}/trove.jar
%endif

%files
%doc LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{old_name}-%{version}.jar
%{_javadir}/%{old_name}.jar
%{_javadir}/%{short_name}-%{version}.jar
%{_javadir}/%{short_name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_9jpp6
- added pom

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_7jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_6jpp5
- converted from JPackage by jppimport script

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_5jpp1.7
- converted from JPackage by jppimport script

