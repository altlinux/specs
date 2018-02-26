Patch33: hibernate-annotations-pom-alt-maven3.patch
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 3.4.0
%define name hibernate3-annotations
# Copyright (c) 2000-2011, JPackage Project
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

%define repodir %{_javadir}/repository.jboss.com/hibernate-annotations/%{namedversion}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%define reltag GA
%define hname hibernate-annotations
%global namedversion %{version}.%{reltag}

Summary:        Relational persistence and query service
Name:           hibernate3-annotations
Version:        3.4.0
Release:        alt2_3jpp6
Epoch:          0
License:        LGPLv2+
URL:            http://annotations.hibernate.org/
Group:          Databases
# svn export http://anonsvn.jboss.org/repos/hibernate/annotations/tags/3.4.0.GA_CP01/ hibernate-annotations-3.4.0.GA && tar cjf hibernate-annotations-3.4.0.GA.tar.bz2 hibernate-annotations-3.4.0.GA
# Exported revision 20918.
Source0:        hibernate-annotations-3.4.0.GA.tar.bz2
Source2:        %{hname}-component-info.xml
Source3:        %{hname}-settings.xml
Source4:        %{hname}-jpp-depmap.xml
Patch0:         %{hname}-pom.xml.patch
Patch1:         %{hname}-no-cp.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires:  jpackage-utils >= 0:1.7.3
%if 0
# JBPAPP-1701, there is no javadoc of jdk installed in the brew environment, so i have to include this in the project
BuildRequires:  java-javadoc >= 0:1.5
%endif
BuildRequires:  maven2
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-enforcer
BuildRequires:  maven-injection-plugin
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-source
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven-release
BuildRequires:  maven-surefire
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-shared-enforcer-rule-api
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-doxia-sitetools
BuildRequires:  commons-parent >= 0:5
BuildRequires:  junit >= 3.8.2
BuildRequires:  hsqldb
BuildRequires:  slf4j >= 0:1.5.6
BuildRequires:  hibernate3-commons-annotations >= 3.1.0
BuildRequires:  dom4j >= 0:1.6.1
BuildRequires:  hibernate3-ejb-persistence-3.0-api >= 0:3.4.0
BuildRequires:  hibernate3 >= 0:3.3.2
BuildRequires:  antlr >= 0:2.7.6
BuildRequires:  objectweb-asm >= 3.1
BuildRequires:  jakarta-commons-collections >= 0:3.1
BuildRequires:  javassist >= 0:3.9.0
BuildRequires:  jta_1_1_api
BuildRequires:  log4j >= 1.2.14
BuildRequires:  jboss-parent
#BuildRequires:  maven-test-ext-plugin
BuildRequires:  maven-jdocbook-plugin

Requires:  hibernate3 >= 0:3.3.2
Requires:  hibernate3-ejb-persistence-3.0-api >= 0:3.4.0
Requires:  hibernate3-commons-annotations >= 3.1.0
Requires:  jpackage-utils
#Requires:  hibernate3-validator >= 0:3.0.0

BuildArch:      noarch
Source44: import.info

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

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java
Requires:        jpackage-utils

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n hibernate-annotations-%{namedversion}
%patch1 -p1 -b .sav1

%if 0
%patch0 -p0 -b .sav0

sed -i 's|__DOCS_DIR_PLACEHOLDER__|%{_javadocdir}/java|g' ./pom.xml
%else
sed -i 's|\@version\@|%{namedversion}|' ./pom.xml
%endif

cp -p %{SOURCE3} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

cp %{SOURCE2} .
sed -i 's/@VERSION@/%{namedversion}-brew/g' %{hname}-component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{hname}-component-info.xml

%if 0
# FIXME: (dwalluck): breaks build
rm src/main/java/org/hibernate/cfg/annotations/._CollectionBinder.java
rm src/main/java/org/hibernate/cfg/annotations/._Version.java
%endif

%patch33

%build
export LANG=en_US.ISO8859-1

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE4} \
        -Dmaven.test.failure.ignore=true \
        -Dversion=%{namedversion} \
install

%if 0
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE4} \
        -Dmaven.test.failure.ignore=true \
        javadoc:javadoc
%endif

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{hname}-%{namedversion}_CP01.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{namedversion}.jar
%if 0
cp -p target/%{hname}-%{namedversion}-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{hname}-%{namedversion}-sources.jar
%endif
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{namedversion}.jar; do ln -s ${jar} `echo $jar| sed "s|%{name}|%{hname}|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{namedversion}.jar; do ln -s ${jar} `echo $jar| sed "s|-%{namedversion}||g"`; done)

%if 0
## javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{namedversion}
(cd $RPM_BUILD_ROOT%{_javadocdir} && for doc in *-%{namedversion}; do ln -s ${doc} `echo $doc| sed "s|%{name}|%{hname}|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadocdir} && for doc in *-%{namedversion}; do ln -s ${doc} `echo $doc| sed "s|-%{namedversion}||g"`; done)
%endif

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.hibernate %{hname} %{namedversion} JPP %{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
cp -p %{hname}-component-info.xml $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
cp -p %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{repodirsrc}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{repodirsrc}
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{hname}.jar $RPM_BUILD_ROOT%{repodirlib}
%if 0
cp -p $RPM_BUILD_ROOT%{_javadir}/%{hname}-sources.jar $RPM_BUILD_ROOT%{repodirlib}         
%endif
%endif

%files
%doc lgpl.txt
%{_javadir}/%{hname}-%{namedversion}.jar
%if 0
%{_javadir}/%{hname}-%{namedversion}-sources.jar
%{_javadir}/%{hname}-sources.jar
%endif
%{_javadir}/%{hname}.jar
%{_javadir}/%{name}-%{namedversion}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%if 0
%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}
%{_javadocdir}/%{hname}-%{namedversion}
%{_javadocdir}/%{hname}
%endif

%if %with repolib
%files repolib
%dir %{_javadir}/
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.4.0-alt2_3jpp6
- fixed build with new plexus-containers

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.4.0-alt1_3jpp6
- new jpp release

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.4.0-alt1_1.4jpp6
- jpp 6 release

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_5jpp5
- rebuild with new lucene

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_5jpp5
- new version

* Wed Jan 23 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_0.cr1.2jpp5.0
nobootstrap build

