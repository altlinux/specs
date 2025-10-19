Name:    maven-dependency-tree
Version: 3.3.0
Release: alt1
Summary: Maven dependency tree artifact
License: Apache-2.0
Group:   Development/Java
URL:     https://maven.apache.org/
BuildArch: noarch

Source0: https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
BuildRequires: unzip
BuildRequires: maven-local
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.eclipse.aether:aether-api)
BuildRequires: mvn(org.eclipse.aether:aether-util)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)

Provides: maven-shared-dependency-tree = %EVR

%description
Apache Maven dependency tree artifact. Originally part of maven-shared.

%javadoc_package

%prep
%setup
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-invoker-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Wed Oct 08 2025 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 3.0.1-alt1_8jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_7jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_3jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_1jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_1jpp7
- update

