Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define gcj_support 0


Name:           sf-collections-generic
Version:        4.01
Release:        alt1_1jpp6
Epoch:          0
Summary:        Commons Collections with Generics

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://larvalabs.com/collections/
Source0:        collections-generic-4.01-src.tar.gz
Source1:        http://repo1.maven.org/maven2/net/sourceforge/collections/collections-generic/4.01/collections-generic-4.01.pom

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
BuildRequires: junit
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0


%description
This is a new version of the popular Jakarta 
Commons-Collections project. It features support for Java 
1.5 Generics. Generics introduce a whole new level of 
usability and type-safety to the Commons-Collections classes.
The functionality of the package is otherwise left unchanged.

Commons-Collections builds on the powerful Java Collections
Framework by providing new collection types and 
implementations, including (from the Jakarta site):
* Bag interface for collections that have a number of copies 
  of each object
* Buffer interface for collections that have a well defined 
  removal order, like FIFOs
* BidiMap interface for maps that can be looked up from value 
  to key as well and key to value
* MapIterator interface to provide simple and quick iteration 
  over maps
* Type checking decorators to ensure that only instances of a 
  certain type can be added
* Transforming decorators that alter each object as it is 
  added to the collection
* Composite collections that make multiple collections look 
  like one
* Ordered maps and sets that retain the order elements are 
  added in, including an LRU based map
* Identity map that compares objects based on their identity 
  (==) instead of the equals method
* Reference map that allows keys and/or values to be garbage 
  collected under close control
* Many comparator implementations
* Many iterator implementations
* Adapter classes from array and enumerations to collections
* Utilities to test or create typical set-theory properties 
  of collections such as union, intersection, and closure


%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.


%prep
%setup -q -n collections-generic-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
export OPT_JAR_LIST="ant/ant-junit junit"
ant jar test javadoc

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 build/collections-generic-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap net.sourceforge.collections collections-generic %{version} JPP %{name}

# javadocs
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.01-alt1_1jpp6
- new version

