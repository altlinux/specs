BuildRequires: /proc
BuildRequires: jpackage-core
# Copyright (c) 2000-2008, JPackage Project
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

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jboss/common/1.2.1.GA-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0

%if 0
%define __jar_repack %{nil}
%define gcj_support 0
%endif

%define version_full %{version}.GA

Name:           jboss-common    
Version:        1.2.1
Release:	alt2_9jpp5
Epoch:          0
Summary:        Common Utilities for JBoss Projects     
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com

# svn export http://anonsvn.jboss.org/repos/common/common-old/tags/JBossCommon_1_2_1_GA/
# tar czf JBossCommon_1_2_1_GA.tar.gz JBossCommon_1_2_1_GA
Source0:        JBossCommon_1_2_1_GA.tar.gz
# Files used for clean-binary-files and create-jar-links
Source1:        jboss-common-exclusion
Source2:        jboss-common-jar-map
Source3:        jboss-common-thirdparty-instructions
Source4:        jboss-common-thirdparty-jar-map
Source5:        jboss-common-libraries.ent
# A modified create-jar-links that preserves the original
# name of the jar.
Source6:        modified-create-jar-links
# Used for repolib
Source7:        jboss-common-component-info.xml
Source8:        jboss-common-1.2.1.GA.pom
Patch0:         jboss-common-build-compile.patch
Patch1:         jboss-common-ant17.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: jpackage-utils
BuildRequires: jaf
BuildRequires: ant17
BuildRequires: ant17-nodeps
BuildRequires: ant17-javamail
BuildRequires: ant17-junit
BuildRequires: ant17-trax
BuildRequires: bsf
# FIXME: Not being built from source in el4ep1 yet
#BuildRequires: jboss4-buildmagic-tasks
#BuildRequires: jbossbuild
BuildRequires: junit
%if 0
BuildRequires: maven2-plugin-deploy
%endif
BuildRequires: xml-commons-resolver
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
BuildRequires: concurrent
BuildRequires: dtdparser
BuildRequires: jakarta-commons-httpclient
BuildRequires: ws-jaxme
BuildRequires: log4j
BuildRequires: snmptrapappender
BuildRequires: jakarta-slide-webdavclient
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch: noarch
%endif
Source44: import.info


%description
Common Utilities for JBoss Projects

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
%setup -q -n JBossCommon_1_2_1_GA

# ant 1.8 support hack
for i in `find . -name buildmagic.ent`; do sed -i 's,fail unless="buildmagic.ant.compatible",fail if="never",' $i; done
%patch0 -p0
%patch1 -p0

# FIXME: (dwalluck) these two jars are not build from source
find -name '*.jar' ! -name buildmagic-tasks.jar -a ! -name jbossbuild.jar | xargs -t %{__rm}

#tools/lib
pushd tools/lib
# clean files and create symlinks
clean-binary-files -e %{SOURCE1} -l > instructions
clean-binary-files -e %{SOURCE1} -n
sh %{SOURCE6} -d %{SOURCE2} -f instructions
popd

# Thirdparty 

# How to generate the instruction file
#
# 1) take the source tar and unzip
# 2) 'cd build; ant -f build-thirdparty.xml'
# 3) 'cd thirdparty'
# 4) 'clean-binary-files -e jboss-common-exclusion -l > instructions'
# 5) create dep-map file

mkdir -p thirdparty
pushd thirdparty
        cp -p %{SOURCE5} libraries.ent
        # creates the proper links for the binaries
        sh %{SOURCE6} -d %{SOURCE4} -f %{SOURCE3}
popd 

%build
export CLASSPATH=
export OPT_JAR_LIST="ant17/ant17-nodeps"
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 644 output/lib/* $RPM_BUILD_ROOT%{_javadir}/%{name}

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *; do mv ${jar} ${jar/.jar/-%{version}.jar};done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

%if 0
mkdir -p %{buildroot}%{_datadir}/repository.jboss.org/maven2

mvn-jpp deploy:deploy-file \
    -DgroupId=jboss \
    -DartifactId=jboss-common \
    -Dversion=%{version_full}-brew \
    -Dpackaging=jar \
    -DgeneratePom=true \
    -Dfile=$RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar \
    -DrepositoryId=repository.jboss.org \
    -Durl=file://%{buildroot}%{_datadir}/repository.jboss.org/maven2
%endif

# poms
%add_to_maven_depmap jboss jboss-common %{version_full} JPP/%{name} %{name}
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE8} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        sed -i "s/@VERSION@/%{version_full}/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
        tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
        sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
	install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
	install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/namespace.jar $RPM_BUILD_ROOT%{repodirlib}
	cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar $RPM_BUILD_ROOT%{repodirlib}
	cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-client.jar $RPM_BUILD_ROOT%{repodirlib}
	cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-sources.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jboss-common-%{version}.jar
%{_javadir}/%{name}/jboss-common.jar
%{_javadir}/%{name}/jboss-common-client-%{version}.jar
%{_javadir}/%{name}/jboss-common-client.jar
%{_javadir}/%{name}/jboss-common-sources-%{version}.jar
%{_javadir}/%{name}/jboss-common-sources.jar
%{_javadir}/%{name}/namespace-%{version}.jar
%{_javadir}/%{name}/namespace.jar
%{_javadir}/%{name}/testsuite-support-%{version}.jar
%{_javadir}/%{name}/testsuite-support.jar
%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root,) %{_libdir}/gcj/%{name}/*.jar.*
%endif

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_9jpp5
- ant 18 support

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_9jpp6
- ant 1.8.x support

* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_9jpp5
- new jpp release

* Sun Oct 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_6jpp5
- jpackage 5.0

