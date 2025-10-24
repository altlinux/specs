%define _unpackaged_files_terminate_build 1
%def_with check

Name: xgradle
Version: 0.1.0
Release: alt1

Summary: Gradle plugin for system dependency resolution and offline builds
License: Apache-2.0
Group: Development/Java
Url: https://github.com/IvanKhanas/xgradle
Vcs: https://github.com/IvanKhanas/xgradle.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name-stage1.tar
Source2: %name-stage2.tar
Source3: %name-tags.tar
Source4: commit.sh

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: gradle
BuildRequires: rpm-build-java-osgi
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-lib
BuildRequires: plexus-utils
BuildRequires: shadow-gradle-plugin
BuildRequires: slf4j log4j-over-slf4j
BuildRequires: google-guice
BuildRequires: guava
BuildRequires: beust-jcommander
BuildRequires: atinject
BuildRequires: objectweb-asm
BuildRequires: aopalliance
BuildRequires: junit5
BuildRequires: apiguardian
Requires: xgradle-core
Requires: xgradle-tool
Requires: rpm-macros-gradle

%if_with check
BuildRequires: apache-commons-io
BuildRequires: apache-commons-cli
BuildRequires: google-gson
%endif

%package core
Summary: Artifacts for the plugin to function
Group: Development/Java
Requires: gradle

%package tool
Summary: Cli utility for easy packaging
Group: Development/Java
Requires: maven-local

%package -n rpm-macros-gradle
Summary: Macros for working with Gradle
Group: Development/Java
Requires: rpm-macros-java

%package javadoc
Summary: API documentation for XGradle
Group: Development/Java

%description
XGradle is a custom Gradle plugin that provides enhanced dependency resolution
capabilities using system-installed artifacts rather than remote repositories.
It handles both regular dependencies and Gradle plugins, supports BOM (Bill of
Materials) packages, and enables fully offline builds by leveraging locally
available JAR files and POM metadata. The plugin automatically resolves version
conflicts, manages transitive dependencies, and provides detailed logging
throughout the resolution process.

%description core
XGradle plugin for system dependency resolution. Enables Gradle to use
system-installed artifacts instead of remote repositories.  Contains the main
plugin JAR, initialization scripts, and POM metadata.

%description tool
CLI utility for XGradle artifact management. Handles artifact registration, BOM
processing, and plugin installation. Supports XMvn compatibility and duplicate
prevention.

%description -n rpm-macros-gradle
RPM macros for Gradle packaging. Provides build helpers and macros for
packaging Gradle projects in ALT Linux and other RPM-based distributions.

%description javadoc
API documentation for XGradle system. Javadoc references for core plugin and
CLI tool APIs. Essential for developers extending XGradle functionality.

%prep
%setup -a1 -a2 -a3

XGRADLE_BUILD_DIR="$PWD/xgradle-stage1/build/libs"

sed -i "s|gradle.gradleHomeDir.getAbsolutePath() + \"/lib/plugins\"|\"$XGRADLE_BUILD_DIR\"|g" \
  xgradle-stage1/src/main/resources/xgradle-plugin.gradle

XGRADLE_BUILD_DIR="$PWD/xgradle-stage2/build/dist"

sed -i "s|gradle.gradleHomeDir.getAbsolutePath() + \"/xgradle\"|\"$XGRADLE_BUILD_DIR\"|g" \
  xgradle-stage2/xgradle-core/main/resources/xgradle-plugin.gradle

cp %SOURCE4 .
chmod +x commit.sh

%build

pushd xgradle-stage1
gradle build -x check
popd

pushd xgradle-stage2
gradle copyPublicationsToDist \
  --init-script ../xgradle-stage1/src/main/resources/xgradle-plugin.gradle \
  -Djava.library.dir=%_javadir \
  -Dmaven.poms.dir=%_mavenpomdir \
  -Ddisable.ansi.color=true
  #
popd

gradle copyPublicationsToDist \
  --init-script xgradle-stage2/xgradle-core/main/resources/xgradle-plugin.gradle \
  -Djava.library.dir=%_javadir \
  -Dmaven.poms.dir=%_mavenpomdir \
  -Ddisable.ansi.color=true \
  -DgitCommitId=$(./commit.sh) \
  -Prelease \
  -x check \
  #

%install
install -Dm 644 xgradle-core/build/dist/xgradle-core.jar \
  -t %buildroot%_datadir/gradle/xgradle

install -Dm 644 xgradle-core/build/dist/xgradle-plugin.gradle \
 -t %buildroot%_datadir/gradle/init.d

install -Dm 644 xgradle-core/build/dist/xgradle-core.pom \
  -t %buildroot%_mavenpomdir/xgradle

install -Dm 644 xgradle-core/build/dist/xgradle-core-javadoc.jar \
  -t %buildroot%_javadocdir/xgradle

install -Dm 644 xgradle-tool/build/dist/xgradle-tool.jar \
  -t %buildroot%_javadir/xgradle

ln -s %_datadir/gradle/xgradle/xgradle-core.jar \
  -t %buildroot/%_javadir/xgradle

install -Dm 644 xgradle-tool/build/dist/xgradle-tool.pom \
  -t %buildroot%_mavenpomdir/xgradle

install -Dm 755 xgradle-tool/build/dist/xgradle-tool \
  -t %buildroot%_javadir/xgradle

install -d %buildroot%_bindir

ln -s %_javadir/xgradle/xgradle-tool \
  -t %buildroot%_bindir

install -Dm 644 xgradle-tool/build/dist/xgradle-tool-javadoc.jar \
  -t %buildroot%_javadocdir/xgradle

install -Dm 644 rpm-macros/xgradle-fjava \
  -t %buildroot/%_rpmmacrosdir

%check
gradle check \
  --init-script xgradle-stage2/xgradle-core/main/resources/xgradle-plugin.gradle \
  -Djava.library.dir=%_javadir \
  -Dmaven.poms.dir=%_mavenpomdir \
  -Ddisable.ansi.color=true \
  #

%files

%files core
%_javadir/xgradle/xgradle-core.jar
%_datadir/gradle/xgradle/xgradle-core.jar
%_datadir/gradle/init.d/xgradle-plugin.gradle
%_mavenpomdir/xgradle/xgradle-core.pom

%files tool
%_bindir/xgradle-tool
%_javadir/xgradle/xgradle-tool
%_javadir/xgradle/xgradle-tool.jar
%_mavenpomdir/xgradle/xgradle-tool.pom

%files javadoc
%doc LICENSE README.md
%_javadocdir/xgradle/xgradle-core-javadoc.jar
%_javadocdir/xgradle/xgradle-tool-javadoc.jar

%files -n rpm-macros-gradle
%_rpmmacrosdir/xgradle-fjava

%changelog
* Thu Oct 23 2025 Ivan Khanas <xeno@altlinux.org> 0.1.0-alt1
- First build for ALT.
