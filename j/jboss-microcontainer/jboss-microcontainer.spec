Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-core
# Copyright (c) 2000-2007, JPackage Project
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

%define version_full %{version}

%define _with_repolib 1
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jboss/microcontainer/%{version_full}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           jboss-microcontainer
Version:        1.0.2
Release:	alt3_5jpp6
Epoch:          1
Summary:        JBoss Microcontainer
URL:            http://www.jboss.com/products/jbossmc
Source0:        jboss-microcontainer-1.0.2-src.tar.bz2
%if 0
mkdir jboss-microcontainer-1.0.2-src
cd jboss-microcontainer-1.0.2-src
cvs -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r JBossMC_1_0_2 microkernel
cvs -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r JBossMC_1_0_2 container
cvs -d:pserver:anonymous@anoncvs.forge.jboss.com:/cvsroot/jboss export -r JBossMC_1_0_2 jboss-dependency
svn export http://anonsvn.jboss.org/repos/jbossas/tags/JBossMC_1_0_2/tools
cd ..
tar cjf jboss-microcontainer-1.0.2-src.tar.bz2 jboss-microcontainer-1.0.2-src
rm -r jboss-microcontainer-1.0.2-src
%endif
Source1:        http://downloads.sourceforge.net/jboss/microcontainer-1.0.2-src.tar.gz
Source2:        jboss-microcontainer-component-info.xml
Source3:        jboss-microcontainer-1.0.2.pom
Patch0:         jboss-microcontainer-libraries.patch
Patch1:         jboss-microcontainer-microkernel-build.patch
Patch2:         jboss-microcontainer-microkernel-build-test.patch
Patch3:         jboss-microcontainer-1.0.2-buildmagic-ant17-jdk5.patch
Patch4:         jboss-microcontainer-no-retrotranslator.patch
License:        LGPLv2+
Group:          Development/Java
BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant17 >= 0:1.6.5
BuildRequires: ant17-nodeps
BuildRequires: ant17-junit
BuildRequires: buildmagic
BuildRequires: jboss-test
BuildRequires: junit
BuildRequires: log4j
BuildRequires: xerces-j2
BuildRequires: concurrent
BuildRequires: jboss-common
BuildRequires: jbossxb
Requires: jpackage-utils >= 0:1.7.3
Requires: concurrent
Requires: jboss-common
Requires: jbossxb
Provides:       jboss-container = %{epoch}:%{version}-%{release}
Obsoletes:      jboss-container = 0:5.0-0.JBossMC_1_0_2.1jpp
Obsoletes:      jboss-container = 0:5.0-0.Branch_AOP_1_5.1jpp
Provides:       jboss-dependency = %{epoch}:%{version}-%{release}
Obsoletes:      jboss-dependency = 0:5.0-0.JBossMC_1_0_2.1jpp
Obsoletes:      jboss-dependency = 0:5.0-0.Branch_AOP_1_5.1jpp

%description
The JBoss Microcontainer provides a lightweight container for 
managing POJOs, their deployment and configuration.
Project goals include:
* Make the JBoss Microcontainer available as a standalone project.
* Embrace JBoss' POJO middleware strategy.
* Enable JBoss services to be easily deployed in the other 
  containers.
* Allow the features to be used in more restrictive environments 
  (e.g. Applets, J2ME, etc.).
* Provide POJO configuration management, support for dependencies, 
  and support for clustering.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jboss-container-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jboss-container-javadoc = 0:5.0-0.JBossMC_1_0_2.1jpp
Obsoletes:      jboss-container-javadoc = 0:5.0-0.Branch_AOP_1_5.1jpp
Provides:       jboss-dependency-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jboss-dependency-javadoc = 0:5.0-0.JBossMC_1_0_2.1jpp
Obsoletes:      jboss-dependency-javadoc = 0:5.0-0.Branch_AOP_1_5.1jpp
BuildArch: noarch

%description javadoc
%{summary}.

%if %{with_repolib}
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{name}-%{version}-src
sed -i 's,fail unless="buildmagic.ant.compatible",fail if="true",' tools/etc/buildmagic/buildmagic.ent
%setup -q -D -T -a 1 -n %{name}-%{version}-src
cp -pr microcontainer-1.0.2-src/* microkernel/src
rm -r microcontainer-1.0.2-src
chmod -R go=u-w *
find . -name "*.jar" | xargs -t rm

mkdir -p tools/lib
pushd tools/lib
ln -sf $(build-classpath buildmagic) buildmagic-tasks.jar
popd

mkdir thirdparty
cp tools/etc/buildmagic/libraries.ent thirdparty

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1

mkdir -p thirdparty/junit-junit/lib
pushd thirdparty/junit-junit/lib
ln -sf $(build-classpath junit)
popd

mkdir -p thirdparty/apache-log4j/lib
pushd thirdparty/apache-log4j/lib
ln -sf $(build-classpath log4j)
popd

mkdir -p thirdparty/apache-xerces/lib
pushd thirdparty/apache-xerces/lib
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
popd

mkdir -p thirdparty/oswego-concurrent/lib
pushd thirdparty/oswego-concurrent/lib
ln -sf $(build-classpath concurrent)
popd

mkdir -p thirdparty/jboss/common/lib
pushd thirdparty/jboss/common/lib
ln -sf $(build-classpath jboss-common/jboss-common)
popd

mkdir -p thirdparty/jboss/jbossxb/lib
pushd thirdparty/jboss/jbossxb/lib
ln -sf $(build-classpath jboss/jboss-xml-binding)
popd

mkdir -p test/output/lib
pushd test/output/lib
ln -sf $(build-classpath jboss-test)
popd

mkdir -p thirdparty/jboss/microcontainer/lib

%build
export CLASSPATH=
export OPT_JAR_LIST="ant17/ant17-nodeps ant17/ant17-junit junit"
pushd container
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars docs
popd
cp container/output/lib/jboss-container.jar thirdparty/jboss/microcontainer/lib
pushd jboss-dependency
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars docs
popd
cp jboss-dependency/output/lib/jboss-dependency.jar thirdparty/jboss/microcontainer/lib
pushd microkernel
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars docs
popd
cp microkernel/output/lib/jboss-microcontainer.jar thirdparty/jboss/microcontainer/lib
pushd microkernel
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f build-test.xml jars tests
popd

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 0644 container/output/lib/jboss-container.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-container-%{version}.jar
install -p -m 0644 jboss-dependency/output/lib/jboss-dependency.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-dependency-%{version}.jar
install -p -m 0644 microkernel/output/lib/jboss-microcontainer.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-microcontainer-%{version}.jar
install -p -m 0644 microkernel/output/lib/jboss-microcontainer-test.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-microcontainer-test-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/container
cp -pr container/output/api/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/container
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/dependency
cp -pr jboss-dependency/output/api/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/dependency
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/microkernel
cp -pr microkernel/output/api/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/microkernel
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# poms
%add_to_maven_depmap org.jboss.microcontainer jboss-microcontainer %{version} JPP/%{name} %{name}
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -a %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom

%if %{with_repolib}
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -a %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version_full}-brew/g" %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH1} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH2} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH3} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH4} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}/jboss-microcontainer-%{version}.jar %{buildroot}%{repodirlib}/jboss-microcontainer.jar
%{__cp} -p %{buildroot}%{_javadir}/%{name}/jboss-container-%{version}.jar %{buildroot}%{repodirlib}/jboss-container.jar
%{__cp} -p %{buildroot}%{_javadir}/%{name}/jboss-dependency-%{version}.jar %{buildroot}%{repodirlib}/jboss-dependency.jar
%endif

%files
%{_javadir}/%{name}
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Mar 11 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt3_5jpp6
- build with ant17

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_5jpp6
- fixed build with new jboss-test

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_5jpp6
- ant 1.8.x support

* Thu Jun 04 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_5jpp5
- new version

* Wed Oct 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

