%define _unpackaged_files_terminate_build 1

Name: mockito
Version: 5.20.0
Release: alt3

Summary: Tasty mocking framework for unit tests in Java
License: MIT
Group: Development/Java
Url: https://site.mockito.org
Vcs: https://github.com/mockito/mockito.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-17-compat
BuildRequires: xgradle
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: junit
BuildRequires: byte-buddy
BuildRequires: byte-buddy-agent
BuildRequires: maven-plugin-bundle
BuildRequires: apiguardian
BuildRequires: assertj-core
BuildRequires: hamcrest
BuildRequires: junit5
BuildRequires: objenesis
BuildRequires: opentest4j
BuildRequires: objectweb-asm
BuildRequires: guava
BuildRequires: google-error-prone-core
BuildRequires: auto-common
BuildRequires: auto-service
Requires: mockito-core

%description
Mockito is a mocking framework that tastes really good. It lets you write
beautiful tests with clean & simple API. Mockito doesn't give you hangover
because the tests are very readable and they produce clean verification
errors.

%package core
Summary: Core classes of Mockito
Group: Development/Java
BuildArch: noarch

%description core
This package contains the core Mockito library with essential APIs and runtime
required for creating and using mocks.

%package junit-jupiter
Summary: JUnit Jupiter integration for Mockito
Group: Development/Java
BuildArch: noarch
Requires: mockito-core

%description junit-jupiter
This package provides integration helpers and extensions to use Mockito with
JUnit Jupiter. It contains the Mockito-specific JUnit 5 extension and
supporting classes that make it easy to use Mockito in JUnit Jupiter based
tests.

%package subclass
Summary: Subclass mocking support for Mockito
Group: Development/Java
BuildArch: noarch
Requires: mockito-core

%description subclass
This package provides the "subclass" mock maker for Mockito. It enables
creation of mocks using subclassing mechanisms and contains the runtime
components required for subclass based mock generation. This subpackage
provides the implementation pieces that enable creating mocks by subclassing
where proxy-based mocking is not suitable.

%package proxy
Summary: Proxy-based mocking utilities for Mockito
Group: Development/Java
BuildArch: noarch
Requires: mockito-core

%description proxy
This package provides the "proxy" mock maker for Mockito. It offers proxy based
mock implementations and includes the runtime infrastructure used to generate
mocks through dynamic proxies. Useful on platforms or configurations that
prefer proxying over subclassing.

%package errorprone
Summary: Integration between Mockito and Error Prone
Group: Development/Java
BuildArch: noarch
Requires: mockito-core

%description errorprone
This package provides integration helpers and runtime components that enable
Mockito to interoperate with Google's Error Prone static analysis tool.
It contains the Mockito-specific error-prone plugin/extension artifacts (jar
and pom) which help Error Prone perform additional compile-time checks and
enhanced diagnostics for code that uses Mockito.

%prep
%setup
%autopatch -p1

# Remove unwanted directory for RPM build(requires kotlin-dsl).
rm -rf buildSrc

# Compatibility alias
%mvn_alias org.mockito:mokito-core org.mockito:mockito-all

%build
%gradle_publish

%install
%gradle_register
%gradle_register_bom

%gradle_install

%files
%nil

%files core
%_mavenmetadatadir/mockito.xml
%_javadir/mockito/mockito-core.jar
%_mavenpomdir/mockito/mockito-core.pom
%_mavenpomdir/mockito/mockito-bom.pom
%doc --no-dereference LICENSE
%doc README.md doc/design-docs/custom-argument-matching.md

%files junit-jupiter
%_javadir/mockito/mockito-junit-jupiter.jar
%_mavenpomdir/mockito/mockito-junit-jupiter.pom

%files subclass
%_javadir/mockito/mockito-subclass.jar
%_mavenpomdir/mockito/mockito-subclass.pom

%files proxy
%_javadir/mockito/mockito-proxy.jar
%_mavenpomdir/mockito/mockito-proxy.pom

# Must be used with adding --enable-preview compiler argument because of error_prone_core.
%files errorprone
%_javadir/mockito/mockito-errorprone.jar
%_mavenpomdir/mockito/mockito-errorprone.pom

%changelog
* Tue Nov 25 2025 Ivan Khanas <xeno@altlinux.org> 5.20.0-alt3
- Add mockito-errorprone subpackage.
- Add mockito-bom installation.
- All modules are packaged except for android.

* Wed Nov 19 2025 Ivan Khanas <xeno@altlinux.org> 5.20.0-alt2
- Add files for mockito meta package.

* Mon Nov 17 2025 Ivan Khanas <xeno@altlinux.org> 5.20.0-alt1
- New version.
- Fix regression: package org.mockito does not exist(closes: 56779).
- Switch to xgradle.
- Add mockito-core subpackage and make the main package meta.
- Add mockito-junit-jupiter subpackage.
- Add mockito-subclass subpackage.
- Add mockito-proxy subpackage.
- Java 11 target compilation.
- Add JPMS support.

* Wed Apr 23 2025 Andrey Cherepanov <cas@altlinux.org> 5.17.0-alt1
- new version

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:3.12.4-alt1_5jpp11
- update

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:3.12.4-alt1_3jpp11
- new version

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0:3.7.13-alt1_3jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:3.5.13-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.28.2-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.23.9-alt1_6jpp8
- fc update

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.23.9-alt1_4jpp8
- new version

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_17jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_15jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_13jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_10jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_4jpp8
- java 8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_9jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt1_9jpp7
- new version

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt5_0.1jpp6
- fixed build

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt4_0.1jpp6
- fixed build with new testng and xbean

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt3_0.1jpp6
- fixed build

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt2_0.1jpp6
- fixed build

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt1_0.1jpp6
- new version

