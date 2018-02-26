# dropped
#BuildRequires:  xsite
BuildRequires: sun-annotation-1.0-api
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define gcj_support 0


Summary:        Instantiate New Object
Name:           objenesis
Version:        1.1
Release:        alt3_1jpp6
Epoch:          0
Group:          Development/Java
License:        MIT
URL:            http://objenesis.googlecode.com/svn/docs/index.html
Source0:        %{name}-%{version}.tar.gz
# svn export http://objenesis.googlecode.com/svn/tags/1_1/ objenesis-1.1

Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml

Patch0:         objenesis-website-pom.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  junit
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-eclipse
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-site
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  xpp3-minimal



Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
Java already supports this dynamic instantiation of classes
using Class.newInstance(). However, this only works if the 
class has an appropriate constructor. There are many times 
when a class cannot be instantiated this way, such as when 
the class contains:
* Constructors that require arguments.
* Constructors that have side effects.
* Constructors that throw exceptions.
As a result, it is common to see restrictions in libraries 
stating that classes must require a default constructor. 
Objenesis aims to overcomes these restrictions by bypassing 
the constructor on object instantiation.
Needing to instantiate an object without calling the 
constructor is a fairly specialized task, however there 
are certain cases when this is useful:
* Serialization, Remoting and Persistence - 
  Objects need to be instantiated and restored to a 
  specific state, without invoking code.
* Proxies, AOP Libraries and Mock Objects - Classes can be 
  subclassed without needing to worry about the super() 
  constructor.
* Container Frameworks - Objects can be dynamically 
  instantatiated in non-standard ways.


%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q 

%patch0 -b .sav0

%build
export LANG=en_US.ISO8859-1
cp %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

pushd website
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        antrun:run 
#	xsite:run
popd

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%add_to_maven_depmap org.objenesis objenesis-parent %{version} JPP %{name}-parent

install -m 644 main/target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 main/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.objenesis objenesis %{version} JPP %{name}

install -m 644 tck/target/%{name}-tck-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tck-%{version}.jar
install -m 644 tck/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-tck.pom
%add_to_maven_depmap org.objenesis objenesis-tck %{version} JPP %{name}-tck

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/main
cp -pr main/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/main
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tck
cp -pr tck/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tck
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr website/target/xsite/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
cp -p LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%dir %{_javadir}/%{name}
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

#files manual
#%{_docdir}/%{name}-%{version}

%changelog
* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_1jpp6
- dropped xsite dependency

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_1jpp6
- fixed build with java 7

* Fri Jan 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp6
- new version

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp5
- fixed build

* Mon Mar 08 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- fixed repocop warnings

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- converted from JPackage by jppimport script

