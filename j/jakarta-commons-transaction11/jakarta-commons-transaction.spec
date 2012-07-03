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

#def_with gcj_support
%bcond_with gcj_support
#def_with maven
%bcond_with maven

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define base_name commons-transaction

Name:           jakarta-commons-transaction11
Version:        1.1
Release:        alt2_10jpp6
Epoch:          0
Summary:        Commons Transaction
License:        ASL 2.0
Url:            http://jakarta.apache.org/commons/transaction/
Group:          Development/Java
Source0:        commons-transaction-1.1-src.tgz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        commons-transaction-1.1-jpp-depmap.xml
Patch0:         commons-transaction-1.1-project_xml.patch
Provides:       commons-transaction11 = %{epoch}:%{version}-%{release}
Requires: jakarta-commons-codec
Requires: log4j
Requires: jta_1_1_api
Requires: xerces-j2
Requires: xml-commons-apis
BuildRequires: jpackage-utils >= 0:1.7
BuildRequires: ant >= 0:1.6
%if %with maven
BuildRequires: maven >= 0:1.0.2
BuildRequires: maven-plugins-base
BuildRequires: maven-plugin-test
BuildRequires: maven-plugin-xdoc
BuildRequires: maven-plugin-license
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
BuildRequires: jta_1_1_api
BuildRequires: junit
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-codec
BuildRequires: log4j
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
Source44: import.info

%description
Commons Transaction aims at providing lightweight, 
standardized, well tested and efficient implementations 
of utility classes commonly used in transactional Java 
programming. Initially there are implementations for 
multi level locks, transactional collections and 
transactional file access. There may be additional 
implementations when the common need for them becomes 
obvious. However, the complete component shall remain 
compatible to JDK1.2 and should have minimal dependencies.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c -n %{base_name}
find . -name "*.jar" | xargs rm

%if %with maven
export DEPCAT=$(pwd)/commons-transaction-1.1-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    %{_bindir}/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
%{_bindir}/saxon $DEPCAT %{SOURCE2} > commons-transaction-1.1-depmap.new.xml
%endif

%patch0 -b .sav

%build
%if %with maven
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    %{_bindir}/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

maven -Dmaven.compile.target=1.4 -Dmaven.javadoc.source=1.4  -Dmaven.repo.remote=file:/usr/share/maven1/repository \
      -Dmaven.javadoc.source=1.4 \
      -Dmaven.home.local=$(pwd)/.maven \
      jar javadoc 
%else
export CLASSPATH=$(build-classpath commons-codec jta_1_1_api log4j):`pwd`/build/classes
export OPT_JAR_LIST=:
%{ant} -Dbuild.sysclasspath=only jar javadocs
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%if %with maven
cp -p target/commons-transaction-%{version}.jar \
           $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%else
cp -p build/lib/commons-transaction-1.1.jar \
           $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%endif

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in jakarta-*; do \
ln -sf ${jar} ${jar/jakarta-/}; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%if %with maven
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr build/doc/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/commons-transaction11-%{version}.jar
%{_javadir}/commons-transaction11.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_10jpp6
- fixed build with moved maven1

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_10jpp6
- new jpp release

