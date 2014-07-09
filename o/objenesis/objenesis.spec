Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: sun-annotation-1.0-api
BuildRequires: /proc
BuildRequires: jpackage-compat
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

Summary:        A library for instantiating Java objects
Name:           objenesis
Version:        1.2
Release:        alt1_13jpp7
Group:          Development/Java
License:        ASL 2.0
URL:            http://objenesis.googlecode.com/svn/docs/index.html
# svn export http://objenesis.googlecode.com/svn/tags/1_2/ objenesis-1.2
# tar cfJ objenesis-1.2.tar.xz objenesis-1.2
Source0:        %{name}-%{version}.tar.xz

# Skipping website (requires xsite), this patch is unused atm
#Patch0:         objenesis-website-pom.patch

# Remove deps for test scope (unavailable); fix
# maven-license-plugin groupID to latest version available.
Patch1:         001-objenesis-fix-build.patch
Patch2:         JRockitInstantntiatorCharacters.patch

BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-license-plugin
BuildRequires:  maven-timestamp-plugin
BuildRequires:  xpp3-minimal
BuildRequires:  asm2
BuildRequires: apache-resource-bundles apache-jar-resource-bundle

Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
Objenesis is a small Java library that serves one purpose: to instantiate 
a new object of a particular class.
Java supports dynamic instantiation of classes using Class.newInstance(); 
however, this only works if the class has an appropriate constructor. There 
are many times when a class cannot be instantiated this way, such as when 
the class contains constructors that require arguments, that have side effects,
and/or that throw exceptions. As a result, it is common to see restrictions 
in libraries stating that classes must require a default constructor. 
Objenesis aims to overcome these restrictions by bypassing the constructor 
on object instantiation. Needing to instantiate an object without calling 
the constructor is a fairly specialized task, however there are certain cases 
when this is useful:
* Serialization, Remoting and Persistence - Objects need to be instantiated 
  and restored to a specific state, without invoking code.
* Proxies, AOP Libraries and Mock Objects - Classes can be subclassed without 
  needing to worry about the super() constructor.
* Container Frameworks - Objects can be dynamically instantiated in 
  non-standard ways.


%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.


# Skipped till xsite avilable in fedora
#%%package manual
#Group:          Documentation
#Summary:        Documents for %%{name}
#
#%%description manual
#This package contains the %%{name} manual.


%prep
%setup -q 
#%%patch0 -b .sav0
%patch1 -p1
%patch2 -p2


%build
# tests are skipped because of missing dependency spring-osgi-test
mvn-rpmbuild -e \
          -Dyear=2009 \
          -Dmaven.test.skip=true \
          install javadoc:javadoc

# Below is for manual (requires xsite), skipped
#pushd website
#mvn-jpp -e \
#        -s ${M2SETTINGS} \
#        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
#        -Dmaven2.jpp.depmap.file=%%{SOURCE1} \
#        antrun:run 
#popd


%install
# jars
install -Dp -m 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}-parent.pom

install -Dp -m 644 main/target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -Dp -m 644 main/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

install -Dp -m 644 tck/target/%{name}-tck-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tck.jar
install -Dp -m 644 tck/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-tck.pom
%add_maven_depmap JPP-%{name}-tck.pom %{name}-tck.jar

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}/main
cp -pr main/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/main
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}/tck
cp -pr tck/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/tck


%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_13jpp7
- update

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_11jpp7
- fc update

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

