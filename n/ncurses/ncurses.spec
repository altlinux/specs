Name: ncurses
Version: 5.7
Release: alt6

%define rootdatadir /lib

Summary: A CRT screen handling and optimization package
License: MIT
Group: System/Base
Url: http://invisible-island.net/%name/%name.html

# ftp://invisible-island.net/%name/%name-%version.tar.gz
Source: %name-%version.tar

Source100: %name-alt-terms.tar
Source101: %name-baseterms
Source102: %name-resetall.sh

Patch: %name-%version-alt.patch

Obsoletes: ncurses3
Requires: termutils-devel = %version-%release

# Automatically added by buildreq on Thu Nov 12 2009
BuildRequires: libgpm-devel libncurses-devel

#build parameters
%def_with utf8
%def_with shared
%def_with normal
%def_without debug
%def_without profile
%def_without cxx
%def_with gpm
%def_without ada
%def_without libtool

%package -n terminfo
Summary: Descriptions of common terminal types
Group: System/Base
Conflicts: %name < %version-%release
Conflicts: screen < 3.9.11-alt1

%package -n terminfo-extra
Summary: Additional terminal type definitions
Group: System/Base
BuildArch: noarch
Provides: %name-extraterms = %version
Obsoletes: %name-extraterms
PreReq: terminfo = %version-%release

%package -n libtinfo
Summary: A low-level terminfo shared library
Group: System/Libraries
PreReq: terminfo = %version-%release

%package -n libtinfo-devel
Summary: A low-level terminfo development library
Group: Development/C
Conflicts: libtermcap-devel < 0:2.0.8-ipl24mdk
# due to incorrect terminfo handling in old libgpm.
Conflicts: libgpm < 1.20.1-alt3.1
Requires: libtinfo = %version-%release

%package -n libtinfo-devel-static
Summary: A low-level terminfo static library
Group: Development/C
Requires: libtinfo-devel = %version-%release

%package -n termutils
Summary: Basic terminal utilities
Group: System/Base
Requires: terminfo = %version-%release
Requires: libtinfo = %version-%release
Requires: libtic = %version-%release
Provides: /bin/tput

%package -n termutils-devel
Summary: Additional terminal utilities
Group: Development/Other
Requires: termutils = %version-%release

%package -n libtic
Summary: A low-level terminfo manipulation shared library
Group: System/Libraries
Requires: libtinfo = %version-%release

%package -n libtic-devel
Summary: A low-level terminfo manipulation development library
Group: Development/C
Requires: libtic = %version-%release
Requires: libtinfo-devel = %version-%release

%package -n lib%name
Summary: A CRT screen handling and optimization libraries
Group: System/Libraries
Provides: libncurses.so.4 libncurses.so.3
PreReq: libtinfo = %version-%release
Conflicts: %name < %version-%release

%package -n lib%name-devel
Summary: Development files for applications which use %name
Group: Development/C
Requires: lib%name = %version-%release
Requires: libtinfo-devel = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel

%package -n lib%name-devel-static
Summary: Development static %name libraries
Group: Development/C
Requires: lib%name-devel = %version-%release
Requires: libtic-devel = %version-%release
Requires: libtinfo-devel-static = %version-%release
%if_with utf8
Requires: lib%{name}w-devel = %version-%release
%endif

%package -n lib%name++
Summary: C++ interface to lib%name
Group: System/Libraries
Requires: lib%name = %version-%release

%package -n lib%name++-devel
Summary: Development files for applications which use lib%name++
Group: Development/C++
Requires: lib%name++ = %version-%release
Requires: lib%name-devel = %version-%release

%package -n lib%name++-devel-static
Summary: Development static lib%name++ library
Group: Development/C++
Requires: lib%name++-devel = %version-%release
Requires: lib%name-devel-static = %version-%release

# UTF-8 extentions
%if_with utf8
%package -n lib%{name}w
Summary: A CRT screen handling and optimization libraries with wide character support
Group: System/Libraries
PreReq: libtinfo = %version-%release

%package -n lib%{name}w-devel
Summary: Development files for applications which use %name (widechar version)
Group: Development/C
Requires: lib%{name}w = %version-%release
Requires: lib%name-devel = %version-%release
%endif

%description
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

%description -n terminfo
Terminfo is a data base describing terminals, used by screen-oriented
programs and libraries such as curses(3X).  Terminfo describes terminals
by giving a set of capabilities which they have, by specifying how to
perform screen operations, and by specifying padding requirements and
initialization sequences.

This package contains what should be a reasonable subset of terminal
definitions, including: ansi, dumb, linux, rxvt, screen, sun, vt100,
vt102, vt220, vt52, and xterm.

%description -n terminfo-extra
Terminfo is a data base describing terminals, used by screen-oriented
programs and libraries such as curses(3X).  Terminfo describes terminals
by giving a set of capabilities which they have, by specifying how to
perform screen operations, and by specifying padding requirements and
initialization sequences.

This package contains all of the terminal definitions not found in
the terminfo package.  There are far too many to list here.

%description -n libtinfo
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains a low-level terminfo shared library.

%description -n libtinfo-devel
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains a low-level terminfo development library and include
files.

%description -n libtinfo-devel-static
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains a low-level terminfo static library.

%description -n libtic
lowlevel terminfo manipulation shared library

%description -n libtic-devel
lowlevel terminfo manipulation development library

%description -n termutils
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains basic terminal manipulation utilities.

%description -n termutils-devel
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains additional terminal manipulation utilities.

%description -n lib%name
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

%description -n lib%name-devel
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains include files for developing applications that use
the %name CRT screen handling and optimization package.

%description -n lib%name-devel-static
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains staic libraries for developing statically linked
applications that use the %name CRT screen handling and optimization package.

%description -n lib%name++
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains a c++ interface shared library.

%description -n lib%name++-devel
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains include files for developing applications that use
c++ interface to ncurses routines.

%description -n lib%name++-devel-static
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains staic library for developing statically linked
applications that use c++ interface to ncurses routines.

#UTF8 extentions
%if_with utf8
%description -n lib%{name}w
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.
This package contains a %name library with wide character support.

%description -n lib%{name}w-devel
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The %name (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

This package contains include files for developing applications that use
the %name CRT screen handling and optimization package (widechar version).
%endif

%prep
%setup -a100

%patch -p1

sed -i 's/EXTRA_LIBS="-ldl -lncurses $EXTRA_LIBS"/EXTRA_LIBS="$EXTRA_LIBS"/
s/SHLIB_LIST="-ldl $SHLIB_LIST"/SHLIB_LIST="-lgpm $SHLIB_LIST"/
s/TINFO_LIST="$SHLIB_LIST"/TINFO_LIST=/' ./configure


%build
%remove_optflags %optflags_notraceback %optflags_nocpp
%ifarch %ix86
%add_optflags -momit-leaf-frame-pointer
%endif


# Predefine these for configure:
export \
	ac_cv_func_mkstemp=yes \
	ac_cv_prog_AWK=gawk \
	ac_cv_prog_MAKE_LOWER_TAGS=yes \
	ac_cv_prog_MAKE_UPPER_TAGS=yes \
	ac_cv_prog_MAN=man \
	#

%define _configure_script ../configure
rm -rf build-classic build-utf8
mkdir -p build-classic build-utf8

# configure classic version
pushd build-classic
%configure \
	--program-transform-name= \
	%{subst_with shared} \
	%{subst_with normal} \
	%{subst_with debug} \
	%{subst_with profile} \
	%{subst_with cxx} \
	%{subst_with ada} \
	%{subst_with libtool} \
	%{subst_with gpm} \
	--without-dlsym \
	--with-termlib \
	--with-ospeed="unsigned int" \
	--with-terminfo-dirs="%rootdatadir/terminfo:%_datadir/terminfo" \
	--disable-termcap \
	--enable-const \
	--enable-hard-tabs \
	--enable-no-padding \
	--enable-sigwinch \
	--enable-echo \
	--enable-warnings \
	--disable-rpath \
	--disable-root-environ \
	--disable-home-terminfo \
	--with-chtype=long \
	#

popd # build-classic

# configure utf8 version
%if_with utf8
pushd build-utf8
%configure \
	--program-transform-name= \
	%{subst_with shared} \
	%{subst_with normal} \
	%{subst_with debug} \
	%{subst_with profile} \
	%{subst_with cxx} \
	%{subst_with ada} \
	%{subst_with libtool} \
	%{subst_with gpm} \
	--without-dlsym \
	--with-termlib=tinfo \
	--with-ticlib=tic \
	--with-ospeed="unsigned int" \
	--with-terminfo-dirs="%rootdatadir/terminfo:%_datadir/terminfo" \
	--disable-termcap \
	--enable-const \
	--enable-hard-tabs \
	--enable-no-padding \
	--enable-sigwinch \
	--enable-echo \
	--enable-warnings \
	--disable-rpath \
	--disable-root-environ \
	--disable-home-terminfo \
	--with-chtype=long \
	--enable-widec \
	#
# Workaround for utf8, rename libtinfow to libtinfo, addon for ncurses-*-alt-utf8-fix.patch
# will be removed when Thomas finish termlib=name feature
    find -type f -name Makefile -print0 |
	xargs -r0 subst s,tinfow,tinfo,g

popd # build-utf8
%endif # with_utf8

# build classic version
pushd build-classic
#NO SMP
%make

%if_with cxx
# Build c++ shared library.
pushd lib
g++ -shared -Wl,-soname,libncurses++.so.5 -o libncurses++.so.%version \
	-Wl,-whole-archive libncurses++.a -Wl,-no-whole-archive \
	-L. -lform -lmenu -lpanel -lncurses -ltinfo
ln -s libncurses++.so.%version libncurses++.so.5
ln -s libncurses++.so.5 libncurses++.so
popd # lib
# Rebuild c++ demo.
rm -f c++/demo
make -C c++
%endif # with_cxx
popd # build-classic

# build utf8 version
%if_with utf8
pushd build-utf8
#NO SMP
%make

%if_with cxx
# Build c++ shared library.
pushd lib
g++ -shared -Wl,-soname,libncursesw++.so.5 -o libncursesw++.so.%version \
	-Wl,-whole-archive libncursesw++.a -Wl,-no-whole-archive \
	-L. -lform -lmenu -lpanel -lncurses -ltinfo
ln -s libncursesw++.so.%version libncursesw++.so.5
ln -s libncursesw++.so.5 libncursesw++.so
popd # lib
# Rebuild c++ demo.
rm -f c++/demo
make -C c++
%endif # with_cxx
popd # build-utf8
%endif # with_utf8

%install
#install classic ncurses library version
pushd build-classic
%makeinstall_std includedir=%_includedir/%name

%if_with cxx
# Install c++ shared library.
install -pm644 lib/libncurses++.so.%version %buildroot%_libdir/
ln -s libncurses++.so.%version %buildroot%_libdir/libncurses++.so.5
ln -s libncurses++.so.5 %buildroot%_libdir/libncurses++.so
%endif # with_cxx
popd # build-classic

#install utf8 ncurses library version
%if_with utf8
pushd build-utf8
%makeinstall_std includedir=%_includedir/%name

ln -s %name %buildroot%_includedir/%{name}w
%if_with cxx
# Install c++ shared library.
install -pm644 lib/libncursesw++.so.%version %buildroot%_libdir/
ln -s libncursesw++.so.%version %buildroot%_libdir/libncursesw++.so.5
ln -s libncursesw++.so.5 %buildroot%_libdir/libncursesw++.so
%endif # with_cxx
popd # build-utf8
%endif # with_utf8

# The resetall script.
install -pD -m755 %SOURCE102 %buildroot%_bindir/resetall

ln -snf %name/curses.h %buildroot%_includedir/%name.h
for n in curses eti form menu panel term termcap unctrl; do
	ln -snf "%name/$n.h" "%buildroot%_includedir/$n.h"
done

# Relocate libtinfo from %_libdir/ to /lib/.
for f in %buildroot%_libdir/libtinfo*.so; do
	t=$(readlink "$f")
	ln -snf ../../%_lib/"$t" "$f"
done
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/libtinfo*.so.* %buildroot/%_lib/

ln -snf lib%name.so %buildroot%_libdir/libcurses.so

# Library compatibility symlinks.
t=$(readlink "%buildroot%_libdir/lib%name.so")
for v in 4 3; do
	ln -s "$t" "%buildroot%_libdir/lib%name.so.$v"
done

# Relocate tput.
mkdir -p %buildroot/bin
mv %buildroot%_bindir/tput %buildroot/bin/
ln -s ../../bin/tput %buildroot%_bindir/

# Generate new terminfo entries (deb).
for n in rxvt rxvt-unicode screen; do
	LD_LIBRARY_PATH=%buildroot/%_lib:%buildroot%_libdir \
        TERMINFO=%buildroot%_datadir/terminfo \
		%buildroot%_bindir/tic -s %name-alt-terms/$n.ti
done

# Split terminfo entries into /lib/terminfo and %_datadir/terminfo.
ln -snf ../l/linux %buildroot%_datadir/terminfo/c/console

rm -f relocation_error
while read -r n; do
	f="${n:0:1}"
	mkdir -p "%buildroot/%rootdatadir/terminfo/$f"
	mv "%buildroot%_datadir/terminfo/$f/$n" "%buildroot/%rootdatadir/terminfo/$f/" ||
		{ touch relocation_error; exit 1; }
	ln -s `relative "%buildroot/%rootdatadir/terminfo/$f/$n" "%buildroot%_datadir/terminfo/$f/"` \
		"%buildroot%_datadir/terminfo/$f/" ||
		{ touch relocation_error; exit 1; }
	echo "%%dir %_datadir/terminfo/$f"
	echo "%_datadir/terminfo/$f/$n"
done < %SOURCE101 | sort -u > base.list
[ ! -f relocation_error ]

find %buildroot%_datadir/terminfo -type f -mindepth 2 |
	sed "s|%buildroot||g" > extra.list

# Prepare docs.
rm -rf %buildroot%_docdir/%name-%version
mkdir -p %buildroot%_docdir/%name-%version
install -pm644 ANNOUNCE NEWS README TO-DO \
	c++/demo.cc doc/*.doc doc/html/*.html \
	%buildroot%_docdir/%name-%version/
install -pm644 c++/README-first \
	%buildroot%_docdir/%name-%version/README.c++
#make clean -C test

# Replace libncurses.so/libncursesw.so symlinks with linker scripts.
for i in ncurses ncursesw; do
	rm -f %buildroot%_libdir/lib$i.so
	cat > %buildroot%_libdir/lib$i.so <<-EOF
	/* GNU ld script */
	GROUP(%_libdir/lib$i.so.5 -ltinfo)
	EOF
done

%files
# ncurses is a pure virtual package.

# TERMINFO
%files -n terminfo -f base.list
%rootdatadir/terminfo
%dir %_datadir/terminfo/
%_datadir/tabset
%_man5dir/*

%files -n terminfo-extra -f extra.list
%dir %_datadir/terminfo/
%dir %_datadir/terminfo/*
%_datadir/terminfo/c/console

# LIBTINFO
%files -n libtinfo
/%_lib/libtinfo.*

%files -n libtic
%_libdir/libtic.so.*

%files -n libtic-devel
%_libdir/libtic.so
%_includedir/%name/term_entry.h
%_includedir/%name/nc_tparm.h

%files -n libtinfo-devel
%_libdir/libtinfo.so
%_includedir/termcap.h
%_includedir/term.h
%dir %_includedir/%name/
%_includedir/%name/termcap.h
%_includedir/%name/term.h
%_includedir/%name/ncurses_dll.h

%files -n libtinfo-devel-static
%_libdir/libtinfo.a

# TERMUTILS
%files -n termutils
/bin/tput
%_bindir/clear
%_bindir/reset*
%_bindir/toe
%_bindir/tput
%_bindir/tset
%_man7dir/*
%_man1dir/clear.*
%_man1dir/reset.*
%_man1dir/toe.*
%_man1dir/tput.*
%_man1dir/tset.*

%files -n termutils-devel
%_bindir/*info*
#_bindir/tack
%_bindir/tic
%_man1dir/*info*
#_man1dir/tack.*
%_man1dir/tic.*

# LIBNCURSES
%files -n lib%name
%_libdir/lib*[musl].so.*
%dir %_docdir/%name-%version/
%_docdir/%name-%version/[A-Z]*

%files -n lib%name-devel
%_bindir/%{name}5-config
%_libdir/lib*[musl].so
%_includedir/*
%exclude %_includedir/term*.h
%exclude %_includedir/%name/term*.h
%exclude %_includedir/%name/ncurses_dll.h
%exclude %_includedir/%name/nc_tparm.h
%if_with cxx
%exclude %_includedir/%name/cursesapp.h
%exclude %_includedir/%name/curses?.h
%exclude %_includedir/%name/cursslk.h
%exclude %_includedir/%name/etip.h
%endif # with_cxx
%if_with utf8
%exclude %_includedir/%{name}w
%endif # with_utf8
%_man3dir/*
%dir %_docdir/%name-%version/
%_docdir/%name-%version/[a-z]*
#%doc test

%files -n lib%name-devel-static
%_libdir/lib*.a
%exclude %_libdir/libtinfo.a
%if_with cxx
%exclude %_libdir/libncurses++*.a
%endif # with_cxx

# LIBNCURSES++
%if_with cxx
%files -n lib%name++
%_libdir/libncurses++*.so.*

%files -n lib%name++-devel
%_libdir/libncurses++*.so
%dir %_includedir/%name/
%_includedir/%name/cursesapp.h
%_includedir/%name/curses?.h
%_includedir/%name/cursslk.h
%_includedir/%name/etip.h

%files -n lib%name++-devel-static
%_libdir/libncurses++*.a
%endif # with_cxx

%if_with utf8
%files -n lib%{name}w
%_libdir/lib*[musl]w.so.*

%files -n lib%{name}w-devel
%_bindir/%{name}w5-config
%_libdir/lib*[musl]w.so
%_includedir/%{name}w
%endif # with_utf8

%changelog
* Thu Feb 10 2011 Dmitry V. Levin <ldv@altlinux.org> 5.7-alt6
- Rebuilt for debuginfo.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 5.7-alt5
- Packaged terminfo-extra subpackage as noarch.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 5.7-alt4
- Rebuilt for soname set-versions.

* Tue Aug 24 2010 Alexey I. Froloff <raorn@altlinux.org> 5.7-alt3.1
- NMU:
  + Updated rxvt-unicode definition (closes: #23927)

* Fri Nov 13 2009 Dmitry V. Levin <ldv@altlinux.org> 5.7-alt3
- libtic-devel: Added libtinfo-devel to the package requirements.

* Thu Nov 12 2009 Dmitry V. Levin <ldv@altlinux.org> 5.7-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Updated BuildRequires.

* Wed Nov 05 2008 Stanislav Ievlev <inger@altlinux.org> 5.7-alt1
- 5.7

* Thu Oct 02 2008 Dmitry V. Levin <ldv@altlinux.org> 5.6-alt5
- libncurses-devel: Do not package libtic.so.
- libncursesw-devel: Turned libncursesw.so into linker script.
- libtic, libtic-devel, libncurses-devel-static: Fixed package dependencies.

* Tue Sep 25 2007 Stanislav Ievlev <inger@altlinux.org> 5.6-alt4
- merge with current upstream version(20070908)
- build with ticlib and without tack

* Fri May 11 2007 Stanislav Ievlev <inger@altlinux.org> 5.6-alt3
- merge with current upstream version (20070505)
- mk-1st patch dropped (upstream has improved build system)
- use upstream xterm definition
- add rxvt-unicode
- new patches:
    fix tack build (TODO tack will be maintained in separate tarball),
    fix kbs in xterm terminal description (replace ^H with /177 to satisfy emacs)

* Mon Apr 09 2007 Stanislav Ievlev <inger@altlinux.org> 5.6-alt2
- move %_lib/terminfo to /lib/terminfo

* Wed Dec 27 2006 Stanislav Ievlev <inger@altlinux.org> 5.6-alt1
- update to current snapshot (20061223) of 5.6

* Fri Sep 08 2006 Stanislav Ievlev <inger@altlinux.org> 5.5-alt4
- update to current snapshot (20060903)

* Tue Aug 29 2006 Stanislav Ievlev <inger@altlinux.org> 5.5-alt3
- merged with current version
- replaced ncurses.so symlink with a linker script

* Tue May 30 2006 Stanislav Ievlev <inger@altlinux.org> 5.5-alt2
- merge with current version
- added libinfow-devel library (patch from raorn@)

* Thu May 18 2006 Stanislav Ievlev <inger@altlinux.org> 5.5-alt1
- 5.5, enable utf8 again

* Mon Feb 14 2005 Stanislav Ievlev <inger@altlinux.org> 5.4.20050108-alt3
- latest snapshot, fixed bugs 6092,4889

* Mon Jan 17 2005 Stanislav Ievlev <inger@altlinux.org> 5.4.20050108-alt2
- temporary turn off building of widechar version 
  (tinfo and tinfow are binary incompatible now)

* Wed Jan 12 2005 Stanislav Ievlev <inger@altlinux.org> 5.4.20050108-alt1
- latest rollup

* Fri Aug 06 2004 Stanislav Ievlev <inger@altlinux.org> 5.4.20040731-alt1
- latest rollup, apply x86_64 fixes from mouse@

* Tue Apr 27 2004 Stanislav Ievlev <inger@altlinux.org> 5.4.20040424-alt1
- latest rollup, rebuild with glibc2.3

* Thu Feb 26 2004 Stanislav Ievlev <inger@altlinux.org> 5.4.20040221-alt1
- 5.4 final, wide-char support now really works

* Thu Feb 05 2004 Stanislav Ievlev <inger@altlinux.org> 5.4.20040131-alt1
- latest patches from Thomas
- disable home terminfo feature, so please use TERMINFO variable instead

* Fri Jan 30 2004 Dmitry V. Levin <ldv@altlinux.org> 5.4.20040125-alt1
- Minor specfile tweaks.

* Fri Jan 30 2004 Stanislav Ievlev <inger@altlinux.org> 5.4.20040125-alt0.3
- Added '--with gpm' building feature (#2827).
- Fixed build for non-x86 platforms (#2827).

* Fri Jan 30 2004 Stanislav Ievlev <inger@altlinux.org> 5.4.20040125-alt0.2
- Added conflicts with libgpm < 1.20.1-alt3.1.
  All old libgpm versions are incompatible with 5.4

* Thu Jan 29 2004 Stanislav Ievlev <inger@altlinux.org> 5.4.20040125-alt0.1
- Updated code to patchlevel 20040125 (5.4 prerelease).
- Do not build orphaned c++ bindings.
- Build both classic and utf8 libraries.
- Build single terminfo library both for classic and utf8 ncurses.

* Wed Jul 09 2003 Dmitry V. Levin <ldv@altlinux.org> 5.3.20021019-alt2
- Fixed smp build.
- Build libncurses++ as shared library, too (0002675).
- Move all ncurses++ stuff to separate subpackages.

* Sun Dec 08 2002 Dmitry V. Levin <ldv@altlinux.org> 5.3.20021019-alt1
- Updated code to patchlevel 20021019 (minor fixes).
- Relocated /usr/bin/tput to /bin/tput.

* Wed Oct 16 2002 Dmitry V. Levin <ldv@altlinux.org> 5.3.20021012-alt1
- Updated code to patchlevel 20021012 (5.3 release).

* Thu Sep 26 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.20020921-alt1
- Updated code to patchlevel 20020921.
- xterm.ti:
  + updated from xterm-167/terminfo;
  + dropped all changes made in 5.2.20020901-alt1 except khome/kend.

* Mon Sep 09 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.20020907-alt1
- Updated code to patchlevel 20020907.

* Mon Sep 02 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.20020901-alt1
- Updated code to patchlevel 20020901.
- xterm.ti: fixed entries for khome, kend,
  kf1, kf13, kf14, kf15, kf16, kf17, kf18, kf19, kf2, kf20, kf3, kf4.
- Updated devel-static requirements.

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.20020810-alt1
- Updated code to patchlevel 20020810.
- Added "Eterm" to list of basic terminfo entries (28 items now).
- Added "Conflicts: screen < 3.9.11-alt1" to terminfo (#0001177).
- Relocated manpages from 5th section to terminfo subpackage.
- Redistributed contents of ncurses subpackage:
  + to termutils: clear, reset*, toe, tput, tset;
  + to termutils-devel: *info*, tack, tic;
  + to libncurses: documentation.
 
* Fri Jul 19 2002 Ivan Zakharyaschev <imz@altlinux.ru> 5.2.20020622-alt2
- moved term.h from libncurses-devel to libtinfo-devel;

* Mon Jul 01 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.20020622-alt1
- Updated code to patchlevel 20020622.
- Relocated libncurses shared library back to %_libdir/:
  reverted first relocation made in 990110 (no need).

* Sat Jun 22 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.20020615-alt1
- Updated code to patchlevel 20020615, reviewed and updated patches.
- Imported terminfo definitions for screen, xterm and rxvt from Debian.
- Reviewed configure flags; most significant changes are:
  --with-terminfo-dirs="/lib/terminfo:/usr/share/terminfo"
  --disable-termcap
  --disable-safe-sprintf
  --disable-root-environ
- When building the ncurses library, organize this as two parts:
  the curses library (libncurses) and the low-level terminfo library (libtinfo).
  This is done to accommodate applications that use only the latter.
  The terminfo library is about half the size of the total.
- Moved libtinfo libraries to separate subpackages.
- Reduced number of basic terminfo entries (27 atm.) and moved them
  to /lib/terminfo.
- Don't build debug and profile static libraries by default.
- Relocated documentation.

* Fri Mar 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 5.2-ipl5mdk
- Moved terminfo database into separate subpackage.
- Renamed %name-extraterms subpackage to terminfo-extra.
- Corrected dependencies:
  + lib%name: PreReq: terminfo = %%version-%%release;
  + lib%name: Conflicts: %name < %%version-%%release;
  + terminfo: Conflicts: %name < %%version-%%release.

* Tue Dec 25 2001 Stanislav Ievlev <inger@altlinux.ru> 5.2-ipl4mdk
- removed buggy xterm-pcolor entry from terminfo

* Fri May 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.2-ipl3mdk
- Libification.

* Fri Nov 24 2000 Dmitry V. Levin <ldv@fandra.org> 5.2-ipl2mdk
- Merged RH patches

* Mon Oct 30 2000 Dmitry V. Levin <ldv@fandra.org> 5.2-ipl1mdk
- 5.2
- Split out definitions for rare terminals to extraterms package.
- Use xterm definitions from RH.

* Wed Jul 12 2000 Dmitry V. Levin <ldv@fandra.org> 5.1-ipl1mdk
- 5.1
- FHSification.

* Mon Jun 12 2000 Dmitry V. Levin <ldv@fandra.org> 5.0-ipl13mdk
* RE and Fandra adaptions.

* Wed May 03 2000 Warly <warly@mandrakesoft.com> 5.0-13mdk
- correct links in /lib

* Mon Apr 10 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 5.0-12mdk
- fix license (again) :-/

* Fri Mar 31 2000 Warly <warly@mandrakesoft.com> 5.0-11mdk
- devel group: Development/C

* Fri Mar 31 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 5.0-10mdk
- changed group
- fixed license

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com> 5.0-9mdk
- PPC fixes

* Wed Jan 12 2000 Pixel <pixel@mandrakesoft.com> 5.0-8mdk
- fix for alpha (use egcs instead of gcc-2.95.2)

* Tue Jan 11 2000 Frederic Lepied <flepied@mandrakesoft.com> 5.0-7mdk
- fix xterm entry for 3.3.6

* Sun Dec 25 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Fix build for K6 (another, AMD K6 is not an i686)

* Fri Nov 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add debian term.

* Fri Nov 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add resetall script(r).

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 5.0 anounced final.

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Wed Sep 29 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- update to 990925

* Mon Sep  6 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- update to 990904

* Fri Jul 16 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Rebuild for new environement (4mdk).

* Mon Jul  5 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- update to 990703

* Wed May 19 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- update to 990516
- Fix the -fomit-frame-pointer problem (using -fno-omit-frame-pointer
  with -pg where needed)

* Mon Apr 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- update to 990410.
- some spec tweaks (yes again ;-))
- removing the patch and build a global ncurses-990410.tar.bz2
- Remove the -fomit-frame-pointer (incompatible with -pg ?)
- Add patch for a bug (?) with two entry in linux-lat.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- add de locale
- update to 990403
- some spec tweaks
- take description + some patches from RH 6.0

* Sun Mar 28 1999 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- update to 990327

* Wed Mar 10 1999 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- update to 990307
- link /lib/libncurses.so* to /usr/lib

* Sun Feb  7 1999 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- update to 990206

* Fri Jan 15 1999 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- update to 990110
- move libncurses.so.* to /lib, where it belongs (needed by sh)

* Thu Dec 24 1998 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- update to 981220

* Tue Dec 15 1998 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- start with RH release 10
- update to 981212; merge patches in tar file
- bzip2 man pages
- use -fno-omit-frame-pointer -pg rather than just -pg for profiled
  version - that way, we can handle RPM_OPT_FLAGS with -fomit-frame-pointer
- Make compatibility links to libncurses.so.3 (they ARE binary compatible)
- update terminfo file to 10.2.5

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- make sure to strip the binaries

* Wed Sep 23 1998 Cristian Gafton <gafton@redhat.com>
- added another zillion of patches. The spec file *is* ugly
- defattr

* Mon Jul 20 1998 Cristian Gafton <gafton@redhat.com>
- added lots of patches. This spec file is starting to look ugly

* Wed Jul 01 1998 Alan Cox <alan@redhat.com>
- Fix setuid trusting. Open termcap/info files as the real user.

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- added terminfo entry for the poor guys using lat1 and/or lat-2 on their
  consoles... Enjoy linux-lat ! Thanks, Erik !

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- new patch to get xterm-color and nxterm terminfo entries
- aliased them to rxvt, as that seems to satisfy everybody

* Sun Apr 12 1998 Cristian Gafton <gafton@redhat.com>
- added %clean section

* Tue Apr 07 1998 Cristian Gafton <gafton@redhat.com>
- removed /usr/lib/terminfo symlink - we shouldn't need that

* Mon Apr 06 1998 Cristian Gafton <gafton@redhat.com>
- updated to 4.2 + patches
- added BuildRoot

* Sat Apr 04 1998 Cristian Gafton <gafton@redhat.com>
- rebuilt with egcs on alpha

* Wed Dec 31 1997 Erik Troan <ewt@redhat.com>
- version 7 didn't rebuild properly on the Alpha somehow -- no real changes
  are in this version

* Tue Dec 09 1997 Erik Troan <ewt@redhat.com>
- TIOCGWINSZ wasn't used properly

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc, linked shared libs against -lc
