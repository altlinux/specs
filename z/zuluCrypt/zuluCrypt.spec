%define _unpackaged_files_terminate_build 1

Name: zuluCrypt
Version: 7.0.0
Release: alt1

Summary: Qt GUI front-end to cryptsetup
License: GPL-2.0-or-later
Group: File tools
URL: https://mhogomchungu.github.io/zuluCrypt/
VCS: https://github.com/mhogomchungu/zuluCrypt

Source: %name-%version.tar
Patch: %name-%version-alt-cmake-libdir-fix.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libdevmapper-devel
BuildRequires: libgcrypt-devel
BuildRequires: libuuid-devel
BuildRequires: glibc-devel
BuildRequires: libblkid-devel
BuildRequires: libsecret-devel
BuildRequires: libpwquality-devel
BuildRequires: qt5-base-devel
BuildRequires: libcryptsetup-devel
BuildRequires: libossp-uuid-devel
BuildRequires: libpcre2-devel
BuildRequires: libselinux-devel
BuildRequires: libffi-devel
BuildRequires: libjson-c-devel
BuildRequires: zlib-devel
BuildRequires: libargon2-devel
BuildRequires: libmount-devel

%description
zuluCrypt is a front end to cryptsetup. It makes it easier to use cryptsetup by
providing a Qt-based GUI and a simpler to use CLI front end to cryptsetup. It
does the same thing truecrypt does but without licensing problems or requiring a
user to setup sudo for it or presenting root's password. This package contains
the applications.

%package devel
Summary: Development library package
Group: Development/C
Requires: lib%name = %EVR

%description devel
This package contains development files and libraries necessary to build
programs around zulucrypt.

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
This package contains libraries that provide higher level access to cryptsetup
API and provide mounting/unmounting API to easy opening and closing of volumes.

%prep
%setup
%autopatch -p1

%build
%cmake \
 -DREUSEMOUNTPOINT=false \
 -DUDEVSUPPORT=true \
 -DNOGUI=false \
 -DQT5=true \
 -DHOMEMOUNTPREFIX=false \
 -DNOGNOME=false \
 -DNOKDE=false \
 -DUSE_POLKIT=true
%cmake_build

%install
%cmake_install

#remove unneeded icons
rm -fv %buildroot%_iconsdir/*.png

%files
%doc LICENSE README.* changelog
%_bindir/zuluMount-gui
%_bindir/zuluMount-cli
%_bindir/zuluCrypt-gui
%_bindir/zuluCrypt-cli
%_bindir/zuluSafe-cli
%_bindir/zuluPolkit
%dir %_libdir/zuluCrypt
%dir %_datadir/zuluCrypt
%_libdir/zuluCrypt/*
%_datadir/applications/zulu*.desktop
%_iconsdir/hicolor/48x48/apps/*.png
%_datadir/zuluCrypt/*
%_datadir/pixmaps/*.png
%dir %_docdir/zuluCrypt
%dir %_datadir/polkit-1
%dir %_datadir/polkit-1/actions
%_datadir/polkit-1/actions/org.zulucrypt.zulupolkit.policy
%_docdir/zuluCrypt/*.pdf
%_datadir/mime/packages/zuluCrypt.xml
%_man1dir/zulu*.1.*

%files -n lib%name
%_libdir/libzuluCrypt.so.*
%_libdir/libzuluCrypt-exe.so.*
%_libdir/libzuluCryptPluginManager.so.*

%files devel
%dir %_includedir/zuluCrypt
%_includedir/zuluCrypt/libzuluCrypt.h
%_includedir/zuluCrypt/libzuluCrypt-exe.h
%_includedir/zuluCrypt/libzuluCryptPluginManager.h
%_libdir/libzuluCryptPluginManager.so
%_libdir/libzuluCrypt.so
%_libdir/libzuluCrypt-exe.so
%_libdir/pkgconfig/libzuluCrypt.pc

%changelog
* Mon Nov 11 2024 Anton Kurachenko <srebrov@altlinux.org> 7.0.0-alt1
- Initial build for Sisyphus.
