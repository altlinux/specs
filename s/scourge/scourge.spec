Name: scourge
Version: 0.21.1
Summary: Rogue-like RPG
Summary(de): Rogue-artiges Rollenspiel
Group: Games/Adventure
Release: alt4.svn3264
License: GPL2
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
URL: http://scourgeweb.org
Source: http://internap.dl.sourceforge.net/sourceforge/scourge/scourge-%{version}.src.tar.gz
Source1: http://internap.dl.sourceforge.net/sourceforge/scourge/scourge-%{version}.data.tar.gz
Requires: %name-data = %version-%release

BuildRequires: gcc4.3-c++ libGL-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libSDL_ttf-devel libX11-devel libfreetype-devel zlib-devel

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
Requires: %name = %version-%release
BuildArch: noarch

%description data
Data for %name

%prep
rm -fr scourge_data
%__tar xzf %SOURCE1
%setup -q -n %name

%build
%autoreconf
%configure --with-data-dir=%_datadir/%name

make

%install
%makeinstall

%__mkdir_p %buildroot%_datadir/%name
%__mkdir_p %buildroot%_datadir/pixmaps
%__mkdir_p %buildroot%_datadir/applications
%__mkdir_p %buildroot%_miconsdir
%__mkdir_p %buildroot%_liconsdir
%__mkdir_p %buildroot%_niconsdir

%__install -p -m 644 assets/%name.png %buildroot%_liconsdir/%name.png
#__install -p -m 644 %SOURCE5 %buildroot%_niconsdir/%name.png
#__install -p -m 644 %SOURCE6 %buildroot%_miconsdir/%name.png

# install menu
%__install -p -m 644 assets/%name.desktop %buildroot%_datadir/applications
%__install -p -m 644 assets/%name.png %buildroot%_datadir/pixmaps

#install data
%__cp -aRf ../scourge_data/* %buildroot%_datadir/%name


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
