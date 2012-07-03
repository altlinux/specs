Name: libpopt
Version: 1.14
Release: alt6
Epoch: 1

%def_with apidocs

Summary: A C library for parsing command line parameters
License: MIT
Group: System/Libraries
Url: http://www.rpm5.org/

Source: popt.tar

Patch1: popt-1.14-alt-alloc-checks.patch
Patch2: popt-1.14-alt-context-checks.patch
Patch3: popt-1.13-alt-x-alloc.patch
Patch4: popt-1.14-alt-man.patch
Patch5: popt-1.14-alt-poptBadOption.patch
Patch6: popt-1.14-alt-doxygen.patch
Patch7: popt-1.14-alt-vers.patch

Provides: popt = %version-%release
Obsoletes: popt

%{?_with_apidocs:BuildPreReq: doxygen graphviz fonts-ttf-dejavu}

# Automatically added by buildreq on Thu May 01 2003
BuildRequires: glibc-devel-static

%package devel
Summary: Developement environment for the popt library
Group: Development/C
Provides: popt-devel = %version-%release
Obsoletes: popt-devel
Requires: %name = %epoch:%version-%release
Requires: glibc-devel

%package devel-static
Summary: Static popt library
Group: Development/C
Provides: popt-devel-static = %version-%release
Obsoletes: popt-devel-static
Requires: %name-devel = %epoch:%version-%release

%package doc
Summary: Development documentation for libpopt
Group: Development/C
BuildArch: noarch
Requires: %name-devel = %epoch:%version-%release

%description
Popt is a C library for parsing command line parameters.  Popt was
heavily influenced by the getopt() and getopt_long() functions, but it
improves on them by allowing more powerful argument expansion.  Popt
can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments.  Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

%description devel
This package contains developement library, include files and
documentation required for development of popt-based software.

%description devel-static
This package contains static library required for development of
statically linked popt-based software.

%description doc
This package contains developement documentation for libpopt.

%prep
%setup -q -n popt
%patch1 -p2
%patch2 -p2
#%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6 -p2
%patch7 -p2

%build
%add_optflags -DHAVE_MCHECK_H
touch config.rpath
gettextize --force --quiet
install -pv -m644 /usr/share/gettext/intl/Makevars* po/Makevars
autoreconf -fisv -I m4
%configure --disable-rpath %{subst_with apidocs}

%make_build
./testit.sh

%{?_with_apidocs:make doxygen}

%install
mkdir -p %buildroot/%_lib
%make_install install DESTDIR="%buildroot" usrlibdir=%_libdir

# Relocate shared libraries from %_libdir/ to /%_lib/.
for f in %buildroot%_libdir/*.so; do
	t=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
	[ -n "$t" ]
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%{?_with_apidocs:install -pm644 doxygen/man/man3/{popt.h,poptAlias,poptArg_u,poptContext_s,poptDone_s,poptItem_s,poptOption}.3 %buildroot%_man3dir/}
%define docdir %_docdir/popt-%version
mkdir -p %buildroot%docdir
install -pm644 README CHANGES *.ps %buildroot%docdir/
bzip2 -9 %buildroot%docdir/*.ps
%{?_with_apidocs:cp -a doxygen/html %buildroot%docdir/}

%find_lang popt

%files -f popt.lang
/%_lib/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_mandir/man?/*
%dir %docdir
%docdir/README
%docdir/CHANGES

%files devel-static
%_libdir/*.a

%files doc
%dir %docdir
%docdir/html
%docdir/*.ps.bz2

%changelog
* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1:1.14-alt6
- Rebuilt for debuginfo.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 1:1.14-alt5
- Rebuilt for soname set-versions.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.14-alt4
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Packaged -doc subpackage as noarch.

* Mon Sep 01 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.14-alt3
- Disabled POPT_fprintf/POPT_dgettext (closes: #16017).
- Removed _* symbols from export list.
- Fixed doxygen warnings.

* Fri Apr 25 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.14-alt2
- Moved development documentation to -doc subpackage.
- Require graphviz and fonts-ttf-dejavu for apidocs.

* Wed Apr 23 2008 Stanislav Ievlev <inger@altlinux.org> 1:1.14-alt1
- 1.14
  * drop patch alt-env-sgid (merged to upstream)
  * drop patch alt-shared (merged to upstream)
  * rediff patch alt-alloc-checks
  * rediff patch alt-context-checks
  * add patch alt-doxygen
  * skip patch alt-x-alloc

* Sun Feb 24 2008 Alex V. Myltsev <avm@altlinux.org> 1:1.13-alt1
- New version.

* Tue Jan 15 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt17
- Fixed build with fresh autotools.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt16
- Fixed potential buffer overflow in singleOptionHelp().

* Mon Apr 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt15
- Uncompressed tarball, cleaned up specfile.

* Tue Aug 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt14
- Restricted list of global symbols exported by the library.

* Thu Feb 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt13
- Fixed multilib (closes #4887).

* Fri May 21 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt12
- Changed poptBadOption() to return more appropriate value
  in case of execCommand() failure (#1928).

* Wed Apr 28 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt11
- Rebuilt with glibc-2.3.x.

* Fri Feb 27 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt10
- Fixed build with fresh autotools.

* Tue Nov 25 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt9
- Do not package .la files.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt8
- Explicitly use old libtool for build.

* Thu May 01 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt7
- Fixed environment issues.
- Packaged some doxygen documentation for popt,
  correct manpage issue mentioned in (#0001458).

* Thu Nov 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt6
- Fixed build with new gettext.
- Explicitly use old autoconf/automake for build.

* Tue Sep 10 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt5
- Fixed %name.la

* Mon Sep 02 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.7-alt4
- Updated %post/%postun scripts.
- Turned absolute symlinks into relative.
- Updated devel-static requirements.

* Mon Mar 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.7-alt3
- Synced with cvs snapshot 20020315 (minor fixes).

* Tue Sep 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.7-alt2
- Synced with cvs snapshot 20010925.

* Wed Sep 05 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.7-alt1
- Synced with cvs snapshot 20010905.
- Moved static library to devel-static subpackage.
- Added context sanity checks.
- Updated alloc sanity checks.
- Updated russian translations.

* Fri Feb 23 2001 Dmitry V. Levin <ldv@fandra.org> 1.7-ipl1mdk
- Synced with cvs.
- Wrapped memory allocation functions.
- Workaround for (argc <= 0) bug.
- Updated russian translation.

* Fri Sep 15 2000 Dmitry V. Levin <ldv@fandra.org> 1.7-ipl0.2mdk
- Added support for float/double args.

* Tue Aug 15 2000 Dmitry V. Levin <ldv@fandra.org> 1.7-ipl0.1mdk
- 1.7

* Sun Aug 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.6-ipl0.1mdk
- Initial revision (cvs snapshot, split from rpm package).
