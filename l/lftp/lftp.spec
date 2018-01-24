Name: lftp
Version: 4.8.3
Release: alt1

Summary: Sophisticated command line file transfer program
License: GPLv3+
Group: Networking/File transfer
Url: http://lftp.yar.ru/

# ftp://ftp.yars.free.net/pub/source/lftp/lftp-%version.tar.xz
Source: lftp-%version.tar
Source1: lftp-l.xpm
Source2: lftp-m.xpm
Source3: lftp-n.xpm
Source4: lftp.desktop
Source5: lftpget.1

# http://git.altlinux.org/gears/l/lftp.git
Patch: lftp-%version-%release.patch

# Due to default pager.
Requires: less

# Automatically added by buildreq on Thu Jan 02 2003
BuildRequires: desktop-file-utils gcc-c++ libexpat-devel libncurses-devel libreadline-devel libssl-devel zlib-devel

%description
lftp is sophisticated file transfer program with command-line
interface.  It supports the FTP, HTTP, HTTPS, SFTP, FISH, and
BitTorrent protocols, advanced and obscure features of the protocols,
proxy servers, automatic retries on non-fatal errors and timeouts,
continuation of interrupted file transfers, mirroring, transfer rate
throttling, multiple connections and background jobs, shell-like
command syntax and comprehensive scripting, command-line editing
(via the GNU Readline library), context-sensitive command completion,
command history, and a lot more.

%prep
%setup
%patch -p1
sed -i 's/curses\.h term\.h/term\.h curses\.h/' m4/terminfo.m4
bzip2 -9k NEWS src/ChangeLog

%build
%def_with openssl
%def_with modules
export CXX=%__cxx
%autoreconf
%configure \
	%{subst_with openssl} \
	%{subst_with modules} \
	--with-pager='exec less' \
	--enable-packager-mode \
	#
%make_build

%install
%makeinstall_std MKDIR_P='mkdir -p'
%{?_with_modules:find %buildroot%_libdir/lftp/ -type f -name \*.la -delete}

install -pm644 %_sourcedir/lftpget.1 %buildroot%_man1dir/
install -pDm644 %_sourcedir/lftp-l.xpm %buildroot%_liconsdir/lftp.xpm
install -pDm644 %_sourcedir/lftp-m.xpm %buildroot%_miconsdir/lftp.xpm
install -pDm644 %_sourcedir/lftp-n.xpm %buildroot%_niconsdir/lftp.xpm

desktop-file-install --dir %buildroot%_desktopdir %_sourcedir/lftp.desktop

%find_lang %name
%set_verify_elf_method strict,rpath=normal
%add_findreq_skiplist %_datadir/lftp/convert-mozilla-cookies
%add_findreq_skiplist %_datadir/lftp/verify-file

%files -f %name.lang
%config(noreplace) %_sysconfdir/lftp.conf
%_bindir/*
%_libdir/liblftp*.so*
%{?_with_modules:%_libdir/lftp}
%_datadir/lftp
%_mandir/man?/*
%_desktopdir/lftp.desktop
%_liconsdir/*.xpm
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%doc src/ChangeLog.bz2 F* MIRRORS NEWS.bz2
%doc AUTHORS README.* THANKS TODO BUGS

%changelog
* Tue Jan 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.3-alt1
- Updated to upstream version 4.8.3.

* Mon Jan 18 2016 Dmitry V. Levin <ldv@altlinux.org> 4.6.5-alt1
- 4.6.4 -> 4.6.5.

* Thu Aug 20 2015 Dmitry V. Levin <ldv@altlinux.org> 4.6.4-alt1
- Updated to 4.6.4.

* Thu Nov 13 2014 Dmitry V. Levin <ldv@altlinux.org> 4.6.0-alt1
- Updated to 4.6.0.

* Sun Feb 16 2014 Dmitry V. Levin <ldv@altlinux.org> 4.4.15-alt1
- Updated to 4.4.15.

* Wed Dec 25 2013 Dmitry V. Levin <ldv@altlinux.org> 4.4.14-alt1
- Updated to 4.4.14.

* Fri Nov 22 2013 Dmitry V. Levin <ldv@altlinux.org> 4.4.11-alt1
- Updated to 4.4.11.

* Wed Oct 16 2013 Dmitry V. Levin <ldv@altlinux.org> 4.4.10-alt1
- Updated to 4.4.10.

* Wed Sep 18 2013 Dmitry V. Levin <ldv@altlinux.org> 4.4.9-alt1
- Updated to 4.4.9.

* Mon Jun 03 2013 Dmitry V. Levin <ldv@altlinux.org> 4.4.8-alt1
- Updated to 4.4.8.

* Mon Apr 08 2013 Dmitry V. Levin <ldv@altlinux.org> 4.4.5-alt1
- Updated to 4.4.5.

* Mon Mar 04 2013 Dmitry V. Levin <ldv@altlinux.org> 4.4.4-alt1
- Updated to 4.4.4.

* Wed Oct 03 2012 Dmitry V. Levin <ldv@altlinux.org> 4.4.0-alt1
- Updated to 4.4.0.

* Fri Aug 31 2012 Dmitry V. Levin <ldv@altlinux.org> 4.3.8-alt1
- Updated to 4.3.8.

* Mon May 21 2012 Dmitry V. Levin <ldv@altlinux.org> 4.3.6-alt2
- Fixed build with ld --no-copy-dt-needed-entries.

* Mon Apr 09 2012 Dmitry V. Levin <ldv@altlinux.org> 4.3.6-alt1
- Updated to 4.3.6.

* Wed Jan 25 2012 Dmitry V. Levin <ldv@altlinux.org> 4.3.5-alt1
- Updated to 4.3.5.

* Thu Jan 12 2012 Dmitry V. Levin <ldv@altlinux.org> 4.3.4-alt1
- Updated to 4.3.4.

* Sun Nov 06 2011 Dmitry V. Levin <ldv@altlinux.org> 4.3.3-alt1
- Updated to 4.3.3.

* Thu Sep 29 2011 Dmitry V. Levin <ldv@altlinux.org> 4.3.2-alt1
- Updated to 4.3.2.

* Fri Aug 19 2011 Dmitry V. Levin <ldv@altlinux.org> 4.3.1-alt1
- Updated to 4.3.1.

* Fri Apr 29 2011 Dmitry V. Levin <ldv@altlinux.org> 4.2.3-alt1
- Updated to 4.2.3.

* Tue Apr 05 2011 Dmitry V. Levin <ldv@altlinux.org> 4.2.1-alt1
- Updated to 4.2.1.

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1.1
- NMU: converted debian menu to freedesktop

* Fri Dec 03 2010 Dmitry V. Levin <ldv@altlinux.org> 4.1.1-alt1
- Updated to 4.1.1.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 4.0.10-alt2
- Rebuilt with libssl.so.10.

* Fri Sep 03 2010 Dmitry V. Levin <ldv@altlinux.org> 4.0.10-alt1
- Updated to 4.0.10.

* Thu Jul 29 2010 Dmitry V. Levin <ldv@altlinux.org> 4.0.9-alt1
- Updated to 4.0.9.

* Thu May 20 2010 Dmitry V. Levin <ldv@altlinux.org> 4.0.7-alt1
- Updated to 4.0.7.

* Tue Jun 02 2009 Dmitry V. Levin <ldv@altlinux.org> 3.7.14-alt1
- Updated to 3.7.14 (closes: #17901).

* Wed Dec 03 2008 Dmitry V. Levin <ldv@altlinux.org> 3.7.6-alt1
- Updated to 3.7.6.

* Wed Sep 10 2008 Dmitry V. Levin <ldv@altlinux.org> 3.7.4-alt1
- Updated to 3.7.4.

* Tue Mar 25 2008 Dmitry V. Levin <ldv@altlinux.org> 3.7.0-alt1
- Updated to 3.7.0.

* Sun Jan 27 2008 Dmitry V. Levin <ldv@altlinux.org> 3.6.2-alt1
- Updated to 3.6.2.

* Tue Sep 25 2007 Dmitry V. Levin <ldv@altlinux.org> 3.5.14-alt1
- Updated to 3.5.14.

* Mon Sep 24 2007 Dmitry V. Levin <ldv@altlinux.org> 3.5.10-alt2
- Changed back permissions of convert-netscape-cookies and
  verify-file plugins (#11512), but disabled requirements lookup
  for them.
- Added "cd.." alias (#11564).

* Fri Mar 30 2007 Dmitry V. Levin <ldv@altlinux.org> 3.5.10-alt1
- Updated to 3.5.10.

* Sun Mar 25 2007 Dmitry V. Levin <ldv@altlinux.org> 3.5.9-alt1
- Updated to 3.5.9.
- Relocated icons to new location.

* Fri Apr 14 2006 Dmitry V. Levin <ldv@altlinux.org> 3.4.4-alt1
- Updated to 3.4.4.
- Relocated pseudo libraries to plugin directory.

* Fri Dec 30 2005 Dmitry V. Levin <ldv@altlinux.org> 3.3.5-alt1
- Updated to 3.3.5.

* Tue Sep 27 2005 Dmitry V. Levin <ldv@altlinux.org> 3.3.0-alt1
- Updated to 3.3.0.
- Fixed tinfo support (closes #8056).

* Thu May 26 2005 Dmitry V. Levin <ldv@altlinux.org> 3.2.1-alt1
- Updated to 3.2.1.

* Tue Apr 26 2005 Dmitry V. Levin <ldv@altlinux.org> 3.1.3-alt1
- Updated to 3.1.3.

* Tue Apr 05 2005 Dmitry V. Levin <ldv@altlinux.org> 3.1.2-alt1
- Updated to 3.1.2.

* Thu Mar 24 2005 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt1
- Updated to 3.1.1.

* Wed Mar 02 2005 Dmitry V. Levin <ldv@altlinux.org> 3.1.0-alt1
- Updated to 3.1.0.

* Thu Dec 23 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.13-alt1
- Updated to 3.0.13.

* Tue Dec 07 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.12-alt1
- Updated to 3.0.12.

* Fri Nov 05 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.11-alt1
- Updated to 3.0.11.

* Wed Sep 22 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.9-alt1
- Updated to 3.0.9.

* Fri Aug 13 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.7-alt1
- Updated to 3.0.7.

* Mon Jun 14 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.6-alt1
- Updated to 3.0.6.

* Tue May 25 2004 Dmitry V. Levin <ldv@altlinux.org> 3.0.4-alt1
- Updated to 3.0.4.

* Wed May 19 2004 Alexey Morozov <morozov@altlinux.org> 3.0.3-alt1
- Updated to 3.0.3.

* Mon Jan 26 2004 Dmitry V. Levin <ldv@altlinux.org> 2.6.12-alt1
- Updated to 2.6.12.

* Sun Jan 04 2004 Dmitry V. Levin <ldv@altlinux.org> 2.6.11-alt1
- Updated to 2.6.11.

* Tue Dec 16 2003 Dmitry V. Levin <ldv@altlinux.org> 2.6.10-alt2
- Handle malformed HTTP server responses gracefully
  (Nalin Dahyabhai, RH).

* Fri Dec 12 2003 Dmitry V. Levin <ldv@altlinux.org> 2.6.10-alt1
- Updated to 2.6.10.
- Merged upstream patches: cvs-fixes, alt-configure.

* Mon Dec 08 2003 Dmitry V. Levin <ldv@altlinux.org> 2.6.9-alt2
- Fixed few buffer overflows (CAN-2003-0963).

* Thu Nov 27 2003 Dmitry V. Levin <ldv@altlinux.org> 2.6.9-alt1
- Updated to 2.6.9.
- Do not package .la files.
- Fixed build with recent autotools.

* Mon Jun 02 2003 Dmitry V. Levin <ldv@altlinux.org> 2.6.6-alt1
- Updated to 2.6.6.
- Reenabled modules support since it works again.
- Corrected package summary and description.

* Mon Mar 03 2003 Dmitry V. Levin <ldv@altlinux.org> 2.6.5-alt1
- Updated to 2.6.5.

* Thu Jan 02 2003 Dmitry V. Levin <ldv@altlinux.org> 2.6.4-alt1
- Updated to 2.6.4:
  + new settings net:socket-bind-ipv4 and net:socket-bind-ipv6
    to bind sockets to a specific address (useful to select a
    specific network interface to use);
  + now reget does not start transfer if not needed;
  + ssl:verify-certificate set to no by default;
  + fixed ~ handling in find and mirror.

* Thu Nov 21 2002 Dmitry V. Levin <ldv@altlinux.org> 2.6.3-alt1
- 2.6.3

* Mon Oct 28 2002 Dmitry V. Levin <ldv@altlinux.org> 2.6.2-alt2
- Changed default pager to less.

* Mon Sep 16 2002 Michael Shigorin <mike@altlinux.ru> 2.6.2-alt1
- 2.6.2
- minor spec cleanup

* Mon Aug 12 2002 Dmitry V. Levin <ldv@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri Jun 28 2002 Dmitry V. Levin <ldv@altlinux.org> 2.5.4-alt2
- Updated conf patch.
- Patched to link with libtinfo.

* Tue Jun 11 2002 Michael Shigorin <mike@altlinux.ru> 2.5.4-alt1
- 2.5.4
- lftp-2.3.8-owl-addr.diff is already rolled in.

* Fri May 24 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Thu Apr 18 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.1-alt1
- 2.5.1
- remove getopt patch

* Thu Feb 07 2002 Stanislav Ievlev <inger@altlinux.ru> 2.4.9-alt2
- Added patch from Owl (addrlen).

* Wed Feb 06 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.9-alt1
- 2.4.9

* Fri Dec 14 2001 Konstantin Timoshenko <kt@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Fri Nov 16 2001 Konstantin Timoshenko <kt@altlinux.ru> 2.4.7-alt1
- 2.4.7

* Tue Nov 06 2001 Konstantin Timoshenko <kt@altlinux.ru> 2.4.6-alt1
- 2.4.6
- Disable modules support (temporary fixes for bug)

* Mon Sep 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Tue Sep 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.3-alt2
- Rebuilt to get all modules.

* Thu Sep 06 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Mon Feb 19 2001 Kostya Timoshenko <kt@petr.kz> 2.3.8-ipl1mdk
- 2.3.8

* Tue Jan 23 2001 Kostya Timoshenko <kt@petr.kz>
- 2.3.7

* Wed Jan  3 2001 Kostya Timoshenko <kt@petr.kz>
- 2.3.6

* Tue Jan  2 2001 Kostya Timoshenko <kt@petr.kz>
- Build for RE

* Wed Dec 20 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.3.5-4mdk
- change the buildrequires back to readline-devel which is what this package
  is called now.

* Fri Dec  8 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.5-3mdk
- Add bz{/cat/more} support.

* Tue Nov 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.5-2mdk
- Change Buildrequires to the new lib policy.

* Sun Nov 26 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.5-1mdk
- insert longtitle.
- Reinsert the modules support.
- 2.3.5.

* Wed Nov 15 2000 Daouda Lo <daouda@mandrakesoft.com> 2.3.4-4mdk
- remove hardcoded path to binary in menu

* Thu Nov 02 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.4-3mdk
- Rebuild for last gcc.

* Wed Oct 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.4-2mdk
- Disable modules support (temporary fixes for bug).

* Sun Oct 15 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.4-1mdk
- 2.3.4.

* Tue Oct 10 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.3-2mdk
- Don't compile with a custom readline take it from our tree.

* Mon Oct  2 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.3-1mdk
- 2.3.3.

* Fri Sep 29 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.0-3mdk
- Correct icons (#458, #459).

* Sat Sep 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.0-2mdk
- Fix queue command.

* Fri Sep 22 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.0-1mdk
- Fix compilation with last libtool.
- 2.3.0.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.2.5-2mdk
- automatically added BuildRequires

* Wed Aug 02 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2.5-1mdk
- new release
- use righ macros

* Tue Jul 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.4-3mdk
- Compile modules with -lc.

* Wed Jul 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.4-2mdk
- Rebuild due to a bad macros.

* Tue Jul 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.4-1mdk
- More macros.
- BM.
- 2.2.4.

* Fri Jun 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.3-1mdk
- 2.2.3.
- Use find_lang and mandir macros.

* Mon Apr  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.0-2mdk
- Fix menu icon.

* Wed Mar 29 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.0-1mdk
- Add menu entry.
- Add lftpget.1 man page from debian package.
- 2.2.0 (using 2.2.0a in fact).

* Mon Mar 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.10-1mdk
- 2.1.10.
- Update groups.

* Tue Feb 22 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.9-2mdk
- Include src/ChangeLog not ChangeLog (outdated).
- 2.1.9.

* Sun Feb 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.8-1mdk
- 2.1.8.

* Wed Feb 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.7-1mdk
- 2.1.7.

* Tue Jan 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.6-1mdk
- 2.1.6.
- use %configure.

* Sun Nov 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Last cvs version.
- Fix completion on directory.
- more alias.

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.1.4.

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.1.3.

* Wed Oct 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.1.2

* Wed Sep 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.1.0

* Wed Sep 22 1999 Daouda Lo <daouda@mandrakesoft.com>
- 2.0.5

* Wed Aug 18 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 2.0.4
- add the url
- fix a bug in spec that preventing from including locales
- fix permissions (now this could be builded as non root)

* Tue Jul 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.0.3 finale.

* Thu Jul 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- pre2.0.3-990722 from CVS.
- enable --with-modules.
- Relifting of Spec files.

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Set passive by default (special Pixel ;-)).
- 2.0.1.

* Mon Jun 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.0.0
