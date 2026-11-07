%define _unpackaged_files_terminate_build 1

%ifarch aarch64
%define skiko_target linux-arm64
%else
%define skiko_target linux-x64
%endif
%define skia_tag m157-8985a65621

Name: skiko
Version: 0.156.1
Release: alt1

Summary: Kotlin Skia JNI runtime for Linux
License: Apache-2.0 AND BSD-3-Clause AND Adobe DNG SDK License Agreement
Group: Development/Java
URL: https://github.com/JetBrains/skiko
VCS: https://github.com/JetBrains/skiko.git
# These are the genuine upstream Linux JNI targets.
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Patch: system-build.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin
BuildRequires: python3-base
BuildRequires: gcc-c++
BuildRequires: binutils
BuildRequires: pkg-config
BuildRequires: pkgconfig(skia)
BuildRequires: dng-sdk
BuildRequires: pkgconfig(dng-sdk)
BuildRequires: libdbus-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libglvnd-devel
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: kotlinx-coroutines
BuildRequires: mvn(org.jetbrains.runtime:jbr-api)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-benchmark-runtime-jvm)
BuildRequires: mvn(junit:junit)
BuildRequires: xvfb-run
BuildRequires: xorg-xvfb
BuildRequires: mesa-dri-drivers
BuildRequires: fonts-ttf-dejavu

%description
Skiko binds Skia graphics, text shaping and raster rendering to Kotlin.
This package supplies the source-built Linux JNI renderer and the genuine
platform Maven runtime artifact. It uses the system Skia and codecs.

%package awt
Summary: Kotlin Skia JVM and AWT API
Group: Development/Java
BuildArch: noarch

%description awt
The complete upstream JVM and AWT API for Skiko, including its common
Kotlin implementation and the genuine org.jetbrains.skiko:skiko-awt
Maven coordinates.

%package skottie-awt
Summary: Kotlin Skottie JVM API
Group: Development/Java
BuildArch: noarch

%description skottie-awt
The upstream JVM API for the Skottie animation extension of Skiko.

%package skottie-runtime
Summary: Skiko Skottie JNI runtime for Linux
Group: Development/Java

%description skottie-runtime
The source-built Skottie JNI extension and genuine platform Maven runtime
artifact, linked to the matching Skiko core renderer.

%prep
%setup
%autopatch -p1

%build
cd alt-jvm
%gradle_publish \
    -PaltVersion=%version -PaltSkiaVersion=%skia_tag \
    -PaltJobs=%__nprocs '-PaltOptflags=%optflags'

%install
cd alt-jvm
%mvn_package org.jetbrains.skiko:skiko-awt awt
%mvn_package org.jetbrains.skiko:skiko-skottie-awt skottie-awt
%mvn_package org.jetbrains.skiko:skiko-skottie-awt-runtime-%skiko_target \
    skottie-runtime
for artifact in skiko-awt skiko-skottie-awt \
    skiko-awt-runtime-%skiko_target \
    skiko-skottie-awt-runtime-%skiko_target; do
    %gradle_register --artifacts="$artifact-%version."
done
%gradle_install

# Keep the upstream JAR loader resource and the installed private library
# identical. The ELF files also supply normal automatic RPM dependencies.
install -d %buildroot%_libdir/skiko
install -m755 build/native/release/libskiko-%skiko_target.so \
    %buildroot%_libdir/skiko/
install -m755 build/native/release/libskiko-skottie-%skiko_target.so \
    %buildroot%_libdir/skiko/

install -d %buildroot%_docdir/%name-%version/skia/skcms
install -d %buildroot%_docdir/%name-%version/dng-sdk
install -m644 ../LICENSE ../NOTICE %buildroot%_docdir/%name-%version/
skia_docs=%_docdir/skia-$(pkg-config --modversion skia)
install -m644 "$skia_docs/LICENSE" \
    %buildroot%_docdir/%name-%version/skia/
install -m644 "$skia_docs/skcms/LICENSE" \
    %buildroot%_docdir/%name-%version/skia/skcms/
dng_docs=%_docdir/dng-sdk-$(pkg-config --modversion dng-sdk)
install -m644 "$dng_docs/LICENSE.txt" \
    %buildroot%_docdir/%name-%version/dng-sdk/

%check
cd alt-jvm
xvfb-run -a -s '-screen 0 1280x1024x24 -nolisten tcp' \
    %gradle_check \
    -PaltVersion=%version -PaltSkiaVersion=%skia_tag \
    -PaltJobs=%__nprocs '-PaltOptflags=%optflags'

%files -f alt-jvm/.mfiles
%dir %_libdir/skiko
%_libdir/skiko/libskiko-%skiko_target.so
%doc %_docdir/%name-%version

%files awt -f alt-jvm/.mfiles-awt

%files skottie-awt -f alt-jvm/.mfiles-skottie-awt

%files skottie-runtime -f alt-jvm/.mfiles-skottie-runtime
%_libdir/skiko/libskiko-skottie-%skiko_target.so

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.156.1-alt1
- Initial build for ALT.
