Name:    libcdirectory
Version: 20260703
Release: alt1

Summary: Library for cross-platform C directory functions
License: LGPL-3.0
Group:   Development/C
Url:     https://github.com/libyal/libcdirectory

Source: %name-experimental-%version.tar

BuildRequires: pkgconfig(libcerror)
BuildRequires: pkgconfig(libclocale)
BuildRequires: pkgconfig(libuna)

%description
%summary.

%package devel
Summary: Development files for cross-platform C directory functions
Group: Development/C
Requires: %name = %version

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%prep
%setup

%build
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%_libdir/%name.so.*

%files devel
%doc AUTHORS ChangeLog COPYING* NEWS README
%_includedir/%name.h
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_man3dir/%name.3.*

%changelog
* Wed Aug 12 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 20260703-alt1
- Initial build for Sisyphus.
