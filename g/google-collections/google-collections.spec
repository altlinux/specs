# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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


Name:           google-collections
Version:        1.0
Release:        alt1_3jpp6
Epoch:          0
Summary:        Google Collections Library
License:        ASL 2.0
Group:          Development/Java
URL:            http://code.google.com/p/google-collections/
Source0:        http://google-collections.googlecode.com/files/google-collect-1.0.zip
Source1:        http://google-maven-repository.googlecode.com/svn/repository/com/google/collections/google-collections/1.0/google-collections-1.0.pom
Source2:        %{name}-build.xml
# get it from  http://google-collections.googlecode.com/svn/trunk/build.xml
Source3:        %{name}-build.properties
# get it from  http://google-collections.googlecode.com/svn/trunk/build.properties
Source4:        %{name}-COPYING
# get it from  http://google-collections.googlecode.com/svn/trunk/COPYING
Source5:        %{name}-testfw.tar.gz
# svn export http://google-collections.googlecode.com/svn/trunk/testfw/ google-collections-testfw
Source6:        %{name}-test.tar.gz
# svn export http://google-collections.googlecode.com/svn/trunk/test/ google-collections-test

Patch0:         google-collections-javadoc-crosslink.patch
Patch1:         google-collections-MapsTest.patch
Patch2:         google-collections-ImmutableSortedMapTest.patch

Provides:       google-collect = %{epoch}:%{version}-%{release}
Requires:       jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  java-javadoc
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  cglib
BuildRequires:  easymock2
BuildRequires:  easymock-classextension2
BuildRequires:  jsr-305
BuildRequires:  junit
BuildRequires:  tl4j
Buildarch:      noarch
Source44: import.info

%description
The Google Collections Library 1.0 is a suite of new 
collections and collection-related goodness for Java 5.0, 
brought to you by Google.

This library is a natural extension of the Java Collections
Framework you already know and love.

The major new types are:

* BiMap. A Map that guarantees unique values, and supports 
  an inverse view.
* Multiset. A Collection that may contain duplicate values 
  like a List, yet has order-independent equality like a Set.
  Often used to represent a histogram.
* Multimap. Similar to Map, but may contain duplicate keys.
  Has subtypes SetMultimap and ListMultimap providing more 
  specific behavior. 

There are also more than a dozen collection implementations,
mostly of the interfaces above, but not all. ReferenceMap, 
for example, is a ConcurrentMap implementation which easily 
handles any combination of strong, soft or weak keys with 
strong, soft or weak values.

Static utility classes include:

* Comparators. Natural order, compound, null-friendly, 
  ad-hoc . . .
* Iterators and Iterables. Element-based equality, cycle, 
  concat, partition, filter with predicate, transform with 
  function . . .
* Lists, Sets and Maps. A plethora of convenient factory 
  methods and much more.
* PrimitiveArrays: "boxing"/"unboxing" of primitive arrays 

And there's more:

* Forwarding collections
* Constrained collections
* Implementation helpers like AbstractIterator 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n google-collect-%{version}
mkdir src
pushd src
unzip -q ../src-1.0.zip
popd
cp %{SOURCE2} build.xml
cp %{SOURCE3} build.properties
cp %{SOURCE4} COPYING
mkdir lib
ln -sf $(build-classpath jsr305) lib
ln -sf $(build-classpath junit) lib
ln -sf $(build-classpath cglib-nodep) lib/cglib-nodep-2.2.jar
ln -sf $(build-classpath easymock2) lib/easymock-2.4.jar
ln -sf $(build-classpath easymock-classextension2) lib/easymockclassextension-2.4.jar
ln -sf $(build-classpath tl4j) lib/tl4j-1.1.0.jar

tar xzf %{SOURCE5}
mv %{name}-testfw testfw
tar xzf %{SOURCE6}
mv %{name}-test test

%patch0 -p1
%patch1 -b .sav1
%patch2 -b .sav2

%build
export OPT_JAR_LIST=:
export CLASSPATH=
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dversion=%{version} jar javadoc

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/dist/google-collect-%{version}/google-collect-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/google-collect-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# poms
%add_to_maven_depmap com.google.code.google-collections %{name} %{version} JPP %{name}
%add_to_maven_depmap com.google.collections %{name} %{version} JPP %{name}

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.pom

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/google-collect-%{version}
%{__ln_s} google-collect-%{version} %{buildroot}%{_javadocdir}/google-collect

%files
%doc COPYING
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/google-collect-%{version}.jar
%{_javadir}/google-collect.jar
%{_datadir}/maven2/poms/JPP.%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/google-collect-%{version}
%{_javadocdir}/google-collect

%changelog
* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.rc2.1jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_1jpp5
- converted from JPackage by jppimport script

