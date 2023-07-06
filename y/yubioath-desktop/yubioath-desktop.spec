%define _unpackaged_files_terminate_build 1

Name: yubioath-desktop
Version: 5.1.0
Release: alt4

Summary: Yubico Authenticator for Desktop
License: BSD-2-Clause
Group: System/Configuration/Hardware
Url: https://github.com/Yubico/yubioath-desktop

Source: %name-%version.tar
Patch0: 0001-Fix-build-on-GCC13.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: python3-dev
BuildRequires: desktop-file-utils

Requires: qt5-quickcontrols
Requires: qt5-quickcontrols2
Requires: qt5-graphicaleffects
Requires: pyotherside
Requires: python3(ykman)
Requires: python3(yubikit)
Requires: python3(smartcard)
Requires: python3(fido2)

%description
Cross-platform application for generating Open Authentication (OATH)
time-based TOTP and event-based HOTP one-time password codes, with
the help of a YubiKey that protects the shared secrets.

%prep
%setup
%patch0 -p1

%build
# fix python version in shebangs
for pyscript in $(grep -lRE '/usr/bin/env' *); do
	sed -i $pyscript -e 's/python/python3/'
done

%qmake_qt5 CONFIG+=nostrip

# fix qmake-spec's wrong path
sed -i Makefile -e '/(INSTALL_ROOT)\/usr\/lib/ s/lib/bin/'
%make_build

install -pD -m0644 COPYING %_builddir/COPYING
install -pD -m0644 NEWS %_builddir/NEWS
install -pD -m0644 README %_builddir/README

%install
%makeinstall_std INSTALL_ROOT=%buildroot

# remove headers of QZXing library (need to package this library separately)
rm -r %buildroot%_includedir/QZXing*

# install desktop file
desktop-file-install --dir %buildroot%_desktopdir resources/com.yubico.yubioath.desktop

# install icons
install -pD -m0644 resources/icons/com.yubico.yubioath.png %buildroot%_iconsdir/hicolor/128x128/apps/com.yubico.yubioath.png
install -pD -m0644 resources/icons/com.yubico.yubioath.svg %buildroot%_iconsdir/hicolor/scalable/apps/com.yubico.yubioath.svg

%files
%doc README COPYING NEWS
%_desktopdir/*
%_bindir/%name
%_iconsdir/hicolor/*/apps/*

%changelog
* Thu Jul  6 2023 Artyom Bystrov <arbars@altlinux.org> 5.1.0-alt4
- Fix build on GCC13

* Fri Sep 16 2022 Anton Zhukharev <ancieg@altlinux.org> 5.1.0-alt3
- add qt5-quickcontrols dependency

* Sat Sep 10 2022 Anton Zhukharev <ancieg@altlinux.org> 5.1.0-alt2
- fix requires

* Wed Jul 27 2022 Anton Zhukharev <ancieg@altlinux.org> 5.1.0-alt1
- initial build for Sisyphus

