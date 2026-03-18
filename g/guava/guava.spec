Name:           guava
Version:        33.5.0
Release:        alt1

Summary:        Google core libraries for Java
License:        Apache-2.0 AND CC0-1.0
Group:          Development/Java
URL:            https://guava.dev
VCS:            https://github.com/google/guava
BuildArch:      noarch

Source0:        %name-%version.tar

Patch0:         0001-remove-missing-dependenvies-frome-module-info.patch

BuildRequires(pre): maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(com.google.errorprone:error_prone_core)
BuildRequires:  mvn(com.google.errorprone:error_prone_annotations)
BuildRequires:  mvn(org.jspecify:jspecify)
BuildRequires:  mvn(com.google.truth:truth)
BuildRequires:  mvn(com.google.jimfs:jimfs)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  jurand

%description
Guava is a set of core Java libraries from Google that includes new collection
types (such as multimap and multiset), immutable collections, a graph library,
and utilities for concurrency, I/O, hashing, primitives, strings, and more!
It is widely used on most Java projects within Google, and widely used by many
other companies as well.

%package testlib
Group:          Development/Java
Summary:        The guava-testlib artifact

%description testlib
Guava testlib is a set of Java classes for more convenient unit testing.

%prep
%setup
%autopatch -p1

%pom_disable_module guava-tests
%pom_disable_module guava-gwt

%pom_remove_plugin -r :central-publishing-maven-plugin
%pom_remove_plugin -r :toolchains-maven-plugin
%pom_remove_plugin -r :maven-toolchains-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :animal-sniffer-maven-plugin

%pom_remove_dep -r :listenablefuture
%pom_remove_dep -r :j2objc-annotations

%pom_xpath_remove pom:jdkToolchain

%pom_xpath_remove pom:annotationProcessorPaths
sed -i /Xplugin:ErrorProne/d pom.xml

# Fix with missing j2objc dependency
jurand -i -s -a guava guava-testlib \
  -p com[.]google[.]j2objc[.]annotations[.] \
  -m com[.]google[.].*[.]annotations \

%pom_xpath_inject pom:modules "<module>futures/failureaccess</module>"
%pom_xpath_inject pom:parent "<relativePath>../..</relativePath>" futures/failureaccess
%pom_xpath_set pom:parent/pom:version %{version}-jre futures/failureaccess

%mvn_package :guava-parent guava
%mvn_package :failureaccess guava

%mvn_package :guava-bom __noinstall
%mvn_package :guava:module: __noinstall

%build
%mvn_build -f -s -j

%install
%mvn_install

%files -f .mfiles-guava
%doc CONTRIBUTORS LICENSE *.md

%files testlib -f .mfiles-guava-testlib

%changelog
* Fri Feb 27 2026 Evgeniy Serov <scala@altlinux.org> 33.5.0-alt1
- Updated to 33.5.0.

* Thu May 15 2025 Andrey Cherepanov <cas@altlinux.org> 31.0.1-alt2_3jpp11
- Use more compatible name jpackage-11-compat.

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 31.0.1-alt1_3jpp11
- new version

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 30.1-alt1_3jpp11
- java11 build

* Tue Jun 07 2022 Igor Vlasenko <viy@altlinux.org> 30.1-alt1_3jpp8
- new version

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 25.0-alt1_9jpp8
- jvm8 update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 25.0-alt1_6jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 25.0-alt1_4jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 25.0-alt1_1jpp8
- java update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 24.0-alt1_2jpp8
- java update

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_11jpp8
- fc update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_10jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_8jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_4jpp8
- added osgi provides

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt1_4jpp8
- unbootsrap build

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_3jpp7
- new release

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_1jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

