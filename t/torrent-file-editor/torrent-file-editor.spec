Name:		torrent-file-editor
Version:	0.3.0
Release:	alt1
License:	GPLv3+
Summary:	Torrent File Editor
Group:		File tools
Url:		http://sourceforge.net/projects/torrent-file-editor/
Source0:	%name-%version.tar.gz

Source1:	%name-qt5.desktop

Patch0:		%name-0.3.0-cmake_version_down.diff

Requires:	%name-common

BuildRequires: cmake gcc-c++ libEGL-devel qt5-tools-devel libqt4-devel qjson-devel

%description
Qt based GUI tool designed to create and edit .torrent files


%package -n %name-qt5
Summary:	Torrent File Editor (Qt5)
Group:		File tools
Requires:	%name-common

%description -n %name-qt5
Qt5 based GUI tool designed to create and edit .torrent files

%package -n %name-common
Summary:	Common files for Torrent File Editor (Qt4 & Qt5)
Group:		File tools
BuildArch:	noarch

%description -n %name-common
Common files for Torrent File Editor (Qt4 & Qt5)

%prep
%setup
%patch0 -p1

%build
mkdir ./build && cd ./build
cmake ../. \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DQT5_BUILD=ON \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build
mv ./%name ../%name-qt5
rm -rf ./*

cmake ../. \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DQT5_BUILD=OFF \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build

%install
cd ./build
%make DESTDIR=%buildroot install
install -m 0755 ../%name-qt5 %buildroot%_bindir/%name-qt5
install -m 0644 %SOURCE1 %buildroot%_desktopdir/%name-qt5.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop

%files -n %name-qt5
%_bindir/%name-qt5
%_desktopdir/%name-qt5.desktop

%files -n %name-common
%doc README.md LICENSE
%_datadir/appdata/*.xml
%_iconsdir/hicolor/*/apps/%name.*

%changelog
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
