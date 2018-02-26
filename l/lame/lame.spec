Name: lame
Version: 3.99.5
Release: alt1
Summary: LAME Ain't an Mp3 Encoder
License: LGPL
Group: Sound
URL: http://%name.sourceforge.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: lib%name = %version-%release
Conflicts: %name-hydrogen

Source: http://prdownloads.sourceforge.net/lame/%name-%version.tar.gz

BuildRequires: libsndfile-devel libtinfo-devel
%ifarch %ix86 x86_64
BuildRequires: nasm
%endif

%description
Lame is a program which can be used to create compressed audio files.
These audio files can be played back by popular mp3 players such as mpg123.

%package -n lib%name
Summary: LAME shared library
Group: System/Libraries
Conflicts: lib%name-hydrogen

%description -n lib%name
This package contains shared library required by %name-based software

%package -n lib%name-devel
Summary: LAME development file
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: lib%name-hydrogen-devel

%description -n lib%name-devel
This package contains header files required to develop
%name-based software

%prep
%setup -q

%build
%configure \
	--disable-static \
%ifarch %ix86
	--enable-nasm
%endif

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc LICENSE USAGE doc/html/*.html
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc API HACKING STYLEGUIDE TODO
%_includedir/*
%_libdir/*.so

%changelog
* Thu Mar 01 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.99.5-alt1
- 3.99.5

* Mon Nov 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.99.3-alt1
- 3.99.3

* Mon Mar 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.98.4-alt3
- rebuild for debuginfo
- enabled nasm for x86

* Sat Oct 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.98.4-alt2
- rebuild

* Mon May 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.98.4-alt1
- 3.98.4

* Mon Mar 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.98.3-alt1
- 3.98.3

* Wed Jul 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.98.2-alt2
- applied lame-3.98-alt-ffmpeg_fix.patch (closes: #20899)

* Wed Feb 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.98.2-alt1
- 3.98.2

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.98-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Jul 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.98-alt1
- 3.98

* Wed Apr 18 2007 ALT QA Team Robot <qa-robot@altlinux.org> 3.97-alt1.0
- Automated rebuild.

* Mon May 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 3.97-alt1
- rebuild with gcc4.1
- disable devel-static

* Mon Oct 31 2005 Andrey Astafiev <andrei@altlinux.ru> 3.97-alt0.1
- 3.97 beta.

* Sun Jun 19 2005 Andrey Astafiev <andrei@altlinux.ru> 3.96.1-alt2
- Added -lm flag.

* Thu Aug 05 2004 Andrey Astafiev <andrei@altlinux.ru> 3.96.1-alt1.1
- Fixed build in hasher.

* Tue Aug 03 2004 Andrey Astafiev <andrei@altlinux.ru> 3.96.1-alt1
- 3.96.1

* Thu Dec 11 2003 Andrey Astafiev <andrei@altlinux.ru> 3.93.1-alt4
- *.la files removed.
- Set textrel=relaxed for now.

* Wed Nov 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.93.1-alt3
- Added %optflags_shared macros.

* Mon Sep 15 2003 Andrey Astafiev <andrei@altlinux.ru> 3.93.1-alt2
- Requires libtool_1.4 for building.

* Mon Dec 02 2002 Andrey Astafiev <andrei@altlinux.ru> 3.93.1-alt1
- 3.93.1

* Mon Nov 25 2002 Andrey Astafiev <andrei@altlinux.ru> 3.93-alt1
- 3.93

* Wed Nov 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 3.92-alt3
- Rebuild

* Thu Jul 18 2002 Andrey Astafiev <andrei@altlinux.ru> 3.92-alt2
- Patched configure.in to link with libtinfo.

* Mon Apr 29 2002 Andrey Astafiev <andrei@altlinux.ru> 3.92-alt1
- 3.92

* Mon Dec 31 2001 Andrey Astafiev <andrei@altlinux.ru> 3.91-alt1
- 3.91

* Mon Dec 24 2001 Stanislav Ievlev <inger@altlinux.ru> 3.90.1-alt2
- fixed build under new nasm

* Sun Dec 23 2001 Andrey Astafiev <andrei@altlinux.ru> 3.90.1-alt1
- 3.90.1
- Relocated documentation.

* Fri Oct 12 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.89-alt3
- Fixed some bugs by use 2.95.3 gcc compiler

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.89-alt2
- Added lame_global_flags.h header required for some programs.

* Thu Aug 23 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.89-alt1
- 3.89
- Added devel-static package.

* Fri Jan 19 2001 Dmitry V. Levin <ldv@fandra.org> 3.87-ipl1
- 3.87
- Split into three subpackages.
- Added vorbis support.

* Sat May 06 2000 Dmitry V. Levin <ldv@fandra.org>
- Initial release
