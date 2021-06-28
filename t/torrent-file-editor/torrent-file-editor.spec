Name:		torrent-file-editor
Version:	0.3.17
Release:	alt3
License:	GPLv3+
Summary:	Torrent File Editor
Group:		File tools
Url:		https://torrent-file-editor.github.io/
Source0:	%name-%version.tar.gz

Patch0:		torrent-file-editor-0.3.17-uk_UA.patch

Provides:	%name-common %name-qt5
Obsoletes:	%name-common %name-qt5

BuildRequires: ccmake qt5-tools-devel

%description
Qt based GUI tool designed to create and edit .torrent files

%prep
%setup
%patch0 -p1

%build
mkdir ./build && cd ./build
cmake ../. \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DQT5_BUILD=ON \
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
%_desktopdir/%name.desktop
%_datadir/appdata/*.xml
%_iconsdir/hicolor/*/apps/%name.*

%changelog
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
