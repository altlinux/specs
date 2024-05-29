Name: libtomlplusplus
Version: 3.4.0
Release: alt3

Summary: Header-only TOML config file parser and serializer for C++17

License: MIT
Group: Development/C++
Url: https://marzer.github.io/tomlplusplus/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/marzer/tomlplusplus/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
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
%ifarch %e2k
sed -E -i '/for \(auto\&.*tbl\)/{N;s/(for \((auto\&*) \[[^,]*, ([^,]*))(\].*)/\11\4\2\3=\31;/}' \
	include/toml++/impl/{*_formatter,parser}.inl
%endif

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_libdir/%name.so.3*

%files devel
%_includedir/toml++/
%_libdir/cmake/tomlplusplus
%_libdir/%name.so

%_pkgconfigdir/tomlplusplus.pc

%changelog
* Wed May 29 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.4.0-alt3
- fix e2k build

* Wed Jan 24 2024 Roman Alifanov <ximper@altlinux.org> 3.4.0-alt2
- NMU: switch to meson for the pkconfig file (and in general for more correct build)

* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 3.4.0-alt1
- new version 3.4.0 (with rpmrb script)

* Sat Mar 18 2023 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- initial build for ALT Sisyphus
