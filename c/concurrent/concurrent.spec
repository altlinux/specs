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

#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%define reltag jboss-update1
%define repodir %{_javadir}/repository.jboss.com/oswego-concurrent/%{version}-%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           concurrent
Version:        1.3.4
Release:        alt1_10jpp6
Epoch:          0
Summary:        Utility classes for concurrent Java programming
License:        Public Domain
Source0:        http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/current/concurrent-1.3.4-src.tar.gz
# Source1 not used, kept for reference
Source1:        %{name}-%{version}.build.xml

Source2:	concurrent-component-info.xml
Source3:	concurrent-README.txt
Source4:        concurrent-1.3.4.pom
Patch0:		concurrent-build.patch
# This effectively fixes the oswego library.
# Several defects were found, including an unthreadsafe call to toArray()
Patch1:		concurrent-ConcurrentHashMap.patch
Patch2:		concurrent-ConcurrentReaderHashMap.patch
Patch3:		concurrent-PooledExecutor.patch
URL:            http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/util/concurrent/
Group:          Development/Java
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant
BuildRequires: /bin/bash
BuildRequires: zip
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description 
This package provides standardized, efficient versions of utility classes
commonly encountered in concurrent Java programming. This code consists of
implementations of ideas that have been around for ages, and is merely intended
to save you the trouble of coding them. Discussions of the rationale and
applications of several of these classes can be found in the second edition of
Concurrent Programming in Java.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:	        Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c

mkdir -p src/EDU/oswego/cs/dl/util
mv concurrent src/EDU/oswego/cs/dl/util

# Build with debug on
pushd src/EDU/oswego/cs/dl/util/concurrent
%patch0 -p0
popd

%patch1 -p0
%patch2 -p0
%patch3 -p0

# Pack sources in a proper way for loading into Eclipse
# Note that the sources for Eclipse contain the patches already
pushd src
find . -name "*.java" -print | zip ../concurrent-src.zip -@
popd
zip -d concurrent-src.zip EDU/oswego/cs/dl/util/concurrent/taskDemo/\*

%build
pushd src/EDU/oswego/cs/dl/util/concurrent

export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  dist javadoc

popd

%install
rm -fr $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
pwd
ls
install -m 644 src/EDU/oswego/cs/dl/util/concurrent/lib/%{name}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr src/EDU/oswego/cs/dl/util/concurrent/docs/* \
       $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# poms
%add_to_maven_depmap concurrent concurrent %{version} JPP %{name}
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE4} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-%{reltag}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{repodirsrc}/README.txt
install -p -m 0644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH3} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p concurrent-src.zip $RPM_BUILD_ROOT%{repodirlib}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/concurrent-1.3.4.jar.*
%endif
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_10jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_9jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_8jpp5
- converted from JPackage by jppimport script

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_7jpp1.7
- updated to new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_6jpp1.7
- converted from JPackage by jppimport script

