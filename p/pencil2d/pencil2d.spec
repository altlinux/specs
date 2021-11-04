Name:    pencil2d
Version: 0.6.6
Release: alt1

Summary: Pencil2D is an easy, intuitive tool to make 2D hand-drawn animations. Pencil2D is open source and cross-platform.
License: GPL-2.0
Group:   Other
Url:     https://github.com/pencil2d/pencil

Source: %name-%version.tar
Patch: %name-alt-glibc-2.34.patch

BuildRequires(pre): qt5-base-devel
BuildRequires: gcc-c++
BuildRequires: qt5-tools
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel

%description
Pencil2D is an animation/drawing software for Windows, macOS, Linux, and
FreeBSD. It lets you create traditional hand-drawn animation (cartoon) using
both bitmap and vector graphics. Pencil2D is free and open source.

%prep
%setup
%patch -p1

%build
%qmake_qt5 PREFIX=%_prefix %name.pro
%make_build
lrelease-qt5 %name.pro

%install
%installqt5

%files
%doc README.md ChangeLog.md
%_bindir/*
%_desktopdir/*.desktop
%_datadir/bash-completion/completions/pencil2d
%_iconsdir/hicolor/256x256/apps/*.png
%_datadir/metainfo/*.metainfo.xml
%_datadir/mime/packages/*.xml
%_datadir/zsh/site-functions/_pencil2d

%changelog
* Thu Nov 04 2021 Andrey Cherepanov <cas@altlinux.org> 0.6.6-alt1
- Initial build for Sisyphus.
