%define rev 81693aec
%define packname megaglest
Name: megaglest-data
Version: 3.9.0
Release: alt1.%rev
Summary: Glest is a project for making a free 3d real-time customizable strategy game
License: GPL
Group: Games/Strategy
Url: http://megaglest.sourceforge.net
Packager: Andrew Clark <andyc@altlinux.org>
Source: %name.tar.bz2

BuildArch: noarch

%description
Glest is a project for making a free 3d real-time customizable
strategy game. Current version is fully playable, includes
single player game against CPU controlled players, two factions
with their corresponding tech trees, units, buildings and some maps.

%prep
%setup -q -n %name

sed -i 's#DataPath=$APPLICATIONDATAPATH#DataPath=/usr/share/games/megaglest/#g' glest.ini
sed -i 's#LogPath=$APPDATA\\megaglest\\#LogPath=$HOME#g' glest.ini
sed -i 's#UserData_Root=$APPDATA\\megaglest\\#UserData_Root=$HOME\/megaglest/#g' glest.ini


%install
mkdir -p %buildroot%_gamesdatadir/%packname
mv * %buildroot%_gamesdatadir/%packname/

%files
%_gamesdatadir/%packname

%changelog
* Sat Jan 11 2014 Andrew Clark <andyc@altlinux.org> 3.9.0-alt1.81693aec
- version update to 3.9.0-alt1.81693aec

* Thu Nov 1 2012 Andrew Clark <andyc@altlinux.org> 3.6.0.3-alt2.svn3813
- version update to 3.6.0.3-alt2.svn3813

* Wed Oct 31 2012 Andrew Clark <andyc@altlinux.org> 3.6.0.3-alt1.svn3813
- version update to 3.6.0.3-alt1.svn3813

* Sat Mar 24 2012 Andrew Clark <andyc@altlinux.org> 3.6.0.3-alt1.svn3171
- version update to 3.6.0.3-alt1.svn3171

* Mon Dec 26 2011 Andrew Clark <andyc@altlinux.org> 3.6.0.2-alt1.svn3030
- version update to 3.6.0.2-alt1.svn3030

* Sat Dec 24 2011 Andrew Clark <andyc@altlinux.org> 3.6.0.2-alt1.svn3026
- version update to 3.6.0.2-alt1.svn3026

* Mon Sep 26 2011 Andrew Clark <andyc@altlinux.org> 3.5.2-alt1.svn2565
- version update to 3.5.2-alt1.svn2565

* Wed Jul 6 2011 Andrew Clark <andyc@altlinux.org> 3.5.2-alt1.svn2449
- version update to 3.5.2-alt1.svn2449

* Fri Jun 3 2011 Andrew Clark <andyc@altlinux.org> 3.5.2-alt1.svn2324
- version update to 3.5.2-alt1.svn2324

* Sun Apr 24 2011 Andrew Clark <andyc@altlinux.org> 3.5.0-alt1.svn2150
- version update to 3.5.0-alt1.svn2150

* Sat Feb 12 2011 Andrew Clark <andyc@altlinux.org> 3.4.0-alt1.svn1738
- version update to 3.4.0-alt1.svn1738

* Sun Oct 31 2010 Andrew Clark <andyc@altlinux.org> 3.3.7.2-alt1.svn1202
- version update to 3.3.7.2-alt1.svn1202

* Wed Jun 30 2010 Andrew Clark <andyc@altlinux.org> 3.3.5-alt1.svn588
- version update to 3.3.5-alt1.svn588

* Sat Jun 12 2010 Andrew Clark <andyc@altlinux.org> 3.3.4-alt2.svn477
- spec cleanup

* Tue Jun 8 2010 Andrew Clark <andyc@altlinux.org> 3.3.4-alt1.svn477
- version update to 3.3.4-alt1.svn477

* Wed Feb 17 2010 Andrew Clark <andyc@altlinux.org> 3.3.1-alt1.svn110
- initial build for ALT.

