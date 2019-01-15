Name: fuse3
Version: 3.4.1
Release: alt1

Summary: a tool for creating virtual filesystems
License: GPL
Group: System/Kernel and hardware

Url: https://github.com/libfuse/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires(pre): fuse-common

BuildRequires: meson ninja-build libudev-devel

%description
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort
as well as for using them.

%package -n lib%name
Group: System/Kernel and hardware
Summary: tool for creating virtual filesystems
Requires: %name = %version-%release

%description -n lib%name
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort.

This package contains shared libraries.

%package -n lib%name-devel
Group: System/Kernel and hardware
Summary: tool for creating virtual filesystems
Requires: lib%name = %version-%release

%description -n lib%name-devel
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort.

This package contains development headers.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/lib%name.so.* %buildroot/%_lib/
ln -sf ../../%_lib/lib%name.so.%version %buildroot%_libdir/lib%name.so

rm -fr %buildroot%_sysconfdir/init.d

%files
%doc AUTHORS README.md doc/README.NFS doc/kernel.txt doc/html
/usr/sbin/mount.fuse3
%attr(4710,root,fuse) %_bindir/fusermount3
%_man1dir/*
%_man8dir/*

%files -n lib%name
/%_lib/lib%name.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Jan 14 2019 Evgeny Sinelnikov <sin@altlinux.org> 3.4.1-alt1
- update to latest release

* Tue Jul 25 2017 Denis Smirnov <mithraen@altlinux.ru> 3.1.0-alt1
- first build for Sisyphus (ALT#33529)
