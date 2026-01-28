%define        _unpackaged_files_terminate_build 1
%define        _stripped_files_terminate_build 1

Name:          platform
Version:       6.1.0
Release:       alt1
Summary:       C++ library for detecting compiler and platform properties
License:       BSD-3-Clause
Group:         Development/C++
Url:           https://github.com/steinwurf/platform
Vcs:           https://github.com/steinwurf/platform.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++

%description
platform is a C++ library for detecting compiler and platform properties.
Currently, it can detect the following properties:

* Compiler: g++, clang, and MSVC
* Operating system: Linux, Mac OSX, Windows, iOS, Android, Emscripten, and
  FreeBSD
* Target architecture: x86, x86_64, ARM, MIPS, and asm.js

%package       devel
Summary:       C++ library for detecting compiler and platform properties
Group:         Development/C++

Requires:      cmake
Requires:      gcc-c++

%description   devel
platform is a C++ library for detecting compiler and platform properties.
Currently, it can detect the following properties:

* Compiler: g++, clang, and MSVC
* Operating system: Linux, Mac OSX, Windows, iOS, Android, Emscripten, and
  FreeBSD
* Target architecture: x86, x86_64, ARM, MIPS, and asm.js


%prep
%setup

%build
%cmake -DMAKE_BUILD_TYPE:STRING=RelWithDebInfo
%cmake_build

%install
%cmakeinstall_std

%files         devel
%doc README.rst
%_includedir/%name/config.hpp
%_cmakedir/%{name}

%changelog
* Tue Jan 27 2026 Pavel Skrylev <majioa@altlinux.org> 6.1.0-alt1
- initial build for Sisyphus
