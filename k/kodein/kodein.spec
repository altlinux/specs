%define _unpackaged_files_terminate_build 1

Name: kodein
Version: 7.33.0
Release: alt1

Summary: Dependency injection library for Kotlin
License: MIT
Group: Development/Java
URL: https://github.com/kosi-libs/Kodein
VCS: https://github.com/kosi-libs/Kodein.git

Source0: %name-%version.tar
Patch0: %name-%version.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: kotlinx-atomicfu
BuildRequires: mvn(org.kodein.type:kaverit-jvm)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(io.ktor:ktor-server-core-jvm)
BuildRequires: mvn(io.ktor:ktor-server-sessions-jvm)
BuildRequires: mvn(io.ktor:ktor-server-test-host-jvm)
BuildRequires: mvn(io.ktor:ktor-server-default-headers-jvm)
BuildRequires: mvn(org.jetbrains.compose.runtime:runtime-desktop)
BuildRequires: mvn(org.jetbrains.androidx.lifecycle:lifecycle-viewmodel-compose-desktop)

BuildArch: noarch

%description
Kodein DI is a dependency injection and retrieval library for Kotlin/JVM.

%package conf
Summary: Configurable Kodein containers
Group: Development/Java

%description conf
Configurable Kodein dependency injection containers for Kotlin/JVM.

%package jxinject-jvm
Summary: JSR-330 injection support for Kodein
Group: Development/Java

%description jxinject-jvm
Support for dependency injection with javax.inject annotations.

%package compose-runtime
Summary: Kodein support for Compose runtime
Group: Development/Java

%description compose-runtime
Composable helpers for accessing a Kodein container.

%package compose
Summary: Kodein support for Compose ViewModels
Group: Development/Java

%description compose
ViewModel integration for Kodein and JetBrains Compose.

%package ktor-server
Summary: Kodein integration for Ktor servers
Group: Development/Java

%description ktor-server
Kodein integration for Ktor servers.

%package ktor-controller
Summary: Kodein routing and controller support for Ktor
Group: Development/Java

%description ktor-controller
Kodein routing and controller support for Ktor.

%prep
%setup -q
%patch0 -p1

%mvn_package :kodein-di %name
%mvn_package :kodein-di-jvm %name
%mvn_package :kodein-di-conf conf
%mvn_package :kodein-di-conf-jvm conf
%mvn_package :kodein-di-jxinject-jvm jxinject-jvm
%mvn_package :kodein-di-framework-compose-runtime compose-runtime
%mvn_package :kodein-di-framework-compose-runtime-jvm compose-runtime
%mvn_package :kodein-di-framework-compose compose
%mvn_package :kodein-di-framework-compose-jvm compose
%mvn_package :kodein-di-framework-ktor-server-jvm ktor-server
%mvn_package :kodein-di-framework-ktor-server-controller-jvm ktor-controller

if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i \
        -e '/^org\.gradle\.jvmargs/s/-Xmx6g/-Xmx1024m/' \
        -e 's/MaxMetaspaceSize=4g/MaxMetaspaceSize=512m/' \
        gradle.properties
fi

%build
%gradle_publish

%install
artifacts=kodein-di,kodein-di-jvm,kodein-di-conf,kodein-di-conf-jvm
artifacts=$artifacts,kodein-di-jxinject-jvm
artifacts=$artifacts,kodein-di-framework-compose-runtime
artifacts=$artifacts,kodein-di-framework-compose-runtime-jvm
artifacts=$artifacts,kodein-di-framework-compose,kodein-di-framework-compose-jvm
artifacts=$artifacts,kodein-di-framework-ktor-server-jvm
artifacts=$artifacts,kodein-di-framework-ktor-server-controller-jvm
%gradle_register --artifacts="$artifacts"
%gradle_install

%check
%gradle_check

%files -f .mfiles-%name
%doc LICENSE.txt

%files conf -f .mfiles-conf

%files jxinject-jvm -f .mfiles-jxinject-jvm

%files compose-runtime -f .mfiles-compose-runtime

%files compose -f .mfiles-compose

%files ktor-server -f .mfiles-ktor-server

%files ktor-controller -f .mfiles-ktor-controller

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 7.33.0-alt1
- Initial build for ALT.
