%define _unpackaged_files_terminate_build 1
%define plugin_marker org.gradle.test-retry.gradle.plugin

# Spock and samples-check providers are unavailable in Sisyphus.
%def_without check

Name: gradle-test-retry
Version: 1.6.6
Release: alt1

Summary: Gradle plugin to retry failed tests
License: Apache-2.0
Group: Development/Java
URL: https://github.com/gradle/test-retry-gradle-plugin
VCS: https://github.com/gradle/test-retry-gradle-plugin.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-system.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: shadow-gradle-plugin
BuildRequires: jetbrains-annotations
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(org.ow2.asm:asm)
%if_with check
BuildRequires: mvn(org.spockframework:spock-bom:pom:)
BuildRequires: mvn(org.spockframework:spock-core)
BuildRequires: mvn(org.spockframework:spock-junit4)
BuildRequires: mvn(net.sourceforge.nekohtml:nekohtml)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.gradle.exemplar:samples-check)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.puppycrawl.tools:checkstyle)
BuildRequires: mvn(org.codenarc:CodeNarc)
%endif

%description
The Gradle test-retry plugin reruns failed tests to mitigate test flakiness.
It provides the Gradle plugin, implementation artifact and plugin marker.

%prep
%setup
%autopatch -p1

%build
%gradle_publish --info

%install
%gradle_register --artifacts=test-retry-gradle-plugin-
marker_dir=$HOME/.m2/repository/org/gradle/test-retry
%mvn_artifact $marker_dir/%plugin_marker/%version/%plugin_marker-%version.pom
%gradle_install

%check
%if_with check
%gradle_check --info
%endif

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 1.6.6-alt1
- Initial build for ALT.
