%define pyname fwnt

Name:    libfwnt
Version: 20260521
Release: alt1

Summary: Library for Windows NT data types 
License: LGPL-3.0
Group:   Development/C
Url:     https://github.com/libyal/libfwnt

Source: %name-alpha-%version.tar

BuildRequires: pkgconfig(libcdata)
BuildRequires: pkgconfig(libcerror)
BuildRequires: pkgconfig(libcnotify)
BuildRequires: pkgconfig(libcthreads)
BuildRequires: python3(setuptools)

%description
A library for Windows NT data types.

%package -n python3-module-%pyname
Summary: Windows NT data types for Python3
Group:   Development/Python3

%description -n python3-module-%pyname 
Subpackage contains python3 module for Windows NT data types

%package devel
Summary: Development files for Windows NT data types
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
    --enable-python \
    --disable-libtool-lock \
    --enable-year2038 \
    --libdir=%_libdir \
    --prefix=%_prefix
%make_build

%install
%makeinstall_std
find %buildroot%python3_sitelibdir -type f -name "*.la" -delete -print

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

%files -n python3-module-%pyname 
%python3_sitelibdir/*.so

%changelog
* Wed Aug 12 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 20260521-alt1
- Initial build for Sisyphus.
