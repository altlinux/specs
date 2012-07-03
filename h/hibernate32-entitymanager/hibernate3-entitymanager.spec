%define oldname hibernate3-entitymanager
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: hsqldb
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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

%define repodir %{_javadir}/repository.jboss.com/hibernate-entitymanager/%{version}.GA-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%define hname hibernate-entitymanager

Name:           hibernate32-entitymanager
Version:        3.2.1
Release:	alt3_6jpp5
Epoch:          0
License:        LGPLv2+
Summary:        Relational persistence and query service
URL:            http://annotations.hibernate.org/
Group:          Databases
Source0:        http://prdownloads.sourceforge.net/hibernate/hibernate-entitymanager-3.2.1.GA.tar.gz
Source1:	hibernate-entitymanager-jdstyle.css
Patch1:		hibernate-entitymanager-build_xml.patch
Patch0:		hibernate-entitymanager-common-build_xml.patch
Source2:	hibernate3-entitymanager-component-info.xml
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: antlr
BuildRequires: asm
BuildRequires: cglib
BuildRequires: dom4j
BuildRequires: geronimo-jta-1.0.1B-api
BuildRequires: hibernate32 >= 0:3.2
BuildRequires: hibernate32-annotations >= 0:3.2.1
BuildRequires: hibernate3-ejb-persistence-3.0-api >= 0:3.2.1
BuildRequires: hsqldb
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-logging
BuildRequires: javassist
BuildRequires: junit
BuildRequires: jboss-common
#BuildRequires:  jboss-archive-browsing

# EAP only - The environment will need to provide a compatible hibernate
#Requires:  hibernate32 >= 0:3.2
Requires: hibernate32-annotations >= 0:3.2.1
Requires: javassist
BuildArch:      noarch

%description
EJB3 standardizes the basic APIs and the metadata needed for
any object/relational persistence mechanism. Hibernate
EntityManager implements the programming interfaces,
lifecycle rules and packaging archive support as defined by
the EJB3 persistence specification.
Together with Hibernate Annotations, this wrapper implements
a complete (and standalone) EJB3 persistence provider, as
defined by the JSR-220 public final draft, on top of the
mature Hibernate3 core.

%if %{with_repolib}
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:	        Development/Java

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
find . -name "*.jar" | xargs -t rm
mkdir test_output
cp -p %{SOURCE1} doc/api/jdstyle.css

%patch0 -b .sav
%patch1 -b .sav

%build
ln -s $(build-classpath hibernate32) hibernate3.jar

mkdir jdbc
build-jar-repository -s -p jdbc hsqldb

build-jar-repository -s -p lib \
antlr \
asm/asm \
cglib-nodep \
commons-collections \
commons-logging \
dom4j \
javassist \
jboss-common/jboss-common \
jta \
hibernate32 \
hibernate32-annotations \
hibernate3-ejb-persistence-3.0-api

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
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
#(cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}.jar hibernate-entitymanager.jar)

## javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p lgpl.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}


%if %{with_repolib}
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}.GA-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/hibernate32-entitymanager.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-entitymanager.jar
cp -p $RPM_BUILD_DIR/hibernate-entitymanager-3.2.1.GA/lib/hibernate3-ejb-persistence-3.0-api.jar $RPM_BUILD_ROOT%{repodirlib}/ejb3-persistence.jar
%endif

%files
%doc lgpl.txt
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Feb 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt3_6jpp5
- compat build

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_6jpp5
- selected java5 compiler explicitly

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_6jpp5
- new version

* Mon Dec 08 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt2_0.cr1.0jpp5
- hack: built with ejb-persistence-3.0-api-3.2.0 instead of 3.2.1

* Wed Jan 23 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_0.cr1.2jpp5.0
- nobootstrap build

