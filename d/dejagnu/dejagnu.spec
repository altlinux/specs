Name: dejagnu
Version: 1.5.1
Release: alt0.3
Epoch: 1

Summary: A front end for testing other programs
License: GPLv3+
Group: Development/Other
Url: http://www.gnu.org/software/%name/
BuildArch: noarch

# git://git.altlinux.org/gears/d/dejagnu.git
Source: %name-%version-%release.tar

Requires: expect /dev/pts
BuildRequires: expect gcc-c++
%{?!_without_check:%{?!_disable_check:BuildRequires: screen /dev/pts}}

%description
DejaGnu is an Expect/Tcl based framework for testing other programs.
DejaGnu has several purposes: to make it easy to write tests for any
program; to allow you to write tests which will be portable to any
host or target where a program must be tested; and to standardize the
output format of all tests (making it easier to integrate the testing
into software development).

%prep
%setup -n %name-%version-%release

%build
%configure
%make_build MAKEINFOFLAGS=--no-split

%install
%makeinstall_std
find %buildroot%_datadir/%name -type f -name \*.exp -print0 |
	xargs -r0 chmod 644 --
%add_findreq_skiplist %_datadir/%name/libexec/config.guess

%check
[ -w /dev/ptmx ] || exit 0
# Dejagnu test suite also has to test reporting to user.  It needs a
# terminal for that.  That doesn't compute in mock.  Work around it by
# running the test under screen and communicating back to test runner
# via temporary file.  If you have better idea, we accept patches.
t=$(mktemp %name.XXXXXXXX)
SCREENDIR=$HOME/.screen \
screen -D -m sh -c '(make check RUNTESTFLAGS="RUNTEST=$PWD/runtest"; echo $?) >'$t
r=$(tail -n1 $t)
cat $t
rm $t
exit $r

%files
%_bindir/*
%_datadir/%name
%_includedir/*
%_infodir/*
%_mandir/man?/*
%doc NEWS README AUTHORS ChangeLog

%changelog
* Wed Apr 11 2012 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.1-alt0.3
- Added /dev/pts to requirements.

* Tue Apr 10 2012 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.1-alt0.2
- Updated to v1.5-20-gdbd264c.
- Packaged %_datadir/%name/libexec/config.guess file.

* Fri Dec 02 2011 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.1-alt0.1
- Updated to v1.5-15-g6a76be5.
- Fixed %%check for new screen.

* Thu Sep 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.4-alt3
- Imported fixes from FC dejagnu-1.4.4-15 package.
- Removed obsolete %%install_info/%%uninstall_info calls.
- Unpackaged %_datadir/%name/config.guess.
- Fixed test suite invocation.

* Thu Feb 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.4-alt2
- Updated build dependencies.

* Wed Jan 05 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.4-alt1
- Adopted for ALT Linux.
- Build and install texinfo documentation.

* Mon Nov  8 2004 Jakub Jelinek <jakub@redhat.com> 1:1.4.4-3
- add URL (#138280)

* Mon Sep 27 2004 Warren Togami <wtogami@redhat.com> 1:1.4.4-2
- remove INSTALL & redundant copies of overview

* Tue Aug  3 2004 Jakub Jelinek <jakub@redhat.com> 1:1.4.4-1
- update to 1.4.4
- run make check during rpm build

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec 30 2002 Karsten Hopp <karsten@redhat.de> 1:1.4.2-9
- more missing BuildRequires

* Tue Dec 17 2002 Karsten Hopp <karsten@redhat.de> 1:1.4.2-8
- Add jadetex Buildrequires

* Wed Nov 27 2002 Tim Powers <timp@redhat.com> 1:1.4.2-7
- include dejagnu.h
- move %%{_libexecdir}/config.guess into %%{_datadir}/dejagnu
- include overview docs (bug #59095)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Apr 29 2002 Jakub Jelinek <jakub@redhat.com> 1.4.2-4
- fix makefile style variable passing (#63984)

* Thu Feb 28 2002 Jakub Jelinek <jakub@redhat.com> 1.4.2-3
- rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Nov 28 2001 Jakub Jelinek <jakub@redhat.com> 1.4.2-1
- update to 1.4.2, mainly so that it can be built with gcc3+

* Fri Sep  7 2001 Jakub Jelinek <jakub@redhat.com> 1.4.1-3
- make it noarch again

* Wed Aug 29 2001 Jakub Jelinek <jakub@redhat.com>
- fix a typo (#52404)

* Thu Jun 28 2001 Tim Powers <timp@redhat.com>
- rebuilt for the distro

* Tue Feb 27 2001 Tim Powers <timp@redhat.com>
- minor modifications to the spec file. Built for Powertools.
- added Epoch

* Wed Feb 21 2001 Rob Savoye <rob@welcomehome.org>
- Fixed Requires line, and changed the URL to the new ftp site.

* Sun Oct 31 1999 Rob Savoye <rob@welcomehome.org>
- updated to the latest snapshot
- added doc files
- added the site.exp config file

* Mon Jul 12 1999 Tim Powers <timp@redhat.com>
- updated to 19990628
- updated patches as needed
- added %%defattr in files section

* Wed Mar 10 1999 Jeff Johnson <jbj@redhat.com>
- add alpha expect patch (#989)
- use %%configure

* Thu Dec 17 1998 Jeff Johnson <jbj@redhat.com>
- Update to 19981215.

* Thu Nov 12 1998 Jeff Johnson <jbj@redhat.com>
- Update to 1998-10-29.

* Wed Jul  8 1998 Jeff Johnson <jbj@redhat.com>
- Update to 1998-05-28.

* Sun Feb  1 1998 Jeff Johnson <jbj@jbj.org>
- Create.

