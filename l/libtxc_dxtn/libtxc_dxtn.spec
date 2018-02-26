Name: libtxc_dxtn
Version: 070518
Release: alt2
Summary: A library to enable S3 Texture Compression with DRI drivers
License: BSD
Group: System/Libraries
Url: http://homepage.hispeed.ch/rscheidegger/dri_experimental/s3tc_index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: libGL-devel rpm-macros-make

Source: http://homepage.hispeed.ch/rscheidegger/dri_experimental/libtxc_dxtn070518.tar.gz

%description
A library to enable S3 Texture Compression with DRI drivers.

%prep
%setup

%build
%make_build_ext

%install
%makeinstall_std

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir
%endif

%files
%doc Changelog
%_libdir/*.so

%changelog
* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 070518-alt2
- Rebuilt for debuginfo

* Mon Sep 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 070518-alt1
- Initial build for Sisyphus

