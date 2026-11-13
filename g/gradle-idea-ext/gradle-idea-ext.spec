%define _unpackaged_files_terminate_build 1

Name: gradle-idea-ext
Version: 1.4.1
Release: alt1

Summary: IntelliJ IDEA settings DSL extension for Gradle
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/gradle-idea-ext-plugin
VCS: https://github.com/JetBrains/gradle-idea-ext-plugin.git

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-build-statistics
BuildRequires: kotlin-tooling-core
BuildRequires: google-gson
BuildRequires: java-17-openjdk-devel
BuildRequires: spock
BuildRequires: groovy-ant
BuildRequires: groovy-astbuilder
BuildRequires: groovy-json
BuildRequires: groovy-xml
BuildRequires: junit5
BuildRequires: assertj-core

%description
Gradle plugin that extends the IDEA DSL with code style, facets, run
configurations, compiler settings, and other IntelliJ IDEA project metadata.

%prep
%setup -q
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=gradle-idea-ext-
marker=%_mavenrepolocal/repository/org/jetbrains/gradle/plugin/idea-ext
marker=$marker/org.jetbrains.gradle.plugin.idea-ext.gradle.plugin/%version
%mvn_artifact $marker/org.jetbrains.gradle.plugin.idea-ext.gradle.plugin-%version.pom
%mvn_file org.jetbrains.gradle.plugin.idea-ext:gradle-idea-ext \
    %name/%name
%mvn_file \
    org.jetbrains.gradle.plugin.idea-ext:org.jetbrains.gradle.plugin.idea-ext.gradle.plugin \
    %name/org.jetbrains.gradle.plugin.idea-ext.gradle.plugin
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 1.4.1-alt1
- Initial build for ALT.
