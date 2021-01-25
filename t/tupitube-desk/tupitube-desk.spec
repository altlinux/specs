Name:     tupitube-desk
Version:  0.2.17
Release:  alt1

Summary:  TupiTube Desk is vector editor for images, storyboards and animations
License:  GPL-2.0
Group:    Graphics
Url:      http://www.tupitube.com/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: tupitube.desk-%version.tar
Patch1: tupitube.desk-alt-libquazip5.patch
Patch2: tupitube.desk-alt-qt-5.15.patch
Patch3: tupitube.desk-alt-rpath.patch

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
BuildRequires: ruby
BuildRequires: ruby-gem(os)
BuildRequires: libavformat-devel
BuildRequires: libquazip-devel
BuildRequires: libquazip-qt5-devel
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
%patch1 -p2
%patch2 -p2
%patch3 -p2
subst 's|@LIBDIR@|%_libdir|' src/shell/shell.pro

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

%changelog
* Mon Jan 25 2021 Andrey Cherepanov <cas@altlinux.org> 0.2.17-alt1
- Initial build for Sisyphus.
