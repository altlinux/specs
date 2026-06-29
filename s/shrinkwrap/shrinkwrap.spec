Name:           shrinkwrap
Version:        1.2.6
Release:        alt2

Summary:        Java API for Archive Manipulation
License:        Apache-2.0
Group:          Development/Java
URL:            http://arquillian.org/modules/shrinkwrap-shrinkwrap/
VCS:            https://github.com/shrinkwrap/shrinkwrap

Source0:        %name-%version.tar.gz

Patch0:         0001-Replace-javax-with-jakarta-activation.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)

BuildArch:      noarch

%description
Shrinkwrap provides a simple mechanism to assemble archives
like JARs, WARs, and EARs with a friendly, fluent API.

%javadoc_package

%package        api-nio2
Group:          Development/Java
Summary:        ShrinkWrap NIO.2 API

%description    api-nio2
ShrinkWrap NIO.2 API.

%package        bom
Group:          Development/Java
Summary:        ShrinkWrap Bill of Materials

%description    bom
Centralized dependencyManagement for the ShrinkWrap Project.

%package        build-resources
Group:          Development/Java
Summary:        Shrinkwrap Build Resources

%description    build-resources
Shrinkwrap Build Resources.

%package        depchain
Group:          Development/Java
Summary:        ShrinkWrap Dependency Chain

%description    depchain
Single-POM Definition to export the
ShrinkWrap artifacts in proper scope.

%package        depchain-java7
Group:          Development/Java
Summary:        ShrinkWrap Dependency Chain for Java7 Environments

%description    depchain-java7
Single-POM Definition to export the
ShrinkWrap artifacts in proper scope
for Java 7 Environments.

%package        impl-base
Group:          Development/Java
Summary:        ShrinkWrap Implementation Base
License:        Apache-2.0 and Public Domain

%description    impl-base
Common Base for Implementations of the ShrinkWrap Project.

%package        impl-nio2
Group:          Development/Java
Summary:        ShrinkWrap NIO.2 Implementation

%description    impl-nio2
ShrinkWrap NIO.2 Implementation.

%package        parent
Group:          Development/Java
Summary:        ShrinkWrap Aggregator and Build Parent

%description    parent
ShrinkWrap Aggregator POM.

%package        spi
Group:          Development/Java
Summary:        ShrinkWrap SPI

%description    spi
Generic Service Provider Contract of the ShrinkWrap Project.

%prep
%setup
%autopatch -p1

%pom_remove_parent

%pom_xpath_remove "pom:requireProperty"
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'
%pom_xpath_remove "pom:configuration/pom:argLine"

%pom_xpath_remove "pom:configuration/pom:jvm" api
%pom_xpath_remove "pom:configuration/pom:jvm" impl-base

%pom_add_dep jakarta.activation:jakarta.activation-api impl-base

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :lifecycle-mapping

# remove a few tests that are broken with Java 9+ class loading changes
rm impl-base/src/test/java/org/jboss/shrinkwrap/impl/base/spec/EnterpriseArchiveImplTestCase.java
rm impl-base/src/test/java/org/jboss/shrinkwrap/impl/base/spec/JavaArchiveImplTestCase.java
rm impl-base/src/test/java/org/jboss/shrinkwrap/impl/base/spec/ResourceAdapterArchiveImplTestCase.java
rm impl-base/src/test/java/org/jboss/shrinkwrap/impl/base/spec/WebArchiveImplTestCase.java
rm api/src/test/java/org/jboss/shrinkwrap/api/asset/UrlAssetTestCase.java

%pom_disable_module dist

%mvn_package :%name-api::tests: %name-api
%mvn_package :%name-impl-base::tests: %name-impl-base

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%name-api
%doc LICENSE NOTICE.txt

%files bom -f .mfiles-%name-bom
%doc LICENSE NOTICE.txt

%files api-nio2 -f .mfiles-%name-api-nio2
%files impl-base -f .mfiles-%name-impl-base
%files impl-nio2 -f .mfiles-%name-impl-nio2
%files spi -f .mfiles-%name-spi
%files build-resources -f .mfiles-%name-build-resources
%files depchain -f .mfiles-%name-depchain
%files depchain-java7 -f .mfiles-%name-depchain-java7
%files parent -f .mfiles-%name-parent

%changelog
* Thu Jun 25 2026 Evgeniy Serov <scala@altlinux.org> 1.2.6-alt2
- Returned to Sisyphus.

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.2.6-alt1_5jpp11
- update

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 1.2.6-alt1_2jpp8
- new version

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt2_8jpp8
- fc update

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt2_7jpp8
- explicit build with java8

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt2_5jpp8
- fixed build with new maven surefire

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_7jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

