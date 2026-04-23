%define _unpackaged_files_terminate_build 1

Name: iconoscope
Version: 0.9.9
Release: alt3

Summary: Explore the system's icon theme database
License: GPL-3.0
Group: Graphics
Url: https://github.com/santileortiz/Iconoscope

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: pkgconfig(gtk+-3.0)

%description
%summary

%prep
%setup
%patch -p1
sed -i 's|^Categories=.*|Categories=Graphics;2DGraphics;|' data/iconoscope.desktop

%build
sed -i "s/{C_FLAGS}/{C_FLAGS} -std=gnu17/" pymk.py
./pymk.py iconoscope

%install
./pymk.py install --install_completions --destdir %buildroot%prefix/

%files
%doc LICENCE.txt README.md data/screenshot.png
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/metainfo/*%{name}.appdata.xml

%changelog
* Thu Apr 23 2026 Nikolay Strelkov <snk@altlinux.org> 0.9.9-alt3
- Fixed FTBFS caused by gcc15.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 0.9.9-alt2
- Applied repocop fix for freedesktop-categories

* Fri May 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.9.9-alt1
- Initial build for Sisyphus
