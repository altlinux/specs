%define _unpackaged_files_terminate_build 1
%def_with check

Name: xgradle
Version: 0.2.0
Release: alt1

Summary: Gradle plugin for system dependency resolution and offline builds
License: Apache-2.0
Group: Development/Java
Url: https://github.com/IvanKhanas/xgradle
Vcs: https://github.com/IvanKhanas/xgradle.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name-tags.tar
Source2: commit.sh
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: gradle
BuildRequires: rpm-build-java-osgi
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
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
BuildRequires: google-gson
BuildRequires: mockito mockito-junit-jupiter
Requires: xgradle-resolution-plugin
Requires: xgradle-cli
Requires: rpm-macros-gradle

%if_with check
BuildRequires: apache-commons-io
BuildRequires: apache-commons-cli
%endif

%package resolution-plugin
Summary: Artifacts for the plugin to function
Group: Development/Java
Requires: gradle
Provides: xgradle-core = %EVR
Obsoletes: xgradle-core < %EVR

%package cli
Summary: Cli utility for easy packaging
Group: Development/Java
Requires: maven-local
Provides: xgradle-tool = %EVR
Obsoletes: xgradle-tool < %EVR

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

%description resolution-plugin
XGradle plugin for system dependency resolution. Enables Gradle to use
system-installed artifacts instead of remote repositories.  Contains the main
plugin JAR, initialization scripts, and POM metadata.

%description cli
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
%setup -a1
%autopatch -p1

cp %SOURCE2 .
chmod +x commit.sh

%build
%gradle_publish -DgitCommitId=$(./commit.sh) \
  -Prelease \
  #

%install
install -Dm 644 xgradle-resolution-plugin/build/dist/xgradle-resolution-plugin.jar \
  -t %buildroot%_datadir/gradle/xgradle

install -Dm 644 xgradle-resolution-plugin/build/dist/xgradle-resolution-plugin.gradle \
 -t %buildroot%_datadir/gradle/init.d

install -Dm 644 xgradle-resolution-plugin/build/dist/xgradle-resolution-plugin.pom \
  -t %buildroot%_mavenpomdir/xgradle

install -Dm 644 xgradle-resolution-plugin/build/dist/xgradle-resolution-plugin-javadoc.jar \
  -t %buildroot%_javadocdir/xgradle

install -d %buildroot%_javadir/xgradle

ln -s %_datadir/gradle/xgradle/xgradle-resolution-plugin.jar \
  -t %buildroot/%_javadir/xgradle

install -Dm 644 xgradle-cli/build/dist/xgradle-cli.jar \
  -t %buildroot%_javadir/xgradle

install -Dm 644 xgradle-cli/build/dist/xgradle-cli.pom \
  -t %buildroot%_mavenpomdir/xgradle

install -Dm 755 xgradle-cli/build/dist/xgradle-cli \
  -t %buildroot%_javadir/xgradle

install -d %buildroot%_bindir

ln -s %_javadir/xgradle/xgradle-cli \
  -t %buildroot%_bindir

install -Dm 644 xgradle-cli/build/dist/xgradle-cli-javadoc.jar \
  -t %buildroot%_javadocdir/xgradle

install -Dm 644 rpm-macros/xgradle-fjava \
  -t %buildroot/%_rpmmacrosdir

%check
%gradle_check

%files

%files resolution-plugin
%_javadir/xgradle/xgradle-resolution-plugin.jar
%_datadir/gradle/xgradle/xgradle-resolution-plugin.jar
%_datadir/gradle/init.d/xgradle-resolution-plugin.gradle
%_mavenpomdir/xgradle/xgradle-resolution-plugin.pom

%files cli
%_bindir/xgradle-cli
%_javadir/xgradle/xgradle-cli
%_javadir/xgradle/xgradle-cli.jar
%_mavenpomdir/xgradle/xgradle-cli.pom

%files javadoc
%doc LICENSE README.md
%_javadocdir/xgradle/xgradle-resolution-plugin-javadoc.jar
%_javadocdir/xgradle/xgradle-cli-javadoc.jar

%files -n rpm-macros-gradle
%_rpmmacrosdir/xgradle-fjava

%changelog
* Tue Mar 17 2026 Ivan Khanas <xeno@altlinux.org> 0.2.0-alt1
- New version.
- Sbom generation support.
- Rename subpackages.

* Thu Oct 23 2025 Ivan Khanas <xeno@altlinux.org> 0.1.0-alt1
- First build for ALT.
