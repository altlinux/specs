%define _unpackaged_files_terminate_build 1

Name: evas-java
Version: 1.5.0
Release: alt1

Summary: Kotlin event bus and state container
License: MIT
Group: Development/Java
URL: https://github.com/sellmair/evas
VCS: https://github.com/sellmair/evas.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: xgradle
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-plugins
BuildRequires: kotlinx-atomicfu
BuildRequires: kotlinx-coroutines
BuildRequires: mvn(org.jetbrains.compose.runtime:runtime-desktop)

%description
Evas provides coroutine-based events and state containers for Kotlin.

%package compose
Summary: Compose integration for Evas
Group: Development/Java

%description compose
Composable state and event helpers for Evas.

%prep
%setup
%autopatch -p1

%build
%gradle_publish -p alt-jvm -Pevas.version=%version

%install
cd alt-jvm
%mvn_alias io.sellmair:evas-jvm io.sellmair:evas
%mvn_alias io.sellmair:evas-compose-jvm io.sellmair:evas-compose
%mvn_package io.sellmair:evas-compose-jvm compose
%gradle_register --artifacts=evas-jvm-,evas-compose-jvm-
%gradle_install

%files -f alt-jvm/.mfiles
%doc LICENSE

%files compose -f alt-jvm/.mfiles-compose

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 1.5.0-alt1
- Initial build for ALT.
