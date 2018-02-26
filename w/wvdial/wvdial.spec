Name: wvdial
Version: 1.61
Release: alt3.git20090513

Summary: A heuristic autodialer for PPP connections
License: LGPL
Group: Networking/Remote access
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

URL: http://alumnit.ca/wiki/index.php?page=WvDial
# git pull git://github.com/wlach/wvdial.git master:upstream
Source: %name-%version.tar.gz
Patch: wvdial-1.61-LIBS_ATDP.patch

# Added by buildreq2 on Sun May 01 2005
BuildRequires: gcc-c++
BuildRequires: libwvstreams-devel-static libuniconf-devel

%description
WvDial automatically locates and configures modems and can log into
almost any ISP's server without special configuration. You need to
input the username, password, and phone number, and then WvDial will
negotiate the PPP connection using any mechanism needed.

%prep
%setup
%patch -p0

%build
%configure
%make_build VERBOSE=1 CFLAGS="%optflags"

%install
%makeinstall \
	PREFIX=%buildroot%_prefix \
	PPPDIR=%buildroot%_sysconfdir/ppp/peers \
	BINDIR=%buildroot%_bindir \
	MANDIR=%buildroot%_mandir \
	install

%files
%_bindir/%name
%_bindir/wvdialconf
%_man1dir/%name.*
%_man1dir/wvdialconf.*
%_man5dir/%name.conf.*
%attr(640,root,uucp) %config(noreplace) %_sysconfdir/ppp/peers/%name
%attr(640,root,uucp) %config(noreplace) %_sysconfdir/ppp/peers/%name-pipe
%doc CHANGES FAQ MENUS README TODO

%changelog
* Wed May 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.61-alt3.git20090513
- Rebuild with gcc 4.4

* Thu Mar 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.61-alt2.git20090319
- reform directory structure (pull from upstream)
- change attributes of %%_sysconfdir/ppp/peers/%%name and
	%%_sysconfdir/ppp/peers/%%name-pipe for run %%name by members of uucp group
	(this works if root call 'control ppp uucp' before using wvdial)

* Mon Jan 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.61-alt1
- Get up from orphaned; version 1.61

* Tue Nov 15 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.54.0-alt3.1
- rebuild with libgsf-1.so.113 .

* Sun May 01 2005 Alexey Tourbin <at@altlinux.ru> 1.54.0-alt3
- rebuilt against wvstreams-4.0

* Fri Mar 04 2005 Alexey Tourbin <at@altlinux.ru> 1.54.0-alt2
- rebuilt against wvstreams-3.75 and libstdc++3.4

* Wed Feb 11 2004 Alexey Tourbin <at@altlinux.ru> 1.54.0-alt1
- 1.53 -> 1.54.0, maintainer change
- build against wvstreams-3.74.0
- mdk-bad_analyse.patch: fix unitialized and unneeded buffer in analyse_line()
- requires ppp

* Mon Oct 21 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.53-alt1
- 1.53

* Tue Oct 16 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.42-alt3
- Changes to new /var/lock/serial scheme
- Some spec cleanups
- Fixed %%patch0 - removed "-g" option

* Tue Jun 05 2001 Sergey V Turchin <zerg@altlinux.ru> 1.42-alt2
- new version

* Sun Mar  7 2001 Mikhail Zabaluev <zabaluev@parascript.com> 1.41-ipl7mdk
- Added patch to compile with glibc-2.2.2

* Sun Feb 18 2001 AEN <aen@logic.ru>
- group name fixed

* Mon Dec 11 2000 AEN <aen@logic.ru>
- RE adaptations
- ATDP by default now

* Mon Aug 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- Merge in latest -libs patch from rp3.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul  2 2000 Jakub Jelinek <jakub@redhat.com>
- Rebuild with new C++

* Sat Jun 17 2000 Bill Nottingham <notting@redhat.com>
- add %%defattr

* Fri Jun 16 2000 Nalin Dahyabhai <nalin@redhat.com>
- Merge in latest -libs patch from rp3.

* Sun Jun  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- FHS fixes.

* Fri May  5 2000 Bill Nottingham <notting@redhat.com>
- fix build with more strict c++ compiler

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Fri Jan 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- sync up to copy in rp3's CVS repository for consistency, except for
  changes to Makefiles

* Thu Jan 13 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.41, backing out patches that are now in mainline source

* Sat Sep 18 1999 Michael K. Johnson <johnsonm@redhat.com>
- improved the speed up dialing patch
- improved the inheritance patch

* Fri Sep 17 1999 Michael K. Johnson <johnsonm@redhat.com>
- added explicit inheritance to wvdial.conf
- speed up dialing

* Mon Sep 13 1999 Michael K. Johnson <johnsonm@redhat.com>
- improved the chat mode fix to allow specifying the remotename
  so that multiple wvdial instances can't step on each other.

* Fri Sep 10 1999 Michael K. Johnson <johnsonm@redhat.com>
- chat mode fix to make CHAP/PAP work with chat mode

* Mon Aug 02 1999 Michael K. Johnson <johnsonm@redhat.com>
- Packaged 1.40

* Wed Jul 28 1999 Michael K. Johnson <johnsonm@redhat.com>
- Initial Red Hat package
