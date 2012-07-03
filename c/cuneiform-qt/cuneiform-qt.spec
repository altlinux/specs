Name:		cuneiform-qt
Version:	0.1.2
Release:	alt1
Summary:	GUI frontend for Cuneiform OCR

License:	GPLv3+
Group:		Graphics
URL:		http://www.altlinux.org/Cuneiform-Qt

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	%name-%version.tar.bz2

BuildRequires: ImageMagick gcc-c++ libqt4-devel >= 4.3.0

Requires: cuneiform

%description
This application is GUI frontend for Cuneiform (OCR system originally 
developed and open sourced by Cognitive technologies). It allow
to open scanned image, view this one in preview pane, recornize text via
Cuneiform and save result in HTML file.

%prep
%setup -q
PREFIX=%prefix qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro

%build
%make_build

%install
make install INSTALL_ROOT=%buildroot

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 icons/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 icons/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 icons/%name.png %buildroot%_miconsdir/%name.png

%files
%doc AUTHORS README TODO
%_bindir/%name
%_datadir/apps/%name/*.qm
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Fri Apr 10 2009 Andrey Cherepanov <cas@altlinux.org> 0.1.2-alt1
- Fix build with Qt 4.3 

* Fri Apr 10 2009 Motsyo Gennadi <drool@altlinux.ru> 0.1.1-alt1.2
- created Ukrainian translation
- add Ukrainian to desktop-file

* Wed Apr 08 2009 Motsyo Gennadi <drool@altlinux.ru> 0.1.1-alt1.1
- fix optflags
- change icons from pixmapsdir to iconsdir
- cleanup spec

* Tue Apr 07 2009 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1
- Add Russian translation
- Save from text widget instead copy temporary file
- Remove temporary file
- Check for errors during saving
- Differ saved format and filter in saved file selection dialog
- Show application icon in about dialog
- Remove native option because it is binary format and it will not display correctly
- Fix readOnly flag for result text
- Move installation instruction from spec to QMake project file

* Mon Apr 06 2009 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial release
