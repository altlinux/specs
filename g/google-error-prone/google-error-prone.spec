%define _unpackaged_files_terminate_build 1

Name: google-error-prone
Version: 2.52.0
Release: alt2

Summary: Catch common Java mistakes as compile-time errors
License: Apache-2.0
Group: Development/Java
URL: https://errorprone.info
VCS: https://github.com/google/error-prone.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name-%version-protobuf31.1.tar
Source2: software-and-algorithms-LICENSE
Source3: safere-LICENSE
Source4: safere-LICENSE-Unicode.txt
Source5: protobuf-java-LICENSE
Source6: CC0-1.0.txt
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: checker-dataflow-errorprone
BuildRequires: checker-javacutil
BuildRequires: checker-compat-qual
BuildRequires: geronimo-annotation
BuildRequires: kotlin-bootstrap-libs
BuildRequires: auto-value
BuildRequires: auto-service
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-resources-plugin
BuildRequires: bnd-maven-plugin
BuildRequires: maven-shade-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: os-maven-plugin
BuildRequires: mvn(com.beust:jcommander)
BuildRequires: mvn(com.github.ben-manes.caffeine:caffeine)
BuildRequires: mvn(com.github.kevinstern:software-and-algorithms)
BuildRequires: mvn(com.github.spullara.mustache.java:compiler)
BuildRequires: mvn(com.google.auto.factory:auto-factory)
BuildRequires: mvn(com.google.auto.service:auto-service)
BuildRequires: mvn(com.google.auto.service:auto-service-annotations)
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(com.google.auto:auto-common)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.google.common.html.types:proto)
BuildRequires: mvn(com.google.common.html.types:types)
BuildRequires: mvn(com.google.dagger:dagger)
BuildRequires: mvn(com.google.dagger:dagger-producers)
BuildRequires: mvn(com.google.flogger:flogger)
BuildRequires: mvn(com.google.googlejavaformat:google-java-format)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: guice7-assistedinject
BuildRequires: guice7-servlet
BuildRequires: guice7-testlib
BuildRequires: google-guice7
BuildRequires: mvn(com.google.j2objc:j2objc-annotations)
BuildRequires: mvn(com.google.jimfs:jimfs)
BuildRequires: mvn(com.google.protobuf:protobuf-java)
BuildRequires: mvn(com.google.protobuf:protobuf-java-util)
BuildRequires: mvn(com.google.testing.compile:compile-testing)
BuildRequires: mvn(com.google.testparameterinjector:test-parameter-injector)
BuildRequires: mvn(com.google.truth.extensions:truth-java8-extension)
BuildRequires: mvn(com.google.truth.extensions:truth-proto-extension)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(com.ibm.icu:icu4j)
BuildRequires: mvn(io.github.java-diff-utils:java-diff-utils)
BuildRequires: mvn(io.netty:netty-all)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.checkerframework:checker-qual)
BuildRequires: mvn(org.checkerframework:dataflow-errorprone)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.jmock:jmock)
BuildRequires: mvn(org.jmock:jmock-junit4)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.pcollections:pcollections)
BuildRequires: mvn(org.safere:safere)
BuildRequires: mvn(org.threeten:threeten-extra)
BuildRequires: mvn(org.yaml:snakeyaml)
BuildRequires: mvn(pl.pragmatists:JUnitParams)
BuildRequires: mvn(org.checkerframework:javacutil)

%description
Error Prone performs static analysis during Java compilation and provides
checks, refactoring support and APIs for custom checks.

%package parent
Summary: Shared Maven parent POM for Error Prone
Group: Development/Java

%description parent
Shared Maven configuration for the Error Prone modules.

%package annotation
Summary: Error Prone checker registration annotation
Group: Development/Java

%description annotation
Checker registration and suppression annotation definitions.

%package annotations
Summary: Annotations for Error Prone static analysis
Group: Development/Java

%description annotations
Annotations for Error Prone checks and checked APIs.

%package check-api
Summary: API for implementing Error Prone checks
Group: Development/Java

%description check-api
Compiler APIs for implementing Error Prone static analysis checks.

%package core
Summary: Error Prone static analysis engine
License: Apache-2.0 and MIT and BSD-3-Clause and Unicode-3.0 and CC0-1.0
Group: Development/Java

%description core
The Error Prone Java compiler analysis engine and built-in checks.

%package refaster
Summary: Error Prone Refaster template compiler
License: Apache-2.0 and MIT and BSD-3-Clause and Unicode-3.0 and CC0-1.0
Group: Development/Java

%description refaster
Refaster support for compiling source transformation templates.

%package type-annotations
Summary: Error Prone type annotations
Group: Development/Java

%description type-annotations
Type annotations used by Error Prone compiler integrations.

%package test-helpers
Summary: Error Prone compilation and refactoring test helpers
Group: Development/Java

%description test-helpers
Helpers for testing checks against Java snippets and verifying fixes.

%package docgen
Summary: Error Prone checker documentation generator
Group: Development/Java

%description docgen
The upstream generator for Error Prone checker documentation.

%package docgen-processor
Summary: Error Prone checker documentation annotation processor
Group: Development/Java

%description docgen-processor
The annotation processor that extracts checker documentation metadata.

%prep
%setup -a1
%autopatch -p1
cp %SOURCE2 software-and-algorithms-LICENSE
cp %SOURCE3 safere-LICENSE
cp %SOURCE4 safere-LICENSE-Unicode.txt
cp %SOURCE5 protobuf-java-LICENSE
cp %SOURCE6 CC0-1.0.txt

# Refaster requires the genuine bundled Core classifier.
%mvn_package :error_prone_core:jar:with-dependencies: error_prone_core

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-toolchains-plugin
# Surefire uses the RPM-selected Java 21 without a separate toolchain registry.
surefire='pom:project/pom:build/pom:plugins/pom:plugin'
surefire="$surefire[pom:artifactId='maven-surefire-plugin']"
%pom_xpath_remove "$surefire/pom:configuration/pom:jdkToolchain"
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :protobuf-maven-plugin core
%pom_remove_dep com.google.gwt.inject:gin core

# These optional annotation APIs are used by the unchanged Core test sources.
%pom_add_dep org.apache.geronimo.specs:geronimo-annotation_1.3_spec:1.0:test \
    core
%pom_add_dep org.checkerframework:checker-compat-qual:2.5.6:test core
%pom_add_dep com.google.j2objc:j2objc-annotations:3.1:test core

%pom_remove_dep io.github.eisop:dataflow-errorprone core
%pom_add_dep org.checkerframework:dataflow-errorprone core
%pom_remove_dep io.github.eisop:dataflow-errorprone check_api
%pom_add_dep org.checkerframework:dataflow-errorprone check_api
%pom_add_dep org.checkerframework:javacutil check_api
%pom_remove_dep io.github.eisop:dataflow-errorprone test_helpers
%pom_add_dep org.checkerframework:dataflow-errorprone test_helpers

%build
%mvn_build -s -j

%install
%mvn_install

%files parent -f .mfiles-error_prone_parent

%files annotation -f .mfiles-error_prone_annotation

%files annotations -f .mfiles-error_prone_annotations

%files check-api -f .mfiles-error_prone_check_api

%files core -f .mfiles-error_prone_core
%doc COPYING software-and-algorithms-LICENSE
%doc safere-LICENSE safere-LICENSE-Unicode.txt protobuf-java-LICENSE
%doc CC0-1.0.txt

%files refaster -f .mfiles-error_prone_refaster

%files type-annotations -f .mfiles-error_prone_type_annotations

%files test-helpers -f .mfiles-error_prone_test_helpers

%files docgen -f .mfiles-error_prone_docgen

%files docgen-processor -f .mfiles-error_prone_docgen_processor

%changelog
* Wed Nov 11 2026 Ivan Khanas <xeno@altlinux.org> 2.52.0-alt2
- Add the J2ObjC annotations build dependency.

* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 2.52.0-alt1
- New version.

* Sun Nov 30 2025 Ivan Khanas <xeno@altlinux.org> 2.44.0-alt2
- Build fat jar with dependencies for core.
- Fix services registration.
- Java 21 compilation.

* Tue Nov 25 2025 Ivan Khanas <xeno@altlinux.org> 2.44.0-alt1
- First build for ALT.
