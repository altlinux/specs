%define _unpackaged_files_terminate_build 1
%define common_version 1.2.2
%define service_version 1.1.1
%define factory_version 1.1.0

Name: auto
Version: 1.11.1
Release: alt2

Summary: Java annotation processors and source generators
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/auto
VCS: https://github.com/google/auto.git

Source0: auto-value-%version.tar
Source1: common-%common_version.tar
Source2: service-%service_version.tar
Source3: legacy-auto-parent.pom
Source4: factory-%factory_version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: atinject-javax
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(com.google.escapevelocity:escapevelocity)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(com.google.testing.compile:compile-testing)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(com.squareup:javapoet)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.ltgt.gradle.incap:incap)
BuildRequires: mvn(net.ltgt.gradle.incap:incap-processor)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.checkerframework:checker-qual)
BuildRequires: mvn(org.eclipse.jdt:ecj)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(com.google.auto.service:auto-service)
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(com.google.testparameterinjector:test-parameter-injector)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(jakarta.inject:jakarta.inject-api)
BuildRequires: mvn(org.checkerframework:checker-compat-qual)

%description
Auto annotation processors generate immutable values, dependency injection
factories and ServiceLoader configuration. The main package preserves the
legacy Auto parent POM.

%package common
Summary: Common annotation processor utilities
Group: Development/Java

%description common
Common annotation processor utilities.

%package service
Summary: ServiceLoader annotations and processor
Group: Development/Java

%description service
ServiceLoader annotations and processor.

%package value
Summary: Immutable value and builder annotation processor
Group: Development/Java

%description value
Immutable value and builder annotation processor.

%package value-annotations
Summary: AutoValue and AutoBuilder annotations
Group: Development/Java

%description value-annotations
AutoValue and AutoBuilder annotations.

%package value-parent
Summary: Parent POM for AutoValue
Group: Development/Java

%description value-parent
Parent POM for AutoValue.

%package factory
Summary: Annotation processor for dependency injection factories
Group: Development/Java

%description factory
AutoFactory generates JSR-330-compatible factories from annotated Java
constructors. It supports both javax.inject and jakarta.inject clients.

%prep
%setup -n auto-value-%version -a1 -a2 -a4
rm -rf common service factory
mv common-%common_version common
mv service-%service_version service
mv factory-%factory_version factory
%pom_remove_parent common service
# Guava no longer brings Checker qualifiers transitively.
%pom_add_dep org.checkerframework:checker-qual:3.52.0:provided common factory
%pom_disable_module src/it/functional value
profiles='pom:project/pom:profiles/pom:profile'
# Compile-testing uses the same javac opens as newer upstream Factory.
factory_flags='--add-opens=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED
--add-opens=jdk.compiler/com.sun.tools.javac.main=ALL-UNNAMED
--add-opens=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED
--add-opens=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED
--add-opens=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED
--add-opens=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED'
factory_profile="$profiles[pom:id='open-modules']"
%pom_xpath_set -- "$factory_profile/pom:properties/pom:test.jvm.flags" \
    "$factory_flags" factory
%pom_xpath_remove "$profiles[pom:id='java-11-and-after']" value
%pom_xpath_remove "$profiles[pom:id='sonatype-oss-release']" value
plugins='pom:project//pom:plugin'
%pom_xpath_remove -r -f \
    "$plugins[pom:artifactId='central-publishing-maven-plugin']" \
    common factory service value
%pom_xpath_remove -r -f \
    "$plugins[pom:artifactId='maven-gpg-plugin']" \
    common factory service value
%pom_xpath_remove -r -f \
    "$plugins[pom:artifactId='maven-shade-plugin']" \
    common factory service value
%pom_xpath_remove -r -f \
    "$plugins[pom:artifactId='maven-javadoc-plugin']" \
    common factory service value
%pom_xpath_remove -r -f \
    "$plugins[pom:artifactId='maven-invoker-plugin']" \
    common factory service value
%pom_change_dep com.google.auto:auto-common \
    com.google.auto:auto-common:%common_version service/processor
cp %SOURCE3 legacy-auto-parent.pom
%pom_remove_parent legacy-auto-parent.pom
%mvn_artifact legacy-auto-parent.pom
%mvn_package :build-only __noinstall
%mvn_package com.google.auto:auto-parent auto-parent
%mvn_package com.google.auto:auto-common auto-common
%mvn_package 'com.google.auto.service:*' auto-service
%mvn_package com.google.auto.value:auto-value auto-value
%mvn_package com.google.auto.value:auto-value-annotations auto-value-annotations
%mvn_package com.google.auto.value:auto-value-parent auto-value-parent
%mvn_package com.google.auto.factory:auto-factory auto-factory

%build
%mvn_build -j -- -f build-pom.xml

%install
%mvn_install

%files -f .mfiles-auto-parent
%doc LICENSE

%files common -f .mfiles-auto-common

%files service -f .mfiles-auto-service

%files value -f .mfiles-auto-value

%files value-annotations -f .mfiles-auto-value-annotations

%files value-parent -f .mfiles-auto-value-parent

%files factory -f .mfiles-auto-factory

%changelog
* Wed Nov 4 2026 Ivan Khanas <xeno@altlinux.org> 1.11.1-alt2
- Package AutoFactory with its annotation processor tests.

* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.11.1-alt1
- New version.

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 1.6.1-alt1_3jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.5.4-alt1_6jpp11
- update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.5.4-alt1_2jpp11
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_1jpp8
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3jpp8
- new version

