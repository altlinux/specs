Name:    libexe
Version: 20260705
Release: alt1

Summary: Library to access the executable (EXE) format
License: LGPL-3.0
Group:   Development/C
Url:     https://github.com/libyal/libexe

Source: %name-experimental-%version.tar

BuildRequires: pkgconfig(libbfio)
BuildRequires: pkgconfig(libcdata)
BuildRequires: pkgconfig(libcerror)
BuildRequires: pkgconfig(libcfile)
BuildRequires: pkgconfig(libclocale)
BuildRequires: pkgconfig(libcnotify)
BuildRequires: pkgconfig(libcpath)
BuildRequires: pkgconfig(libcsplit)
BuildRequires: pkgconfig(libcthreads)
BuildRequires: pkgconfig(libfcache)
BuildRequires: pkgconfig(libfdata)
BuildRequires: pkgconfig(libfdatetime)
BuildRequires: pkgconfig(libuna)
BuildRequires: python3(setuptools)

%description
%summary.
The goal of this project is to provide functionality to parse EXE
(PE/COFF) and the resources stored in them using libwrc.
This functionality is used in libevt and libevx to parse EventLog messages from
PE/COFF message files.

%package -n python3-module-%name
Summary: Python bindings for libexe, which can read Windows executable files
Group:   Development/Python3

%description -n python3-module-%name
Python bindings for libexe, which can read Windows executable files.

%package tools
Summary: Tool exeinfo to interact with Windows executable files
Group:   File tools

%description tools
Tool exeinfo to interact with Windows executable files.

%package devel
Summary: Development files for access the executable (EXE) format
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

%files devel
%doc AUTHORS ChangeLog COPYING* NEWS README
%_includedir/%name.h
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_man3dir/%name.3.*

%files -n python3-module-%name
%python3_sitelibdir/pyexe*.so

%files tools
%_bindir/exeinfo
%_man1dir/exeinfo.1.*

%changelog
* Wed Aug 12 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 20260705-alt1
- Initial build for Sisyphus.
