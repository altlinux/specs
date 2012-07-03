Name: hugs98
Version: 20060921
Release: alt5

%define real_version Sep2006

Summary: Hugs 98 - A Haskell Interpreter

License: BSD-style
Group: Development/Haskell
Url: http://haskell.org/hugs/

Packager: Konstantin Baev <kipruss@altlinux.org>

Source: http://cvs.haskell.org/Hugs/downloads/2006-09/%name-plus-%real_version.tar.gz
Source1: haskell16.png
Source2: haskell32.png
Source3: haskell48.png

Provides: haskell
Requires: libreadline

# Automatically added by buildreq on Wed Nov 19 2008
BuildRequires: docbook-utils-print imake libGL-devel libX11-devel libfreeglut-devel libncurses-devel libopenal-devel libreadline-devel xorg-cf-files

%description
Hugs 98 is a functional programming system based on Haskell 98, the de facto
standard for non-strict functional programming languages. Hugs 98 provides an
almost complete implementation of Haskell 98, including:

* Lazy evaluation, higher order functions, and pattern matching.

* A wide range of built-in types, from characters to bignums, and lists to
  functions, with comprehensive facilities for defining new datatypes and type
  synonyms.

* An advanced polymorphic type system with type and constructor class
  overloading.

* All of the features of the Haskell 98 expression and pattern syntax including
  lambda, case, conditional and let expressions, list comprehensions,
  do-notation, operator sections, and wildcard, irrefutable and `as' patterns.

* An implementation of the Haskell 98 primitives for monadic I/O, with support
  for simple interactive programs, access to text files, handle-based I/O, and
  exception handling.

* An almost complete implementation of the Haskell module system. Hugs 98 also
  supports a number of advanced and experimental extensions including
  multi-parameter classes, extensible records, rank-2 polymorphism,
  existentials, scoped type variables, and restricted type synonyms.

%prep
%setup -q -n %name-plus-%real_version

%build
%configure
%make_build

%install
make DESTDIR=%buildroot install_all_but_docs
make -C docs DESTDIR=%buildroot install_man

# icons
mkdir -p %buildroot{%_niconsdir,%_liconsdir,%_miconsdir}
install -pD -m644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE3 %buildroot%_liconsdir/%name.png

# menu
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << __EOF__
[Desktop Entry]
Type=Application
Name=Hugs 98
GenericName=A Haskell Interpreter
Comment=Hugs 98 is a functional programming system based on Haskell 98
Icon=hugs98
Terminal=true
Categories=Development;IDE;
Exec=%_bindir/hugs
TryExec=hugs
__EOF__

%files
%doc Credits
%doc License
%doc Readme
%doc docs/ffi-notes.txt
%doc docs/libraries-notes.txt
%doc docs/machugs-notes.txt
%doc docs/server.html
%doc docs/server.tex
%doc docs/winhugs-notes.txt
%doc docs/users_guide/users_guide
%_man1dir/hugs.1.bz2
%_bindir/cpphs-hugs
%_bindir/ffihugs
%_bindir/hsc2hs-hugs
%_bindir/hugs
%_bindir/runhugs
%_libdir/hugs/demos
%_libdir/hugs/include
%_libdir/hugs/oldlib
%_libdir/hugs/packages
%_libdir/hugs/programs
%_datadir/hsc2hs-0.67/template-hsc.h
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Wed Nov 19 2008 Konstantin Baev <kipruss@altlinux.org> 20060921-alt5
- Fix repocop errors - remove update_menus macros
  update BuildRequires

* Fri Aug 15 2008 Konstantin Baev <kipruss@altlinux.org> 20060921-alt4
- Fixed .desktop - removed extension from icon name

* Fri Aug 01 2008 Konstantin Baev <kipruss@altlinux.org> 20060921-alt3
- Cleanup spec

* Mon Jun 23 2008 Konstantin Baev <kipruss@altlinux.org> 20060921-alt2
- Fixed spec and changed menu according freedesktop standards

* Wed Jun 11 2008 Konstantin Baev <kipruss@altlinux.org> 20060921-alt1
- New version 20060921 (with packages)

* Fri Nov 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 20031127-alt3.1
- Removed libelf-devel from build dependencies.

* Wed May 05 2004 Vitaly Lugovsky <vsl@altlinux.ru> 20031127-alt3
- Happy dependency dropped

* Sat Apr 10 2004 Vitaly Lugovsky <vsl@altlinux.ru> 20031127-alt2
- rebuild to avoid a Happy dependency

* Wed Dec 17 2003 Vitaly Lugovsky <vsl@altlinux.ru> 20031127-alt1
- New version

* Wed Nov 20 2002 Vitaly Lugovsky <vsl@altlinux.ru> 20021119-alt1
- New version
- location of system files changed (/usr/share/hugs -> /usr/lib/hugs)

* Mon Jun 24 2002 Vitaly Lugovsky <vsl@altlinux.ru> 20011215-alt1
- New version.

* Wed Jun 20 2001 Stanislav Ievlev <inger@altlinux.ru> 20010215-alt1
- version 20010215

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 2000229-8mdk
- fix for new glibc (backport from cvs)

* Thu Aug 31 2000 Pixel <pixel@mandrakesoft.com> 2000229-7mdk
- remove menu

* Wed Aug 23 2000 Pixel <pixel@mandrakesoft.com> 2000229-6mdk
- add packager field

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2000229-5mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 2000229-4mdk
- macroization, BM

* Tue Mar 28 2000 Pixel <pixel@mandrakesoft.com> 2000229-3mdk
- really add menu

* Mon Mar 27 2000 Pixel <pixel@mandrakesoft.com> 2000229-2mdk
- add menu

* Sat Mar 11 2000 Pixel <pixel@mandrakesoft.com> 2000229-1mdk
- new version

* Sun Nov 28 1999 Pixel <pixel@linux-mandrake.com>
- mandrake adaptation (and much cleanup)
