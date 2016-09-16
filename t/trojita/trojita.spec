#
# spec file for package trojita
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: trojita
Version: 0.7
Release: alt1

# Almost everything: dual-licensed under the GPLv2 or GPLv3
# (with KDE e.V. provision for relicensing)
# src/XtConnect: BSD
# src/Imap/Parser/3rdparty/kcodecs.*: LGPLv2
# Nokia imports: LGPLv2.1 or GPLv3
# src/Imap/Parser/3rdparty/rfccodecs.cpp: LGPLv2+
# src/qwwsmtpclient/: GPLv2
Summary: Qt IMAP e-mail client
License: (GPLv2 or GPLv3) and BSD and LGPLv2 and (LGPLv2.1 or GPLv3) and LGPLv2+ and GPLv2
Group: Networking/Mail

Url: http://trojita.flaska.net/
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: http://sourceforge.net/projects/trojita/files/src/%name-%version.tar.bz2

BuildRequires: libstdc++-devel gcc-c++
BuildRequires: pkgconfig(Qt5Gui) >= 5.6
BuildRequires: pkgconfig(Qt5WebKit) >= 5.6
BuildRequires: pkgconfig(Qt5Svg) >= 5.6
BuildRequires: pkgconfig(Qt5UiTools) >= 5.6
#BuildRequires: libqt4-devel
#BuildRequires: xorg-xvfb xkeyboard-config
BuildRequires: cmake >= 2.8.7
BuildRequires: libqtkeychain-qt5-devel
BuildRequires: kde5-gpgmepp-devel

%define X_display         ":98"

%if "%{?_lib}" == "lib64"
%define my_cmake_lib_suffix "-DLIB_SUFFIX=64"
%else
%define my_cmake_lib_suffix "-ULIB_SUFFIX"
%endif

%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
%global _hardened_build 1
%endif

%description
Trojita is a Qt IMAP e-mail client which:
  * Enables you to access your mail anytime, anywhere.
  * Does not slow you down. If we can improve the productivity
    of an e-mail user, we better do.
  * Respects open standards and facilitates modern technologies.
    We value the vendor-neutrality that IMAP provides and are committed
    to be as interoperable as possible.
  * Is efficient - be it at conserving the network bandwidth, keeping
    memory use at a reasonable level or not hogging the system's CPU.
  * Can be used on many platforms. One UI is not enough for everyone,
    but our IMAP core works fine on anything from desktop computers
    to cell phones and big ERP systems.
  * Plays well with the rest of the ecosystem. We don't like reinventing
    wheels, but when the existing wheels quite don't fit the tracks,
    we're not afraid of making them work.

%package plugin-qtkeychain
Summary: Add secure password storage to Trojita, a fast e-mail client
Group: Networking/Mail

%description plugin-qtkeychain
Plugin which enables Trojita to save passwords in platform-specific
encrypted storage.

%prep
%setup

%build
export CXXFLAGS="${CXXFLAGS:-%optflags} -fPIC"
export LDFLAGS="-pie"
cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DWITH_QTKEYCHAIN_PLUGIN=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%prefix \
    -DCMAKE_INSTALL_LIBDIR:PATH=%_libdir %my_cmake_lib_suffix \
    -DSHARE_INSTALL_PREFIX:PATH=%_datadir

%make_build

%install
%makeinstall_std

%files
%doc LICENSE README
%_libdir/libtrojita_plugins.so
%_bindir/trojita
%_bindir/be.contacts
%_desktopdir/trojita.desktop
%_iconsdir/hicolor/32x32/apps/trojita.png
%_iconsdir/hicolor/scalable/apps/trojita.svg
%dir %_datadir/trojita
%dir %_datadir/trojita/locale
%_datadir/trojita/locale/trojita_common_*.qm
%_datadir/appdata/trojita.appdata.xml

%files plugin-qtkeychain
%dir %_libdir/trojita
%_libdir/trojita/trojita_plugin_QtKeychainPasswordPlugin.so

%changelog
* Fri Sep 16 2016 Konstantin Artyushkin <akv@altlinux.org> 0.7-alt1
- new version

* Wed Feb 25 2015 Michael Shigorin <mike@altlinux.org> 0.5-alt1
- built for ALT Linux (based on upstream OBS spec)

