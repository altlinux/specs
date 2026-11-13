%define _unpackaged_files_terminate_build 1

Name: compose-multiplatform-core
Version: 1.12.2
Release: alt1

Summary: Compose Multiplatform desktop runtime and UI libraries
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/compose-multiplatform-core
VCS: https://github.com/JetBrains/compose-multiplatform-core.git

Source0: %name-%version.tar
Patch0: %name-desktop.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: kotlin-compiler
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:compose-compiler-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-serialization)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: kotlinx-coroutines
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-core-jvm)
BuildRequires: kotlinx-atomicfu
BuildRequires: mvn(org.jetbrains.skiko:skiko-awt)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-test-jvm)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.jetbrains.runtime:jbr-api)
BuildRequires: mvn(io.reactivex.rxjava3:rxjava)

%description
Compose Multiplatform runtime, state retention and desktop UI implementations
built from the complete upstream source tree.

%package annotation
Summary: AndroidX annotations from the Compose source tree
Group: Development/Java

%description annotation
AndroidX annotation JVM implementation built from the shared source release.

%package collection
Summary: AndroidX collections from the Compose source tree
Group: Development/Java

%description collection
AndroidX collection JVM implementation built from the shared source release.

%package lifecycle
Summary: Lifecycle and Compose lifecycle integration
Group: Development/Java

%description lifecycle
Lifecycle common, runtime, viewmodel and Compose integration libraries.

%package savedstate
Summary: Saved state and Compose saved state integration
Group: Development/Java

%description savedstate
Saved state serialization and Compose integration libraries.

%package navigationevent
Summary: Navigation events and Compose navigation integration
Group: Development/Java

%description navigationevent
Navigation event dispatch and Compose integration libraries.

%package foundation
Summary: Compose Foundation, layout and animation libraries
Group: Development/Java

%description foundation
Desktop Foundation, layout, animation and animation core implementations.

%package material
Summary: Compose Material components and ripple libraries
Group: Development/Java

%description material
Desktop Material components and ripple implementations.

%package tooling
Summary: Compose UI preview and animation tooling
Group: Development/Java

%description tooling
Compose UI previews, composition inspection and animation tooling APIs.

%package runtime-rxjava3
Summary: Compose Runtime integration with RxJava 3
Group: Development/Java

%description runtime-rxjava3
Compose Runtime state adapters for RxJava 3 observable types.

%package desktop
Summary: Compose Desktop application library
Group: Development/Java

%description desktop
Compose Desktop application integration and shared desktop library.

%prep
%setup
%autopatch -p1

%build
%gradle_publish -p alt-jvm writePublicationsList --no-configuration-cache

%install
artifacts=$(paste -sd, alt-jvm/build/publications.list)
%gradle_register --artifacts="$artifacts"
%mvn_package androidx.annotation:* annotation
%mvn_package androidx.collection:* collection
%mvn_package org.jetbrains.androidx.lifecycle:* lifecycle
%mvn_package org.jetbrains.androidx.savedstate:* savedstate
%mvn_package androidx.navigationevent:* navigationevent
%mvn_package org.jetbrains.androidx.navigationevent:* navigationevent
%mvn_package org.jetbrains.compose.foundation:* foundation
%mvn_package org.jetbrains.compose.animation:* foundation
%mvn_package org.jetbrains.compose.material:* material
%mvn_package androidx.compose.animation:animation-tooling-internal tooling
%mvn_package org.jetbrains.compose.ui:ui-tooling* tooling
%mvn_package androidx.compose.runtime:runtime-rxjava3* runtime-rxjava3
%mvn_package org.jetbrains.compose.desktop:* desktop
%gradle_install

%check
%__gradle %_xgradleflags -p alt-jvm --no-configuration-cache \
    :collection:jvmTest :runtime:desktopTest \
    :runtime:legacyJvmOriginalTest :runtime-retain:desktopTest \
    :ui-util:desktopTest :ui-geometry:desktopTest :ui-unit:desktopTest \
    :kruth:jvmTest :material:desktopTest

%files -f .mfiles
%doc LICENSE.txt

%files annotation -f .mfiles-annotation

%files collection -f .mfiles-collection

%files lifecycle -f .mfiles-lifecycle

%files savedstate -f .mfiles-savedstate

%files navigationevent -f .mfiles-navigationevent

%files foundation -f .mfiles-foundation

%files material -f .mfiles-material

%files tooling -f .mfiles-tooling

%files runtime-rxjava3 -f .mfiles-runtime-rxjava3

%files desktop -f .mfiles-desktop

%changelog
* Fri Nov 06 2026 Ivan Khanas <xeno@altlinux.org> 1.12.2-alt1
- Initial build for ALT.
