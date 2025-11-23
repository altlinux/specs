%define _unpackaged_files_terminate_build 1

Name: qspeakers
Version: 1.8.5
Release: alt1

Summary: Loudspeaker design software
License: GPL-3.0
Group: Sciences/Physics
Url: http://brouits.free.fr/qspeakers/
VCS: https://github.com/be1/qspeakers

Source: %name-%version.tar

BuildRequires: qt6-base-devel
BuildRequires: qt6-tools
BuildRequires: pkgconfig(Qt6Charts)

%description
QSpeakers is a simple graphical program that
simulates common acoustical enclosures behaviour
to help designing loudspeaker systems, based on
the loudspeaker driver's Thiele / Small parameters
and the chosen enclosure type.

This software is mostly useful for do-it-yourself
loudspeaker enthusiasts, acoustics teaching, and
to a lesser extent, for loudspeaker engineering.

%prep
%setup
sed -i "s|Categories=.*|Categories=Science;Physics;|" qspeakers.desktop

%build
lrelease-qt6 qspeakers.pro
qmake-qt6 \
          PREFIX=%_prefix \
          -config release
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc *.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%_man1dir/*
%_iconsdir/hicolor/scalable/apps/%{name}.svg
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/metainfo/*%{name}.metainfo.xml
%_datadir/mime/packages/*%{name}.xml

%changelog
* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.8.5-alt1
- New version 1.8.5.

* Thu Jul 03 2025 Nikolay Strelkov <snk@altlinux.org> 1.8-alt1
- Initial build for Sisyphus
