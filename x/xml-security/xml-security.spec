Name:           xml-security
Version:        4.0.4
Release:        alt1

Summary:        Implementation of W3C security standards for XML
License:        Apache-2.0
Group:          Development/Java
URL:            https://santuario.apache.org/
VCS:            https://github.com/apache/santuario-xml-security-java

Source0:        %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local
BuildRequires:  jaxb-xjc

BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildREquires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires:  mvn(org.xmlunit:xmlunit-core)
BuildRequires:  mvn(org.xmlunit:xmlunit-matchers)
BuildRequires:  mvn(org.slf4j:slf4j-jdk14)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(org.openjdk.jmh:jmh-core)
BuildRequires:  mvn(org.openjdk.jmh:jmh-generator-annprocess)

BuildArch:      noarch

%description
The XML Security project is aimed at providing implementation
of security standards for XML. Currently the focus is on the
W3C standards :
- XML-Signature Syntax and Processing; and
- XML Encryption Syntax and Processing.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :jaxb30-maven-plugin
%pom_remove_plugin :replacer
%pom_remove_plugin :cyclonedx-maven-plugin
%pom_remove_plugin :modernizer-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin

sed -i 's|${maven.test.argLine} @{argLine}|${maven.test.argLine}|' pom.xml

# missing jetty-servlets for tests
%pom_remove_dep :jetty-servlets
rm \
    src/test/java/org/apache/xml/security/test/stax/utils/HttpRequestRedirectorProxy.java \
    src/test/java/org/apache/xml/security/test/stax/signature/BaltimoreRemoteReferenceTest.java \
    src/test/java/org/apache/xml/security/test/stax/signature/PhaosRemoteReferenceTest.java \
    src/test/java/org/apache/xml/security/test/stax/signature/SignatureCreationReferenceURIResolverTest.java \
    src/test/java/org/apache/xml/security/test/stax/signature/SignatureVerificationReferenceURIResolverRemoteReferenceTest.java

%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:annotationProcessorPaths"

%build

# replace jaxb30-maven-plugin with direct XJC source generation
mkdir -p target/generated-sources/xjc
xjc \
    -d target/generated-sources/xjc \
    -target 3.0 \
    -nv \
    -extension \
    -npa \
    -no-header \
    -catalog src/main/resources/bindings/bindings.cat \
    -b src/main/resources/bindings/c14n.xjb \
    -b src/main/resources/bindings/dsig.xjb \
    -b src/main/resources/bindings/dsig11.xjb \
    -b src/main/resources/bindings/dsig-more.xjb \
    -b src/main/resources/bindings/xenc.xjb \
    -b src/main/resources/bindings/xenc11.xjb \
    -b src/main/resources/bindings/security-config.xjb \
    -b src/main/resources/bindings/xop.xjb \
    src/main/resources/schemas/security-config.xsd \
    src/main/resources/bindings/schemas/exc-c14n.xsd \
    src/main/resources/bindings/schemas/xmldsig-core-schema.xsd \
    src/main/resources/bindings/schemas/xmldsig11-schema.xsd \
    src/main/resources/bindings/schemas/dsig-more_2001_04.xsd \
    src/main/resources/bindings/schemas/dsig-more_2007_05.xsd \
    src/main/resources/bindings/schemas/dsig-more_2021_04.xsd \
    src/main/resources/bindings/schemas/xenc-schema.xsd \
    src/main/resources/bindings/schemas/xenc-schema-11.xsd

cp -a target/generated-sources/xjc/org/* src/main/java/org/

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.md LICENSE NOTICE

%changelog
* Fri Aug 14 2026 Evgeniy Serov <scala@altlinux.org> 4.0.4-alt1
- Updated to 4.0.4.
- Returned to Sisyphus.

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_8jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_7jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_2jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_3jpp8
- full build

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt3_1jpp7
- rebuild with maven-local

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt2_1jpp7
- fixed build

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt1_1jpp7
- update

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0:1.4.5-alt1_4jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for xml-security

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.5-alt1_4jpp7
- new release

* Sun Mar 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt3_0jpp6
- added depmap for org.apache.santuario:xmlsec:jar

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt2_0jpp6
- added jbossas42 compatible repolib

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt1_0jpp6
- new version (closes: #20786)

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_5jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_2jpp5
- jpp5 build

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

