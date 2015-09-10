%define ver_major 12.10
%define api_ver 0.1

Name: ido
Version: %ver_major.2
Release: alt1

Summary: Indicator Display Objects Library
License: GPLv3/LGPLv3
Group: System/Libraries
Url: https://launchpad.net/%name

Source: https://launchpad.net/%name/%ver_major/%version/+download/%name-%version.tar.gz

BuildRequires: libgtk+3-devel >= 3.4.0 gtk-doc

%description
Library providing extra gtk menu items for display in system indicators.

%package -n lib%{name}3
Summary: Indicator Display Objects Library
Group: System/Libraries

%description -n lib%{name}3
Library providing extra gtk3 menu items for display in system indicators.

%package -n lib%{name}3-devel
Summary: Indicator Display Objects Library - development files
Group: Development/C
Requires: lib%{name}3 = %version-%release

%description -n lib%{name}3-devel
Library providing extra gtk3 menu items for display in system indicators.
This package contains files that are needed to develop applications.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
#%make check

%files -n lib%{name}3
%_libdir/lib%{name}3-%api_ver.so.*

%files -n lib%{name}3-devel
%_includedir/lib%{name}3-%api_ver/
%_libdir/lib%{name}3-%api_ver.so
%_pkgconfigdir/lib%{name}3-%api_ver.pc

%changelog
* Tue Sep 08 2015 Yuri N. Sedunov <aris@altlinux.org> 12.10.2-alt1
- first build for Sisyphus

