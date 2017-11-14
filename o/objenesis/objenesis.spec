Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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
Version:        2.1
Release:        alt1_7jpp8
License:        ASL 2.0
URL:            http://objenesis.org/
Source0:        https://github.com/easymock/%{name}/archive/%{version}.tar.gz

Patch1:         0001-Fix-build-with-current-jar-plugin.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
# xmvn-builddep misses this:
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)

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
* Proxies, AOP Libraries and Mock Objects - Classes can be sub-classed without 
  needing to worry about the super() constructor.
* Container Frameworks - Objects can be dynamically instantiated in 
  non-standard ways.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q

%patch1 -p1

# Enable generation of pom.properties (rhbz#1017850)
%pom_xpath_remove pom:addMavenDescriptor

%pom_remove_plugin :maven-timestamp-plugin
%pom_remove_plugin :maven-license-plugin
%pom_xpath_remove "pom:dependency[pom:scope='test']" tck

%pom_xpath_remove pom:build/pom:extensions

%build
# tests are skipped because of missing dependency spring-osgi-test
%mvn_build -- -Dyear=2009 -Dmaven.test.skip=true

%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_2jpp8
- new version

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_13jpp7
- rebuild with new apache-resource-bundles

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

