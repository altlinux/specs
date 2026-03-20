%define _unpackaged_files_terminate_build 1

Name: gromit-mpx
Version: 1.9.0
Release: alt1

Summary: GTK+ based tool to make annotations on screen with multiple pointers
License: GPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/bk138/gromit-mpx

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(liblz4)

%description
Gromit-MPX is an on-screen annotation tool that works with any Unix 
desktop environment under X11 as well as Wayland. 

Gromit-MPX enables you to make annotations on your screen using
multiple pointing devices at once.

This is especially useful when making presentations, to highlight
things or point out things of interest.

Gromit-MPX is XInput-Aware, so if you have a graphic tablet you can
draw lines with different strength, color, erase things, etc.

%prep
%setup
sed -i 's|^Categories=.*|Categories=Graphics;2DGraphics;|' data/net.christianbeier.Gromit-MPX.desktop

%build
%cmake \
       -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir
%cmake_build

%install
%cmake_install
rm -rv %{buildroot}%{_datadir}/doc/

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS ChangeLog CONTRIBUTING.md COPYING NEWS.md README.md
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%{name}.cfg
%_bindir/*
%_man1dir/*
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.appdata.xml
%_datadir/pixmaps/*

%changelog
* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 1.9.0-alt1
- New version 1.9.0.

* Fri Nov 14 2025 Nikolay Strelkov <snk@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 1.7.0-alt2
- Applied repocop fix for freedesktop-categories

* Sun Mar 09 2025 Nikolay Strelkov <snk@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus
