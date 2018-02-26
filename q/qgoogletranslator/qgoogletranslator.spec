Name: qgoogletranslator
Version: 1.2.1
Release: alt2
Summary: Qt gui for google translate based on ajax api 
License: GPLv3
Group: System/Internationalization
URL: http://code.google.com/p/qgt/

Source: %name-%version.tar 

BuildRequires: gcc-c++ libqt4-devel
BuildRequires: cmake

Packager: Andrey Cherepanov <cas@altlinux.org>

%description
Description: dictionary lookup program, based on translate.google.com site
* Translation of selection buffer contents (by key press or automatically)
* Show up translation result in tool tip, main window and system tray
* Support for pronouncing feature
* Proxy support
* Reserved words (words, excluded from translation)
* Translation history
* Input language autodetection


%prep
%setup -q
subst "s,/usr/local,%buildroot/usr/,g" ./CMakeLists.txt
subst "s,X11_LIBRARIES},X11_LIBRARIES} X11,g" ./CMakeLists.txt

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
%make

%install
cd build
make install DESTDIR=%buildroot

%files 
%_bindir/%name
%dir %_datadir/%name
%dir %_datadir/%name/l10n
%_datadir/%name/*
%_datadir/pixmaps/%name.png
%_datadir/applications/%name.desktop

%changelog
* Fri Jun 08 2012 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt2
- Explicit link with libX11

* Mon Nov 22 2010 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

