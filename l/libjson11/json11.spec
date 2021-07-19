%define oname json11
Name: libjson11
Version: 1.0.0
Release: alt1

Summary: A tiny JSON library for C++11

License: MIT
Group: Development/C++
Url: https://github.com/dropbox/%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %url/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake

%description
Json11 is a tiny JSON library for C++11, providing JSON parsing
and serialization.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/C++

%description devel
%summary.

%prep
%setup
%__subst 's@lib/@%_lib/@g' CMakeLists.txt
%__subst 's@lib/@%_lib/@g' json11.pc.in
echo "set_property(TARGET json11 PROPERTY SOVERSION 0)" >> CMakeLists.txt

%build
%cmake -G Ninja \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DJSON11_BUILD_TESTS=ON
%cmake_build

%check
# TODO
#%%ctest

%install
%cmake_install

%files
%doc README.md
%doc LICENSE.txt
%_libdir/%name.so.0

%files devel
%_libdir/%name.so
%_includedir/json11.hpp
%_pkgconfigdir/%oname.pc

%changelog
* Sun Jul 18 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Initial SPEC release.
