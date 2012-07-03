%define libname nxcl
Name: libnxcl
Version: 0.9
Release: alt2.1

Epoch: 1

Summary: Freenx application/thin-client client library
Group: Networking/Remote access
License: GPLv2
URL: http://freenx.berlios.de

Packager: Boris Savelev <boris@altlinux.org>

Source0: http://download.berlios.de/freenx/%name.tar.bz2
Patch0: %name-gcc43.patch
Patch10: dodnx.patch
Patch11: gcc-warnings.patch
Patch14: doxygen.patch
Patch15: restorekeyboard.patch
Patch16: publicKey.patch
Patch17: deletelogfiles.patch
Patch18: ssh_dnserror.patch

Requires: nx

# Automatically added by buildreq on Fri Jun 13 2008
BuildRequires: doxygen gcc-c++

%description
A library for building NX clients.
Based on nxclientlib by George Wright, but with all dependencies on Qt
removed and the Qt build system replaced with GNU autotools.

%package devel
Group: Development/Other
Summary: libnxcl header
Requires: %name = %version-%release

%description devel
This package provides the support files which can be used to
build applications using the libnxcl

%package devel-static
Group: Development/Other
Summary: libnxcl static library
Requires: %name-devel = %version-%release

%description devel-static
This package provides static libnxcl library

%prep
%setup -n %name
%patch0 -p0

%patch10 -p1
%patch11 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall_std docdir=%_docdir/%name-%version

%files
%doc README doc/html*
%_bindir/*
%_libdir/*.so.*

%files devel
%_includedir/%libname/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-static
%_libdir/*.a

%changelog
* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.9-alt2.1
- Rebuilt for soname set-versions

* Sun Sep 27 2009 Boris Savelev <boris@altlinux.org> 1:0.9-alt2
- add patches from nx-mobile (Fabian Franz)

* Sat Feb 28 2009 Boris Savelev <boris@altlinux.org> 1:0.9-alt1
- fix version (add Epoch)
- fix work with nx > 3.2.0 (define NXCL_USE_NXSSH)
- remove pre/post
- add hard requires to devel

* Sun Oct 26 2008 Boris Savelev <boris@altlinux.org> 1.0-alt3
- fix build with gcc43

* Thu Jul 03 2008 Boris Savelev <boris@altlinux.org> 1.0-alt2
- clean spec
- svn build

* Fri Jun 13 2008 Boris Savelev <boris@altlinux.org> 1.0-alt1
- initial build
