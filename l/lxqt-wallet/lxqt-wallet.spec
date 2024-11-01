# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 6

Name: lxqt-wallet
Version: 4.0.2
Release: alt1
Summary: Create a kwallet like functionality for LXQt
Group: Graphical desktop/Other

License: BSD
Url: https://github.com/mhogomchungu/lxqt_wallet
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: liblxqt-devel
BuildRequires: kf6-kwallet-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: libgcrypt-devel
BuildRequires: qt6-tools-devel

Requires: liblxqt-wallet%sover = %EVR

%description
This project seeks to give a functionality for secure storage
of information that can be presented in key-values pair like
user names-passwords pairs.

Currently the project can store the information in KDE's kwallet,
GNOME's secret service or in an internal system that use libgcrypt
as its cryptographic backend.

The internal secure storage system allows the functionality to
be provided without dependencies on KDE or GNOME libraries.

This project is designed to be used by other projects simply by
adding the source folder in the build system and start using it.

%package -n liblxqt-wallet%sover
Summary: Create a kwallet like functionality for LXQt
Group: System/Libraries

%description -n liblxqt-wallet%sover
%summary.

%package -n liblxqt-wallet-devel
Summary: Development files for %name
Group: Development/Other
Requires: lib%name%sover = %EVR
Requires: liblxqt-devel

%description -n liblxqt-wallet-devel
%summary.

%prep
%setup
%patch -p1
cp -p backend/README README-backend
cp -p frontend/README README-frontend

%build
%cmake \
 -DQT6=true \
 -DLIB_SUFFIX=default \
 -DNOKDESUPPORT=false \
 -DNOSECRETSUPPORT=false \
 -DBUILD_SHARED=true

%cmake_build

%install
%cmake_install
%find_lang %name --with-qt

%files -f %name.lang
%doc README.md changelog LICENSE
%_bindir/lxqt_wallet-cli

%files -n liblxqt-wallet%sover
%_libdir/liblxqt-wallet.so.%sover.*

%files  -n liblxqt-wallet-devel
%doc README-{backend,frontend}
%_includedir/lxqt/lxqt-wallet.h
%_includedir/lxqt/lxqt_wallet.h
%_libdir/liblxqt-wallet.so
%_pkgconfigdir/lxqt-wallet.pc

%changelog
* Sat Nov 02 2024 Anton Midyukov <antohami@altlinux.org> 4.0.2-alt1
- New version 4.0.2.

* Thu Oct 24 2024 Anton Midyukov <antohami@altlinux.org> 4.0.0-alt1
- initial build
