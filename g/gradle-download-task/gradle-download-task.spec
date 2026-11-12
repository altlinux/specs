%define _unpackaged_files_terminate_build 1

%def_with check

%define plugin_marker de.undercouch.download.gradle.plugin

Name: gradle-download-task
Version: 5.7.0
Release: alt1

Summary: Download and verification tasks for Gradle
License: Apache-2.0
Group: Development/Java
URL: https://github.com/michel-kraemer/gradle-download-task
VCS: https://github.com/michel-kraemer/gradle-download-task.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: xgradle
BuildRequires: mvn(org.apache.httpcomponents.client5:httpclient5)
BuildRequires: mvn(org.slf4j:slf4j-nop)
%if_with check
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
%endif

%description
A Gradle plugin providing download and checksum verification tasks with
progress reporting, authentication, conditional requests and caching.

%prep
%setup
%autopatch -p1

%build
%gradle_publish -PwithoutHttpTestFixtures

%install
artifact_root=%_mavenrepolocal/repository/de/undercouch
%gradle_register --artifacts=%name-
%mvn_artifact \
    "$artifact_root/download/%plugin_marker/%version/%plugin_marker-%version.pom"
%gradle_install

%check
%if_with check
# WireMock/littleproxy are unavailable; run the independent checksum tests.
%gradle_check -PwithoutHttpTestFixtures
%endif

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 5.7.0-alt1
- Initial build for ALT.
