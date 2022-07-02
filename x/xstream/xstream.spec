Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without activation
%bcond_without cglib
%bcond_without dom4j
%bcond_without jdom
%bcond_without jdom2
%bcond_with jettison
%bcond_with joda-time
%bcond_with kxml2
%bcond_with stax
%bcond_with woodstox
%bcond_with xom
%bcond_with xpp3

Name:           xstream
Version:        1.4.19
Release:        alt1_2jpp11
Summary:        Java XML serialization library
License:        BSD
URL:            https://x-stream.github.io
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/com/thoughtworks/%{name}/%{name}-distribution/%{version}/%{name}-distribution-%{version}-src.zip

BuildRequires:  maven-local
BuildRequires:  mvn(io.github.x-stream:mxparser)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%if %{with activation}
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
%endif

%if %{with cglib}
BuildRequires:  mvn(cglib:cglib-nodep)
%endif

%if %{with dom4j}
BuildRequires:  mvn(dom4j:dom4j)
%endif

%if %{with jdom}
BuildRequires:  mvn(org.jdom:jdom)
%endif

%if %{with jdom2}
BuildRequires:  mvn(org.jdom:jdom2)
%endif

%if %{with jettison}
BuildRequires:  mvn(org.codehaus.jettison:jettison)
%endif

%if %{with joda-time}
BuildRequires:  mvn(joda-time:joda-time)
%endif

%if %{with kxml2}
BuildRequires:  mvn(net.sf.kxml:kxml2-min)
%endif

%if %{with stax}
BuildRequires:  mvn(stax:stax)
BuildRequires:  mvn(stax:stax-api)
%endif

%if %{with woodstox}
BuildRequires:  mvn(org.codehaus.woodstox:wstx-asl)
%endif

%if %{with xom}
BuildRequires:  mvn(xom:xom)
%endif

%if %{with xpp3}
BuildRequires:  mvn(xpp3:xpp3_min)
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

%package -n %{name}-benchmark
Group: Development/Java
Summary:        Benchmark module for %{name}
%description -n %{name}-benchmark
Benchmark module for %{name}.

%{?javadoc_package}

%prep
%setup -q -n %{name}-%{version}


find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

# https://jakarta.ee/about/faq#What_happened_with_javax.*_namespace?
%pom_change_dep javax.activation:activation jakarta.activation:jakarta.activation-api %{name}

%pom_remove_plugin -r :maven-dependency-plugin

%if %{without activation}
%pom_remove_dep -r jakarta.activation:jakarta.activation-api
rm xstream/src/java/com/thoughtworks/xstream/converters/extended/ActivationDataFlavorConverter.java
%endif

%if %{without cglib}
%pom_remove_dep -r cglib:cglib-nodep
rm xstream/src/java/com/thoughtworks/xstream/converters/reflection/CGLIBEnhancedConverter.java
rm xstream/src/java/com/thoughtworks/xstream/mapper/CGLIBMapper.java
rm xstream/src/java/com/thoughtworks/xstream/security/CGLIBProxyTypePermission.java
%endif

%if %{without dom4j}
%pom_remove_dep -r dom4j:dom4j
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JReader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JWriter.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JXmlWriter.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamDom4J.java
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

%if %{without jettison}
%pom_remove_dep -r org.codehaus.jettison:jettison
rm xstream/src/java/com/thoughtworks/xstream/io/json/JettisonMappedXmlDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/json/JettisonStaxWriter.java
%endif

%if %{without joda-time}
%pom_remove_dep -r joda-time:joda-time
rm xstream/src/java/com/thoughtworks/xstream/core/util/ISO8601JodaTimeConverter.java
%endif

%if %{without kxml2}
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
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamBEAStax.java
%endif

%if %{without woodstox}
%pom_remove_dep -r org.codehaus.woodstox:wstx-asl
rm xstream/src/java/com/thoughtworks/xstream/io/xml/WstxDriver.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamWoodstox.java
%endif

%if %{without xom}
%pom_remove_dep -r xom:xom
rm xstream/src/java/com/thoughtworks/xstream/io/xml/XomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/XomReader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/XomWriter.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamXom.java
%endif

%if %{without xpp3}
%pom_remove_dep -r xpp3:xpp3_min
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Xpp3DomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Xpp3Driver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/xppdom/Xpp3DomBuilder.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamXpp3.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamXpp3DOM.java
%endif

%pom_disable_module %{name}-distribution

%pom_disable_module %{name}-hibernate

%pom_disable_module %{name}-jmh

%mvn_package :%{name}-parent __noinstall

%build
%mvn_build -s -f -- -Dversion.java.source=1.8 -Dversion.java.target=1.8

%install
%mvn_install

%files -n %{name} -f .mfiles-%{name}
%doc --no-dereference LICENSE.txt
%doc README.txt

%files -n %{name}-benchmark -f .mfiles-%{name}-benchmark
%doc --no-dereference LICENSE.txt
%doc README.txt

%changelog
* Sat Jul 02 2022 Igor Vlasenko <viy@altlinux.org> 0:1.4.19-alt1_2jpp11
- update

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

