%define rev svn864
%define origname vdrift
Name: vdrift-data
Version: 20100630
Release: alt1.%rev
Summary: VDrift is a cross-platform, open source driving simulation game
Group: Games/Arcade
License: GPL
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://vdrift.net/
Source: %name.tar.bz2

BuildArch: noarch

%description
VDrift is a cross-platform, open source driving simulation made with
drift racing in mind. The driving physics engine was recently
re-written from scratch but was inspired and owes much to the
Vamos physics engine.

%prep
%setup -q -n %name

%install
mkdir -p %buildroot%_gamesdatadir/%origname/
mv %_builddir/%name/ %buildroot%_gamesdatadir/%origname/data/

%files
%_gamesdatadir/%origname

%changelog
* Thu Jul 7 2011 Andrew Clark <andyc@altlinux.org> 20100630-alt1.svn864
- version update to 20100630-alt1.svn864

* Sat Feb 19 2011 Andrew Clark <andyc@altlinux.org> 20100630-alt1.svn795
- version update to 20100630-alt1.svn795

* Fri Aug 6 2010 Andrew Clark <andyc@altlinux.org> 20100630-alt1.svn663
- version update to 20100630-alt1.svn663

* Mon Feb 1 2010 Andrew Clark <andyc@altlinux.org> 20090615-alt1.svn476
- version update to 20090615-alt1.svn476

* Wed Nov 25 2009 Andrew Clark <andyc@altlinux.org> 20090615-alt1
- initial build for ALT.

