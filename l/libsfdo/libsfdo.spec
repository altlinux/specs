%define sover 0

Name: libsfdo
Version: 0.1.3
Release: alt1
Summary: A collection of libraries implementing freedesktop.org specifications
Group: System/Libraries

License: BSD-2-Clause
Url: https://gitlab.freedesktop.org/vyivel/libsfdo
# Source-url:   %url/-/archive/v%version/%name-v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
%summary.

%package -n %name%sover
Summary: A collection of libraries implementing freedesktop.org specifications
Group: System/Libraries

%description -n %name%sover
%summary.

%package devel
Summary: Development libraries and header files for %name
Group: Development/C
Requires: %name%sover = %EVR

%description devel
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n %name%sover
%doc README.md LICENSE
%_libdir/libsfdo-*.so.%sover

%files devel
%_includedir/sfdo-*.h
%_libdir/libsfdo-*.so
%_pkgconfigdir/libsfdo-*.pc

%changelog
* Tue Nov 12 2024 Anton Midyukov <antohami@altlinux.org> 0.1.3-alt1
- initial build
