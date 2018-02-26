%define oldname jakarta-commons-compress
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with             maven

%define gcj_support 0

%define base_name commons-compress
%define svnrev 701433

Name:           jakarta-commons-compress10
Version:        1.0
Release:        alt3_0.701433.1jpp5
Epoch:          0
Summary:        Commons Compress
License:        ASL 2.0
Group:          Development/Java
URL:            http://jakarta.apache.org/commons/sandbox/compress/
# svn export http://svn.apache.org/repos/asf/commons/sandbox/compress/trunk commons-compress-1.0-701433
# tar cjf commons-compress-1.0-701433.tar.bz2 commons-compress-1.0-701433
Source0:        commons-compress-1.0-%{svnrev}.tar.bz2
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        commons-compress-0.1-jpp-depmap.xml
Source5:        commons-sandbox-build-project.xml
Source6:        commons-compress-0.1-build.xml
Patch0:         commons-compress-0.1-project_xml.patch
BuildRequires: ant >= 0:1.6
BuildRequires: jakarta-commons-io
BuildRequires: junit
%if %with maven
BuildRequires: maven2
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven-surefire-plugin
%endif
BuildRequires: saxon
BuildRequires: saxon-scripts
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

%description
Commons Compress is a component that contains 
Tar, Zip and BZip2 packages.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%prep
%setup -q -n %{base_name}-%{version}-%{svnrev}
cp -p %{SOURCE5} .
cp -p %{SOURCE6} build.xml

%if %with maven
export DEPCAT=$(pwd)/commons-compress-0.1-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    %{_bindir}/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
%{_bindir}/saxon $DEPCAT %{SOURCE2} > commons-compress-0.1-depmap.new.xml
%endif

%patch0 -p0

%build
%if %with maven
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    %{_bindir}/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.javadoc.source=1.4 \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.home.local=$(pwd)/.maven \
        jar javadoc 
%else
export CLASSPATH=$(build-classpath commons-io):`pwd`/target/classes:`pwd`/target/test-classes
export OPT_JAR_LIST=:
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    -Djunit.jar=file://$(build-classpath junit) \
    -Dbuild.sysclasspath=only \
    jar javadoc
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/commons-compress-0.1-dev.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in jakarta-*; do ln -sf ${jar} ${jar/jakarta-/}; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# FIXME: (dwalluck): breaks --short-circuit
rm -rf target/docs/apidocs

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{base_name}10-%{version}.jar
%{_javadir}/%{base_name}10.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.701433.1jpp5
- fixed build with moved maven1

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.701433.1jpp5
- compat build

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.701433.1jpp5
- fixed repocop warnings

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_4jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_3jpp1.7
- converted from JPackage by jppimport script

