Name:		grooveoff
Version:	0.1.8
Release:	alt1
License:	GPLv3+
Summary:	GrooveOff is an unofficial client for grooveshark.com
Url:		http://gcala.blogspot.com/
Group:		Sound
Source0:	%name-%version.tar.gz

BuildRequires: automoc cmake gcc-c++ qjson-devel libqt4-devel

%description
GrooveOff is an unofficial client for grooveshark.com. With it you can search its
huge database (thanks to a public api) for artists, songs and albums and save them
on disk for offline playing. It provides easy to use filters by artists and albums.

%prep
%setup

%build
mkdir build
cd build
cmake ../. -DCMAKE_INSTALL_PREFIX=%prefix
%make_build

%install
cd build
make DESTDIR=%buildroot install

%files
%doc README.md
%dir %_datadir/grooveoff
%dir %_datadir/grooveoff/translations
%_bindir/grooveoff
%_datadir/grooveoff/translations/*.qm
%_desktopdir/grooveoff.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Tue Dec 10 2013 Motsyo Gennadi <drool@altlinux.ru> 0.1.8-alt1
- initial build for ALT Linux
