Name: nestopia
Version: 1.40h
%define sversion 	%(sed -e "s/[a-z.]//g"<<<%version)
%define oversion 	%(sed -e "s/[0-9.]//g"<<<%version)
%define distsuffix	alt
Release: alt2
Packager: Ilya Mashkin <oddity@altlinux.ru>
Summary: A portable Nintendo Entertainment System emulator
License: GPLv2+
Group: Emulators
Url: http://rbelmont.mameworld.info/?page_id=200
# and http://nestopia.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/nestopia/Nestopia%{sversion}src.zip
Source1: http://rbelmont.mameworld.info/nst%{sversion}_lnx_release_%oversion.zip
Source2: nestopia-wrapper
Source3: nestopia-48.png

BuildRequires: libgtk+2-devel unzip
BuildRequires: libSDL-devel gcc-c++
BuildRequires: libalsa-devel

%description
NEStopia is a portable Nintendo Entertainment System emulator written in C++
by Martin Freij and ported to Linux by R. Belmont.

NEStopia strives for the most accurate emulation possible at the
pixel-by-pixel and sample-by-sample level, and it has excellent mapper
and UNIF board support as well.

A few features:
- Supports .nes, .unf/.unif, and XML format ROMs, including Vs. and
 Playchoice 10 games
- Supports .fds discs (a file named diskrom.sys is needed for this feature)
- Supports .nsf music rips
- All supported files can be extracted from zip or 7zip containers (an
 archive browser is not yet included - this assumes the common GoodSet case
 of one zip or 7zip per game)
- Supports save states
- Supports movie recordings
- Supports the rewinder - if you make a bad jump and screw up your
 game, press Backspace and the game will run in reverse. Press \ to take over
 again and try to fix your mistake.
- Friendly GUI configuration
- Autodetection of PAL and NTSC format games
- Supports drag and drop of compatible games and music rips from modern Linux
 file managers, including KDE Konqueror and GNOME Nautilus.


%prep
%setup -c -a1

%build
%install

make

# binary
install -d -m 755 %buildroot/%_bindir
install -m 755 nst %buildroot/%_bindir/

# wrapper
install -m 755 %_sourcedir/nestopia-wrapper %buildroot/%_bindir/nestopia

# data files
install -d -m 755 %buildroot/%_datadir/nestopia
install -m 644 NstDatabase.xml %buildroot/%_datadir/nestopia/
install -m 644 nstcontrols %buildroot/%_datadir/nestopia/

# icon
install -d -m 755 %buildroot/%_iconsdir
install -m 644 %_sourcedir/nestopia-48.png %buildroot/%_iconsdir/nestopia.png

# xdg menu
install -d -m 755 %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/nestopia.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=NEStopia
Comment=%summary
Exec=%_bindir/nestopia
Icon=nestopia
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

%files
%doc README.Linux
%_bindir/nestopia
%_bindir/nst
%_datadir/nestopia
%_iconsdir/nestopia.png
%_datadir/applications/nestopia.desktop


%changelog
* Tue May 01 2012 Ilya Mashkin <oddity@altlinux.ru> 1.40h-alt2
- fix desktop file

* Sun Apr 29 2012 Ilya Mashkin <oddity@altlinux.ru> 1.40h-alt1
- build for Sisyphus

* Fri Oct 24 2008 Guillaume Bedot <littletux@zarb.org> 1.40h-1plf2009.1
- 1.40h

* Fri Aug 15 2008 Guillaume Bedot <littletux@zarb.org> 1.40g-1plf2009.0
- First package of NEStopia for PLF.
