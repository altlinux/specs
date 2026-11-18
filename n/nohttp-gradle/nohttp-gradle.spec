%define _unpackaged_files_terminate_build 1
%define plugin_marker io.spring.nohttp.gradle.plugin

Name: nohttp-gradle
Version: 0.0.11
Release: alt1

Summary: Gradle plugin detecting non-HTTPS URLs
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spring-io/nohttp
VCS: https://github.com/spring-io/nohttp.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires(pre): rpm-macros-java
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(com.puppycrawl.tools:checkstyle)
BuildRequires: mvn(info.picocli:picocli)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-tooling-core)

%description
Gradle plugin for detecting non-HTTPS URLs.

%package -n nohttp
Summary: Library detecting non-HTTPS URLs
Group: Development/Java

%description -n nohttp
Core library for finding and replacing non-HTTPS URLs in files.

%package -n nohttp-checkstyle
Summary: Checkstyle checks detecting non-HTTPS URLs
Group: Development/Java

%description -n nohttp-checkstyle
Checkstyle integration for detecting non-HTTPS URLs.

%package -n nohttp-cli
Summary: Command-line tool detecting non-HTTPS URLs
Group: Development/Java

%description -n nohttp-cli
Command-line interface for finding and replacing non-HTTPS URLs in files.

%javadoc_package

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%mvn_package io.spring.nohttp:nohttp nohttp
%mvn_package io.spring.nohttp:nohttp-checkstyle nohttp-checkstyle
%mvn_package io.spring.nohttp:nohttp-cli nohttp-cli
%mvn_package io.spring.nohttp:nohttp-gradle
%mvn_package io.spring.nohttp:%plugin_marker
%gradle_register --artifacts=nohttp-
%gradle_register_javadoc --artifacts=nohttp-
marker_dir=$HOME/.m2/repository/io/spring/nohttp
%mvn_artifact $marker_dir/%plugin_marker/%version/%plugin_marker-%version.pom
%gradle_install

%check
%gradle_check -PaltOfflineTests

%files -f .mfiles
%doc LICENSE.txt

%files -n nohttp -f .mfiles-nohttp

%files -n nohttp-checkstyle -f .mfiles-nohttp-checkstyle

%files -n nohttp-cli -f .mfiles-nohttp-cli

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 0.0.11-alt1
- Initial build for ALT.
