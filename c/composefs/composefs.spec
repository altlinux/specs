Name: composefs
Version: 1.0.2
Release: alt1
Summary: Tools to handle creating and mounting composefs images

License: GPL-3.0-or-later AND LGPL-2.0-or-later AND Apache-2.0
URL: https://github.com/containers/composefs
Source: %name-%version.tar

Group: System/Kernel and hardware

BuildRequires: go-md2man libfuse3-devel

%description
Tools to handle creating and mounting composefs images. The composefs
project combines several underlying Linux features to provide a very
flexible mechanism to support read-only mountable filesystem trees,
stacking on top of an underlying "lower" Linux filesystem.

Please see https://github.com/containers/composefs for more information.

%package -n lib%name-devel
Summary: Devel files for %name
Group: Development/C
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
%summary.

%package -n lib%name
Group: System/Libraries
Summary: Libraries files for %name
License: LGPL-2.1-or-later AND (GPL-2.0-only OR Apache-2.0)

%description -n lib%name
%summary.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--enable-man \
	--with-fuse

%make_build DESTDIR=%buildroot

%install
%makeinstall_std

mkdir -p %buildroot/sbin
ln -sf %_sbindir/mount.composefs %buildroot/sbin/mount.composefs
rm -rf %buildroot%_libdir/libcomposefs.la

%files -n lib%name-devel
%_includedir/libcomposefs
%_libdir/libcomposefs.so
%_pkgconfigdir/%name.pc

%files -n lib%name
%_libdir/libcomposefs.so.*

%files
%doc COPYING COPYING.LIB COPYING.LESSERv3 COPYINGv3 LICENSE.Apache-2.0 BSD-2-Clause.txt
%doc README.md
/sbin/mount.composefs
%_bindir/mkcomposefs
%_bindir/composefs-info
%_sbindir/mount.composefs
%_mandir/man*/*

%changelog
* Tue Dec 19 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.0.2-alt1
- Initial build for ALT 

