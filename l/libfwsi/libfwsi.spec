Name:    libfwsi
Version: 20260522
Release: alt1

Summary: Library to access the Windows Shell Item format
License: LGPL-3.0
Group:   Development/C
Url:     https://github.com/libyal/libfwsi

Source: %name-experimental-%version.tar

BuildRequires: pkgconfig(libcdata)
BuildRequires: pkgconfig(libcerror)
BuildRequires: pkgconfig(libclocale)
BuildRequires: pkgconfig(libcnotify)
BuildRequires: pkgconfig(libcthreads)
BuildRequires: pkgconfig(libfdatetime)
BuildRequires: pkgconfig(libfguid)
BuildRequires: pkgconfig(libfole)
BuildRequires: pkgconfig(libfwps)
BuildRequires: pkgconfig(libuna)
BuildRequires: python3(setuptools)

%description
%summary
The Windows Shell uses Shell Items to represents items within the Windows Shell,
such as files or control panel items. Shell items can be identified by a list of
identifiers, also refererred to as IDList or PIDL (pointer to an item identifier
list). Such an item identifier list is comparable to a file system path with
"Desktop" as the root item.
The format of item identifiers are internal to the Shell Items, it is
undocumented and varies between Windows versions.

%package -n python3-module-%name
Summary: Python bindings for libfwsi, which can access Windows Shell Item format
Group:   Development/Python3

%description -n python3-module-%name
Python bindings for libfwsi, which can access Windows Shell Item format.

%package devel
Summary: Development files for access Windows Shell Item format
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
%python3_sitelibdir/pyfwsi.so

%changelog
* Fri Aug 14 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 20260522-alt1
- Initial build for Sisyphus.
