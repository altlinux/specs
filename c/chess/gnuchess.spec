Name: chess
Version: 5.07
Release: alt3

%define real_name gnu%name

Summary: The GNU chess program
License: %gpl2plus
Group: Games/Boards
Packager: Egor Vyscrebentsov <evyscr@altlinux.org>

Source: ftp://ftp.gnu.org/gnu/chess/%real_name-%version.tar
Source1: book_1.00.pgn
Patch0: gnuchess-5.07-alt-gcc4.patch
Patch1: %real_name-5.07-alt-getline.patch

Provides: %real_name = %version
Obsoletes: %real_name

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Aug 04 2009
BuildRequires: flex libncurses-devel libreadline-devel

%description
The gnuchess package contains the GNU chess program.  By default, GNUchess
uses a curses text-based interface.  Alternatively, GNUchess can be used
in conjunction with the xboard user interface and the X Window System for
a graphical chessboard.

You should install the gnuchess package if you would like to play chess on
your computer.  You'll also need to install the curses package.  If you'd
like to use a graphical interface with GNUchess, you'll also need to
install the xboard package and the X Window System.

%prep
%setup -q -n %real_name-%version
%patch0 -p1
%patch1 -p2

%build
%configure
%make_build

#compile book
pushd src
./%real_name<<EOF
book add %SOURCE1
quit
EOF
popd

%install
mkdir -p %buildroot%_bindir
cd src
%make_install DESTDIR=%buildroot install
#install -pm755 gnuchessx $RPM_BUILD_ROOT%_bindir
install -d %buildroot%_gamesdatadir/%real_name
install -pm644 book.dat %buildroot%_gamesdatadir/%real_name

%files
%_bindir/*
%_datadir/games/%real_name

%changelog
* Tue Aug 04 2009 Egor Vyscrebentsov <evyscr@altlinux.org> 5.07-alt3
- new packager
- add Packager: tag
- renamed getline() into get_line()

* Tue May 16 2006 Stanislav Ievlev <inger@altlinux.org> 5.07-alt2
- fixed build with gcc4

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 5.07-alt1.1
- Rebuilt with libreadline.so.5.

* Tue Mar 02 2004 Stanislav Ievlev <inger@altlinux.org> 5.07-alt1
- 5.07, also book 1.01
  gnuchessx script now in upstream
- remove menu entry

* Fri Sep 12 2003 Stanislav Ievlev <inger@altlinux.ru> 5.06-alt1
- 5.06

* Fri Feb 28 2003 Stanislav Ievlev <inger@altlinux.ru> 5.05-alt1
- 5.05
- added book into distribution again

* Tue Feb 04 2003 Stanislav Ievlev <inger@altlinux.ru> 5.04-alt4
- fix menu entry (needs text)

* Tue Oct 15 2002 Stanislav Ievlev <inger@altlinux.ru> 5.04-alt3
- fixed paths

* Tue Sep 17 2002 Stanislav Ievlev <inger@altlinux.ru> 5.04-alt2
- rebuild with gcc3

* Thu Apr 05 2001 Stanislav Ievlev <inger@altlinux.ru> 5.02-alt1
- Upgrade to 5.02. Hack to make program workable.

* Fri Jan 05 2001 AEN <aen@logic.ru>
- adopted for RE

* Sat Sep 23 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 4.0.p180-5mdk
- BM
- macro's
- compress & strip files with spec helper
- use update_menus and clean_menus

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.0.pl80-4mdk
- automatically added BuildRequires

* Mon Apr 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 4.0.pl80-3mdk
- added menu files

* Thu Apr 06 2000 Christopher Molnar <molnarc@mandrakesoft.com> 4.0.pl80-2mdk
- changes in spec file for groups
- considered upgrading to version 5.00 (now renamed to chess-5.00)
- but this would have taken away some features (x, curses, etc).

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- update to 4.0pl80.
- provide chessprogram, don't require xboard.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Mon Jan 23 1999 Michael Maher <mike@redhat.com>
- changed group name

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- rebuilt for 6.0, cleaned up spec file.

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- BuildRoot'ed

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
