Name:     tupitube-desk
Version:  0.2.18
Release:  alt3.1

Summary:  TupiTube Desk is vector editor for images, storyboards and animations
License:  GPL-2.0
Group:    Graphics
Url:      http://www.tupitube.com/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: tupitube.desk-%version.tar
Source1: %name.watch
Patch1: tupitube.desk-alt-rpath.patch
Patch2: tupitube.desk-alt-quazip1.2.patch

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
BuildRequires: ruby
BuildRequires: gem(os)
BuildRequires: gem(rexml)
BuildRequires: libavformat-devel
BuildRequires: quazip-qt5-devel
BuildRequires: zlib-devel

%description
TupiTube Desk is a desktop application focused on 2D vector-based
content like images (PNG), storyboards (HTML) and animations (OGG,
AVI, MPEG, etc).
Its interface has been designed looking for provide a high level
experience of usability for artists and non artists, using as main
development resource the Qt framework.

%prep
%setup -n tupitube.desk-%version
%autopatch1 -p2
subst 's|@LIBDIR@|%_libdir|' src/framework/gui/gui.pro

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/*
%_libdir/tupitube
%_datadir/tupitube
%_desktopdir/tupitube.desktop
%_datadir/mime/packages/tupitube.xml
%_pixmapsdir/tupitube.desk.png
%_datadir/metainfo/*.appdata.xml

%changelog
* Wed Nov 23 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.18-alt3.1
- ! fix ruby gem build deps

* Fri Mar 04 2022 Andrey Cherepanov <cas@altlinux.org> 0.2.18-alt3
- FTBFS: linked libraries in subdirectories.

* Thu Jan 13 2022 Andrey Cherepanov <cas@altlinux.org> 0.2.18-alt2
- FTBFS: fix build with quazip-qt5-1.2.

* Mon Nov 29 2021 Andrey Cherepanov <cas@altlinux.org> 0.2.18-alt1
- New version.

* Mon Jan 25 2021 Andrey Cherepanov <cas@altlinux.org> 0.2.17-alt1
- Initial build for Sisyphus.
