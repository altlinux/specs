%define origname assaultcube
Name: assaultcube-data
Version: 1.1.0.4
Release: alt1.svn6772
Summary: Free first-person-shooter based on the game Cube

Group: Games/Arcade
License: Creative Commons
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://assault.cubers.net/
Source: %name.tar.bz2

BuildArch: noarch

%description
AssaultCube,formerly ActionCube, is a free first-person-shooter based on
the game Cube. Set in a realistic looking environment, as far as that's
possible with this engine, while gameplay stays fast and arcade. This
game is all about team oriented multiplayer fun.

%prep
%setup -q -n %name

%install
mkdir -p %buildroot%_gamesdatadir/%origname/

mv %_builddir/%name/config %buildroot/%_gamesdatadir/%origname/
mv %_builddir/%name/bot/ %buildroot/%_gamesdatadir/%origname/
mv %_builddir/%name/packages %buildroot/%_gamesdatadir/%origname/

%files 
%_gamesdatadir/%origname

%changelog
* Sun Mar 25 2012 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn6772
- version update to 1.1.0.4-alt1.svn6772

* Fri Jan 6 2012 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn6746
- version update to 1.1.0.4-alt1.svn6746

* Sat Sep 24 2011 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn6656
- version update to 1.1.0.4-alt1.svn6656

* Sat Jun 4 2011 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn6490
- version update to 1.1.0.4-alt1.svn6490

* Fri Jan 7 2011 Andrew Clark <andyc@altlinux.org> 1.1.0.4-alt1.svn5994
- version update to 1.1.0.4-alt1.svn5994

* Sun Oct 10 2010 Andrew Clark <andyc@altlinux.org> 1.1.0.2-alt1.svn5740
- version update to 1.1.0.2-alt1.svn5740

* Sat Aug 14 2010 Andrew Clark <andyc@altlinux.org> 1.1.0.1-alt1.svn5613
- version update to 1.1.0.1-alt1.svn5613

* Wed May 26 2010 Andrew Clark <andyc@altlinux.org> 1.0.4-alt3.svn5057
- version update to 1.0.4-alt3.svn5057

* Mon Apr 5 2010 Andrew Clark <andyc@altlinux.org> 1.0.4-alt3.svn4799
- version update to 1.0.4-alt3.svn4799

* Fri Mar 12 2010 Andrew Clark <andyc@altlinux.org> 1.0.4-alt3.svn4788
- version update to 1.0.4-alt3.svn4788

* Wed Dec 30 2009 Andrew Clark <andyc@altlinux.org> 1.0.4-alt3.svn4746
- version update to 1.0.4-alt3.svn4746

* Sun Oct 18 2009 Andrew Clark <andyc@altlinux.org> 1.0.4-alt3.svn4660
- version update to 1.0.4-alt3.svn4660
- data files are separeted into data package

* Mon Aug 31 2009 Andrew Clark <andyc@altlinux.org> 1.0.4-alt2
- Added CFLAGS and CXXOPTFLAGS. desktop file correction.

* Sun Aug  2 2009 Andrew Clark <andyc@altlinux.org> 1.0.4-alt1
- new version.

* Mon Jun  9 2009 Andrew Clark <andyc@altlinux.org> 1.0.2-alt1
- initial build for ALT.

