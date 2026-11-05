%define _unpackaged_files_terminate_build 1

Name: osdetector-gradle-plugin
Version: 1.7.3
Release: alt1

Summary: Gradle plugin detecting the operating system and architecture
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/osdetector-gradle-plugin
VCS: https://github.com/google/osdetector-gradle-plugin.git

BuildArch: noarch

Source: %name-%version.tar
Patch: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires(pre): rpm-macros-java
BuildRequires: xgradle
BuildRequires: rpm-build-java
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(kr.motd.maven:os-maven-plugin)
BuildRequires: mvn(junit:junit)

%description
Gradle plugin that detects the operating system and architecture and provides
a uniform classifier for native artifacts. Includes the com.google.osdetector
plugin marker.

%prep
%setup
%patch -p1

%build
%gradle_publish --no-daemon --max-workers=4

%install
%gradle_register --artifacts=osdetector-gradle-plugin-
marker=%_mavenrepolocal/repository/com/google/osdetector
marker=$marker/com.google.osdetector.gradle.plugin/%version
%mvn_artifact $marker/com.google.osdetector.gradle.plugin-%version.pom
%mvn_file com.google.gradle:osdetector-gradle-plugin \
    %name/osdetector-gradle-plugin
%mvn_file com.google.osdetector:com.google.osdetector.gradle.plugin \
    %name/com.google.osdetector.gradle.plugin
%gradle_install

%check
%gradle_check --no-daemon --max-workers=4


%files -f .mfiles
%doc LICENSE

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 1.7.3-alt1
- Initial build for ALT.
