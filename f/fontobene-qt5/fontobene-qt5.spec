Name: fontobene-qt5
Version: 0.2.0
Release: alt1
Summary: FontoBene parser for Qt5 (header-only)
License: Apache-2.0 or MIT
Group: Development/C++
Url: https://github.com/fontobene/fontobene-qt5

# Source-url: https://github.com/fontobene/fontobene-qt5/archive/%version.tar.gz#/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)

%description
A header-only library to parse FontoBene stroke fonts with C++/Qt5.

%package devel
Summary: FontoBene parser for Qt5 (header-only)
Group: Development/C++

%description devel
A header-only library to parse FontoBene stroke fonts with C++/Qt5.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dm0755 fontobene-qt5.pc.example %buildroot%_pkgconfigdir/%name.pc

%files devel
%doc LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%_includedir/%name
%_pkgconfigdir/%name.pc

%changelog
* Wed Sep 27 2023 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- initial build
