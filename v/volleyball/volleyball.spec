Summary: Video game similar to GNU Arcade Volleyball
Name: volleyball
Version: 0.8.6
%define dversion 0.8.5
Epoch: 1
Release: alt2
Source: %name-%version.tar.gz
Source1: %name.desktop
Source2: %name-data-%dversion.tar.gz
License: GPL
Group: Games/Sports 
URL: http://www.losersjuegos.com.ar/juegos/volleyball

# due to .desktop
Requires: /usr/bin/sound_wrapper

# Automatically added by buildreq on Tue Apr 12 2011
# optimized out: libSDL-devel
BuildRequires: libSDL_image-devel libSDL_mixer-devel

%description
Volleyball - video game similar to GNU Arcade Volleyball


%prep
%setup -q
tar xvf %SOURCE2 && mv %name-data-%dversion data

%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
# DSO HACK
sed -i 's/-lSDL /-lm -lSDL /g' src/Makefile
%make_build
(
cd data
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make
)


%install
mkdir -p %buildroot{%_gamesbindir,%_gamesdatadir}
make install DESTDIR=%buildroot
make -C data install DESTDIR=%buildroot
# desktop-file
install -p -m644 -D %SOURCE1  %buildroot%_desktopdir/%name.desktop

%files
%_gamesbindir/*
%_gamesdatadir/*
%_man6dir/*
%_desktopdir/%name.desktop
%doc README ChangeLog TODO AUTHORS

%changelog
* Mon May 28 2012 Fr. Br. George <george@altlinux.ru> 1:0.8.6-alt2
- DSO list completion

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1:0.8.6-alt1
- Version up

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 1:0.8.5-alt1.qa2
- NMU: .desktop files should use /usr/bin/sound_wrapper

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1:0.8.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for volleyball
  * postclean-05-filetriggers for spec file

* Mon Oct 08 2007 Fr. Br. George <george@altlinux.ru> 1:0.8.5-alt1
- Epoch changed
- Version up

* Mon Dec 18 2006 Fr. Br. George <george@altlinux.ru> 0.82-alt2
- Fix-up rebuild

* Tue Mar 14 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.82-alt1
- implementation build


