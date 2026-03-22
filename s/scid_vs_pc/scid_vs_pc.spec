Name: scid_vs_pc
Version: 4.26
Release: alt1
Group: Games/Boards

Summary: A chess database application

License: GPLv2+

ExcludeArch: ppc64le

Url: https://scidvspc.sourceforge.net/
VCS: https://svn.code.sf.net/p/scidvspc/code/

Source0: %name-%version.tar
Source1: scid.desktop

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: tcl-devel tk-devel

Requires: tcl-snack
Requires: %name-data = %EVR

%description
Shane's Chess Information Database is a huge chess toolkit with extensive
database, analysis, and chess-playing features.

Scid vs. PC is a usability and bug-fix fork of Scid. It has extensive interface
fixes and improvements and is fully compatible with Scid's .si4 databases.
Its new features include a rewitten Gamelist, a Computer Tournament, and FICS,
Tree, and Book improvements.

%package data
Group: Games/Boards
BuildArch: noarch
Summary: Data for %name
License: GPLv2+

%description data
This package provides noarch data needed for %name.

%prep
%setup

%build
./configure \
        OPTIMIZE="%optflags" \
        BINDIR=%_bindir \
        SHAREDIR=%_datadir/%name

# j1 to avoid races
make -j1

%install
%makeinstall_std

mkdir -p %buildroot%_desktopdir
install -m0644 %SOURCE1 %buildroot%_desktopdir/scid.desktop

mkdir -p %buildroot%_iconsdir/hicolor/128x128/apps/
install -m0644 icons/scid.png %buildroot%_iconsdir/hicolor/128x128/apps/scid.png

mkdir -p %buildroot%_datadir/%name/sounds
install -m0644 sounds/*.wav %buildroot%_datadir/%name/sounds

%files
%doc COPYING README.txt
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/128x128/apps/*.png
%_datadir/%name/bitmaps/MkScidPieces

%files data
%_datadir/%name
%exclude %_datadir/%name/bitmaps/MkScidPieces

%changelog
* Sun Feb 15 2026 Leonid Znamenok <respublica@altlinux.org> 4.26-alt1
- New version (4.26).

* Fri Jan 17 2025 Leonid Znamenok <respublica@altlinux.org> 4.25-alt1
- Initial build for Sisyphus.
