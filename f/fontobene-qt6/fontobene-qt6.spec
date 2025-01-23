Name: fontobene-qt6
Version: 1.0.0
Release: alt1
Summary: FontoBene parser for Qt6 (header-only)
License: Apache-2.0 or MIT
Group: Development/C++
Url: https://github.com/fontobene/fontobene-qt

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: pkgconfig(Qt6Core)

%description
A header-only library to parse FontoBene stroke fonts with C++/Qt6.

%package devel
Summary: FontoBene parser for Qt6 (header-only)
Group: Development/C++

%description devel
A header-only library to parse FontoBene stroke fonts with C++/Qt6.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dm0755 fontobene-qt-6.pc.example %buildroot%_pkgconfigdir/%name.pc

%files devel
%doc LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%_includedir/%name
%_pkgconfigdir/%name.pc

%changelog
* Sat Nov 30 2024 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- initial build
