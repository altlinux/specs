%define oname io.github.torrent_file_editor.Torrent-file-editor

Name: torrent-file-editor
Version: 1.0.3
Release: alt1

License: GPLv3+
Summary: Torrent File Editor
Group: File tools

Url: https://torrent-file-editor.github.io
Vcs: https://github.com/torrent-file-editor/torrent-file-editor

Source: %name-%version.tar

BuildRequires: ccmake qt6-tools-devel qt6-5compat-devel qt6-svg-devel

%description
Qt based GUI tool designed to create and edit .torrent files

%prep
%setup

%build
mkdir ./build && cd ./build
cmake ../. \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DQT6_BUILD=ON \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DENABLE_PCH:BOOL=OFF
%make_build

%install
cd ./build
%make DESTDIR=%buildroot install

%files
%doc README.md LICENSE
%_bindir/%name
%_desktopdir/%oname.desktop
%_datadir/metainfo/*.xml
%_iconsdir/hicolor/*/apps/%oname.*

%changelog
* Sat Jun 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.3-alt1
- updated from 1.0.2 to 1.0.3

* Mon Mar 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.2-alt1
- 1.0.1 -> 1.0.2

* Fri Mar 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.1-alt1
- 1.0.0 -> 1.0.1

* Fri Jun 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.0.0-alt1
- 0.3.17 -> 1.0.0
- fixed FTBFS
- build with Qt6
- removed patch
- added VCS

* Mon Jun 28 2021 Motsyo Gennadi <drool@altlinux.ru> 0.3.17-alt3
- build only with Qt5

* Sat Apr 11 2020 Motsyo Gennadi <drool@altlinux.ru> 0.3.17-alt1.2
- fix build with cmake 3.17

* Sun Feb 02 2020 Motsyo Gennadi <drool@altlinux.ru> 0.3.17-alt1.1
- cleanup git

* Sat Feb 01 2020 Motsyo Gennadi <drool@altlinux.ru> 0.3.17-alt1
- 0.3.17

* Tue Mar 26 2019 Motsyo Gennadi <drool@altlinux.ru> 0.3.13-alt1
- 0.3.13

* Mon Nov 07 2016 Motsyo Gennadi <drool@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Wed Nov 18 2015 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt3.1
- fix build

* Wed Nov 18 2015 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt3
- build subpackage with Qt5

* Tue Nov 17 2015 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt2
- fix open files with cyrillic symbols

* Mon Nov 16 2015 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Sun Aug 09 2015 Motsyo Gennadi <drool@altlinux.ru> 0.2.0-alt1
- initial build for ALT Linux
