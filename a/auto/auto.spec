%define _unpackaged_files_terminate_build 1
%define common_version 1.2.2
%define service_version 1.1.1

Name: auto
Version: 1.11.1
Release: alt1
Summary: Java annotation processors and source generators
License: Apache-2.0
Group: Development/Java
Url: https://github.com/google/auto
VCS: https://github.com/google/auto.git
BuildArch: noarch

Source0: auto-value-%version.tar
Source1: common-%common_version.tar
Source2: service-%service_version.tar
Source3: legacy-auto-parent.pom
BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
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

%description
Auto annotation processors generate immutable values, builders and service
provider configuration. This package preserves the legacy Auto parent POM.

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

%prep
%setup -n auto-value-%version -a1 -a2
rm -rf common service
mv common-%common_version common
mv service-%service_version service
%pom_remove_parent common service
# Guava no longer brings Checker qualifiers transitively.
%pom_add_dep org.checkerframework:checker-qual:3.52.0:provided common
%pom_disable_module factory build-pom.xml
%pom_disable_module src/it/functional value
%pom_xpath_remove "pom:project/pom:profiles/pom:profile[pom:id='java-11-and-after' or pom:id='sonatype-oss-release']" value
%pom_xpath_remove -r -f "pom:project//pom:plugin[pom:artifactId='central-publishing-maven-plugin']" build-pom.xml
%pom_xpath_remove -r -f "pom:project//pom:plugin[pom:artifactId='maven-gpg-plugin']" build-pom.xml
%pom_xpath_remove -r -f "pom:project//pom:plugin[pom:artifactId='maven-shade-plugin']" build-pom.xml
%pom_xpath_remove -r -f "pom:project//pom:plugin[pom:artifactId='maven-javadoc-plugin']" build-pom.xml
%pom_xpath_remove -r -f "pom:project//pom:plugin[pom:artifactId='maven-invoker-plugin']" build-pom.xml
%pom_change_dep com.google.auto:auto-common com.google.auto:auto-common:%common_version service/processor
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

%build
%mvn_build -j -- -f build-pom.xml

%install
%mvn_install

%files -f .mfiles-auto-parent
%doc LICENSE README.md

%files common -f .mfiles-auto-common
%doc common/README.md

%files service -f .mfiles-auto-service
%doc service/README.md

%files value -f .mfiles-auto-value
%doc value/README.md

%files value-annotations -f .mfiles-auto-value-annotations

%files value-parent -f .mfiles-auto-value-parent

%changelog
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

