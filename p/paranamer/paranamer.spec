Patch33: paranamer-1.5-alt-drop-xsite.patch
#BuildRequires: sun-annotation-1.0-api
# tmp hack
#BuildRequires: maven2-plugin-plugin
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

%define gcj_support 0

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}


Summary:        Method parameter name access
Name:           paranamer
Version:        1.5
Release:        alt3_1jpp6
Epoch:          0
License:        Apache-style Software License
URL:            http://paranamer.codehaus.org/
Group:          Development/Java
Source0:        paranamer-1.5.tar.gz
# svn export http://svn.codehaus.org/paranamer/tags/paranamer-1.5/
# tar czf paranamer-1.5.tar.gz paranamer-1.5/


Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         paranamer-generator-pom.patch
Patch1:         paranamer-paranamer-pom.patch
Patch2:         paranamer-distribution-pom.patch
Patch3:         paranamer-distribution-skin.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
%if %{with_maven}
BuildRequires: maven2 >= 2.0.8
BuildRequires: maven2-plugin-ant
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-pmd
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-common-poms >= 1.0
BuildRequires: maven-plugin-tools
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-surefire-report-maven-plugin
BuildRequires: maven-release
BuildRequires: mojo-maven2-plugin-cobertura
BuildRequires: apache-commons-parent
BuildRequires: jmock >= 0:1.0
#BuildRequires: xsite
%endif

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info


%description
Paranamer is a library that allows the parameter names of 
non-private methods and constructors to be accessed at 
runtime. Normally this information is dropped by the 
compiler. In effect, methods like 
'doSometing(mypkg.Person toMe)' currently look like 
'doSomething(mypackage.Person ???)' to people using i
Java's reflection to inspect methods.  

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %{with_maven}
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q 
cp %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml


%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch33 -b .sav33

%build
%if %{with_maven}
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir -p target/site

mvn-jpp \
        -e \
        -s settings.xml \
        -Dproject.build.directory=$(pwd)/target \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven.test.failure.ignore=true \
	install
#       ant:ant install javadoc:javadoc site

%else
ant -Dbuild.sysclasspath=only jar test javadoc
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 %{name}-ant/target/%{name}-ant-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/ant-%{version}.jar
install -m 644 %{name}-generator/target/%{name}-generator-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/generator-%{version}.jar
install -m 644 %{name}-maven-plugin/target/%{name}-maven-plugin-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-plugin-%{version}.jar
install -m 644 %{name}-more-integration-tests/target/%{name}-more-integration-tests-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/more-integration-tests-%{version}.jar
install -m 644 %{name}/target/%{name}-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)



# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-parent.pom
%add_to_maven_depmap  com.thoughtworks.paranamer paranamer-parent %{version} JPP/%{name} parent
install -m 644 %{name}-ant/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ant.pom
%add_to_maven_depmap  com.thoughtworks.paranamer paranamer-ant %{version} JPP/%{name} ant
install -m 644 %{name}-generator/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-generator.pom
%add_to_maven_depmap  com.thoughtworks.paranamer paranamer-generator %{version} JPP/%{name} generator
install -m 644 %{name}-maven-plugin/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-maven-plugin.pom
%add_to_maven_depmap  com.thoughtworks.paranamer paranamer-maven-plugin %{version} JPP/%{name} maven-plugin
install -m 644 %{name}-more-integration-tests/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-more-integration-tests.pom
%add_to_maven_depmap  com.thoughtworks.paranamer paranamer-more-integration-tests %{version} JPP/%{name} more-integration-tests
install -m 644 %{name}/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core.pom
%add_to_maven_depmap  com.thoughtworks.paranamer paranamer %{version} JPP/%{name} core


# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#cp -pr target/docs/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf target/docs/javadoc

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
#cp -pr target/docs $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

#%files javadoc
#%doc %{_javadocdir}/*

%if %{with_maven}
#%files manual
#%doc %{_docdir}/%{name}-%{version}
%endif

%changelog
* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_1jpp6
- fixed build

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_1jpp6
- fixed build (added BR: sun-annotation-1.0-api)

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp6
- new version

