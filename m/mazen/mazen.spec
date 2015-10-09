Name: mazen
Version: 1.0.1
Release: alt2

Summary: Simple Gnome-base maze creator
License: GPLv3
Group: Games/Puzzles
Url: http://mazen.sourceforge.net

Packager: Slava Dubrovskiy <dubrsl@altlinux.org>
Source: %name-%version.tar.gz
#Source4: %name-16x16.png
#Source5: %name-32x32.png
#Source6: %name-48x48.png

BuildRequires: gcc-c++ intltool libgtkmm2-devel librsvg-devel libcairomm-devel libglibmm-devel

%description
Can create various types of mazes, and export them in PDF, PNG or SVG formats.

%prep
%setup -q

%build
%add_optflags -std=gnu++11
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%__mkdir_p %buildroot%_pixmapsdir
%__install -p -m 644 artwork/mazen.png %buildroot%_pixmapsdir/%name.png


# menu
%__mkdir_p %buildroot%_desktopdir
%__cat << EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Name=Mazen
Comment=Simple Gnome-base maze creator
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING
%_bindir/*
%_datadir/%name/
%_pixmapsdir/*
%_desktopdir/*

%changelog
* Fri Oct 09 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2
- Fix build with gcc5

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1-alt1.qa1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Jan 29 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt1
- initial build for ALT
