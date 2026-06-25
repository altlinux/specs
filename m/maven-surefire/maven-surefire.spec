Name:           maven-surefire
Version:        3.5.6
Release:        alt1

Summary:        Apache Maven Surefire
License:        Apache-2.0 and CPL-1.0
Group:          Development/Java
URL:            https://maven.apache.org/surefire/
VCS:            https://github.com/apache/maven-surefire

Source0:        %name-%version.tar

Patch0:         port-to-testng-7.4.0.patch

BuildRequires(pre):  maven-local
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

sed -i 's|<groupId>org\.javacc\.plugin</groupId>|<groupId>org.codehaus.mojo</groupId>|g' surefire-grouper/pom.xml

%mvn_package ":*{surefire-plugin}*" @1
%mvn_package ":*junit-platform*" junit5
%mvn_package ":*{junit,testng,failsafe-plugin}*" @1
%mvn_package ":*tests*" __noinstall

%build
# Tests disabled due missing powermock
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%files plugin -f .mfiles-surefire-plugin
%files provider-junit -f .mfiles-junit
%files provider-junit5 -f .mfiles-junit5
%files provider-testng -f .mfiles-testng
%files -n maven-failsafe-plugin -f .mfiles-failsafe-plugin

%changelog
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

