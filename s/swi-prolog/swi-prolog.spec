Name: swi-prolog
Version: 5.6.15
Release: alt1.qa1

Summary: Prolog interpreter and compiler
License: LGPL/GPL
Group: Development/Other

URL: http://www.swi-prolog.org
Source: pl-%version.tar.bz2

# Added by buildreq2 on Sun Jul 02 2006
BuildRequires: libgmp-devel libncursesw-devel libreadline-devel tetex-context tetex-latex

%define plbase %_libdir/swi-prolog

# not perl
%add_findreq_skiplist %plbase/*.pl
%add_findprov_skiplist %plbase/*.pl

%description
Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage-collector, stack-expandor, C-interface, GNU-readline and GNU-Emacs
interface, very fast compiler.

%prep
%setup -q -n pl-%version

%build
cd ./src
export ac_cv_prog_ETAGS=ctags
%configure --enable-shared
%make_build PLBASE=%plbase LDLFAGS=

cd ../man
sed -i 1s:/usr/local/bin/perl:%_bindir/perl: doc2tex
sed -i- '/usepackage{times}/d' doc.doc
make manual.pdf PDF=manual.pdf

%install
cd ./src
%makeinstall PLBASE=%buildroot%plbase

mv %buildroot%plbase/lib/*/libpl.so.%version %buildroot%_libdir/
ln -s libpl.so.%version %buildroot%_libdir/libpl.so
rm -rv %buildroot%plbase/lib

rmdir %buildroot%plbase/man

%files
%doc ANNOUNCE ChangeLog LSM README man/manual.pdf
%_bindir/pl*
%_man1dir/pl*.1*
%_libdir/libpl.so.%version
%_libdir/libpl.so
%plbase/

%changelog
* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 5.6.15-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for swi-prolog
  * postun_ldconfig for swi-prolog
  * postclean-05-filetriggers for spec file

* Sun Jul 02 2006 Alexey Tourbin <at@altlinux.ru> 5.6.15-alt1
- 5.0.10 -> 5.6.15
- configured --enable-shared
- installed swi-prolog libraries under %plbase
- built and packaged manual.pdf

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 5.0.10-alt1.1
- Rebuilt with libreadline.so.5.

* Fri Jan 24 2003 Vitaly Lugovsky <vsl@altlinux.ru> 5.0.10-alt1
- 5.0.10

* Tue Nov 27 2001 Stanislav Ievlev <inger@altlinux.ru> 4.0.10-alt1
- 4.0.10

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Fri Oct 27 2000 Pixel <pixel@mandrakesoft.com> 3.4.1-1mdk
- new version

* Wed Aug 23 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-6mdk
- add packager field

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.3.6-5mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-4mdk
- BM

* Tue Jul 11 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-3mdk
- and pixel changed a few other things to stef's changes

* Mon Jul 10 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 3.3.6-2mdk
- makeinstall macro
- macroszifications

* Wed Jun  7 2000 Pixel <pixel@mandrakesoft.com> 3.3.6-1mdk
- change name to swi-prolog
- new version
- fix licence
- fix buildroot
- much cleanup

* Wed Jun  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.2.9-2mdk
- first package for Mandrake

* Thu Jul 29 1999 David Kuester <kuestler@zeta.org.au>
- New source build version 3.2.9
* Tue Jun 22 1999 David Kuester <kuestler@zeta.org.au>
- New source build version 3.2.8
- Split the single patch in two (emacs) and (powerpc)
* Sun Nov 15 1998 Justin Cormack <jpc1@doc.ic.ac.uk>
- added changelog
- various tidying up things
- adjusted so will build on all architectures
- previous packagers:
- David Kuestler <kuestler@zeta.org.au>
- Kjetil Wiekhorst Jørgensen <jorgens@zarhan.pvv.org>
- Adam P. Jenkins <ajenkins@cs.umass.
