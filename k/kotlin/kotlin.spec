%define _unpackaged_files_terminate_build 1

%global snapshot 5031

Name: kotlin
Version: 2.4.20
Release: alt0.%snapshot

%global source_dir %name-%version-dev-%snapshot
%global dist_dir %_libexecdir/%name
%global dist_common_dir %dist_dir/common
%global dist_root_dir %dist_dir
%global dist_kotlinc_lib_dir %dist_dir/kotlinc/lib
%global kotlin_maven_version 2.4.255-SNAPSHOT
%global gradle_cache_dir %_builddir/gradle-home
%global m2_seed_repo %gradle_cache_dir/m2-seed
%global build_home %_builddir/home
%global build_tmp %build_home/tmp
%global m2_repo %build_home/.m2/repository
%global share_java_kotlin_dir %_javadir/%name
%global lib_java_kotlin_dir %_jnidir/%name

Summary: Kotlin compiler distribution
License: Apache-2.0
Group: Development/Java
Url: https://github.com/JetBrains/kotlin
ExclusiveArch: %java_arches

Source0: %source_dir.tar
Source1: gradle-cache-base.tar.zst
Source2: gradle-cache-m2-seed-installjps.tar.zst
Source3: gradle-cache-modules-metadata.tar.zst
Source4: gradle-cache-caches-misc.tar.zst
Source5: gradle-cache-caches-8-14-core.tar.zst
Source6: gradle-cache-caches-8-14-kotlin-dsl-accessors.tar.zst
Source7: gradle-cache-caches-8-14-kotlin-dsl-scripts.tar.zst
Source8: gradle-cache-caches-8-14-transforms-1.tar.zst
Source9: gradle-cache-caches-8-14-transforms-0-7.tar.zst
Source10: gradle-cache-caches-8-14-transforms-8-f.tar.zst
Source11: gradle-cache-caches-8-14-3-core.tar.zst
Source12: gradle-cache-caches-8-14-3-kotlin-dsl-accessors.tar.zst
Source13: gradle-cache-caches-8-14-3-kotlin-dsl-scripts.tar.zst
Source14: gradle-cache-caches-8-14-3-transforms-0-3.tar.zst
Source15: gradle-cache-caches-8-14-3-transforms-4-7.tar.zst
Source16: gradle-cache-caches-8-14-3-transforms-8-f.tar.zst
Source17: gradle-cache-modules-jetbrains-kotlin-compiler-embeddable.tar.zst
Source18: gradle-cache-modules-jetbrains-kotlin-gradle-plugin.tar.zst
Source19: gradle-cache-modules-jetbrains-kotlin-rest.tar.zst
Source20: gradle-cache-modules-rest-gradle-api-legacy.tar.zst
Source21: gradle-cache-modules-rest-gradle-api-current.tar.zst
Source22: gradle-cache-modules-rest-intellij-platform.tar.zst
Source23: gradle-cache-modules-rest-nodejs.tar.zst
Source24: gradle-cache-modules-rest-large.tar.zst
Source25: gradle-cache-modules-rest-small.tar.zst
Source26: gradle-cache-aarch64-native.tar.zst

Patch0: 0001-ALT-Apply-Kotlin-build-compatibility-fixes.patch
Patch1: 0002-ALT-Add-aarch64-native-build-support.patch

%global kotlin_native_enabled false

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven
BuildRequires: maven-local
BuildRequires: gradle
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
Kotlin compiler distribution built from the upstream bootstrap tag used to
produce the latest Kotlin release line. The package installs the full dist
layout, including compiler launchers, libraries, common klibs and bundled
metadata produced by the build.

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
Maven artifacts for the Kotlin Gradle plugin and its marker modules.

%package maven
Summary: Additional Maven artifacts for the Kotlin bootstrap build
License: Apache-2.0
Group: Development/Java

%description maven
Published Maven artifacts produced by the Kotlin bootstrap build, including
POM files and final JAR payloads not split into dedicated subpackages.

%prep
%setup -n %source_dir
%autopatch -p1

rm -rf %gradle_cache_dir %_builddir/gradle-home-* %build_home
for tarball in \
  %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 \
  %SOURCE7 %SOURCE8 %SOURCE9 %SOURCE10 %SOURCE11 %SOURCE12 \
  %SOURCE13 %SOURCE14 %SOURCE15 %SOURCE16 %SOURCE17 %SOURCE18 \
  %SOURCE19 %SOURCE20 %SOURCE21 %SOURCE22 %SOURCE23 %SOURCE24 \
  %SOURCE25 %SOURCE26
do
  tar --zstd -xf "$tarball" -C %_builddir
done
if [ ! -d %gradle_cache_dir ]; then
  for candidate in %_builddir/gradle-home-*; do
    if [ -d "$candidate" ]; then
      mv "$candidate" %gradle_cache_dir
      break
    fi
  done
fi
if [ ! -d %gradle_cache_dir ]; then
  echo "vendored Gradle cache directory was not restored" >&2
  exit 1
fi
mkdir -p %build_home
mkdir -p %m2_repo
mkdir -p %build_tmp
if [ -d %m2_seed_repo ]; then
  cp -a %m2_seed_repo/. %m2_repo/
fi

%build
export HOME=%build_home
export TMPDIR=%build_tmp
export GRADLE_USER_HOME=%gradle_cache_dir
export GRADLE_OPTS="-Duser.home=%build_home -Dmaven.repo.local=%m2_repo \
  -Djava.io.tmpdir=%build_tmp \
  -Dorg.gradle.java.installations.auto-detect=false \
  -Dorg.gradle.java.installations.auto-download=false"
export MAVEN_OPTS="-Dmaven.repo.local=%m2_repo -Djava.io.tmpdir=%build_tmp"
export npm_config_cache="%gradle_cache_dir/npm-cache"
export JDK_1_8="$(ls -d %_jvmdir/java-1.8.0-openjdk-* | head -n1)"
export JDK_11="$(ls -d %_jvmdir/java-11-openjdk-* | head -n1)"
export JDK_17_0="$(ls -d %_jvmdir/java-17-openjdk-* | head -n1)"
export JDK_21="$(ls -d %_jvmdir/java-21-openjdk-* | head -n1)"
export JDK_25_0="$(ls -d %_jvmdir/java-25-openjdk-* | head -n1)"

export GRADLE_OPTS="$GRADLE_OPTS \
  -Dorg.gradle.java.installations.paths=$JDK_1_8,$JDK_11,$JDK_17_0,$JDK_21,$JDK_25_0"
export JAVA_HOME="$JDK_21"
export PATH="$JAVA_HOME/bin:$PATH"

gradle dist installJps --offline --no-daemon --no-watch-fs \
  --no-configuration-cache --dependency-verification=off \
  -Pkotlin.native.enabled=%kotlin_native_enabled \
  -PdisableBreakpad

%install
rm -rf %buildroot%dist_dir
install -d %buildroot%dist_dir
cp -al dist/. %buildroot%dist_dir/
rm -rf %buildroot%dist_dir/maven
find %buildroot%dist_dir -type f \
  \( -name '*-sources.jar' -o -name '*-javadoc.jar' \) -delete
find %buildroot%dist_dir -type l \
  \( -name '*-sources.jar' -o -name '*-javadoc.jar' \) -delete

symlink_kotlinc_lib() {
  rm -f "%buildroot%dist_kotlinc_lib_dir/$1"
  ln -s "$2" "%buildroot%dist_kotlinc_lib_dir/$1"
}

symlink_common_lib() {
  rm -f "%buildroot%dist_common_dir/$1"
  ln -s "$2" "%buildroot%dist_common_dir/$1"
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
  symlink_kotlinc_lib "$jar" "../../../../share/java/kotlin/$jar"
done

symlink_kotlinc_lib kotlin-compiler.jar \
  "../../../java/kotlin/kotlin-compiler.jar"
symlink_kotlinc_lib allopen-compiler-plugin.jar \
  "../../../../share/java/kotlin/kotlin-allopen-compiler-plugin.jar"
symlink_kotlinc_lib assignment-compiler-plugin.jar \
  "../../../../share/java/kotlin/kotlin-assignment-compiler-plugin.jar"
symlink_kotlinc_lib compose-compiler-plugin.jar \
  "../../../../share/java/kotlin/kotlin-compose-compiler-plugin.jar"
symlink_kotlinc_lib kotlinx-serialization-compiler-plugin.jar \
  "../../../../share/java/kotlin/kotlin-serialization-compiler-plugin.jar"
symlink_kotlinc_lib lombok-compiler-plugin.jar \
  "../../../../share/java/kotlin/kotlin-lombok-compiler-plugin.jar"
symlink_kotlinc_lib noarg-compiler-plugin.jar \
  "../../../../share/java/kotlin/kotlin-noarg-compiler-plugin.jar"
symlink_kotlinc_lib parcelize-runtime.jar \
  "../../../../share/java/kotlin/kotlin-parcelize-runtime.jar"
symlink_kotlinc_lib power-assert-compiler-plugin.jar \
  "../../../../share/java/kotlin/kotlin-power-assert-compiler-plugin.jar"
symlink_kotlinc_lib sam-with-receiver-compiler-plugin.jar \
  "../../../../share/java/kotlin/kotlin-sam-with-receiver-compiler-plugin.jar"
symlink_kotlinc_lib scripting-compiler.jar \
  "../../../../share/java/kotlin/kotlin-scripting-compiler.jar"

symlink_root_lib kotlin-stdlib-jvm-minimal-for-test.jar \
  "../../share/java/kotlin/kotlin-stdlib-jvm-minimal-for-test.jar"

install -d %buildroot%_bindir
for tool in kapt kotlin kotlinc kotlinc-js kotlinc-jvm; do
  ln -sfn ../lib/%name/kotlinc/bin/$tool %buildroot%_bindir/$tool
done

rm -rf .xmvn .xmvn-reactor
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

%mvn_package : maven
rm -rf .javapackages_cache
find %m2_repo -type f -path "*/%kotlin_maven_version/*.pom" \
  | LC_ALL=C sort > pom.list
while read -r pom; do
  dir=$(dirname "$pom")
  version=$(basename "$dir")
  artifact_id=$(basename "$(dirname "$dir")")
  rel_dir=${dir#%m2_repo/}
  group_path=$(dirname "$(dirname "$rel_dir")")
  [ "$group_path" = "." ] && group_path=
  group_id=$(printf '%%s\n' "$group_path" | tr '/' '.')

  %mvn_artifact --skip-dependencies "$pom"

  for artifact in \
    "$dir/$artifact_id-$version".jar \
    "$dir/$artifact_id-$version"-*.jar
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
      sources|javadoc)
        continue
        ;;
    esac
    %mvn_artifact --skip-dependencies \
      "$group_id:$artifact_id:$ext:$classifier:$version" "$artifact"
  done
done < pom.list

%mvn_install

find %buildroot -type f -name '*-sources.jar' -delete
find %buildroot -type l -name '*-sources.jar' -delete
for mfiles in .mfiles-*; do
  [ -f "$mfiles" ] || continue
  awk '!/-sources\.jar$/' "$mfiles" > "$mfiles.filtered"
  mv "$mfiles.filtered" "$mfiles"
done

%files
%doc ReadMe.md
%_bindir/kapt
%_bindir/kotlin
%_bindir/kotlinc
%_bindir/kotlinc-js
%_bindir/kotlinc-jvm
%dist_dir

%files stdlib -f .mfiles-stdlib
%files reflect -f .mfiles-reflect
%files test -f .mfiles-test
%files compiler -f .mfiles-compiler
%files plugins -f .mfiles-plugins
%files gradle-plugin -f .mfiles-gradle-plugin
%files maven -f .mfiles-maven

%changelog
* Mon Jun 22 2026 Ivan Khanas <xeno@altlinux.org> 2.4.20-alt0.5031
- Initial vendored build for bootstraping.

* Wed Jul 15 2020 Michael Shigorin <mike@altlinux.org> 1.3.72-alt1
- initial release
