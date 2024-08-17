Name: libtoml11
Version: 4.2.0
Release: alt1

Summary: TOML for Modern C++
License: MIT
Group: Development/C++

Url: https://github.com/ToruNiina/toml11
# Source-url: https://github.com/ToruNiina/toml11/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
toml11 is a C++11 (or later) header-only toml parser/encoder depending only on
C++ standard library.
  * It is compatible to the latest version of TOML v1.0.0.
  * It is one of the most TOML standard compliant libraries, tested with the
    language agnostic test suite for TOML parsers by BurntSushi.
  * It shows highly informative error messages. You can see the error messages
    about invalid files at CircleCI.
  * It has configurable container. You can use any random-access containers
    and key-value maps as backend containers.
  * It optionally preserves comments without any overhead.
  * It has configurable serializer that supports comments, inline tables,
    literal strings and multiline strings.
  * It supports user-defined type conversion from/into toml values.
  * It correctly handles UTF-8 sequences, with or without BOM, both on posix
    and Windows.}

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
%summary

%prep
%setup

%build
%cmake \
    -G Ninja \
%nil
%cmake_build

%install
%cmake_install

%files devel
%doc LICENSE
%doc README.md
%_includedir/*.hpp
%_includedir/toml11/
%_cmakedir/toml11/

%changelog
* Sat Aug 17 2024 Boris Yumankulov <boria138@altlinux.org> 4.2.0-alt1
- initial build for ALT Sisyphus
