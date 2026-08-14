Name:    libfwevt
Version: 20260702
Release: alt1

Summary: Library for Windows XML Event Log (EVTX) data types
License: LGPL-3.0
Group:   Development/C
Url:     https://github.com/libyal/libfwevt

Source: %name-experimental-%version.tar

BuildRequires: pkgconfig(libcdata)
BuildRequires: pkgconfig(libcerror)
BuildRequires: pkgconfig(libcnotify)
BuildRequires: pkgconfig(libcthreads)
BuildRequires: pkgconfig(libfdatetime)
BuildRequires: pkgconfig(libfguid)
BuildRequires: pkgconfig(libfwnt)
BuildRequires: pkgconfig(libuna)
BuildRequires: python3(setuptools)

%description
%summary.

%package -n python3-module-fwevt
Summary: Python3 bindings for %name
Group:   Development/Python3

%description -n python3-module-fwevt
%summary.

%package devel
Summary: Development files for generic file data functions
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

%check
%make_build check

%files
%_libdir/%name.so.*

%files -n python3-module-fwevt
%python3_sitelibdir/*.so

%files devel
%doc AUTHORS ChangeLog COPYING* NEWS README
%_includedir/%name.h
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_man3dir/%name.3.*

%changelog
* Wed Aug 12 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 20260702-alt1
- Initial build for Sisyphus.
