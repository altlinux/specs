Name: CloudCross
Version: 1.4.1
Release: alt1
License: BSD
Group: Networking/File transfer
Summary: Syncronization of local files and folders with clouds
Source: v%version.tar.gz
Url: https://cloudcross.mastersoft24.ru/#usage

# Automatically added by buildreq on Wed Jul 26 2017
# optimized out: gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libqt5-core libqt5-network libstdc++-devel python-base python-modules qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-script-devel qt5-webchannel-devel qt5-xmlpatterns-devel
BuildRequires: qt5-3d-devel qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-quickcontrols2-devel qt5-scxml-devel qt5-sensors-devel qt5-serialbus-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel libcurl-devel

%description
CloudCross it's open source software for the synchronization of local
files and folders with multiple cloud storages. On this moment
CloudCross supports sync with Yandex.Disk Google Drive Cloud mail.ru
OneDrive and Dropbox. This program was written in pure Qt, without any
third-party libraries.

%prep
%setup -n %name-%version

%build
%qmake_qt5
%make_build

%install
##install -D ccross %buildroot/%_bindir/ccross
%makeinstall INSTALL_ROOT=%buildroot
install -D ccross-app/doc/ccross %buildroot%_man1dir/ccross.1

%files
%doc ccross-app/doc/*.* README* CHANGES*
%_bindir/*
%_man1dir/*

%changelog
* Mon Mar 19 2018 Fr. Br. George <george@altlinux.ru> 1.4.1-alt1
- Autobuild version bump to 1.4.1

* Wed Jul 26 2017 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Autobuild version bump to 1.4.0

* Wed Jul 26 2017 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Initial build for ALT

