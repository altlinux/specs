Name: libtxc_dxtn
Epoch: 1
Version: 1.0.1
Release: alt1
Summary: A library to enable S3 Texture Compression with DRI drivers
License: BSD
Group: System/Libraries
Url: http://people.freedesktop.org/~cbrill/libtxc_dxtn/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: libGL-devel rpm-macros-make

Source: http://people.freedesktop.org/~cbrill/libtxc_dxtn/libtxc_dxtn-1.0.1.tar.gz

%description
A library to enable S3 Texture Compression with DRI drivers.

%package devel
Summary: Header of S3TC with DRI drivers
Group: Development/C
Requires: %name = %EVR
BuildArch: noarch

%description devel
A library to enable S3 Texture Compression with DRI drivers.

This package contains header of S3TC with DRI drivers.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
#doc Changelog
%_libdir/*.so

%files devel
%_includedir/*

%changelog
* Mon Jul 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.0.1-alt1
- Version 1.0.1 (ALT #29208)

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 070518-alt2
- Rebuilt for debuginfo

* Mon Sep 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 070518-alt1
- Initial build for Sisyphus

