%define rev svn6200
%define packname bloodfrontier 
Name: bloodfrontier-data
Version: 0.84
Release: alt2.%rev
Summary: Blood Frontier is a free multiplayer/singleplayer FPS
Group: Games/Other
License: Zlib
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://www.bloodfrontier.com/
Source: %name.tar.gz

BuildArch: noarch

%description
The game is a single-player and multi-player first-person shooter,
built as a total conversion of Cube Engine 2, which lends itself
toward a balanced gameplay, completely at the control of map makers,
while maintaining a general theme of tactics and low gravity.

%prep
%setup -q -n %name

%install

mkdir -p %buildroot%_gamesdatadir/%packname/
mv %_builddir/%name/data/ %buildroot/%_gamesdatadir/%packname/

%files
%_gamesdatadir/%packname

%changelog
* Sat Jun 12 2010 Andrew Clark <andyc@altlinux.org> 0.84-alt2.svn6200
- spec cleanup

* Mon Jun 7 2010 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn6200
- version update to 0.84-alt1.svn6200
- added patch to fix game build

* Fri Mar 12 2010 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn5546
- version update to 0.84-alt1.svn5546

* Wed Dec 30 2009 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn5059
- version update to 0.84-alt1.svn5059

* Thu Dec  3 2009 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn4822
- version update to 0.84-alt1.svn4822

* Mon Sep 28 2009 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn4292
- version update to 0.84-alt1.svn4292
- data files are separeted into data package

* Wed Jun 17 2009 Andrew Clark <andyc@altlinux.org> 0.84-alt1.svn3914
- initial build for ALT.

