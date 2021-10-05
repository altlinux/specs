%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: scourge
Version: 0.21.1
Release: alt7.svn3264
Summary: Rogue-like RPG
Summary(de): Rogue-artiges Rollenspiel
Group: Games/Adventure
License: GPL2
URL: https://sourceforge.net/projects/scourge/

Source: scourge-%{version}.src.tar
Source1: scourge-%{version}.data.tar
Patch1: scourge-0.21.1-alt-build.patch

BuildRequires: gcc-c++ libGL-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libSDL_ttf-devel libX11-devel libfreetype-devel zlib-devel

Requires: %name-data = %EVR
Requires: fonts-ttf-dejavu-lgc

# data contains some scripts, ignore them
%add_findreq_skiplist  %_datadir/%name/*
%add_findprov_skiplist %_datadir/%name/*

%description
S.C.O.U.R.G.E. is a rogue-like game in the fine tradition of NetHack and Moria It sports 
a graphical front-end, similar to glHack or the Falcon's eye. I tried to design the 
3D UI as a best of both worlds from old to new: It lets you rotate the view, zoom in/out, 
view special effects, etc. On the other hand I've always liked the old-school isometric 
games like Exult or Woodward.

%description -l de
S.C.O.U.R.G.E. ist ein rogue-artiges Rollenspiel in der edlen Tradition von Nethack und Moria. 
Es verfügt über ein grafisches Frontend, ähnlich glHack oder Falcon's Eye. Ich habe versucht, 
in der 3D-Schnittstelle das Beste beider Welten, alt wie neu, zu vereinen: Es ist möglich, 
die Ansicht zu drehen, zu zoomen, Spezialeffekte zu betrachten usw. Andererseits habe ich 
stets althergebrachte isometrische Spiele wie Exult oder Woodward geschätzt.

%package data
Summary: Data for %name
Group: Games/Adventure
BuildArch: noarch

%description data
Data for %name

%prep
tar xf %SOURCE1
%setup -q -n %name
%patch1 -p2

%build
%add_optflags -std=c++14
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure --with-data-dir=%_datadir/%name

%make

%install
%makeinstall

mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/pixmaps
mkdir -p %buildroot%_datadir/applications
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_niconsdir

install -p -m 644 assets/%name.png %buildroot%_liconsdir/%name.png

# install menu
install -p -m 644 assets/%name.desktop %buildroot%_datadir/applications
install -p -m 644 assets/%name.png %buildroot%_datadir/pixmaps

#install data
cp -aRf ../scourge_data/* %buildroot%_datadir/%name

# remove bundled fonts (see ALT 25635)
rm %buildroot%_datadir/%name/fonts/DejaVuLGCSans.ttf %buildroot%_datadir/%name/fonts/DejaVuLGCSansMono.ttf
ln -srf %buildroot%_datadir/fonts/ttf/dejavu-lgc/DejaVuLGCSans.ttf %buildroot%_datadir/%name/fonts/DejaVuLGCSans.ttf
ln -srf %buildroot%_datadir/fonts/ttf/dejavu-lgc/DejaVuLGCSansMono.ttf %buildroot%_datadir/%name/fonts/DejaVuLGCSansMono.ttf

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/*
%_datadir/pixmaps/*
#_miconsdir/*
%_liconsdir/*
#_niconsdir/*
%_datadir/applications/*

%files data
%_datadir/%name

%changelog
* Tue Oct 05 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.21.1-alt7.svn3264
- Fixed build with gcc-11.

* Tue Jun 26 2018 Grigory Ustinov <grenka@altlinux.org> 0.21.1-alt6.svn3264
- Removed bundled fonts (Closes: #25635).

* Thu Apr 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.21.1-alt5.svn3264
- Fixed build.

* Wed Mar 30 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.21.1-alt4.svn3264
- Add xlib-devel to BuildRequires

* Mon Feb 01 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.21.1-alt3.svn3264
- Use svn for build
- Fix build
- Switch to git

* Mon Aug 17 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.21.1-alt2
- Fix build

* Fri Mar 06 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.21.1-alt1
- Build for ALT
