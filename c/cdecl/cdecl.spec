Name: cdecl
Version: 2.5
Release: alt2
Epoch: 1

Summary: Programs for encoding and decoding C and C++ function declarations.
License: distributable
Group: Development/C
Url: ftp://ibiblio.org/pub/Linux/devel/lang/c
Packager: Damir Shayhutdinov <damir@altlinux.ru>

Source: %url/%name-%version.tar.bz2
Patch0: %name-2.5-include.patch
Patch1: %name-2.5-modernization.patch
Patch2: %name-2.5-fix-getline.patch
BuildPreReq: flex libreadline-devel

%description
The %name package includes the %name and c++decl utilities, which are
used to translate English to C or C++ function declarations and vice versa.

You should install the %name package if you intend to do C and/or C++
programming.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
perl -pi -e 's/^(INSTALL_DATA\s*=\s*).*$/$1\$(INSTALL) -m644/' Makefile

%build
%add_optflags -Wextra -Wno-unused -Werror
%make_build CFLAGS="$RPM_OPT_FLAGS -DUSE_READLINE"

%install
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_mandir/man1}
%make_install install BINDIR=$RPM_BUILD_ROOT%_bindir MANDIR=$RPM_BUILD_ROOT%_mandir/man1
ln -snf %name $RPM_BUILD_ROOT%_bindir/c++decl

%clean

%files
%_bindir/*
%_mandir/man?/*

%changelog
* Fri May 08 2009 Damir Shayhutdinov <damir@altlinux.ru> 1:2.5-alt2
- Fixed build with new glibc (getline name clash)

* Sat Feb 09 2008 Damir Shayhutdinov <damir@altlinux.ru> 1:2.5-alt1
- ipl16mdk -> alt1

* Sat May 20 2006 Damir Shayhutdinov <damir@altlinux.ru> 2.5-ipl15mdk
- Resurrected from orphaned.
- Updated BuildRequires.
- Updated to modern libreadline.

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.5-ipl14mdk
- RE adaptions.

* Thu Aug  3 2000 Dmitry V. Levin <ldv@fandra.org> 2.5-ipl13mdk
- FHSification.

* Tue Mar 28 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 2.5-12mdk
- change group

* Sun Nov 28 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- SMP build macro

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 9)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- built for glibc 2.1

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- built against readline lib w/ proper soname

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
