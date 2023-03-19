Name: libtomlplusplus
Version: 3.3.0
Release: alt1

Summary: Header-only TOML config file parser and serializer for C++17

License: MIT
Group: Development/C++
Url: https://marzer.github.io/tomlplusplus/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/marzer/tomlplusplus/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
Header-only TOML config file parser and serializer for C++17.

%package devel
Summary: Header-only TOML config file parser and serializer for C++17
Group: Development/C++

%description devel
Header-only TOML config file parser and serializer for C++17.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
rm -v %buildroot%_includedir/meson.build

%files devel
%doc LICENSE README.md
%_includedir/toml++/
%_libdir/cmake/tomlplusplus
%_datadir/tomlplusplus

%changelog
* Sat Mar 18 2023 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- initial build for ALT Sisyphus
