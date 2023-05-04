%define sover 7
%def_with gtk2

Name: libayatana-indicator
Version: 0.9.1
Release: alt2

Summary: Ayatana Indicator Display Objects
License: GPLv3
Group: System/Libraries

Url: https://github.com/AyatanaIndicators/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/AyatanaIndicators/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: libayatana-ido3-devel

%if_with gtk2
BuildRequires: libgtk+2-devel
%endif

%description
This library contains information to build indicators to go into
the indicator applet.

%package -n %name%sover
Summary: Ayatana Indicator Display Objects
Group: System/Libraries

%description -n %name%sover
This library contains information to build indicators to go into
the indicator applet.

%package devel
Summary: Development files for the Ayatana panel indicator applet library
Group: Development/C++

%description devel
This library contains information to build indicators to go into
the indicator applet.

%package -n %{name}3-%sover
Summary: Ayatana Indicator Display Objects
Group: System/Libraries

%description -n %{name}3-%sover
This library contains information to build indicators to go into
the indicator applet.

%package -n %{name}3-devel
Summary: Development files for the Ayatana panel indicator applet library
Group: Development/C++

%description -n %{name}3-devel
This library contains information to build indicators to go into
the indicator applet.

%prep
%setup -a 0
%__mv %name-%version %name-%version-gtk3

%build
%if_with gtk2
# Build with GTK2
%cmake -DFLAVOUR_GTK2:BOOL=TRUE
%cmake_build
%endif

# Build with GTK3
pushd %name-%version-gtk3
%cmake -DCMAKE_INSTALL_LIBEXECDIR:PATH=%_libexecdir
%cmake_build
popd

%install
%if_with gtk2
%cmake_install
%endif

pushd %name-%version-gtk3
%cmake_install
popd

%if_with gtk2
%files -n %name%sover
%_libdir/%name.so.*

%files devel
%_includedir/%name-0.4
%_libdir/%name.so
%_pkgconfigdir/ayatana-indicator-0.4.pc
%endif

%files -n %{name}3-%sover
%_libdir/%{name}3.so.*

%files -n %{name}3-devel
%_includedir/%{name}3-0.4
%_libdir/%{name}3.so
%_pkgconfigdir/ayatana-indicator3-0.4.pc
%_libexecdir/%name
%_datadir/%name

%changelog
* Thu Mar 16 2023 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt2
- NMU: cleanup BR, add if_with for build with gtk2

* Mon Mar 07 2022 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt1
- Version 0.9.1

* Sun Feb 13 2022 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt2
- Rename subpackages
- Fix BR
- Build also with GTK2

* Fri Jan 14 2022 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt1
- Initial build for ALT Linux
