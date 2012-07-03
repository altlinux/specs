%define		svn svn77

%define		srcname iTest
Version:	1.4.1.1
Name:		itest
Release:	alt1.%svn.1
Summary:	%srcname is a simple examination system
Summary(ru_RU.UTF8): %srcname - простая система проведения тестов, экзаменов
License: 	GPLv2
Group: 		Education
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://itest.sourceforge.net/
Source0:	http://kent.dl.sourceforge.net/sourceforge/itest/%srcname-%version-src.tar.gz
Source1:	%name-1.3-client.tar.bz2
Source2:	%name-1.3-server.tar.bz2
Source3:	%name.desktop
Source4:	%{name}server.desktop

Patch0:		%name-1.4-qt4.7.diff

Requires:	%{get_dep libqt4-core}

BuildRequires: gcc-c++ /usr/bin/convert libqt4-devel libqt4-network libqt4-svg

%description
iTest is a Qt application consisting of a Server and a Client
designed for easy computerised examination.

%description -l ru_RU.UTF8
iTest - приложение для лёгкого проведения компьютеризованного
тестирования. iTest создан на основе фреймворка Qt и состоит
из серверной и клиентской частей.

%package server
Summary:	Server for %srcname
Group:		Education

%description server
A question/answer database editor and exam server for %srcname

%prep
%setup -q -n %srcname-%version-src
%patch0 -p1
cp %SOURCE1 %SOURCE2 ./

%build
export PATH=$PATH:%_qt4dir/bin
    cd iTestServer
    qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" -config release
    lrelease iTestServer.pro
    cd ..
    cd iTestClient
    qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" -config release
    lrelease iTestClient.pro
    cd ..
    qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" -config release
%make_build

%install
%__install -Dp -m 0755 bin/%{srcname}Client %buildroot%_bindir/%{name}client
%__install -Dp -m 0755 bin/%{srcname}Server %buildroot%_bindir/%{name}server

# Desktop files
%__install -Dp -m 0644 %SOURCE3 %buildroot%_desktopdir/%name.desktop
%__install -Dp -m 0644 %SOURCE4 %buildroot%_desktopdir/%{name}server.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 iTestClient/images/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 iTestClient/images/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 iTestClient/images/%name.png %buildroot%_miconsdir/%name.png

convert -resize 48x48 iTestServer/images/%{name}server.png %buildroot%_liconsdir/%{name}server.png
convert -resize 32x32 iTestServer/images/%{name}server.png %buildroot%_niconsdir/%{name}server.png
convert -resize 16x16 iTestServer/images/%{name}server.png %buildroot%_miconsdir/%{name}server.png

%files
%doc %name-1.3-client.tar.bz2
%_bindir/%{name}client
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop

%files server
%doc %name-1.3-server.tar.bz2
%_bindir/%{name}server
%_miconsdir/%{name}server.png
%_niconsdir/%{name}server.png
%_liconsdir/%{name}server.png
%_desktopdir/%{name}server.desktop

%changelog
* Tue Nov 23 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.1.1-alt1.svn77.1
- fix build for Qt4.7 (thanks to DOOMer for patch)

* Mon Sep 20 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.1.1-alt1.svn77
- new svn snapshot 77

* Sat Nov 21 2009 Motsyo Gennadi <drool@altlinux.ru> 1.4.1-alt1.1
- added russian description and summary (fixed #22158). Thanks to Phantom.

* Sat Apr 04 2009 Motsyo Gennadi <drool@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 1.4.0-alt2
- delete post/postun scripts (new rpm)

* Sat Jul 05 2008 Motsyo Gennadi <drool@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Sun Apr 06 2008 Motsyo Gennadi <drool@altlinux.ru> 1.3.0-alt1
- initial build for ALT Linux
