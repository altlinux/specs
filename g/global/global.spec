# TODO: see spec from PLD with separate packages
Name: global
Version: 6.6.1
Release: alt1

Summary: Source code tag system

Group: Text tools
License: GPL/BSD
Url: http://www.gnu.org/software/global

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://tamacom.com/global/global-%version.tar

#Patch: %name-%version-fix-DESTDIR.patch

# Automatically added by buildreq on Tue Apr 17 2012
# optimized out: emacs-base emacs-cedet-speedbar emacs-common emacs-ecb emacs23-cedet fontconfig libX11-locales libgdk-pixbuf libtinfo-devel libwayland-client libwayland-server
BuildRequires: ctags glibc-devel libltdl7-devel libncurses-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

%package htags
Summary: GNU GLOBAL - programs for making hypertext from source code
Group: Text tools
Requires: %name = %version-%release
Provides: gozilla-%version-%release
Provides: htags-%version-%release

%description htags
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

Htags makes hypertext from source code. The package also contains the
gozilla wrapper, which enforces Mozilla-based web browsers to display
source code in an elegant way. Htags can also work with a CVS
repository, which makes it more easy to navigate though the code over
the Web.

%prep
%setup
#patch -p2

%build
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -fr %buildroot%_datadir/emacs
rm -f %buildroot%_infodir/dir
rm -f %buildroot%_libdir/gtags/*.la

%files
%doc README THANKS LICENSE AUTHORS COPYING FAQ gtags.el
%_bindir/global
%_bindir/globash
%_bindir/gtags*
%_infodir/*
%_man1dir/global*
%_man1dir/globash*
%_man1dir/gtags*
%_man5dir/gtags*
%_datadir/gtags/
%_libdir/gtags/*.so

%files htags
%_bindir/htags
%_bindir/htags-server
%_bindir/gozilla
%_man1dir/htags*
%_man1dir/gozilla*

%changelog
* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 6.6.1-alt1
- new version 6.6.1 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 6.5.7-alt1
- new version 6.5.7 (with rpmrb script)

* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 6.5.6-alt1
- new version 6.5.6 (with rpmrb script)

* Thu Apr 21 2016 Vitaly Lipatov <lav@altlinux.ru> 6.5.2-alt1
- new version 6.5.2 (with rpmrb script)

* Sat Jan 30 2016 Vitaly Lipatov <lav@altlinux.ru> 6.5.1-alt1
- new version 6.5.1 (with rpmrb script)

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 6.3.3-alt1.1
- NMU: added BR: texinfo

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 6.3.3-alt1
- new version 6.3.3 (with rpmrb script)

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 6.2.12-alt1
- new version 6.2.12 (with rpmrb script)

* Wed Feb 26 2014 Vitaly Lipatov <lav@altlinux.ru> 6.2.9-alt1
- new version 6.2.9 (with rpmrb script)

* Thu Apr 18 2013 Vitaly Lipatov <lav@altlinux.ru> 6.2.8-alt1
- new version 6.2.8 (with rpmrb script)
- remove emacs build requires

* Tue Apr 17 2012 Vitaly Lipatov <lav@altlinux.ru> 6.2.2-alt1
- new version 6.2.2 (with rpmrb script)
- update buildreqs

* Sat Oct 02 2010 Vitaly Lipatov <lav@altlinux.ru> 5.9.2-alt1
- new version 5.9.2 (with rpmrb script)

* Fri Mar 19 2010 Vitaly Lipatov <lav@altlinux.ru> 5.8.1-alt1
- new version (5.8.1) import in git

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 5.7.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for global
  * postclean-05-filetriggers for spec file

* Sun May 17 2009 Vitaly Lipatov <lav@altlinux.ru> 5.7.5-alt1
- new version 5.7.5 (with rpmrb script)

* Fri Jan 30 2009 Vitaly Lipatov <lav@altlinux.ru> 5.7.4-alt1
- new version 5.7.4 (with rpmrb script)

* Sat Jun 28 2008 Vitaly Lipatov <lav@altlinux.ru> 5.7.1-alt1
- initial build for ALT Linux Sisyphus

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.4-2
- Autorebuild for GCC 4.3

* Sat Feb 24 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.4-1
- new version 5.4

* Sat Dec  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.3-1
- new version 5.3

* Wed Aug 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.2-1
- new version 5.2

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0-2
- Rebuild for FE6

* Sun Apr 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0-1
- new version 5.0

* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.8.7-3
- Rebuild for Fedora Extras 5

* Wed Oct  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.7-2
- Remove dir in %_datadir/info

* Sat Oct  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.7-1
- New Version 4.8.7

* Tue Jul  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.6-1
- New Version 4.8.6

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 4.8.4-4
- fix build with gcc4 (#156212)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 4.8.4-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Mar  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.4-1
- New Version 4.8.4

* Mon Dec 27 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.8.2-0.fdr.1
- New Version 4.8.2

* Sat Oct 23 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.8.1-0.fdr.1
- New Version 4.8.1

* Sat Jul 17 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.7.2-0.fdr.1
- New Version 4.7.2

* Fri Mar 19 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.7-0.fdr.1
- New Version 4.7

* Thu Nov 27 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:4.6.1-0.fdr.1
- First Fedora release

