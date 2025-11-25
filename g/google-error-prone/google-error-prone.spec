Name: google-error-prone
Version: 2.44.0
Release: alt1

Summary: Catch common Java mistakes as compile-time errors
License: Apache-2.0
Group: Development/Java
Url: https://errorprone.info
Vcs: https://github.com/google/error-prone.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: rpm-build-java
# Java-17 target compilation for noarch packaging.
BuildRequires: jpackage-17-compat
BuildRequires: truth
BuildRequires: guava
BuildRequires: jspecify
BuildRequires: checker-dataflow-errorprone
BuildRequires: checker-javacutil
BuildRequires: auto-common
BuildRequires: auto-value
BuildRequires: auto-value-annotations
BuildRequires: protobuf-java
BuildRequires: protobuf-java-util
BuildRequires: jakarta-annotations
BuildRequires: os-maven-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-source-plugin
BuildRequires: bnd-maven-plugin
BuildRequires: software-and-algorithms
BuildRequires: auto-service
BuildRequires: maven-shade-plugin
BuildRequires: pcollections

%description
Error Prone is a static analysis tool for Java that catches common programming
mistakes at compile time. Developed by Google, it integrates with the Java
compiler to detect bug-prone patterns, enforce best practices, and provide
actionable diagnostics. Error Prone helps developers improve code quality,
maintainability, and reliability by preventing subtle errors before they reach
production.

%package parent
Summary: Shared Maven parent POM for Error Prone ecosystem projects
Group: Development/Java
BuildArch: noarch

%description parent
Error Prone Parent is a Maven parent POM that provides shared configuration,
dependency management, and plugin settings for projects in the Error Prone ecosystem.
It ensures consistent build behavior across Error Prone integrations and related tools.

%package annotations
Summary: Annotation library for Error Prone static bug detection tool
Group: Development/Java
BuildArch: noarch

%description annotations
A collection of Java annotations used by Error Prone compiler to perform
advanced static analysis and catch bugs during compilation.  Includes
@CheckReturnValue, @Immutable, and other annotations for improved code
analysis.

%package annotation
Summary: Error Prone Annotation module
Group: Development/Java
BuildArch: noarch

%description annotation
Error Prone Annotation module containing core annotation definitions.

%package check-api
Summary: Error Prone Check API module
Group: Development/Java
BuildArch: noarch

%description check-api
API for creating custom Error Prone checks and static analysis rules.

%package core
Summary: Error Prone Core analysis engine
Group: Development/Java
BuildArch: noarch

%description core
Core Error Prone static analysis engine that performs Java code inspection
and bug detection during compilation.

%package refaster
Summary: Error Prone Refaster template system
Group: Development/Java
BuildArch: noarch

%description refaster
Refaster template system for defining code transformation rules and refactoring
patterns in Error Prone.

%package type-annotations
Summary: Error Prone Type Annotations support
Group: Development/Java
BuildArch: noarch

%description type-annotations
Type annotation support for Error Prone, enabling advanced type-based
static analysis and verification.

%prep
%setup
%autopatch -p1

%pom_disable_module docgen
%pom_disable_module docgen_processor
%pom_disable_module test_helpers

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-toolchains-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_plugin :protobuf-maven-plugin core

# We don`t want to package forked checker-framework.
%pom_remove_dep io.github.eisop:dataflow-errorprone core
%pom_add_dep org.checkerframework:dataflow-errorprone core

%pom_remove_dep io.github.eisop:dataflow-errorprone check_api
%pom_add_dep org.checkerframework:dataflow-errorprone check_api
%pom_add_dep org.checkerframework:javacutil check_api

%pom_remove_dep com.github.ben-manes.caffeine:caffeine check_api

%pom_remove_dep com.google.auto.service:auto-service-annotations core
%pom_remove_dep com.google.googlejavaformat:google-java-format core

# getLast and getFirst are unavailable in java-17.
find check_api -name "*.java" -type f -exec sed -i 's/\.getFirst()/.get(0)/g' {} \;
find core -name "*.java" -type f -exec sed -i 's/\.getFirst()/.get(0)/g' {} \;
find core -name "*.java" -type f -exec perl -i -pe 's/(\w+)\.getLast\(\)/$1.get($1.size() - 1)/g' {} \;

%pom_remove_dep com.google.auto.service:auto-service-annotations refaster

%build
# Most of test deps are unavailable now and have cyclic dependencies on errorprone.
%mvn_build -s -f -j -- -Dmaven.test.skip=true

%install
%mvn_install

# We don`t need other errorprone elements as deps for core artifact because of shade jar packaging.
%pom_remove_dep  com.google.errorprone: %buildroot/%_mavenpomdir/google-error-prone/error_prone_core.pom

%files parent -f .mfiles-error_prone_parent

%files annotation -f .mfiles-error_prone_annotation

%files annotations -f .mfiles-error_prone_annotations

# Must be used with adding --enable-preview compiler argument because of java-17 compilation.
%files check-api -f .mfiles-error_prone_check_api

# Must be used with adding --enable-preview compiler argument because of java-17 compilation.
%files core -f .mfiles-error_prone_core

%files refaster -f .mfiles-error_prone_refaster

%files type-annotations -f .mfiles-error_prone_type_annotations

%changelog
* Tue Nov 25 2025 Ivan Khanas <xeno@altlinux.org> 2.44.0-alt1
- First build for ALT.
