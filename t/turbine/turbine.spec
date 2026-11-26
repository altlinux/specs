%define _unpackaged_files_terminate_build 1

Name: turbine
Version: 1.17.0
Release: alt1

Summary: Java header compiler
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/turbine
VCS: https://github.com/google/turbine.git

Source: %name-%version.tar
Patch0: 0001-Build-Turbine-and-its-compatible-tests-with-JDK-21.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: protobuf-compiler
BuildRequires: mvn(com.google.auto:auto-common)
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(com.google.jimfs:jimfs)
BuildRequires: mvn(com.google.protobuf:protobuf-java)
BuildRequires: mvn(com.google.testparameterinjector:test-parameter-injector)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(com.google.truth.extensions:truth-java8-extension)
BuildRequires: mvn(com.google.truth.extensions:truth-proto-extension)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-tree)
BuildRequires: mvn(org.ow2.asm:asm-util)

%description
Turbine compiles Java API headers into interface JARs for downstream
compilation and dependency tracking.

%prep
%setup
%autopatch -p1
%pom_xpath_remove pom:project/pom:build/pom:extensions
%pom_xpath_remove pom:project/pom:profiles
%pom_remove_plugin org.xolstice.maven.plugins:protobuf-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-shade-plugin
%pom_xpath_remove \
    '//pom:compilerArgs/pom:arg[starts-with(text(),"-Xplugin:ErrorProne")]'
%pom_xpath_remove \
    '//pom:annotationProcessorPaths/pom:path[pom:artifactId="error_prone_core"]'
protoc --java_out=java proto/deps.proto proto/manifest.proto
%mvn_file :turbine turbine

%build
%mvn_build -j

%install
%mvn_install
%jpackage_script com.google.turbine.main.Main "" "" %name:guava:protobuf %name

%files -f .mfiles
%doc LICENSE
%_bindir/turbine

%changelog
* Fri Nov 27 2026 Ivan Khanas <xeno@altlinux.org> 1.17.0-alt1
- Initial build for ALT.
