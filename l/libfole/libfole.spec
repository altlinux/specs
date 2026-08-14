Name:    libfole
Version: 20260521
Release: alt1

Summary: Library for Object Linking and Embedding (OLE) data types
License: LGPL-3.0
Group:   Development/C
Url:     https://github.com/libyal/libfole

Source: %name-alpha-%version.tar

BuildRequires: pkgconfig(libcerror)

%description
%summary.

%package devel
Summary: Header files and libraries for developing applications for libfole
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
* Fri Aug 14 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 20260521-alt1
- Initial build for Sisyphus.
