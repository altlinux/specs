%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: qabc
Version: 1.13
Release: alt1

Summary: Minimal GUI for ABC music notation
License: GPL-3.0
Group: Sound
Url: http://brouits.free.fr/qabc/
VCS: https://github.com/be1/qabc

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: qt6-base-devel
BuildRequires: qt6-tools

Requires: /usr/bin/abcm2ps
Requires: /usr/bin/abc2midi
Requires: /usr/bin/fluidsynth
Requires: /usr/bin/evince
Requires: ghostscript-common

%description
QAbc is a simple graphical program that allow to write musical scores
in the ABC notation.

This program allow to play the written music, preview the output score
and print it, using third party software.

%prep
%setup
%patch -p1
sed -i "s|Categories=.*|Categories=Music;AudioVideo;|" qabc.desktop

%build
lrelease-qt6 qabc.pro
qmake-qt6 \
          PREFIX=%_prefix \
          -config release \
          CONFIG+=nostrip \
          QMAKE_CXXFLAGS="%optflags"
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc *.md
%_bindir/%name
%_man1dir/*
%_desktopdir/%{name}.desktop
%_pixmapsdir/%{name}.png
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/metainfo/*%{name}.metainfo.xml
%_datadir/mime/packages/*%{name}.xml

%changelog
* Thu Jul 03 2025 Nikolay Strelkov <snk@altlinux.org> 1.13-alt1
- Initial build for Sisyphus
