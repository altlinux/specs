Name:		torrent-file-editor
Version:	0.2.1
Release:	alt1
License:	GPLv3+
Summary:	Torrent File Editor
Group:		File tools
Url:		http://sourceforge.net/projects/torrent-file-editor/
Source0:	%name-%version.tar.gz

Patch0:		%name-0.2.0-cmake_version_down.diff
Patch1:		%name-0.2.0-file_open_with.diff

BuildRequires: cmake gcc-c++ libqt4-devel qjson-devel

%description
Qt based GUI tool designed to create and edit .torrent files

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
mkdir ./build && cd ./build
cmake ../. \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"
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
* Mon Nov 16 2015 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Sun Aug 09 2015 Motsyo Gennadi <drool@altlinux.ru> 0.2.0-alt1
- initial build for ALT Linux
