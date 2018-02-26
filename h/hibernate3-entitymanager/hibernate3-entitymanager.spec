BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 3.4.0
%define name hibernate3-entitymanager
# Copyright (c) 2000-2009, JPackage Project
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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/hibernate-entitymanager/%{namedversion}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%define reltag .GA
%define hname hibernate-entitymanager
%global namedversion %{version}%{?reltag}

Name:           hibernate3-entitymanager
Version:        3.4.0
Release:        alt2_2.8jpp6
Epoch:          0
Summary:        Relational persistence and query service
License:        LGPLv2+
URL:            http://entitymanager.hibernate.org/
Group:          Databases
# svn export http://anonsvn.jboss.org/repos/hibernate/entitymanager/tags/3.4.0.GA_CP01/ hibernate-entitymanager-3.4.0.GA && tar cjf hibernate-entitymanager-3.4.0.GA.tar.bz2 hibernate-entitymanager-3.4.0.GA
# Exported revision 20918.
Source0:        hibernate-entitymanager-3.4.0.GA.tar.bz2
#Source1:        %{hname}-jdstyle.css
Source2:        %{hname}-component-info.xml
Source3:        %{hname}-settings.xml
Source4:        %{hname}-jpp-depmap.xml
Source5:        pom.xml
Patch0:         hibernate-entitymanager-pom.xml.patch
Patch1:         hibernate-entitymanager-no-cp.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  java-javadoc >= 0:1.5
BuildRequires:  maven2
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-enforcer
BuildRequires:  maven-injection-plugin
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-source
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven-release
BuildRequires:  maven-shared-enforcer-rule-api
BuildRequires:  maven-surefire
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-doxia-sitetools
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
BuildRequires:  cglib >= 2.2
BuildRequires:  jboss-parent
BuildRequires:  hibernate3-annotations >= 0:3.4.0
BuildRequires:  commons-parent

Requires:  hibernate3 >= 0:3.3.2
Requires:  hibernate3-commons-annotations >= 0:3.1.0
Requires:  hibernate3-ejb-persistence-3.0-api >= 0:3.4.0
Requires:  hibernate3-annotations >= 0:3.4.0
Requires:  hsqldb >= 0:1.8.0.2
Requires:  javassist >= 0:3.9.0
Requires:  jta_1_1_api

BuildArch:      noarch
Source44: import.info

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

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

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
%setup -q -n %{hname}-%{namedversion}

%{__cp} -p %{SOURCE5} pom.xml

%patch0 -p0 -b .sav0
%patch1 -p1 -b .sav1

sed -i 's|__DOCS_DIR_PLACEHOLDER__|%{_javadocdir}/java|g' ./pom.xml
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

#tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
#sed -i "s/@TAG@/$tag/g" %{SOURCE2}
#sed -i 's/@VERSION@/%{namedversion}-brew/g'  %{SOURCE2}

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE4} \
        -Dmaven.test.failure.ignore=true \
        -Dversion=%{namedversion} \
        install javadoc:javadoc

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p target/%{hname}-%{namedversion}_CP01.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{namedversion}.jar
cp -p target/%{hname}-%{namedversion}_CP01-sources.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-sources-%{namedversion}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{namedversion}.jar; do ln -sf ${jar} `echo $jar| sed "s|%{name}|%{hname}|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{namedversion}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{namedversion}||g"`; done)

## javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{namedversion}
#cp -pr target/%{hname}/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{namedversion}
(cd $RPM_BUILD_ROOT%{_javadocdir} && for doc in *-%{namedversion}; do ln -sf ${doc} `echo $doc| sed "s|%{name}|%{hname}|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadocdir} && for doc in *-%{namedversion}; do ln -sf ${doc} `echo $doc| sed "s|-%{namedversion}||g"`; done)

#pom
# or, not sure
#%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.hibernate %{hname} %{namedversion} JPP %{name}
#or, not sure
#%{__install} -p -m 644 build/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

%if %with repolib
        install -d -m 755 $RPM_BUILD_ROOT%{repodir}
        install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
        install -m 755 %{hname}-component-info.xml $RPM_BUILD_ROOT%{repodir}/component-info.xml
        install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
        install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
        install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{repodirsrc}
        install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{repodirsrc}
        install -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{repodirsrc}
        install -m 755 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
        cp $RPM_BUILD_ROOT%{_javadir}/%{hname}.jar $RPM_BUILD_ROOT%{repodirlib}
        cp $RPM_BUILD_ROOT%{_javadir}/%{hname}-sources.jar $RPM_BUILD_ROOT%{repodirlib} 
        # create source jars
        #mkdir -p $RPM_BUILD_ROOT%{repodirlib}/sources
        #cp -pr src/main/java/org $RPM_BUILD_ROOT%{repodirlib}/sources        
        #cp -p build/src.jar $RPM_BUILD_ROOT%{repodirlib}/%{hname}-sources.jar
        cp %{_javadir}/hibernate3-ejb-persistence-3.0-api.jar $RPM_BUILD_ROOT%{repodirlib}/ejb3-persistence.jar
        cp %{_javadir}/hibernate3-ejb-persistence-3.0-api-sources.jar $RPM_BUILD_ROOT%{repodirlib}/ejb3-persistence-sources.jar
%endif

%files
%doc lgpl.txt
%{_javadir}/%{name}-%{namedversion}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-sources-%{namedversion}.jar
%{_javadir}/%{name}-sources.jar
%{_javadir}/%{hname}-%{namedversion}.jar
%{_javadir}/%{hname}.jar
%{_javadir}/%{hname}-sources-%{namedversion}.jar
%{_javadir}/%{hname}-sources.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}
%{_javadocdir}/%{hname}-%{namedversion}
%{_javadocdir}/%{hname}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.4.0-alt2_2.8jpp6
- build w/java6
- manually fixed install section (added _CP01 prefix)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.4.0-alt1_2.8jpp6
- new jpp release

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.4.0-alt1_2.7jpp6
- jpp 6 release

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_6jpp5
- selected java5 compiler explicitly

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_6jpp5
- new version

* Mon Dec 08 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt2_0.cr1.0jpp5
- hack: built with ejb-persistence-3.0-api-3.2.0 instead of 3.2.1

* Wed Jan 23 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_0.cr1.2jpp5.0
- nobootstrap build

