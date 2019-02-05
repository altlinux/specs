Name:     libqtelegram-ae
Version:  10.0.0
Release:  alt1

Summary:  Most powerfull telegram library that created using C++ and Qt.

License:  GPLv3
Group:    System/Configuration/Other
Url:      https://github.com/Aseman-Land/libqtelegram-aseman-edition

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

Patch: libqtelegram-ae-openssl-1.1.x.patch

BuildRequires(pre): rpm-macros-qt5

BuildRequires: libssl-devel python3-module-zope zlib-devel
BuildRequires: qt5-3d-devel qt5-connectivity-devel qt5-multimedia-devel
BuildRequires: qt5-phonon-devel qt5-quick1-devel qt5-quickcontrols2-devel
BuildRequires: qt5-sensors-devel qt5-serialport-devel qt5-speech-devel
BuildRequires: qt5-svg-devel qt5-tools-devel qt5-wayland-devel
BuildRequires: qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel

%description
This is a Qt asynchronous library to be used as Telegram client. It was
based originally on telegram-cli code (https://github.com/vysheng/tg),
but it's now completely different. Now works using signal-slot mechanism
and has an external easy to use API for client applications to interact to.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Development files for %name.

%prep
%setup
%patch -p1

%build
%qmake_qt5 CONFIG+=typeobjects
%make_build

%install
INSTALL_ROOT=%buildroot %makeinstall_std

%files
%doc README*
%_libdir/*.so.*

%files devel
%_includedir/*

%_libdir/lib*.so

%changelog
* Tue Feb 05 2019 Grigory Ustinov <grenka@altlinux.org> 10.0.0-alt1
- Initial build for Sisyphus.
