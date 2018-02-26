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


Name:           jsr-305
Version:        0.1
Release:        alt1_3jpp6
Epoch:          0
Summary:        JSR 305: Annotations for Software Defect Detection in Java
# http://groups.google.com/group/jsr-305/browse_thread/thread/8105869a258c8c4f
License:        BSD
Group:          Development/Java
URL:            http://code.google.com/p/jsr-305/
# svn export -r '{20101219}' http://jsr-305.googlecode.com/svn/trunk/ jsr-305-0.1
# tar cjf jsr-305-0.1.tar.bz2 jsr-305-0.1
Source0:        jsr-305-0.1.tar.bz2
Source1:        jsr-305-ri-build.xml
Source2:        jsr-305-settings.xml
Source3:        jsr-305-jpp-depmap.xml
Patch0:         jsr-305-pom.patch
Provides:       jsr305 = %{epoch}:%{version}-%{release}
Requires: jpackage-utils >= 0:1.7.5
BuildRequires: java-javadoc
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
%if %{with_maven}
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-default-skin
BuildRequires: maven-shared-filtering
BuildRequires: apache-commons-parent
BuildRequires: fonts-ttf-liberation
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
Buildarch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
This project contains reference implementations, test cases, and other
documents under source code control for Java Specification Request 305:
Annotations for Software Defect Detection. More information at the Google
group: http://groups.google.com/group/jsr-305.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jsr305-javadoc = %{epoch}:%{version}-%{release}
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
%{__cp} -a %{SOURCE1} ri/build.xml
cp %{SOURCE2} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
%patch0 -b .sav0

%build
%if %{with_maven}
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s settings.xml \
        -Dmaven2.jpp.depmap.file=%{SOURCE3} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:aggregate site
#       -Dmaven.test.failure.ignore=true \

%else
export OPT_JAR_LIST=:
export CLASSPATH=
pushd ri
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dversion=%{version} -Djava.javadoc=%{_javadocdir}/java
popd
%endif

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
%if %{with_maven}
install -m 644 ri/target/ri-0.1-SNAPSHOT.jar \
        %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -m 644 proposedAnnotations/target/proposedAnnotations-0.1-SNAPSHOT.jar \
        %{buildroot}%{_javadir}/%{name}-proposedAnnotations-%{version}.jar
install -m 644 tcl/target/tcl-0.1-SNAPSHOT.jar \
        %{buildroot}%{_javadir}/%{name}-tcl-%{version}.jar
%else
install -m 644 ri/jsr-305-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%endif
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/jsr305-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# poms

install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%add_to_maven_depmap org.jsr-305 %{name} %{version} JPP %{name}-parent
install -m 644 ri/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jsr-305 ri %{version} JPP %{name}
install -m 644 tcl/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-tcl.pom
%add_to_maven_depmap org.jsr-305 tcl %{version} JPP %{name}


# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%if %{with_maven}
%{__cp} -a target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%else
%{__cp} -a ri/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%endif
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/jsr305-%{version}
%{__ln_s} jsr305-%{version} %{buildroot}%{_javadocdir}/jsr305

%if %{with_maven}
rm -rf target/site/apidocs
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -a target/site/* %{buildroot}%{_docdir}/%{name}-%{version}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db || :
fi
%endif

%postun
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db || :
fi
%endif

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/jsr305-%{version}
%{_javadocdir}/jsr305

%if %{with_maven}
%files manual
%{_docdir}/%{name}-%{version}
%endif

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_3jpp6
- jpp 6 release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_2jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_1jpp5
- converted from JPackage by jppimport script

