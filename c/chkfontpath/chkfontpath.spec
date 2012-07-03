Name: chkfontpath
Version: 2.0.2
Release: alt1

Summary: Simple interface for editing the font path for the X font server
License: GPL
Group: System/Configuration/Other
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: %name-%version.tar

%description
This is a simple batch mode program for configuring the directories
in the X font server's path.  It is mostly intended to be used in %%post
scripts of RPM packages when fonts are added or removed, but it may be
useful as a stand-alone utility in some instances.

%prep
%setup -q

%build
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_sbindir/*
%_mandir/man?/*

%changelog
* Sat Apr 07 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.2-alt1
- Fixed compilation warnings.

* Fri Nov 22 2002 Kachalov Anton <mouse@altlinux.ru> 2.0.1-alt1
- Fixed ALT#1050.

* Sun Jan 27 2002 Dmitry V. Levin <ldv@fandra.org> 2.0.0-alt0.1
- Rewritten.

* Sun Dec 30 2001 Ivan Zakharyaschev <imz@altlinux.ru> 1.9.5-alt1
- new version
- patch redone

* Mon Jan 15 2001 Dmitry V. Levin <ldv@fandra.org> 1.7.2-ipl1mdk
- Rewritten "unscaled" patch.
- 1.7.2 (FHS patch moved to source).
- RE adaptions.

* Wed Oct 18 2000 dam's <damien@mandrakesoft.com> 1.7-4mdk
- added patch0 (chkfontpath-1.7-unscaled.patch) to be able to add an unscaled fonts dir.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.7-3mdk
- automatically added BuildRequires

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.7-2mdk
- BM, macros

* Fri Mar 31 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.7-1mdk
- 1.7
- group fix.

* Sun Mar  5 2000 Pixel <pixel@mandrakesoft.com> 1.5-3mdk
- add require pidof

* Mon Sep 14 1999 Sean P. Kane <kane@ca.metsci.com>
- Merged Mandrake 1.4.1 and Redhat 1.5 RPMS.
- Removed Patch

* Fri Aug 15 1999 Preston Brown <pbrown@redhat.com>
- fixed up basename
- default to list, not help
- if trailing slash '/' is appended to paths given, strip it off

* Thu May 22 1999 Alexei Mikhalev <leha@linuxfan.com>
- added "first" option. Fixed first line deletion.

* Thu Apr 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Wed Apr 14 1999 Preston Brown <pbrown@redhat.com>
- preserve permissions on config file

* Thu Apr 07 1999 Preston Brown <pbrown@redhat.com>
- if /proc isn't mounted, don't do a killall

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- don't use psmisc, use pidof from SysVinit

* Fri Mar 12 1999 Preston Brown <pbrown@redhat.com>
- made psmisc a requirement.

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- added "quiet" option.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- injected new group / description.

* Tue Feb 16 1999 Preston Brown <pbrown@redhat.com>
- important fix - kill font server with USR1 instead of HUP.

* Mon Feb 15 1999 Preston Brown <pbrown@redhat.com>
- initial spec file
