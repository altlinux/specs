%define verdata 2005-01-06
Name:	 xblast-data
Version: 2.10.3
Release: alt1
Summary: The X11 bomberman team game (data files)
License: GPL
Group: Games/Arcade
Source0: http://heanet.dl.sourceforge.net/sourceforge/xblast/images-%verdata.tar.gz
Source1: http://heanet.dl.sourceforge.net/sourceforge/xblast/musics-%verdata.tar.gz
Source2: http://heanet.dl.sourceforge.net/sourceforge/xblast/models-%verdata.tar.gz
Source3: http://heanet.dl.sourceforge.net/sourceforge/xblast/levels-%verdata.tar.gz
Source4: http://heanet.dl.sourceforge.net/sourceforge/xblast/sounds.tar.gz
Url: http://xblast.sourceforge.net/
BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>

%description
Images, levels, characters, sounds and music data faile for XBlast

%prep
%setup -qc
tar xf %SOURCE1
tar xf %SOURCE2
tar xf %SOURCE3
tar xf %SOURCE4

%build

%install
mkdir -p %buildroot/%_gamesdatadir/XBlast-TNT
cp -r levels-%verdata %buildroot/%_gamesdatadir/XBlast-TNT/level
cp -r images-%verdata %buildroot/%_gamesdatadir/XBlast-TNT/image
cp -r models-%verdata %buildroot/%_gamesdatadir/XBlast-TNT/image/sprite
cp -r sounds %buildroot/%_gamesdatadir/XBlast-TNT/
cp musics-%verdata/* %buildroot/%_gamesdatadir/XBlast-TNT/sounds/

%files
%_gamesdatadir/XBlast-TNT/*

%changelog
* Tue Dec 18 2007 Fr. Br. George <george@altlinux.ru> 2.10.3-alt1
- Initial build as separate package from various sources

* Sat Jan 29 2005 Fr. Br. George <george@altlinux.ru> 2.10.0-alt1
- Totally new branch XBlast-TNT, initial ALT build

* Fri Oct 31 2003 Fr. Br. George <george@altlinux.ru> 2.6.1-alt1
- ALT Linux port

