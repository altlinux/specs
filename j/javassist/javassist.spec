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

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'

%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/javassist//%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


%define reltag  GA

Name:           javassist
Version:        3.9.0
Release:        alt1_3jpp6
Epoch:          0
Summary:        Java Programming Assistant: bytecode manipulation
License:        MPLv1.1/LGPLv2.1
URL:            http://www.csg.is.titech.ac.jp/~chiba/javassist/
Group:          Development/Java
# cvs -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r rel_3_9_0_ga javassist
# tar cjf javassist-rel_3_9_0_ga-src.tar.bz2 javassist
Source0:        javassist-rel_3_9_0_ga-src.tar.bz2
Source1:        javassist-component-info.xml
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6
BuildArch:      noarch
Source44: import.info

%description
Javassist (Java Programming Assistant) makes Java bytecode manipulation 
simple. It is a class library for editing bytecodes in Java; it enables Java 
programs to define a new class at runtime and to modify a class file when the 
JVM loads it. Unlike other similar bytecode editors, Javassist provides two 
levels of API: source level and bytecode level. If the users use the 
source-level API, they can edit a class file without knowledge of the 
specifications of the Java bytecode. The whole API is designed with only the 
vocabulary of the Java language. You can even specify inserted bytecode in the 
form of source text; Javassist compiles it on the fly. On the other hand, the 
bytecode-level API allows the users to directly edit a class file as other 
editors.

%if %{with_repolib}
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Tutorial for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{name}
find . -name "*.jar" | xargs -t rm

mkdir tmpsrc
pushd src/main 2>&1 > /dev/null && \
%{jar} cf ../../tmpsrc/%{name}-src.jar %{name} && \
popd 2>&1 > /dev/null

%build
export OPT_JAR_LIST=:
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  dist

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr sample/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr html/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
cp -pr tutorial/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap javassist javassist %{version} JPP %{name}

%if %{with_repolib}
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/javassist.jar
cp -p tmpsrc/%{name}-src.jar $RPM_BUILD_ROOT%{repodirlib}/javassist-src.jar
%endif

%files
%doc License.html
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.9.0-alt1_3jpp6
- new versuin

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.8.0-alt1_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.8.0-alt1_1jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_0.cr1.2jpp1.7
- converted from JPackage by jppimport script

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt1
- Initial build for ALT Linux Sisyphus

