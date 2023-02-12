%define _unpackaged_files_terminate_build 1
%define common_name ayatana-indicator-common

%define lname   %{name}0
%define soname  %name
%define sover   0
%define typelib %name-gir
Name: libayatana-common
Version: 0.9.8
Release: alt1

Summary: Common files and libraries used by Ayatana System Indicators
License: GPLv3
Group: System/Libraries
Url: https://github.com/AyatanaIndicators/libayatana-common
Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-systemd rpm-build-vala

BuildRequires: ayatana-cmake-modules cmake gcc-c++ intltool vala vala-tools
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libblkid-devel
BuildRequires: libgio-devel
BuildRequires: libffi-devel
BuildRequires: libmount-devel
BuildRequires: libpcre2-devel
BuildRequires: libpcre-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: libtool
BuildRequires: pkg-config
BuildRequires: zlib-devel

Requires: gobject-introspection

%description
This package contains common files used by Ayatana system
indicators.

%package -n %common_name
Summary: Common files used by Ayatana System Indicators
BuildArch: noarch
Group: System/Libraries

%description -n %common_name
This package contains common files used by Ayatana system
indicators.

%package -n %lname
Summary: Shared library providing common API functions used by Ayatana System Indicators
Group: System/Libraries

%description -n %lname
Shared library providing common API functions used by Ayatana
system indicators.

This package contains shared libraries.

%package -n %typelib
Summary: Ayatana Indicator Common typelib
Group: Development/Other
Requires: %common_name = %version

%description -n %typelib
Shared library providing common API functions used by Ayatana
system indicators.

This package provides the GObject Introspection bindings.

%package devel
Summary: Development files for Ayatana Indicator Common
Group: Development/C++
Requires: %lname = %version
Requires: %typelib = %version
Requires: gobject-introspection-devel

%description devel
Shared library providing common API functions used by Ayatana
system indicators.

This package contains the development files.

%prep
%setup

%build
%cmake \
  -Denable_tests=Off
%cmake_build

%install
%cmake_install

# Create empty directory for owning within this package.
install -d -m 755 %buildroot%_datadir/ayatana/indicators

%post -n %common_name
%systemd_user_post ayatana-indicators.target

%preun -n %common_name
%systemd_user_preun ayatana-indicators.target

%postun -n %common_name
%systemd_user_postun ayatana-indicators.target

%files -n %common_name
%doc COPYING NEWS README.md
%dir %_datadir/ayatana
%dir %_datadir/ayatana/indicators
%dir %_datadir/glib-2.0
%dir %_datadir/glib-2.0/schemas
%_datadir/glib-2.0/schemas/org.ayatana.common.gschema.xml
%_userunitdir/ayatana-indicators.target
%_datadir/locale/*/LC_MESSAGES/*.mo

%files -n %lname
%doc COPYING
%_libdir/%soname.so*

%files -n %typelib
%_libdir/girepository-1.0/AyatanaCommon-0.0.typelib

%files devel
%doc COPYING AUTHORS ChangeLog
%dir %_includedir/ayatana
%_includedir/ayatana/common
%_pkgconfigdir/%soname.pc
%_datadir/gir-1.0/AyatanaCommon-0.0.gir
%_vapidir/AyatanaCommon.vapi

%changelog
* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 0.9.8-alt1
- Initial build for Sisyphus
