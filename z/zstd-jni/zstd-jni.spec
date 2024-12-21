%define rev 4

Name:    zstd-jni
Version: 1.5.6
Release: alt1.%rev

Summary: JNI binding for Zstd
License: BSD-2-Clause
Group:   Development/Java
Url:     https://github.com/luben/zstd-jni

Source: %name-%version.tar
Source1: sbt-launch.tar
Patch0: zstd-jni-link-to-pthread.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-java
BuildRequires(pre): rpm-build-ninja
BuildRequires: libzstd-devel
BuildRequires: /proc java-openjdk-devel

%description
JNI bindings for Zstd native library that provides fast and high compression
lossless algorithm for Android, Java and all JVM languages:
- static compress/decompress methods
- implementation of InputStream and OutputStream for transparent compression
  of data streams fully compatible with the "zstd" program.
- minimal performance overhead

%package -n lib%name
Summary: Library for %name
Group: Development/Java

%description -n lib%name
JNI bindings for Zstd native library that provides fast and high compression
lossless algorithm for Android, Java and all JVM languages:
- static compress/decompress methods
- implementation of InputStream and OutputStream for transparent compression
  of data streams fully compatible with the "zstd" program.
- minimal performance overhead

%prep
%setup
%patch0 -p1
tar xf %SOURCE1 -C ~

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
install -Dpm0664 "%_cmake__builddir"/libzstd-jni-%{version}-%rev.so %buildroot%_libdir/libzstd-jni-%{version}-%rev.so

%files -n lib%name
%doc *.md
%_libdir/libzstd-jni-*.so

%changelog
* Fri Dec 20 2024 Andrey Cherepanov <cas@altlinux.org> 1.5.6-alt1.4
- New version for kafka-3.8.1.

* Fri Dec 20 2024 Andrey Cherepanov <cas@altlinux.org> 1.5.6-alt1.3
- Initial build for Sisyphus.
