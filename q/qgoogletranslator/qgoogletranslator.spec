Name: qgoogletranslator
Version: 1.2.1
Release: alt2.1
Summary: Qt gui for google translate based on ajax api 
License: GPLv3
Group: System/Internationalization
URL: http://code.google.com/p/qgt/

Source: %name-%version.tar 
Patch: qgoogletranslator-1.2.1-alt-glibc-2.16.patch

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
%patch -p2
subst "s,/usr/local,%buildroot/usr/,g" ./CMakeLists.txt
subst "s,X11_LIBRARIES},X11_LIBRARIES} X11,g" ./CMakeLists.txt

%build
mkdir build
cd build
cmake .. \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_C_FLAGS='%optflags' \
	-DCMAKE_CXX_FLAGS='%optflags'
%make VERBOSE=1

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
* Mon Dec 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2.1
- Fixed build with glibc 2.16

* Fri Jun 08 2012 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt2
- Explicit link with libX11

* Mon Nov 22 2010 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

