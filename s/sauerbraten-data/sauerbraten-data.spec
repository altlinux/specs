%define packname sauerbraten
Name: sauerbraten-data
Version: 20130404
Release: alt1
Summary: Sauerbraten is a free multiplayer/singleplayer FPS

Group: Games/Arcade
License: Zlib
Url: http://sauerbraten.org/
Source: %name.tar

BuildArch: noarch

%description
Cube 2: Sauerbraten is a free multiplayer/singleplayer
first person shooter, built as a major redesign of the
Cube FPS.

%prep
%setup -n %name

%install
mkdir -p %buildroot%_gamesdatadir/%packname
mv data/ %buildroot/%_gamesdatadir/%packname/
mv packages %buildroot/%_gamesdatadir/%packname/

%files
%_gamesdatadir/%packname

%changelog
* Mon Feb 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 20130404-alt1
- Updated to upstream version 2013.04.04.

* Fri Jan 2 2015 Andrew Clark <andyc@altlinux.org> 20130203-alt1.svn5065
- version update to 20130203-alt1.svn5065

* Sun Feb 3 2013 Andrew Clark <andyc@altlinux.org> 20130126-alt1.svn4781
- version update to 20130126-alt1.svn4781

* Thu Oct 4 2012 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn4252
- version update to 20100721-alt1.svn4252

* Fri Jan 6 2012 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3956
- version update to 20100721-alt1.svn3956

* Sun Sep 25 2011 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3711
- version update to 20100721-alt1.svn3711

* Sat Jun 4 2011 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3603
- version update to 20100721-alt1.svn3603

* Sun Feb 13 2011 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3443
- version update to 20100721-alt1.svn3443

* Sun Oct 10 2010 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3299
- version update to 20100721-alt1.svn3299

* Sat Jul 24 2010 Andrew Clark <andyc@altlinux.org> 20100721-alt1.svn3213
- version update to 20100721-alt1.svn3213

* Wed May 26 2010 Andrew Clark <andyc@altlinux.org> 20090619-alt3.2875
- version update to 20090619-alt3.svn2875

* Fri Mar 12 2010 Andrew Clark <andyc@altlinux.org> 20090619-alt3.2372
- version update to 20090619-alt3.svn2372

* Wed Dec 30 2009 Andrew Clark <andyc@altlinux.org> 20090619-alt3.2077
- version update to 20090619-alt3.svn2077

* Thu Oct 15 2009 Andrew Clark <andyc@altlinux.org> 20090619-alt3.1928
- version update to 20090619-alt3.svn1928
- data files are separeted into data package

* Mon Aug 31 2009 Andrew Clark <andyc@altlinux.org> 20090619-alt2
- Added CFLAGS and CXXOPTFLAGS. desktop file correction.

* Wed Aug  5 2009 Andrew Clark <andyc@altlinux.org> 20090619-alt1
- new version

* Mon Jun  8 2009 Andrew Clark <andyc@altlinux.org> 20090504-alt1
- initial build for ALT.

