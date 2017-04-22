Name: libqtelegram
Version: 1.0.0
Release: alt1
Epoch: 1

Summary: This is a Qt asynchronous library to be used as Telegram client

%define libname libqtelegram
%define sname qtelegram

License: GPLv3


Group: System/Configuration/Other
Url: https://launchpad.net/libqtelegram
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %sname-%version.tar

BuildRequires(pre): rpm-macros-qt5

# Automatically added by buildreq on Fri Apr 21 2017
# optimized out: gcc-c++ libGL-devel libqt5-core libqt5-gui libqt5-multimedia libqt5-network libstdc++-devel python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-script-devel qt5-webchannel-devel qt5-xmlpatterns-devel
BuildRequires: libssl-devel python3-module-zope zlib-devel
BuildRequires: qt5-3d-devel qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-quickcontrols2-devel 
BuildRequires: qt5-sensors-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel
BuildRequires: qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel

%description
This is a Qt asynchronous library to be used as Telegram client. It was
based originally on telegram-cli code (https://github.com/vysheng/tg),
but it's now completely different. Now works using signal-slot mechanism
and has an external easy to use API for client applications to interact to.

%package -n %libname-devel
Summary: Development files for %name
Group: Development/Other
Requires: %libname = %version-%release

%description -n %libname-devel
Development files for %name.

%prep
%setup -n %sname-%version

%build
%qmake_qt5 CONFIG+=typeobjects
%make_build

cat << EOF > qtelegram.pc 
prefix=%prefix
exec_prefix=%prefix
libdir=%_libdir
includedir=%_includedir/qt5/libqtelegram-ae

Name: libqtelegram
Description: Telegram library written in Qt 
Version: 1.0.0
Libs: -L${libdir} -lqtelegram-ae
Cflags: -I${includedir}
EOF

%install
INSTALL_ROOT=%buildroot %makeinstall_std
install -d %buildroot%_pkgconfigdir/
install -m 644 qtelegram.pc %buildroot%_pkgconfigdir/qtelegram.pc 

%files
%doc README README.md
%_libdir/*.so.*

%files -n %libname-devel
%_includedir/*
%_pkgconfigdir/*

%_libdir/lib*.so

%changelog
* Mon Apr 24 2017 Hihin Ruslan <ruslandh@altlinux.ru> 1:1.0.0-alt1
- Add pkgconfigdir/*

* Thu Apr 20 2017 Hihin Ruslan <ruslandh@altlinux.ru> 10.0.0-alt1
-  initial build for ALT Linux Sisyphus



