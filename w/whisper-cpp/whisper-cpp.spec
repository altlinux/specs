%define soversion 1

Name: whisper-cpp
Version: 1.7.6
Release: alt1

Summary: Port of OpenAI's Whisper model in C/C++
Group: Sound
License: MIT
Url: https://github.com/ggerganov/whisper.cpp

Source: %name-%version.tar
Patch0: whisper-cpp-1.7.5-alt-cmake-fix-destination-pkgconfig.patch
Patch1: whisper-cpp-1.7.5-alt-cmake-fix-soname.patch

Requires: lib%name%soversion = %EVR

BuildRequires: cmake gcc-c++ git libstdc++-devel-static

%package -n lib%name%soversion
Summary: Shared libraries for whisper-cpp.
Group: System/Libraries

%package -n lib%name-devel
Summary: Development files for lib%name%soversion.
Group: Development/C++
Requires: lib%name%soversion = %EVR

%description
High-performance inference of OpenAI's Whisper automatic speech
recognition (ASR) model.

%description -n lib%name%soversion
Contains shared libraries for OpenAI's Whisper automatic speech
recognition (ASR) model.

%description -n lib%name-devel
Contains development files for lib%name%soversion.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*

%files -n lib%name%soversion
%_libdir/libwhisper.so.%{soversion}*
%_libdir/libggml.so.%{soversion}*
%_libdir/libggml-cpu.so.%{soversion}*
%_libdir/libggml-base.so.%{soversion}*

%files -n lib%name-devel
%_libdir/libwhisper.so
%_libdir/libggml.so
%_libdir/libggml-cpu.so
%_libdir/libggml-base.so
%_libdir/cmake/*
%_includedir/*
%_libdir/pkgconfig/whisper.pc

%changelog
* Tue Sep 23 2025 Evgeniy Gorbanyov <esgor@altlinux.org> 1.7.6-alt1
- New version 1.7.6.

* Tue Jun  3 2025 Evgeniy Gorbanyov <esgor@altlinux.org> 1.7.5-alt1
- Initial build for Sisyphus.
