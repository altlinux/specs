Packager: Igor Vlasenko <viy@altlinux.ru>
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


Summary:	JBoss Container
URL:		http://www.jboss.com/products/jbossmc
Source0:	jboss-container-5.0-JBossMC_1_0_2-src.tar.gz
# cvs -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r JBossMC_1_0_2 container

Source1:        jboss-container-buildmagic-libraries.ent
Source2:	jboss-container-buildmagic-buildmagic.ent
Source3:	jboss-container-buildmagic-targets.ent
Source4:        jboss-container-buildmagic-modules.ent
Source5:        jboss-container-buildmagic-autoload.properties
Source6:        jboss-container-buildmagic-task.properties
Source7:        jboss-container-buildmagic-common.properties
Source8:        jboss-container-buildmagic-common.xml

Source9:	jboss-container-5.0.Branch_AOP_1_5-src.tar.gz

Patch0:		jboss-container-build_xml.patch
Patch1:		jboss-container-build-test_xml.patch
Patch2:		jboss-container-5.0-JBossMC_1_0_2-IntrospectionTypeInfoFactoryImpl.patch

Name:		jboss-container
Version:	5.0
Release:	alt1_0.JBossMC_1_0_2.1jpp5
Epoch:		0
License:	LGPL
Group:		Development/Java
BuildArch:	noarch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: jboss4-common
BuildRequires: jboss4-test
BuildRequires: jboss4-buildmagic-tasks
Requires: jpackage-utils >= 0:1.6
Requires: jboss4-common
Patch33: jboss-4-generic-alt-ant17support.patch

%description
JBoss container.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}

%prep
%setup -q -n %{name}-%{version}-JBossMC_1_0_2-src
gzip -dc %{SOURCE9} | tar xf -
cp -pr jboss-container-5.0.Branch_AOP_1_5-src/src/main/org/jboss/repository src/main/org/jboss
chmod -R go=u-w *
find . -name "*.jar" -exec rm {} \;

mkdir -p tools/lib
pushd tools/lib
ln -sf $(build-classpath jboss4/jboss4-buildmagic-tasks) buildmagic-tasks.jar
popd

mkdir -p thirdparty
cp %{SOURCE1} thirdparty/libraries.ent

mkdir -p tools/etc/buildmagic
cp %{SOURCE2} tools/etc/buildmagic/buildmagic.ent
cp %{SOURCE3} tools/etc/buildmagic/targets.ent
cp %{SOURCE4} tools/etc/buildmagic/modules.ent
cp %{SOURCE5} tools/etc/buildmagic/autoload.properties
cp %{SOURCE6} tools/etc/buildmagic/task.properties
cp %{SOURCE7} tools/etc/buildmagic/common.properties
cp %{SOURCE8} tools/etc/buildmagic/common.xml

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav

mkdir -p common/output/lib
pushd common/output/lib
ln -sf $(build-classpath jboss4/jboss-common) .
popd

mkdir -p test/output/lib
pushd test/output/lib
ln -sf $(build-classpath jboss4/jboss-test) .
popd
%patch33 -p1

%build

ant all
ant -f build-test.xml jars tests

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 output/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_0.JBossMC_1_0_2.1jpp5
- new version

* Wed Oct 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.JBossMC_1_0_1.1jpp1.7
- converted from JPackage by jppimport script

