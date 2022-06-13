Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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

%bcond_with dom4j
%bcond_with hibernate
%bcond_with jdom
%bcond_with jdom2
%bcond_with joda
%bcond_with kxml
%bcond_with stax
%bcond_with woodstox

Name:           xstream
Version:        1.4.14
Release:        alt1_2jpp11
Summary:        Java XML serialization library
License:        BSD
URL:            http://x-stream.github.io/
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/com/thoughtworks/%{name}/%{name}-distribution/%{version}/%{name}-distribution-%{version}-src.zip

# patch pom.xml to target Java 8 / 1.8
Patch0:         xstream-java-8-target.patch

BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(com.sun.activation:jakarta.activation)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(xpp3:xpp3)
BuildRequires:  mvn(xpp3:xpp3_min)


%if %{with dom4j}
BuildRequires:  mvn(dom4j:dom4j)
%endif

%if %{with hibernate}
BuildRequires:  mvn(javassist:javassist)
BuildRequires:  mvn(org.codehaus.jettison:jettison)
BuildRequires:  mvn(org.hibernate:hibernate-core)
BuildRequires:  mvn(org.hibernate:hibernate-envers)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(xom:xom)
%endif

%if %{with jdom}
BuildRequires:  mvn(org.jdom:jdom)
%endif

%if %{with jdom2}
BuildRequires:  mvn(org.jdom:jdom2)
%endif

%if %{with joda}
BuildRequires:  mvn(joda-time:joda-time)
%endif

%if %{with kxml}
BuildRequires:  mvn(net.sf.kxml:kxml2-min)
%endif

%if %{with stax}
BuildRequires:  mvn(stax:stax)
BuildRequires:  mvn(stax:stax-api)
%endif

%if %{with woodstox}
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
%endif
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
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
%{name} API documentation.

%if %{with hibernate}
%package        hibernate
Group: Development/Java
Summary:        hibernate module for %{name}
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description    hibernate
hibernate module for %{name}.
%endif

%package        benchmark
Group: Development/Java
Summary:        benchmark module for %{name}
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description    benchmark
benchmark module for %{name}.

%package parent
Group: Development/Java
Summary:        Parent POM for %{name}
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description parent
Parent POM for %{name}.


%prep
%setup -qn %{name}-%{version}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%patch0 -p1

# Require org.codehaus.xsite:xsite-maven-plugin
%pom_disable_module xstream-distribution

# missing artifacts:
#  org.openjdk.jmh:jmh-core:jar:1.11.1
#  org.openjdk.jmh:jmh-generator-annprocess:jar:1.11.1
%pom_disable_module xstream-jmh

# Unwanted
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-eclipse-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :xsite-maven-plugin

%pom_xpath_set "pom:dependency[pom:groupId = 'org.codehaus.woodstox' ]/pom:artifactId" woodstox-core-asl
%pom_xpath_set "pom:dependency[pom:groupId = 'org.codehaus.woodstox' ]/pom:artifactId" woodstox-core-asl xstream
%pom_xpath_set "pom:dependency[pom:groupId = 'cglib' ]/pom:artifactId" cglib
%pom_xpath_set "pom:dependency[pom:groupId = 'cglib' ]/pom:artifactId" cglib xstream
# Replace old xmlpull dependency with xpp3
%pom_change_dep :xmlpull xpp3:xpp3:1.1.4c xstream
# Require unavailable proxytoys:proxytoys
%pom_remove_plugin :maven-dependency-plugin xstream

%pom_remove_plugin :maven-javadoc-plugin xstream

%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'cglib' ]/pom:artifactId" cglib xstream-hibernate
%pom_xpath_inject "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'junit' ]" "<scope>test</scope>" xstream-hibernate
%pom_remove_plugin :maven-dependency-plugin xstream-hibernate
%pom_remove_plugin :maven-javadoc-plugin xstream-hibernate

%pom_xpath_inject "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'junit' ]" "<scope>test</scope>" xstream-benchmark
%pom_remove_plugin :maven-javadoc-plugin xstream-benchmark

# Fix dep on activation
%pom_change_dep javax.activation:activation com.sun.activation:jakarta.activation . xstream

%if %{without dom4j}
%pom_remove_dep -r dom4j:dom4j
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JReader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JWriter.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JXmlWriter.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamDom4J.java
%endif

%if %{without hibernate}
# Don't build hibernate module
%pom_disable_module xstream-hibernate
# Disable support for some lesser used XML backends
%pom_remove_dep -r xom:xom
%pom_remove_dep -r org.codehaus.jettison:jettison
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Xom*
rm xstream/src/java/com/thoughtworks/xstream/io/json/Jettison*
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamXom.java
%endif

%if %{without jdom}
%pom_remove_dep -r org.jdom:jdom
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDomReader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDomWriter.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamJDom.java
%endif

%if %{without jdom2}
%pom_remove_dep -r org.jdom:jdom2
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDom2Driver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDom2Reader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDom2Writer.java
%endif

%if %{without joda}
%pom_remove_dep -r joda-time:joda-time
rm xstream/src/java/com/thoughtworks/xstream/core/util/ISO8601JodaTimeConverter.java
rm xstream/src/test/com/thoughtworks/acceptance/JodaTimeTypesTest.java
%endif

%if %{without kxml}
%pom_remove_dep -r net.sf.kxml:kxml2-min
rm xstream/src/java/com/thoughtworks/xstream/io/xml/KXml2DomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/KXml2Driver.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamKXml2.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamKXml2DOM.java
%endif

%if %{without stax}
%pom_remove_dep -r stax:stax
%pom_remove_dep -r stax:stax-api
rm xstream/src/java/com/thoughtworks/xstream/io/xml/BEAStaxDriver.java
rm xstream/src/test/com/thoughtworks/xstream/io/xml/BEAStaxReaderTest.java
rm xstream/src/test/com/thoughtworks/xstream/io/xml/BEAStaxWriterTest.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamBEAStax.java
%endif

%if %{without woodstox}
%pom_remove_dep -r org.codehaus.woodstox:woodstox-core-asl
rm xstream/src/java/com/thoughtworks/xstream/io/xml/WstxDriver.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamWoodstox.java
%endif

%mvn_file :%{name} %{name}/%{name} %{name}
%mvn_file :%{name}-benchmark %{name}/%{name}-benchmark %{name}-benchmark

%mvn_package :%{name}

%build
# test skipped for unavailable test deps (com.megginson.sax:xml-writer)
%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc --no-dereference LICENSE.txt

%files parent -f .mfiles-%{name}-parent

%if %{with hibernate}
%files hibernate -f .mfiles-%{name}-hibernate
%endif

%files benchmark -f .mfiles-%{name}-benchmark

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:1.4.14-alt1_2jpp11
- java11 build

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 0:1.4.14-alt1_2jpp8
- new version

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 0:1.4.12-alt1_6jpp8
- new version, use jvm8

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.4.11.1-alt1_5jpp8
- update

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.4.11.1-alt1_2jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.4.9-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4.9-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4.9-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.9-alt1_3jpp8
- new fc release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.9-alt1_1jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.8-alt1_2jpp8
- unbootstrap build

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

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

