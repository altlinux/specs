Name:    libfwps
Version: 20260705
Release: alt1

Summary: Library for Windows Property Store data types
License: LGPL-3.0
Group:   Development/C
Url:     https://github.com/libyal/libfwps

Source: %name-alpha-%version.tar

BuildRequires: pkgconfig(libcdata)
BuildRequires: pkgconfig(libcerror)
BuildRequires: pkgconfig(libclocale)
BuildRequires: pkgconfig(libcnotify)
BuildRequires: pkgconfig(libcthreads)
BuildRequires: pkgconfig(libfdatetime)
BuildRequires: pkgconfig(libfguid)
BuildRequires: pkgconfig(libuna)
BuildRequires: python3(setuptools)

%description
%summary.
The Property store format is used by various Windows file formats like the
Windows Shortcut File (LNK) and in the Windows Shell Items. This specification
is based on earlier work on the format and was complimented by
reverse engineering.

%package -n python3-module-%name
Summary: Python bindings for property store data types library
Group:   Development/Python3

%description -n python3-module-%name
Python bindings for libfwps Property store format

%package devel
Summary: Development files for Property store format library
Group: Development/C
Requires: %name = %version

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%prep
%setup

%build
%configure \
    --disable-static \
    --enable-python
%make_build

%install
%makeinstall_std
find %buildroot%python3_sitelibdir -name "*.la" -print -delete

%files
%_libdir/%name.so.*

%files devel
%doc AUTHORS ChangeLog COPYING* NEWS README
%_includedir/%name.h
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_man3dir/%name.3.*

%files -n python3-module-%name
%python3_sitelibdir/pyfwps.so

%changelog
* Fri Aug 14 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 20260705-alt1
- Initial build for Sisyphus.
