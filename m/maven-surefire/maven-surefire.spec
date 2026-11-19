Name:           maven-surefire
Version:        3.5.6
Release:        alt3

Summary:        Apache Maven Surefire
License:        Apache-2.0 and CPL-1.0
Group:          Development/Java
URL:            https://maven.apache.org/surefire/
VCS:            https://github.com/apache/maven-surefire

Source0:        %name-%version.tar

Patch0:         port-to-testng-7.4.0.patch
Patch1:         relocate-transitive-slf4j.patch
Patch2:         commandline-environment.patch

BuildRequires(pre):  rpm-macros-java
BuildRequires:  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.testng:testng::jdk15:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)

BuildArch:      noarch

%description
Surefire is a test framework project.

%javadoc_package

%package        plugin
Group:          Development/Java
Summary:        Surefire plugin for maven
Requires:       %name-provider-junit  = %version-%release
Requires:       %name-provider-junit3 = %EVR
Requires:       %name-provider-junit47 = %EVR
Requires:       %name-provider-junit5 = %version-%release
Requires:       %name-provider-testng = %version-%release

%description    plugin
Maven surefire plugin for running tests via the surefire framework.

%package        provider-junit
Group:          Development/Java
Summary:        JUnit provider for Maven Surefire

%description    provider-junit
JUnit provider for Maven Surefire.

%package        provider-junit5
Group:          Development/Java
Summary:        JUnit 5 provider for Maven Surefire

%description    provider-junit5
JUnit 5 provider for Maven Surefire.

%package        provider-testng
Group:          Development/Java
Summary:        TestNG provider for Maven Surefire

%description    provider-testng
TestNG provider for Maven Surefire.

%package -n     maven-failsafe-plugin
Group:          Development/Java
Summary:        Maven plugin for running integration tests

%description -n maven-failsafe-plugin
The Failsafe Plugin is designed to run integration tests while the
Surefire Plugin is designed to run unit tests.

%package        shared-utils
Group:          Development/Java
Summary:        Shared utilities for Maven Surefire

%description    shared-utils
Shared utilities for Maven Surefire.

%package        logger-api
Group:          Development/Java
Summary:        Logging API for Maven Surefire

%description    logger-api
Logging API for Maven Surefire.

%package        api
Group:          Development/Java
Summary:        API for Maven Surefire

%description    api
API for Maven Surefire.

%package        extensions-api
Group:          Development/Java
Summary:        Extensions API for Maven Surefire

%description    extensions-api
Extensions API for Maven Surefire.

%package        extensions-spi
Group:          Development/Java
Summary:        Extensions SPI for Maven Surefire

%description    extensions-spi
Extensions SPI for Maven Surefire.

%package        booter
Group:          Development/Java
Summary:        Forked test process launcher for Maven Surefire

%description    booter
Forked test process launcher for Maven Surefire.

%package        grouper
Group:          Development/Java
Summary:        Group expression parser for Maven Surefire

%description    grouper
Group expression parser for Maven Surefire.

%package        providers
Group:          Development/Java
Summary:        Parent POM for Maven Surefire providers

%description    providers
Parent POM for Maven Surefire providers.

%package        common-java5
Group:          Development/Java
Summary:        Common Java support for Maven Surefire providers

%description    common-java5
Common Java support for Maven Surefire providers.

%package        common-junit3
Group:          Development/Java
Summary:        Common JUnit 3 support for Maven Surefire providers

%description    common-junit3
Common JUnit 3 support for Maven Surefire providers.

%package        common-junit4
Group:          Development/Java
Summary:        Common JUnit 4 support for Maven Surefire providers

%description    common-junit4
Common JUnit 4 support for Maven Surefire providers.

%package        common-junit48
Group:          Development/Java
Summary:        Common JUnit 4.8 support for Maven Surefire providers

%description    common-junit48
Common JUnit 4.8 support for Maven Surefire providers.

%package        provider-junit3
Group:          Development/Java
Summary:        JUnit 3 provider for Maven Surefire

%description    provider-junit3
JUnit 3 provider for Maven Surefire.

%package        provider-junit47
Group:          Development/Java
Summary:        JUnit 4.7 provider for Maven Surefire

%description    provider-junit47
JUnit 4.7 provider for Maven Surefire.

%package        testng-utils
Group:          Development/Java
Summary:        Common TestNG support for Maven Surefire providers

%description    testng-utils
Common TestNG support for Maven Surefire providers.

%package        common
Group:          Development/Java
Summary:        Common implementation for Maven Surefire plugins

%description    common
Common implementation for Maven Surefire plugins.

%package        report-parser
Group:          Development/Java
Summary:        Report parser for Maven Surefire

%description    report-parser
Report parser for Maven Surefire.

%package        report-plugin
Group:          Development/Java
Summary:        Maven plugin for Surefire test reports

%description    report-plugin
Maven plugin for Surefire test reports.

%package        its
Group:          Development/Java
Summary:        Integration test support for Maven Surefire

%description    its
Integration test support for Maven Surefire.

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-help-plugin surefire-its

%pom_disable_module surefire-shadefire
%pom_remove_dep -r :surefire-shadefire

# Embedded inputs must not leak their unshaded dependencies into XMvn metadata.
%pom_xpath_inject pom:dependencies/pom:dependency "<optional>true</optional>" surefire-shared-utils

sed -i 's|<groupId>org\.javacc\.plugin</groupId>|<groupId>org.codehaus.mojo</groupId>|g' surefire-grouper/pom.xml

%mvn_package ":*{surefire-plugin}*" @1
%mvn_package ":surefire-junit-platform" junit5
%mvn_package ":surefire-junit4" junit
%mvn_package ":surefire-testng" testng
%mvn_package ":maven-failsafe-plugin" failsafe-plugin
%mvn_package ":*tests*" __noinstall
%mvn_package "*:*:jar:sources" __noinstall

%build
# Tests disabled due missing powermock
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-surefire
%doc LICENSE README.md

%files plugin -f .mfiles-surefire-plugin
%files provider-junit -f .mfiles-junit
%files provider-junit5 -f .mfiles-junit5
%files provider-testng -f .mfiles-testng
%files -n maven-failsafe-plugin -f .mfiles-failsafe-plugin

%files shared-utils -f .mfiles-surefire-shared-utils
%files logger-api -f .mfiles-surefire-logger-api
%files api -f .mfiles-surefire-api
%files extensions-api -f .mfiles-surefire-extensions-api
%files extensions-spi -f .mfiles-surefire-extensions-spi
%files booter -f .mfiles-surefire-booter
%files grouper -f .mfiles-surefire-grouper
%files providers -f .mfiles-surefire-providers
%files common-java5 -f .mfiles-common-java5
%files common-junit3 -f .mfiles-common-junit3
%files common-junit4 -f .mfiles-common-junit4
%files common-junit48 -f .mfiles-common-junit48
%files provider-junit3 -f .mfiles-surefire-junit3
%files provider-junit47 -f .mfiles-surefire-junit47
%files testng-utils -f .mfiles-surefire-testng-utils
%files common -f .mfiles-maven-surefire-common
%files report-parser -f .mfiles-surefire-report-parser
%files report-plugin -f .mfiles-maven-surefire-report-plugin
%files its -f .mfiles-surefire-its

%changelog
* Thu Nov 19 2026 Ivan Khanas <xeno@altlinux.org> 3.5.6-alt3
- Restore automatic installation of the JUnit 3 and JUnit 4.7 providers.

* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 3.5.6-alt2
- Fix logging conflicts in tested applications.
- Honor excluded environment variables in forked tests.
- Package independent Maven modules separately.

* Thu Jun 25 2026 Evgeniy Serov <scala@altlinux.org> 3.5.6-alt1
- Updated to 3.5.6.

* Thu Nov 13 2025 Mikhail Efremov <sem@altlinux.org> 0:3.2.2-alt2
- Dropped unneeded dependencies.

* Tue May 06 2025 Anton Meleshnikov <alton@altlinux.org> 0:3.2.2-alt1
- New version 3.2.2 (thanks CentOS for the spec).

* Thu Jul 07 2022 Igor Vlasenko <viy@altlinux.org> 0:3.0.0_M4-alt1_6jpp11
- fixed build with new testng

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:3.0.0_M4-alt1_3jpp11
- fixed build with maven-shared-utils

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:3.0.0_M4-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.22.0-alt1_9jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.22.0-alt1_6jpp8
- fc update

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.22.0-alt1_4jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.21.0-alt1_1jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.20.1-alt1_3jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.19.1-alt1_8jpp8
- new release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.19.1-alt1_2jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.18.1-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.18.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.16-alt1_1jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.14-alt1_2jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12.4-alt2_2jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12.4-alt1_2jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt2_5jpp7
- fixed build

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt1_5jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

