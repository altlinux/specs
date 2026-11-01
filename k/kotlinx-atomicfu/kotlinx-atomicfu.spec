%define _unpackaged_files_terminate_build 1

Name: kotlinx-atomicfu
Version: 0.33.0
Release: alt1

Summary: Atomic operations for Kotlin JVM and Gradle transformation plugin
License: Apache-2.0
Group: Development/Java
Url: https://github.com/Kotlin/kotlinx-atomicfu
VCS: https://github.com/Kotlin/kotlinx-atomicfu.git
BuildArch: noarch

Source: %name-%version.tar
Patch: offline-jvm.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-compiler
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-maven
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.slf4j:slf4j-api)

%description
Kotlin atomic operations JVM library, JVM bytecode transformer and the
org.jetbrains.kotlinx.atomicfu Gradle plugin.

%prep
%setup
%patch -p1

%build
%gradle_publish -p alt-jvm --no-daemon --max-workers=4 \
    -Pkotlin.compiler.execution.strategy=in-process

%install
%mvn_alias org.jetbrains.kotlinx:atomicfu-jvm org.jetbrains.kotlinx:atomicfu
%gradle_register --artifacts=atomicfu-jvm-,atomicfu-transformer-
install -d %buildroot%_javadir/%name %buildroot%_mavenpomdir/%name
plugins=atomicfu-gradle-plugin-
plugins="$plugins,org.jetbrains.kotlinx.atomicfu.gradle.plugin-"
%gradle_install_plugin --artifacts="$plugins"
%gradle_install

%files -f .mfiles
%doc LICENSE.txt README.md
%_javadir/%name/atomicfu-gradle-plugin.jar
%_mavenpomdir/%name/atomicfu-gradle-plugin.pom
%_mavenpomdir/%name/org.jetbrains.kotlinx.atomicfu.gradle.plugin.pom

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 0.33.0-alt1
- Initial build for ALT.
