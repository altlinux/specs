BuildRequires: junit4
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

%define namedversion 2.0.0RC2

Name:           joone
Version:        2.0.0
Release:        alt3_0.rc2.1jpp6
Summary:        An Object Oriented Neural Engine

Group:          Development/Java
License:        LGPL
URL:            http://sourceforge.net/projects/joone/
Source0:        %{name}-%{namedversion}.tgz
# cvs -d:pserver:anonymous@joone.cvs.sourceforge.net:/cvsroot/joone login 
# cvs -z3 -d:pserver:anonymous@joone.cvs.sourceforge.net:/cvsroot/joone export -r HEAD joone
# tar czf ../SOURCES/joone-2.0.0RC2.tgz joone/

Source1:        %{name}-oat.tgz
# cvs -d:pserver:anonymous@joone.cvs.sourceforge.net:/cvsroot/joone login
# cvs -z3 -d:pserver:anonymous@joone.cvs.sourceforge.net:/cvsroot/joone co -P joone_oat
# tar czf ../SOURCES/joone-oat.tgz joone_oat/

Source2:        joone_oat-build.xml
Source3:        joone_oat-manifest.mf
Source4:        joone-%{version}.pom
Source5:        joone-editor-%{version}.pom
Source6:        joone-engine-%{version}.pom

Patch0:         joone-build.patch
Patch1:         joone_oat-StudentTTest.patch
Patch2:         joone_oat-KruskalWallisTest.patch
Patch3:         joone_oat-ANOVATest.patch
Patch4:         joone_oat-MannWhitneyUTest.patch
Patch5:         joone_oat-RunStatisticSummary.patch
Patch6:         joone-TimeSeriesDemo1.patch
Patch7:         joone-JooneGroovyScript.patch


BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant
BuildRequires: apache-poi
BuildRequires: axis
BuildRequires: bsh
BuildRequires: colt
BuildRequires: groovy15
BuildRequires: javahelp2
BuildRequires: jcommon
BuildRequires: jfreechart
BuildRequires: jhotdraw5
BuildRequires: l2fprod-common
BuildRequires: log4j
BuildRequires: nachocalendar
BuildRequires: osp
BuildRequires: socr
BuildRequires: ssj
BuildRequires: substance
BuildRequires: velocity14
BuildRequires: visad
BuildRequires: xstream

Requires: apache-poi
Requires: axis
Requires: bsh
Requires: colt
Requires: groovy15
Requires: javahelp2
Requires: jcommon
Requires: jfreechart
Requires: jhotdraw5
Requires: l2fprod-common
Requires: log4j
Requires: nachocalendar
Requires: osp
Requires: socr
Requires: ssj
Requires: substance
Requires: velocity14
Requires: visad
Requires: xstream

BuildArch:      noarch
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0


%description
Joone is a neural net framework written in Java(tm). It's 
composed by a core engine, a GUI editor and a distributed 
training environment and can be extended by writing new 
modules to implement new algorithms or architectures starting 
from base component.


%package javadoc
Summary:        Javadoc documentation for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
%{summary}.


%prep
%setup -q -n %{name}
gzip -dc %{SOURCE1} | tar xf -
cp %{SOURCE2} joone_oat/build.xml
mkdir -p joone_oat/src/META-INF/
cp %{SOURCE3} joone_oat/src/META-INF/MANIFEST.MF
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -s $(build-classpath axis/axis) lib
ln -s $(build-classpath jhotdraw5) lib
ln -s $(build-classpath bsh) lib
ln -s $(build-classpath colt) lib
ln -s $(build-classpath groovy15) lib
ln -s $(build-classpath javahelp2) lib
ln -s $(build-classpath jcommon) lib
ln -s $(build-classpath jfreechart) lib
ln -s $(build-classpath l2fprod-common/l2fprod-common-sheet) lib
ln -s $(build-classpath nachocalendar) lib
#ln -s $(build-classpath oat) lib
ln -s $(build-classpath poi/apache-poi) lib
ln -s $(build-classpath velocity14) lib
ln -s $(build-classpath visad) lib
ln -s $(build-classpath xstream) lib
ln -s $(build-classpath log4j) lib
ln -s $(build-classpath osp) lib
ln -s $(build-classpath socr/SOCR_core) lib
ln -s $(build-classpath socr/SOCR_plugin) lib
ln -s $(build-classpath ssj) lib
ln -s $(build-classpath substance) lib

#1. Create a directory structure as the following:
#${base}
#   |___joone  (the source base dir - checkout here the CVS joone module)
#   |     |__org
#   |     |__lib
#   |___build  (the executable base dir - filled running the 'build' and 'rebuild' ANT targets)
#   |___doc    (the javadoc base dir - filled running the 'doc' ANT target)
mkdir joone
mv doc org lib joone
mkdir build
mkdir doc
mkdir releases
%patch0 -b .orig
%patch1 -b .math
%patch2 -b .math
%patch3 -b .math
%patch4 -b .math
%patch5 -b .math
%patch6 -b .jfree
%patch7 -b .groovy15


%build
export LANG=en_US.ISO8859-1
pushd joone_oat
export CLASSPATH=$(build-classpath \
axis \
colt \
commons-math \
jcommon \
jfreechart \
junit4 \
osp \
socr/SOCR_core \
socr/SOCR_plugin \
ssj \
)
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first
popd
cp joone_oat/dist/DSTAMP/optalgtoolkit.jar joone/lib/oat.jar
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbase=$(pwd) build lbuild doc release



%install
install -d $RPM_BUILD_ROOT%{_javadir} \
        $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -m 644 releases/%{name}-engine.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-engine-%{version}.jar
install -m 644 releases/%{name}-editor.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-editor-%{version}.jar
ln -s %{name}-engine-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-engine.jar
ln -s %{name}-editor-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-editor.jar

cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.joone joone %{version} JPP %{name}
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-editor.pom
%add_to_maven_depmap org.joone joone-editor %{version} JPP %{name}-editor
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-engine.pom
%add_to_maven_depmap org.joone joone-engine %{version} JPP %{name}-engine

install -m 644 joone/doc/Latex_Doc/JooneCompleteGuide.pdf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_javadir}/%{name}*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%doc %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.rc2.1jpp6
- built with java 6

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_0.rc2.1jpp6
- fixed build with java 7

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_0.rc2.1jpp6
- new version

