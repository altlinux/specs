%global _unpackaged_files_terminate_build 1
%define lname libcomposefs

Name: composefs
Version: 1.0.8
Release: alt1
Summary: Tools to handle creating and mounting composefs images

License: (GPL-2.0-or-later OR Apache-2.0) AND (GPL-2.0-only OR Apache-2.0) AND LGPL-2.1-or-later
Group: System/Kernel and hardware
URL: https://github.com/containers/composefs
VCS: https://github.com/containers/composefs.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: go-md2man
BuildRequires: pkgconfig(fuse3) >= 3.10.0
BuildRequires: pkgconfig(libcrypto)

%description
Tools to handle creating and mounting composefs images. The composefs
project combines several underlying Linux features to provide a very
flexible mechanism to support read-only mountable filesystem trees,
stacking on top of an underlying "lower" Linux filesystem.

%package -n lib%name-devel
Summary: Devel files for %name
Group: Development/C

Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Devel files for %name.

%package -n lib%name
Group: System/Libraries
Summary: Libraries files for %name

%description -n lib%name
Library files for %name.

%prep
%setup
%autopatch -p1

%build
%meson -Dfuse=enabled -Dman=enabled
%meson_build

%install
%meson_install
mkdir -p %buildroot/sbin
ln -sf %_sbindir/mount.composefs %buildroot/sbin/mount.composefs
rm -v %buildroot%_libdir/libcomposefs*.a

%files -n %lname-devel
%_includedir/%lname
%_libdir/%lname.so
%_pkgconfigdir/%name.pc

%files -n %lname
%_libdir/%lname.so.*

%files
/sbin/mount.composefs
%_bindir/mkcomposefs
%_bindir/composefs-info
%_sbindir/mount.composefs
%_mandir/man*/*
%doc README.md

%changelog
* Tue Dec 02 2025 Vladimir Romanov <rirusha@altlinux.org> 1.0.8-alt1
- New version: 1.0.8.
- Fix package license.

* Thu May 02 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.0.3-alt1
- 1.0.2 -> 1.0.3 

* Tue Dec 19 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.0.2-alt1
- Initial build for ALT 
