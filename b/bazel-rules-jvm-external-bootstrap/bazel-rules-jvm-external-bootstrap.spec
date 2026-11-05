%define _unpackaged_files_terminate_build 1
%define rje_java_package com/github/bazelbuild/rules_jvm_external

%define resolver_package %rje_java_package/resolver

Name: bazel-rules-jvm-external-bootstrap
Version: 7.2
Release: alt1

Summary: Source-built bootstrap and Maven tools for rules_jvm_external
License: Apache-2.0
Group: Development/Java
URL: https://github.com/bazel-contrib/rules_jvm_external
VCS: https://github.com/bazel-contrib/rules_jvm_external.git

Source0: %name-%version.tar
Patch0: %name-%version-alt-system-tools.patch
Source1: tools-pom.xml
Source2: make-launchers.py
# Exact upstream IndexJar regression inputs; never runtime dependencies.
Source4: indexjar-fixtures.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-python3
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: guava
BuildRequires: objectweb-asm
BuildRequires: kotlin-compiler
BuildRequires: kotlin-stdlib
BuildRequires: maven-lib
BuildRequires: junit
BuildRequires: hamcrest
BuildRequires: jetbrains-annotations
BuildRequires: kotlin-reflect
BuildRequires: maven-resolver
BuildRequires: plexus-cipher
BuildRequires: plexus-sec-dispatcher
BuildRequires: plexus-utils
BuildRequires: plexus-xml
BuildRequires: slf4j
BuildRequires: jansi
BuildRequires: maven-dependency-plugin
BuildRequires: mvn(org.altlinux.bootstrap:rules-java-runfiles)

%description
Source-built Hasher, IndexJar, LockFileConverter and Outdated bootstrap tools
and the Maven resolver for rules_jvm_external. The Starlark module is a
separate subpackage; Gradle and cloud backends retain their upstream routes.

%package -n bazel-rules-jvm-external
Summary: Starlark Maven dependency rules with system bootstrap tools

Group: Development/Java

%description -n bazel-rules-jvm-external
Starlark sources for the rules_jvm_external Bazel module. The four bootstrap
JARs and standard Maven pin targets use source-built system tools. Gradle,
cloud publishing and explicit resolver SPI additions retain the upstream
source-build route and need their own dependencies. Module resolution needs
an offline Bazel dependency registry or explicit system module overrides.

%prep
%setup
%autopatch -p1
cp %SOURCE1 pom.xml
cp %SOURCE2 make-launchers.py
tar -xf %SOURCE4
cp -a resolver/src/main/java/%resolver_package/*.java \
    private/tools/java/com/github/bazelbuild/rules_jvm_external/resolver/
%mvn_file : bazel-rules-jvm-external-bootstrap/tools

%build
# Recreate the original Bazel runfiles layout for the unchanged fixture suite.
cp -a indexjar-fixtures .indexjar-runfiles
fixture_root=.indexjar-runfiles/rules_jvm_external/tests
fixture_package=com/github/bazelbuild/rules_jvm_external/jar
install -D -m644 tests/custom_maven_install/service_indexing_testing.json \
    "$fixture_root/custom_maven_install/service_indexing_testing.json"
mkdir -p "$fixture_root/$fixture_package"
# ALT ships the compiler main class rather than a kotlinc wrapper.
compiler_cp=%_jnidir/kotlin/kotlin-compiler.jar
compiler_cp="$compiler_cp:%_javadir/kotlin/kotlin-stdlib.jar"
compiler_cp="$compiler_cp:%_javadir/kotlin/kotlin-reflect.jar"
compiler_cp="$compiler_cp:%_javadir/kotlin/kotlin-script-runtime.jar"
kotlinx_lib=%_javadir/kotlin/bootstrap/org.jetbrains.kotlinx
compiler_cp="$compiler_cp:$kotlinx_lib/kotlinx-coroutines-core-jvm-1.8.0.jar"
compiler_cp="$compiler_cp:%_javadir/jetbrains-annotations/annotations.jar"
java -cp "$compiler_cp" org.jetbrains.kotlin.cli.jvm.K2JVMCompiler \
    -no-stdlib -no-reflect -classpath %_javadir/kotlin/kotlin-stdlib.jar \
    tests/$fixture_package/testdata/TopLevel.kt \
    -d "$fixture_root/$fixture_package/kotlin_top_level_fixture.jar"
export RUNFILES_DIR="$PWD/.indexjar-runfiles"
%mvn_build -j
xmvn --batch-mode --offline \
    org.apache.maven.plugins:maven-dependency-plugin:build-classpath \
    -Dmdep.outputFile=runtime-classpath -DincludeScope=runtime

%install
%mvn_install
python3 make-launchers.py %buildroot %_javadir \
    %_datadir/bazel/tools/rules_jvm_external
install -d %buildroot%_datadir/bazel/rules/rules_jvm_external
cp -a BUILD MODULE.bazel REPO.bazel LICENSE AUTHORS *.bzl *.json private \
    resolver settings gradle.BUILD.bazel \
    %buildroot%_datadir/bazel/rules/rules_jvm_external/
rules_dir=%buildroot%_datadir/bazel/rules/rules_jvm_external
prebuilt_dir="$rules_dir/private/tools/prebuilt"
for helper in hasher index_jar lock_file_converter outdated \
    add_jar_manifest_entry; do
    ln -s ../../../../../tools/rules_jvm_external/${helper}_deploy.jar \
        "$prebuilt_dir/${helper}_deploy.jar"
done

# The source subpackage requires the main package owning this license.
rm %buildroot%_datadir/bazel/rules/rules_jvm_external/LICENSE
ln -s %_defaultdocdir/%name-%version/LICENSE \
    %buildroot%_datadir/bazel/rules/rules_jvm_external/LICENSE

# Keep upstream README files in the source archive only.
find %buildroot%_datadir/bazel -type f -iname '*readme*' -delete

%check
python3 tests/alt_system_tool_test.py private/system_tool.py.tpl

%files -f .mfiles
%doc LICENSE AUTHORS
%doc private/tools/java/%rje_java_package/zip/StableZipEntry.java
%dir %_datadir/bazel
%dir %_datadir/bazel/tools
%dir %_datadir/bazel/tools/rules_jvm_external
%_datadir/bazel/tools/rules_jvm_external/*_deploy.jar
%_datadir/bazel/tools/rules_jvm_external/maven_resolver.jar

%files -n bazel-rules-jvm-external
%doc AUTHORS
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_jvm_external

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 7.2-alt1
- Initial build for ALT.
