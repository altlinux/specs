Name: glest-data
Version: 3.1.2
Release: alt1

Packager: Damir Shayhutdinov <damir@altlinux.ru>

Summary: Glest is a project for making a free 3d real-time customizable strategy game.
URL: http://www.glest.org

License: GPL
Group: Games/Strategy

Source: glest_data_%version.zip
Source2: russian.lng
Requires: glest = %version 

BuildRequires: unzip
BuildArch: noarch

%description
Glest is a project for making a free 3d real-time customizable strategy game.
Current version is fully playable, includes single player game against CPU 
controlled players, two factions with their corresponding tech trees, units, 
buildings and some maps.

%prep
%setup -q -n glest_game

%install
mkdir -p %buildroot%_gamesdatadir/glest

cp -Rv . %buildroot%_gamesdatadir/glest

rm -f %buildroot%_gamesdatadir/glest/glest.log
rm -f %buildroot%_gamesdatadir/glest/glest.ini

install -pm644 %SOURCE2 %buildroot%_gamesdatadir/glest/data/lang/russian.lng

%files
%_gamesdatadir/glest/*

%changelog
* Sun Aug 31 2008 Damir Shayhutdinov <damir@altlinux.ru> 3.1.2-alt1
- 3.1.2

* Fri Dec 01 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Fri Sep 09 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.1.0-alt1
- Initial build for Sisyphus.

