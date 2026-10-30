%define _unpackaged_files_terminate_build 1

%define dist_dir %_libexecdir/%name
%define dist_common_dir %dist_dir/common
%define dist_root_dir %dist_dir
%define dist_kotlinc_lib_dir %dist_dir/kotlinc/lib
%define kotlin_maven_version %version
%define kotlin_gradle_variant gradle96
%define gradle_cache_dir %_builddir/gradle-home
%define m2_seed_repo %gradle_cache_dir/m2-seed
%define runtime_repo %_builddir/runtime-m2
%define vendor_license Apache-2.0 and BSD-2-Clause and BSD-3-Clause
%define vendor_extra_license MIT and EPL-1.0 and EPL-2.0
%define build_home %_builddir/home
%define build_tmp %build_home/tmp
%define m2_repo %build_home/.m2/repository
%define share_java_kotlin_dir %_javadir/%name
%define lib_java_kotlin_dir %_jnidir/%name

%define build_workers 10
%define build_heap 6g
%define build_metaspace 2g
%define build_direct_memory 512m

%define build_jvmargs -Xmx%build_heap -XX:MaxMetaspaceSize=%build_metaspace
%define direct_memory_arg -XX:MaxDirectMemorySize=%build_direct_memory

Name: kotlin
Version: 2.4.21
Release: alt1

Summary: Kotlin compiler distribution
License: Apache-2.0
Group: Development/Java
Url: https://kotlinlang.org/
VCS: https://github.com/JetBrains/kotlin.git
ExclusiveArch: %java_arches

Source0: %name-%version.tar
Source1: gradle-cache-base.tar.zst
Source2: gradle-cache-modules-01.tar.zst
Source3: gradle-cache-modules-02.tar.zst
Source4: gradle-cache-modules-03.tar.zst
Source5: gradle-cache-modules-04.tar.zst
Source6: gradle-cache-intellij.tar.zst
Source7: gradle-cache-kotlin-01.tar.zst
Source8: gradle-cache-kotlin-02.tar.zst
Source9: gradle-cache-m2-seed.tar.zst
Source10: klib-install.xml
# These original Trove notices are absent from its bootstrap JAR.
Source11: trove-LICENSE.txt
Source12: trove-README-license.txt
Source13: gradle-cache-npm.tar.zst
Source14: kotlin-runtime-cache.tar.zst
Source15: install-runtime.py
Source16: gradle-cache-linux-arm64.tar.zst
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven
BuildRequires: maven-local
BuildRequires: gradle
BuildRequires: zstd
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: java-11-openjdk-devel
BuildRequires: java-17-openjdk-devel
BuildRequires: java-21-openjdk-devel
BuildRequires: java-25-openjdk-devel

Requires: java-17-openjdk-headless
Requires: %name-stdlib = %EVR
Requires: %name-reflect = %EVR
Requires: %name-test = %EVR
Requires: %name-compiler = %EVR
Requires: %name-plugins = %EVR

%description
Kotlin compiler distribution built from the stable upstream release.
The package installs the full distribution layout, including compiler
launchers, libraries, common klibs and metadata produced by the build.

%package stdlib
Summary: Kotlin standard library artifacts
License: Apache-2.0
Group: Development/Java

%description stdlib
Maven artifacts for the Kotlin standard library modules.

%package reflect
Summary: Kotlin reflection library artifacts
License: Apache-2.0
Group: Development/Java

%description reflect
Maven artifacts for Kotlin reflection support.

%package test
Summary: Kotlin test library artifacts
License: Apache-2.0
Group: Development/Java

%description test
Maven artifacts for Kotlin test integration modules.

%package compiler
Summary: Kotlin compiler library artifacts
License: Apache-2.0
Group: Development/Java

%description compiler
Maven artifacts for the Kotlin compiler, daemon, scripting and annotation
processing libraries.

%package plugins
Summary: Kotlin compiler plugin artifacts
License: Apache-2.0
Group: Development/Java

%description plugins
Maven artifacts for Kotlin compiler plugins shipped by upstream.

%package gradle-plugin
Summary: Kotlin Gradle plugin artifacts
License: Apache-2.0
Group: Development/Java

%description gradle-plugin
Maven artifacts for the Kotlin Gradle plugin and its marker modules,
using the Gradle 9.6 API variant for the system Gradle.

%package maven
Summary: Additional Maven artifacts for the Kotlin bootstrap build
License: Apache-2.0
Group: Development/Java

%description maven
Published Maven artifacts produced by the Kotlin bootstrap build, including
POM files and final JAR payloads not split into dedicated subpackages.

%package build-statistics
Summary: Kotlin compiler build statistics library
Group: Development/Java

%description build-statistics
Build report metrics and statistics runtime used by the Kotlin Gradle plugin.
Built and published together with the Kotlin compiler and build tools API.

%package tooling-core
Summary: Kotlin shared build tooling API
Group: Development/Java

%description tooling-core
Shared Kotlin build tooling interfaces used by the Kotlin Gradle plugin.

%package bootstrap-libs
Summary: Versioned runtime libraries for the Kotlin bootstrap
License: %vendor_license and %vendor_extra_license and LGPL-2.1-or-later
Group: Development/Java

%description bootstrap-libs
Private versioned runtime libraries retained from the offline Maven cache.
They allow Kotlin to bootstrap without Java library packages from the
repository, including serialization and coroutine dependencies that
themselves need the Kotlin compiler and Gradle plugin.

%package ide
Summary: Kotlin compiler and Analysis API artifacts for IDE integration
Group: Development/Java

%description ide
Compiler, analysis and JPS artifacts published by the same Kotlin source
build for integration with development environments.

%prep
%setup
%autopatch -p1
cp %SOURCE11 %SOURCE12 .

# Keep every offline build independent of earlier contents of the build root.
rm -rf %gradle_cache_dir %build_home
mkdir -p %gradle_cache_dir %m2_repo %build_tmp
tar --zstd -xf %SOURCE1 -C %_builddir
tar --zstd -xf %SOURCE2 -C %_builddir
tar --zstd -xf %SOURCE3 -C %_builddir
tar --zstd -xf %SOURCE4 -C %_builddir
tar --zstd -xf %SOURCE5 -C %_builddir
tar --zstd -xf %SOURCE6 -C %_builddir
tar --zstd -xf %SOURCE7 -C %_builddir
tar --zstd -xf %SOURCE8 -C %_builddir
tar --zstd -xf %SOURCE9 -C %_builddir
tar --zstd -xf %SOURCE13 -C %_builddir
tar --zstd -xf %SOURCE16 -C %_builddir
rm -rf %runtime_repo
tar --zstd -xf %SOURCE14 -C %_builddir
cp -al %m2_seed_repo/. %m2_repo/


%build
export HOME=%build_home
export TMPDIR=%build_tmp
export GRADLE_USER_HOME=%gradle_cache_dir
export GRADLE_OPTS="-Duser.home=%build_home -Djava.io.tmpdir=%build_tmp"
export MAVEN_OPTS="%build_jvmargs \
  -Duser.home=%build_home -Djava.io.tmpdir=%build_tmp"
export npm_config_cache=%gradle_cache_dir/npm-cache
export JDK_1_8=%_jvmdir/java-1.8.0-openjdk
export JDK_11=%_jvmdir/java-11-openjdk
export JDK_17_0=%_jvmdir/java-17-openjdk
export JDK_21=%_jvmdir/java-21-openjdk
export JDK_25_0=%_jvmdir/java-25-openjdk

toolchain_paths=$JDK_1_8,$JDK_11,$JDK_17_0
toolchain_paths=$toolchain_paths,$JDK_21,$JDK_25_0

# Gradle keeps its daemon home; publish to the repository used by Maven.
gradle dist installJps installIdeArtifacts --offline --no-daemon \
  --no-watch-fs --no-configuration-cache --no-build-cache --no-scan \
  --max-workers=%build_workers --dependency-verification=off \
  -x test \
  -Dorg.gradle.java.home=$JDK_21 \
  -Dmaven.repo.local=%m2_repo \
  -Dorg.gradle.jvmargs="%build_jvmargs %direct_memory_arg \
    -Djava.io.tmpdir=%build_tmp" \
  -Dorg.gradle.java.installations.auto-download=false \
  -Dorg.gradle.parallel=true \
  -Pkotlin.compiler.execution.strategy=in-process \
  -Pkotlin.daemon.jvmargs="%build_jvmargs" \
  -Dorg.gradle.java.installations.auto-detect=false \
  -Dorg.gradle.java.installations.paths="$toolchain_paths" \
  -Pkotlin.native.enabled=false \
  -Pkotlin.build.internal.gradle.setup=false \
  -Porg.gradle.kotlin.dsl.allWarningsAsErrors=false \
  -PdeployVersion=%version -Pbuild.number=%version \
  -Ppublish.ide.plugin.dependencies=true -PdisableBreakpad

%install
rm -rf %buildroot%dist_dir
install -d %buildroot%dist_dir
cp -al dist/. %buildroot%dist_dir/
rm -rf %buildroot%dist_dir/maven
find %buildroot%dist_dir -type f \
  \( -name '*-sources.jar' -o -name '*-javadoc.jar' \) -delete
find %buildroot%dist_dir -type l \
  \( -name '*-sources.jar' -o -name '*-javadoc.jar' \) -delete

javadir_rel=$(realpath -m --relative-to=%dist_kotlinc_lib_dir \
  %_javadir/%name)
jnidir_rel=$(realpath -m --relative-to=%dist_kotlinc_lib_dir \
  %_jnidir/%name)
root_javadir_rel=$(realpath -m --relative-to=%dist_root_dir \
  %_javadir/%name)

symlink_kotlinc_lib() {
  rm -f "%buildroot%dist_kotlinc_lib_dir/$1"
  ln -s "$2" "%buildroot%dist_kotlinc_lib_dir/$1"
}

symlink_root_lib() {
  rm -f "%buildroot%dist_root_dir/$1"
  ln -s "$2" "%buildroot%dist_root_dir/$1"
}

for jar in \
  jvm-abi-gen.jar \
  kotlin-annotation-processing-runtime.jar \
  kotlin-annotation-processing.jar \
  kotlin-annotations-jvm.jar \
  kotlin-daemon-client.jar \
  kotlin-daemon.jar \
  kotlin-main-kts.jar \
  kotlin-metadata-jvm.jar \
  kotlin-reflect.jar \
  kotlin-script-runtime.jar \
  kotlin-scripting-common.jar \
  kotlin-scripting-compiler-impl.jar \
  kotlin-scripting-compiler.jar \
  kotlin-scripting-jvm.jar \
  kotlin-serialization-compiler-plugin.jar \
  kotlin-stdlib-jdk7.jar \
  kotlin-stdlib-jdk8.jar \
  kotlin-stdlib.jar \
  kotlin-test-junit.jar \
  kotlin-test-junit5.jar \
  kotlin-test-testng.jar \
  kotlin-test.jar
do
  symlink_kotlinc_lib "$jar" "$javadir_rel/$jar"
done

symlink_kotlinc_lib kotlin-compiler.jar \
  "$jnidir_rel/kotlin-compiler.jar"
symlink_kotlinc_lib allopen-compiler-plugin.jar \
  "$javadir_rel/kotlin-allopen-compiler-plugin.jar"
symlink_kotlinc_lib assignment-compiler-plugin.jar \
  "$javadir_rel/kotlin-assignment-compiler-plugin.jar"
symlink_kotlinc_lib compose-compiler-plugin.jar \
  "$javadir_rel/kotlin-compose-compiler-plugin.jar"
symlink_kotlinc_lib kotlinx-serialization-compiler-plugin.jar \
  "$javadir_rel/kotlin-serialization-compiler-plugin.jar"
symlink_kotlinc_lib lombok-compiler-plugin.jar \
  "$javadir_rel/kotlin-lombok-compiler-plugin.jar"
symlink_kotlinc_lib noarg-compiler-plugin.jar \
  "$javadir_rel/kotlin-noarg-compiler-plugin.jar"
symlink_kotlinc_lib parcelize-runtime.jar \
  "$javadir_rel/kotlin-parcelize-runtime.jar"
symlink_kotlinc_lib power-assert-compiler-plugin.jar \
  "$javadir_rel/kotlin-power-assert-compiler-plugin.jar"
symlink_kotlinc_lib sam-with-receiver-compiler-plugin.jar \
  "$javadir_rel/kotlin-sam-with-receiver-compiler-plugin.jar"
symlink_kotlinc_lib scripting-compiler.jar \
  "$javadir_rel/kotlin-scripting-compiler.jar"

symlink_root_lib kotlin-stdlib-jvm-minimal-for-test.jar \
  "$root_javadir_rel/kotlin-stdlib-jvm-minimal-for-test.jar"

install -d %buildroot%_bindir
launcher_rel=$(realpath -m --relative-to=%_bindir %dist_dir/kotlinc/bin)
for tool in kapt kotlin kotlinc kotlinc-js kotlinc-jvm; do
  ln -sfn "$launcher_rel/$tool" %buildroot%_bindir/$tool
done

rm -rf .xmvn .xmvn-reactor
# XMvn's standard repositories accept JARs; retain Kotlin's KLIB artifacts too.
klib_root=%_javadir
%mvn_config repositories "$(sed \
  "s|@javadir@|${klib_root#/}|g" %SOURCE10)"
%mvn_package org.jetbrains.kotlin:*:jar:gradle* gradle-plugin
%mvn_package :*-for-ide ide
%mvn_package :kotlin-jps* ide
%mvn_package :kotlin-stdlib* stdlib
%mvn_package :kotlin-reflect reflect
%mvn_package :kotlin-test* test

%mvn_package :kotlin-compiler compiler
%mvn_package :kotlin-compiler-client-embeddable compiler
%mvn_package :kotlin-compiler-embeddable compiler
%mvn_package :kotlin-compiler-runner compiler
%mvn_package :kotlin-daemon* compiler
%mvn_package :kotlin-script-runtime compiler
%mvn_package :kotlin-scripting-* compiler
%mvn_package :kotlin-main-kts compiler
%mvn_package :kotlin-metadata-jvm compiler
%mvn_package :kotlin-annotation-processing compiler
%mvn_package :kotlin-annotation-processing-* compiler
%mvn_package :kotlin-annotations-jvm compiler
%mvn_package :jvm-abi-gen compiler

%mvn_package :kotlin-allopen-compiler-plugin* plugins
%mvn_package :kotlin-assignment-compiler-plugin* plugins
%mvn_package :kotlin-compose-compiler-plugin* plugins
%mvn_package :kotlin-lombok-compiler-plugin* plugins
%mvn_package :kotlin-noarg-compiler-plugin* plugins
%mvn_package :kotlin-parcelize-* plugins
%mvn_package :kotlin-power-assert-compiler-plugin* plugins
%mvn_package :kotlin-sam-with-receiver-compiler-plugin* plugins
%mvn_package :kotlin-serialization-compiler-plugin* plugins

%mvn_package :kotlin-gradle-plugin* gradle-plugin
%mvn_package :kotlin-build-tools* gradle-plugin
%mvn_package :kotlin-compiler-args-properties gradle-plugin
%mvn_package :kotlin-allopen gradle-plugin
%mvn_package :kotlin-assignment gradle-plugin
%mvn_package :kotlin-lombok gradle-plugin
%mvn_package :kotlin-noarg gradle-plugin
%mvn_package :kotlin-power-assert gradle-plugin
%mvn_package :kotlin-sam-with-receiver gradle-plugin
%mvn_package :kotlin-serialization gradle-plugin
%mvn_package :compose-compiler-gradle-plugin gradle-plugin
%mvn_package *:org.jetbrains.kotlin.*.gradle.plugin gradle-plugin

%mvn_package :kotlin-build-statistics build-statistics
%mvn_package :kotlin-tooling-core tooling-core
%mvn_file :kotlin-build-statistics \
    kotlin-build-statistics/kotlin-build-statistics
%mvn_file :kotlin-tooling-core kotlin-tooling-core/kotlin-tooling-core

rm -rf .javapackages_cache
# Register vendored runtime providers before resolving Kotlin dependencies.
python3 %SOURCE15 %runtime_repo vendor-licenses \
  --artifact-command="%mvn_artifact" \
  --package-command="%mvn_package" \
  --file-command="%mvn_file" \
  --compat-command="%mvn_compat_version"

find %m2_repo -type f -path "*/%kotlin_maven_version/*.pom" \
  | LC_ALL=C sort > pom.list
# Maven metadata must register parent artifacts before children. These two
# parent POMs sort after their descendants in the local repository paths.
for parent in kotlin-project kotlin-archetypes-parent; do
  parent_dir=%m2_repo/org/jetbrains/kotlin/$parent/%kotlin_maven_version
  parent_pom=$parent_dir/$parent-%kotlin_maven_version.pom
  if [ -f "$parent_pom" ]; then
    %mvn_artifact "$parent_pom"
  fi
done
while read -r pom; do
  dir=$(dirname "$pom")
  version=$(basename "$dir")
  artifact_id=$(basename "$(dirname "$dir")")
  rel_dir=${dir#%m2_repo/}
  group_path=$(dirname "$(dirname "$rel_dir")")
  [ "$group_path" = "." ] && group_path=
  group_id=$(printf '%%s\n' "$group_path" | tr '/' '.')

  # Use upstream publication metadata and let XMvn generate runtime deps.
  # Swift export requires a native toolchain, disabled for this JVM build.
  case "$artifact_id" in
    kotlin-project|kotlin-archetypes-parent|sir*|swift-export*)
      continue
      ;;
  esac

  case "$artifact_id" in
    *-for-ide)
      # publishJarsForIde embeds these source-project JARs in its fat JAR.
      if grep -q '<dependencies>' "$pom"; then
        %pom_remove_dep org.jetbrains.kotlin: "$pom"
      fi
      %pom_add_dep org.jetbrains.kotlin:kotlin-stdlib:%version "$pom"
      ;;
    kotlin-scripting-compiler)
      # The system JLine supplies the API without the upstream jdk8 classifier.
      if grep -q '<classifier>jdk8</classifier>' "$pom"; then
        %pom_xpath_remove \
        "pom:dependencies/pom:dependency[pom:groupId='org.jline']/"\
"pom:classifier" "$pom"
      fi
      ;;
  esac

  main_artifact=
  for ext in jar klib; do
    candidate=$dir/$artifact_id-$version.$ext
    if [ -f "$candidate" ]; then
      main_artifact=$candidate
      break
    fi
  done
  # Use one Gradle API variant for both default and classified coordinates.
  gradle_artifact=$dir/$artifact_id-$version-%kotlin_gradle_variant.jar
  if [ -f "$gradle_artifact" ]; then
    main_artifact=$gradle_artifact
    %mvn_alias "$group_id:$artifact_id:jar::$version" \
      "$group_id:$artifact_id:jar:%kotlin_gradle_variant:$version"
  fi
  if [ -n "$main_artifact" ]; then
    %mvn_artifact "$pom" "$main_artifact"
  else
    %mvn_artifact "$pom"
  fi

  for artifact in \
    "$dir/$artifact_id-$version"-*.jar \
    "$dir/$artifact_id-$version"-*.klib
  do
    [ -f "$artifact" ] || continue
    file_name=${artifact##*/}
    ext=${file_name##*.}
    base_name=$(basename "$artifact" ".$ext")
    classifier=
    case "$base_name" in
      "$artifact_id-$version")
        ;;
      "$artifact_id-$version"-*)
        classifier=${base_name#"$artifact_id-$version"-}
        ;;
      *)
        continue
        ;;
    esac
    case "$classifier" in
      sources|javadoc|*-sources|*-javadoc|gradle[0-9]*)
        continue
        ;;
    esac
    %mvn_artifact \
      "$group_id:$artifact_id:$ext:$classifier:$version" "$artifact"
  done
done < pom.list

%mvn_package : maven
%mvn_install

find %buildroot -type f -name '*-sources.jar' -delete
find %buildroot -type l -name '*-sources.jar' -delete
for mfiles in .mfiles-*; do
  [ -f "$mfiles" ] || continue
  awk '!/-sources\.jar$/' "$mfiles" > "$mfiles.filtered"
  mv "$mfiles.filtered" "$mfiles"
done

%files
%doc ReadMe.md license
%_bindir/kapt
%_bindir/kotlin
%_bindir/kotlinc
%_bindir/kotlinc-js
%_bindir/kotlinc-jvm
%dist_dir

%files stdlib -f .mfiles-stdlib
%doc license

%files reflect -f .mfiles-reflect
%doc license

%files test -f .mfiles-test
%doc license

%files compiler -f .mfiles-compiler
%doc license

%files plugins -f .mfiles-plugins
%doc license

%files gradle-plugin -f .mfiles-gradle-plugin
%doc license

%files maven -f .mfiles-maven
%doc license

%files build-statistics -f .mfiles-build-statistics
%doc license

%files tooling-core -f .mfiles-tooling-core
%doc license

%files bootstrap-libs -f .mfiles-bootstrap-libs
%doc license vendor-licenses trove-LICENSE.txt trove-README-license.txt

%files ide -f .mfiles-ide
%doc license

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 2.4.21-alt1
- New version.
- Ship one Gradle API variant for the system Gradle.
- Include Linux ARM64 Node and Rollup in the offline build cache.
- Defer platform-specific Wasm test engines until tests are requested.
- Honor disabled Native targets and test dependencies on JVM build hosts.
- Package build tooling and IDE artifacts from the same source build.

* Thu Oct 08 2026 Ivan Khanas <xeno@altlinux.org> 2.4.20-alt0.5031.1
- Fix FTBFS: build with system Gradle 9.

* Mon Jun 22 2026 Ivan Khanas <xeno@altlinux.org> 2.4.20-alt0.5031
- Initial vendored build for bootstraping.

* Wed Jul 15 2020 Michael Shigorin <mike@altlinux.org> 1.3.72-alt1
- initial release
