Name: beebeep
Version: 5.8.6
Release: alt1

Summary: Secure Network Chat
License: GPLv3+
Group: Networking/Chat

Url: http://sourceforge.net/projects/beebeep/
Source0: %name-code-%version.tar.bz2
Source1: %name.desktop

# fix patch from openSUSE for change path to data files
Patch: GuiLanguage-5.6.8.patch
Patch1: Settings-5.6.8.patch

BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires: /usr/bin/convert qt5-multimedia-devel qt5-tools-devel qt5-webkit-devel qt5-x11extras-devel
%ifarch %qt5_qtwebengine_arches
BuildRequires: qt5-webview-devel
%endif

%description
BeeBEEP is a secure network chat. You can talk and send files with all your
friends inside a local area network such of an office, home or internet cafe
without a server.

%prep
%setup -n %name-code-r1555
%autopatch -p1

%build
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" -recursive -o Makefile beebeep-desktop.pro
%make_build all

%install
mkdir -p %buildroot%_bindir
mv test/%name %buildroot%_bindir/%name
mkdir -p %buildroot%_libdir
cp -a test/* %buildroot%_libdir
mkdir -p %buildroot%_datadir/%name
cp -a ./locale/*.qm %buildroot%_datadir/%name
cp -a ./misc/*.wav %buildroot%_datadir/%name
install -Dp -m 0644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop

# Icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 src/images/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 src/images/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 src/images/%name.png %buildroot%_miconsdir/%name.png

%files
%doc *.txt
%dir %_datadir/%name
%_bindir/%name
%_libdir/lib*
%_datadir/%name/*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Fri May 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.8.6-alt1
- 5.8.4 -> 5.8.6

* Sat May 13 2023 Michael Shigorin <mike@altlinux.org> 5.8.4-alt2
- use rpm-macros-qt5-webengine

* Sat May 08 2021 Motsyo Gennadi <drool@altlinux.ru> 5.8.4-alt1
- 5.8.4

* Sat Nov 28 2020 Motsyo Gennadi <drool@altlinux.ru> 5.8.3-alt0.svn1449
- svn stapshot 1449

* Thu Nov 26 2020 Motsyo Gennadi <drool@altlinux.ru> 5.8.2-alt1
- initial build for ALT Linux
