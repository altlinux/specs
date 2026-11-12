%define _unpackaged_files_terminate_build 1
%define nativever 1.5.7-26
%ifarch %ix86
%define with_ffm false
%else
%define with_ffm true
%endif

Name: zstd-jni
Version: 1.5.7.26
Release: alt1

Summary: Java JNI and FFM bindings for Zstandard
License: BSD-2-Clause and BSD-3-Clause
Group: Development/Java
URL: https://github.com/luben/zstd-jni
VCS: https://github.com/luben/zstd-jni.git

Source: %name-%version.tar
Patch0: build-desktop-with-system-zstd.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
# FFM needs Java 22; upstream permits the full JNI API on an older JDK.
%ifarch %ix86
BuildRequires: java-21-openjdk-devel
%else
BuildRequires: java-25-openjdk-devel
%endif
BuildRequires: cmake
BuildRequires: rpm-build-ninja
BuildRequires: gcc
BuildRequires: pkgconfig(libzstd)
BuildRequires: mvn(org.jetbrains:annotations)

%description
JNI and Foreign Function and Memory API bindings for Zstandard compression.
The base Java API targets Java 8. Builds with a Java 22+ compiler also include
the Multi-Release FFM implementation. All builds use the system Zstandard library.

%package -n libzstd-jni
Summary: Java Zstandard bindings with the matching native library
Group: Development/Java

%description -n libzstd-jni
Java compression APIs and their matching native JNI/FFM bridge, linked to
the system Zstandard library. Includes streams, buffers and dictionaries.
The FFM implementation is included in builds made with a Java 22+ compiler.

%prep
%setup
%autopatch -p1
mkdir native-notices
cp -p src/main/native/LICENSE native-notices/

%build
%cmake -GNinja -Wno-dev
%ninja_build -C %_cmake__builddir
cd alt-jvm
%gradle_publish -PwithFfm=%with_ffm

%install
install -Dpm755 %_cmake__builddir/libzstd-jni-%nativever.so \
    %buildroot%_libdir/libzstd-jni-%nativever.so
cd alt-jvm
%gradle_register
%gradle_install

%files -n libzstd-jni -f alt-jvm/.mfiles
%doc LICENSE native-notices
%_libdir/libzstd-jni-%nativever.so

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 1.5.7.26-alt1
- New version.

* Fri Dec 20 2024 Andrey Cherepanov <cas@altlinux.org> 1.5.6-alt1.4
- New version for kafka-3.8.1.

* Fri Dec 20 2024 Andrey Cherepanov <cas@altlinux.org> 1.5.6-alt1.3
- Initial build for Sisyphus.
