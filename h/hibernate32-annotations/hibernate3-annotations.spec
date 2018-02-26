%define oldname hibernate3-annotations
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: hsqldb
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

%bcond_with             jdk6

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/hibernate-annotations/%{version}.GA-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%define hname hibernate-annotations

Name:           hibernate32-annotations
Version:        3.2.1
Release:	alt3_5jpp5
Epoch:          0
Summary:        Relational persistence and query service
License:        LGPLv2+
URL:            http://annotations.hibernate.org/
Group:          Databases
Source0:        http://prdownloads.sourceforge.net/hibernate/hibernate-annotations-3.2.1.GA.tar.gz
Source1:	hibernate-annotations-jdstyle.css
Source2:	hibernate-annotations-component-info.xml

Patch0:         hibernate-annotations-common-build_xml.patch
Patch1:               hibernate-annotations-jdk16.patch

BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit
BuildRequires: antlr
BuildRequires: cglib
BuildRequires: dom4j
BuildRequires: geronimo-jta-1.0.1B-api
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-collections
BuildRequires: javassist
BuildRequires: junit
BuildRequires: hibernate32 >= 0:3.2
BuildRequires: hibernate3-ejb-persistence-3.0-api >= 0:3.2.1
BuildRequires: hsqldb
BuildRequires: lucene

Requires: hibernate32 >= 0:3.2
Requires: hibernate3-ejb-persistence-3.0-api >= 0:3.2.1
Requires: lucene
BuildArch:      noarch

%description
Hibernate, like all other object/relational mapping tools, 
requires metadata that governs the transformation of data 
from one representation to the other (and vice versa). In 
Hibernate 2.x, mapping metadata is most of the time declared 
in XML text files. Another option is XDoclet, utilizing 
Javadoc source code annotations and a preprocessor at compile 
time.
The same kind of annotation support is now available in the 
standard JDK, although more powerful and better supported by 
tools. IntelliJ IDEA, for example, supports auto-completion 
and syntax highlighting of JDK 5.0 annotations. The EJB3 
specification standardizes the basic APIs and the metadata 
(using JDK 5.0 annotations) needed for any object/relational 
persistence mechanism. Hibernate EntityManager for EJB3 
implements the programming interfaces and lifecycle rules as 
defined by the EJB3 persistence specification. Both Hibernate 
EntityManager and Hibernate Annotations are available in 
standalone preview releases, however, they require Hibernate 
3.1 and JDK 5.0. If you are not using EJB3 persistence, 
please continue using Hibernate 3.0.x (with any JDK supported).
The Hibernate Annotations package provides annotations for
Standard JSR-220 defined O/R mapping
Hibernate O/R mapping extensions
Data validation via the Hibernate Validator framework

%if %{with_repolib}
%package repolib
Summary:	Artifacts to be uploaded to a repository library
Group:          Development/Java

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
%{summary}.

%prep
%setup -q -n %{hname}-%{version}.GA
find . -type f -name "*.jar" | xargs -t rm
mkdir test_output
cp -p %{SOURCE1} doc/api/jdstyle.css

%patch0 -b .sav
%if %with jdk6
%patch1 -p1
%endif

%build
ln -s $(build-classpath hibernate32) hibernate3.jar

build-jar-repository -s -p lib \
antlr \
cglib-nodep \
commons-collections \
commons-logging \
dom4j \
hibernate32 \
hibernate3-ejb-persistence-3.0-api \
javassist \
jta \
lucene \

mkdir jdbc
build-jar-repository -s -p jdbc hsqldb

#failed to compile junit on jdk6

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
	-Dhibernate-core.home=. \
	-Djdk15.home=%{java_home} \
	jar javadoc \
%if %without jdk6
	junitinstrument junit
%endif

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p target/%{hname}/%{hname}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
#(cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}-%{version}.jar hibernate-annotations-%{version}.jar)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{with_repolib}
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}.GA-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/hibernate32-annotations.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-annotations.jar
%endif

%files
%doc lgpl.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
#%{_javadir}/hibernate-annotations.jar
#%{_javadir}/hibernate-annotations-%{version}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{repodir}
%endif

%changelog
* Tue Feb 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt3_5jpp5
- compat build

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_5jpp5
- rebuild with new lucene

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_5jpp5
- new version

* Wed Jan 23 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_0.cr1.2jpp5.0
nobootstrap build

