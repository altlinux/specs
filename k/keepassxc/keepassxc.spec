Name: keepassxc
Version:  2.2.2
Release:  alt1
Summary: KeePassXC Password Safe - light-weight cross-platform password manager
Group: File tools
License: GPLv2+
URL: http://www.keepassxc.org/

#Source: https://github.com/keepassxreboot/keepassxc/releases/download/%version/%name-%version-src.tar.xz
Source: %name-%version.tar

%def_without yubikey

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ctest gcc-c++
BuildRequires: qt5-base-devel >= 5.2.0 qt5-tools-devel >= 5.2.0
BuildRequires: libgcrypt-devel >= 1.6.0
BuildRequires: zlib-devel >= 1.2.0
# Optional for Auto-Type on X11/Linux:
BuildRequires: libXi-devel, libXtst-devel, qt5-x11extras-devel
# Optional for YubiKey support
%if_with yubikey
BuildRequires: libyubikey-devel, ykpers-devel
%endif

%description
KeePassXC is a community fork of KeePassX, a native cross-platform port of
KeePass Password Safe, with the goal to extend and improve it with new features
and bugfixes to provide a feature-rich, fully cross-platform and modern
open-source password manager.

%prep
%setup -n %name-%version

%build
%cmake \
  -DWITH_CXX11=ON \
  -DWITH_XC_HTTP=ON \
  -DWITH_XC_AUTOTYPE=ON \
%if_with yubikey
  -DWITH_XC_YUBIKEY=ON
%endif

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%files
%_bindir/*
%_libdir/%name
%_desktopdir/org.%name.desktop
%_datadir/metainfo/org.keepassxc.appdata.xml
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/*/*/*
%_datadir/%name

%changelog
* Mon Oct 23 2017 Pavel Vyazovoy <paulelms@altlinux.org> 2.2.2-alt1
- Updated to v2.2.2.

* Sun Oct 15 2017 Pavel Vyazovoy <paulelms@altlinux.org> 2.2.1-alt1
- Initial build v2.2.1.
