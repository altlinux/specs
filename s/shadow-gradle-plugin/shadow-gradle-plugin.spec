%define _unpackaged_files_terminate_build 1
%define build_heap 1500m

%define _mavenrepolocal %_builddir/%name-%version/.m2

Name: shadow-gradle-plugin
Version: 9.6.1
Release: alt1

Summary: Gradle plugin for creating fat/uber JARs
License: Apache-2.0
Group: Development/Java
Url: https://gradleup.com/shadow
VCS: https://github.com/GradleUp/shadow.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: gradle

%description
Shadow creates executable fat JARs by merging dependencies and resources.
It supports shading and relocation to avoid classpath conflicts.

%prep
%setup -q -a1
%autopatch -p1

%build
export HOME=%_builddir/home
export GRADLE_USER_HOME="$PWD/.gradle-vendor"
mkdir -p "$HOME" "%{_mavenrepolocal}/repository"
# The upstream TestKit suite is too expensive for the offline package build.
gradle publishToMavenLocal \
    --offline --no-daemon --max-workers=2 -Ddisable.xgradle=true \
    -Dorg.gradle.jvmargs="-Xmx%build_heap -XX:MaxMetaspaceSize=384m" \
    -Pkotlin.compiler.execution.strategy=in-process \
    -Dorg.gradle.unsafe.isolated-projects=false \
    --no-configuration-cache \
    --gradle-user-home "$GRADLE_USER_HOME" \
    -Dmaven.repo.local="%{_mavenrepolocal}/repository" \
    -x test -x check -x functionalTest -x documentTest

%install
repo="%{_mavenrepolocal}/repository/com/gradleup/shadow"
%mvn_artifact \
    "$repo/shadow-gradle-plugin/%version/shadow-gradle-plugin-%version.pom" \
    "$repo/shadow-gradle-plugin/%version/shadow-gradle-plugin-%version.jar"
%mvn_artifact \
    "$repo/com.gradleup.shadow.gradle.plugin/%version/"\
"com.gradleup.shadow.gradle.plugin-%version.pom"
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 9.6.1-alt1
- New version.
- Bundle plugin runtime libraries from the offline cache.
- Limit build memory on i586.
- Build offline with vendored dependencies and system Gradle.
- Register plugin artifacts and marker POM for system Maven consumers.

* Tue Oct 21 2025 Ivan Khanas <xeno@altlinux.org> 8.3.8-alt3
- Noarch packaging.

* Thu Aug 07 2025 Ivan Khanas <xeno@altlinux.org> 8.3.8-alt2
- Start packing in fat jar.

* Sat Aug 02 2025 Ivan Khanas <xeno@altlinux.org> 8.3.8-alt1
- First build for ALT.
