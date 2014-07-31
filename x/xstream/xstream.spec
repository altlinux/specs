Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%define _without_maven 1
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# Copyright statement from JPackage this file is derived from:

# Copyright (c) 2000-2007, JPackage Project
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

# Tests are disabled by default since we don't have
# all the requirements in Fedora yet
#def_with test
%bcond_with test

Name:           xstream
Version:        1.3.1
Release:        alt1_5jpp7
Summary:        Java XML serialization library

Group:          Development/Java
License:        BSD
URL:            http://xstream.codehaus.org/
Source0:        http://repository.codehaus.org/com/thoughtworks/%{name}/%{name}-distribution/%{version}/%{name}-distribution-%{version}-src.zip


BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  ant >= 0:1.6
BuildRequires:  bea-stax >= 0:1.2.0
BuildRequires:  bea-stax-api >= 0:1.0.1
BuildRequires:  cglib >= 0:2.1.3
BuildRequires:  dom4j >= 0:1.6.1
BuildRequires:  jakarta-commons-lang >= 0:2.1
BuildRequires:  jakarta-oro
BuildRequires:  jdom >= 0:1.0
BuildRequires:  jettison >= 0:1.0
BuildRequires:  joda-time >= 0:1.2.1
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  xom >= 0:1.0
BuildRequires:  xpp3 >= 0:1.1.3.4
BuildRequires:  unzip
BuildRequires:  java-devel-openjdk
%if %with test
BuildRequires:  jmock >= 0:1.0.1
BuildRequires:  wstx >= 0:3.2.0
%endif
Requires:       jpackage-utils
Requires:       xpp3-minimal

BuildArch:      noarch
Source44: import.info


%description
XStream is a simple library to serialize objects to XML 
and back again. A high level facade is supplied that 
simplifies common use cases. Custom objects can be serialized 
without need for specifying mappings. Speed and low memory 
footprint are a crucial part of the design, making it suitable 
for large object graphs or systems with high message throughput. 
No information is duplicated that can be obtained via reflection. 
This results in XML that is easier to read for humans and more 
compact than native Java serialization. XStream serializes internal 
fields, including private and final. Supports non-public and inner 
classes. Classes are not required to have default constructor. 
Duplicate references encountered in the object-model will be 
maintained. Supports circular references. By implementing an 
interface, XStream can serialize directly to/from any tree 
structure (not just XML). Strategies can be registered allowing 
customization of how particular types are represented as XML. 
When an exception occurs due to malformed XML, detailed diagnostics 
are provided to help isolate and fix the problem.


%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{name} API documentation.


%prep
%setup -qn %{name}-%{version}
find . -name "*.jar" -delete

%if %with test
# This test requires megginson's sax2
rm -f xstream/src/test/com/thoughtworks/xstream/io/xml/SaxWriterTest.java
%endif


%build
# Replace bundled tars
pushd xstream/lib
ln -sf $(build-classpath cglib)
ln -sf $(build-classpath commons-lang)
ln -sf $(build-classpath dom4j)
ln -sf $(build-classpath jdom)
ln -sf $(build-classpath jettison)
ln -sf $(build-classpath joda-time)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath oro)
ln -sf $(build-classpath bea-stax-ri)
ln -sf $(build-classpath bea-stax-api)
ln -sf $(build-classpath xom)
ln -sf $(build-classpath xpp3)
%if %with test
ln -sf $(build-classpath jmock)
ln -sf $(build-classpath wstx/wstx-asl)
%endif
popd

# Build
pushd xstream
%if %with test
ant library javadoc
%else
ant benchmark:compile jar javadoc
%endif
popd


%install

# Directory structure
install -d $RPM_BUILD_ROOT%{_javadir}
install -d $RPM_BUILD_ROOT%{_javadocdir}

# Main jar
pushd xstream
install -p -m644 target/xstream-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Benchmarks
install -p -m644 target/xstream-benchmark-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-benchmark-%{version}.jar
ln -s %{name}-benchmark-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-benchmark.jar

# API Documentation
cp -pr target/javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
popd

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}-parent.pom
%add_to_maven_depmap com.thoughtworks.xstream %{name}-parent %{version} JPP %{name}-parent

install -pm 644 xstream/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap com.thoughtworks.xstream %{name} %{version} JPP %{name}


%files
%{_javadir}/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE.txt


%files javadoc
%{_javadocdir}/%{name}-%{version}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_5jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp7
- fc update

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp5
- new version

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_3jpp5
- converted from JPackage by jppimport script

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_1jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_1jpp1.7
- converted from JPackage by jppimport script

