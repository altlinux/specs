Name: tano
Version: 1.2.1
Release: alt1
Summary: An open IP TV player
License: GPLv3
Group: System/Libraries
URL: http://projects.tano.si
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake >= 2.8.6
BuildRequires: libqt4-devel >= 4.8
BuildRequires: libvlc-qt-devel >= 0.8.0

%description
Tano is an open-source cross-platform IP TV player. It features full IP TV
playback with EPG and recorder. Project started because of a need of a simple
IP TV player on Linux providing EPG.


%prep
%setup -q


%build
%cmake_insource
%make_build -j1


%install
%makeinstall_std
install -pD -m 0644 README.md %buildroot%_docdir/%name-%version/README
install -p -m 0644 AUTHORS CHANGELOG %buildroot%_docdir/%name-%version/
install -d -m 0755 %buildroot%_iconsdir/hicolor/64x64/apps
mv %buildroot%_iconsdir/{*.png,hicolor/64x64/apps/}


%files
%doc %_docdir/%name-%version
%_bindir/*
%_libdir/*.so.*
%exclude %_libdir/*.so
%_datadir/%name
%_desktopdir/*
%_iconsdir/hicolor/64x64/apps/*


%changelog
* Sun Sep 22 2013 Led <led@altlinux.ru> 1.2.1-alt1
- initial build
