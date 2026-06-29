Name:           shrinkwrap-descriptors
Version:        2.0.0
Release:        alt4

Summary:        ShrinkWrap subproject for creating Archive Descriptors
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/shrinkwrap/descriptors
VCS:            https://github.com/shrinkwrap/descriptors

Source0:        %name-%version.tar

Patch0:         0001-shrinkwrap-remove-xsl-boolean.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
buildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(net.sf.saxon:saxon)
BuildRequires:  mvn(org.glassfish.jaxb:codemodel)
BuildRequires:  mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires:  mvn(xmlunit:xmlunit)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(org.apache.ant:ant-testutil)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:      noarch

%description
ShrinkWrap sub-project for creating Archive Descriptors

This package contains the ShrinkWrap Descriptors API Base.
API Base for Client View of the ShrinkWrap Descriptors Project.

%package        ant
Summary:        ShrinkWrap Descriptors Ant Extension
Group:          Development/Java

%description    ant
Extension module for ShrinkWrap Descriptors Ant Tasks.

%package        api-javaee
Summary:        ShrinkWrap Descriptors Generated Java EE API
Group:          Development/Java

%description    api-javaee
Client View of the ShrinkWrap Descriptors Project.

%package        api-javaee-prototype
Summary:        ShrinkWrap Descriptors Prototype Java EE API
Group:          Development/Java

%description    api-javaee-prototype
Client View of the ShrinkWrap Descriptors Project.

%package        api-jboss
Summary:        ShrinkWrap Descriptors Generated JBoss API
Group:          Development/Java

%description    api-jboss
Client View of the JBoss related ShrinkWrap Descriptors Project.

%package        api-misc
Summary:        ShrinkWrap Descriptors Generated Misc API
Group:          Development/Java

%description    api-misc
Client View of the ShrinkWrap Descriptors Project.

%package        bom
Summary:        ShrinkWrap Descriptors Bill of Materials
Group:          Development/Java

%description    bom
Centralized dependency Management for the ShrinkWrap Descriptors Project.

%package        build-resources
Summary:        Shrinkwrap Descriptors Build Resources
Group:          Development/Java

%description    build-resources
Shrinkwrap Descriptors Build Resources.

%package        depchain
Summary:        ShrinkWrap Descriptors Dependency Chain
Group:          Development/Java

%description    depchain
Single-POM Definition to export the ShrinkWrap Descriptors artifacts in
proper scope.

%package        gen
Summary:        ShrinkWrap Descriptors Source Generator
Group:          Development/Java

%description    gen
Generates various deployment descriptors via XSLT transformation.

%package        impl-base
Summary:        ShrinkWrap Descriptors Implementation
License:        Apache-2.0 and LGPLv2+
Group:          Development/Java

%description    impl-base
Implementation of the ShrinkWrap Descriptors Project.

%package        impl-javaee
Summary:        ShrinkWrap Descriptors Generated Java EE Implementation
Group:          Development/Java

%description    impl-javaee
Generated Implementation of the ShrinkWrap Descriptors Project.

%package        impl-javaee-prototype
Summary:        ShrinkWrap Descriptors Prototype Java EE Implementation
Group:          Development/Java

%description    impl-javaee-prototype
Prototype Implementation of the ShrinkWrap Descriptors Project.

%package        impl-jboss
Summary:        ShrinkWrap Descriptors Generated JBoss Implementation
Group:          Development/Java

%description    impl-jboss
Generated JBoss Implementation of the ShrinkWrap Descriptors Project.

%package        impl-misc
Summary:        ShrinkWrap Descriptors Generated Misc Implementation
Group:          Development/Java

%description    impl-misc
Generated JBoss Implementation of the ShrinkWrap Descriptors Project.

%package        metadata-parser
Summary:        ShrinkWrap Descriptors Metadata Parser
Group:          Development/Java

%description    metadata-parser
XSD and DTD parser for the ShrinkWrap Descriptors.

%package        metadata-parser-test
Summary:        ShrinkWrap Descriptors Metadata Parser Tests
Group:          Development/Java

%description    metadata-parser-test
Hand-coded Tests for the generated descriptors via metadata plugin.

%package        parent
Summary:        ShrinkWrap Descriptors Aggregator POM
Group:          Development/Java

%description    parent
ShrinkWrap Descriptors Aggregator POM.

%package        spi
Summary:        ShrinkWrap Descriptors SPI
Group:          Development/Java

%description    spi
Service Provider Interface of the ShrinkWrap Descriptors Project.

%package        test-util
Summary:        ShrinkWrap Descriptors Test Utilities
Group:          Development/Java

%description    test-util
Commonly used custom assertions.

%prep
%setup
%autopatch -p1

%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_dep :saxon-dom metadata-parser
%pom_remove_dep -r :fest-assert

%pom_change_dep com.sun.codemodel:codemodel org.glassfish.jaxb:codemodel metadata-parser
%pom_change_dep -r org.mockito:mockito-all org.mockito:mockito-core

%pom_add_dep org.apache.maven:maven-core::test metadata-parser
rm metadata-parser/src/test/java/org/jboss/shrinkwrap/descriptor/metadata/mojo/MetadataParserMojoTest.java

%pom_disable_module test

%mvn_package :%name-impl-base::tests: %name-impl-base

%build
export JAVA5_HOME=%_jvmdir/java
%mvn_build -s -j -- -Dmaven.compiler.target=1.8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-%name-api-base
%doc LICENSE

%files ant -f .mfiles-%name-ant
%files api-javaee -f .mfiles-%name-api-javaee
%files api-javaee-prototype -f .mfiles-%name-api-javaee-prototype
%files api-jboss -f .mfiles-%name-api-jboss
%files api-misc -f .mfiles-%name-api-misc
%files bom -f .mfiles-%name-bom
%doc LICENSE

%files build-resources -f .mfiles-%name-build-resources
%doc LICENSE

%files depchain -f .mfiles-%name-depchain
%doc LICENSE

%files gen -f .mfiles-%name-gen
%doc gen/readme.txt
%doc LICENSE

%files impl-base -f .mfiles-%name-impl-base
%files impl-javaee -f .mfiles-%name-impl-javaee
%files impl-javaee-prototype -f .mfiles-%name-impl-javaee-prototype
%files impl-jboss -f .mfiles-%name-impl-jboss
%files impl-misc -f .mfiles-%name-impl-misc
%files metadata-parser -f .mfiles-%name-metadata-parser
%files metadata-parser-test -f .mfiles-%name-metadata-parser-test
%files parent -f .mfiles-%name-parent
%doc LICENSE

%files spi -f .mfiles-%name-spi
%files test-util -f .mfiles-%name-test-util
%doc LICENSE

%changelog
* Sat Apr 18 2026 Evgeniy Serov <scala@altlinux.org> 2.0.0-alt4
- Updated to 2.0.0 stable version.
- Returned to Sisyphus.

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.22.alpha9jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.20.alpha9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.19.alpha9jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.18.alpha9jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.17.alpha9jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.16.alpha9jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.11.alpha2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.7.alpha2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.4.alpha2jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.2.alpha2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_0.2.alpha2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_0.2.alpha2jpp7
- new version

