Name: libmad
Version: 0.15.1b
Release: alt8.2

Summary: High quality MPEG audio decoder library
License: GPL
Group: Sound
Url: http://mad.sourceforge.net/

Source: libmad-%version.tar.gz
Patch1: libmad-0.15.1b-speedup.patch
Patch2: libmad-0.15.0b-alt-pkgconfig.patch
Patch3: libmad-0.15.1b-no-force-mem-gcc43.patch
Patch4: libmad-0.15.1b-alt-MIPS.patch

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

%package devel
Summary: Development files for MAD
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required for packaging
MAD-based software.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p1
%ifarch e2k
# lcc
sed -i  -e 's,-fthread-jumps,,;s,-fcse-follow-jumps,,;s,-fcse-skip-blocks,,' \
	-e 's,-fexpensive-optimizations,,;s,-fregmove,,' \
	configure.ac
%endif

%build
touch AUTHORS NEWS ChangeLog
%autoreconf
%remove_optflags -mthumb
%configure \
	--enable-accuracy \
	--disable-static

# SMP-incompatiple build 
%make

%install
%makeinstall
# audacity can't find it otherwise
ln -s libmad.pc %buildroot%_pkgconfigdir/mad.pc

%files
%doc CHANGES README CREDITS COPYRIGHT
%_libdir/libmad.so.*

%files devel
%_libdir/libmad.so
%_pkgconfigdir/*
%_includedir/mad.h

%changelog
* Wed Feb 21 2018 Fr. Br. George <george@altlinux.ru> 0.15.1b-alt8.2
- MIPS: patch for GCC>=4

* Wed Mar 15 2017 Michael Shigorin <mike@altlinux.org> 0.15.1b-alt8.1
- E2K: disable lcc-unsupported options

* Fri Apr 25 2014 Michael Shigorin <mike@altlinux.org> 0.15.1b-alt8
- NMU: symlink libmad.pc as mad.pc for enhanced compatibility

* Thu Feb 28 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15.1b-alt7
- fixed build on arm

* Sat Mar 19 2011 Alexey Tourbin <at@altlinux.ru> 0.15.1b-alt6
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.1b-alt5
- Rebuilt for soname set-versions

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.15.1b-alt4.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmad
  * postun_ldconfig for libmad

* Mon Oct 27 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.15.1b-alt4
- Fix build with gcc 4.3.

* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.15.1b-alt3
- Removed libtool/automake version kludges.
- Minor spec cleanup.

* Thu Mar 04 2004 Andrey Astafiev <andrei@altlinux.ru> 0.15.1b-alt2
- 0.15.1b
- Speedup patch updated.

* Fri Nov 21 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt5
- Repaired changelog.

* Fri Nov 14 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt4
- Fixed build for SMP systems.

* Mon Nov 03 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt3
- Added patch for pkgconfig.

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt2
- Added speedup patch.

* Fri Jun 06 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt1
- libmad is now in separate tarball.

* Sat Mar 15 2003 Andrey Astafiev <andrei@altlinux.ru> 0.14.2b-alt4
- Library libid3tag moved to separate binary package.

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.14.2b-alt3
- rebuild with gcc-3.2
- Packager tag added.

* Tue Feb 12 2002 Andrey Astafiev <andrei@altlinux.ru> 0.14.2b-alt2
- Packager field fixed.

* Fri Nov 09 2001 Andrey Astafiev <andrei@altlinux.ru> 0.14.2b-alt1
- 0.14.2b

* Tue Oct 23 2001 Andrey Astafiev <andrei@altlinux.ru> 0.14.1b-alt1
- 0.14.1b

* Fri Oct 19 2001 Andrey Astafiev <andrei@altlinux.ru> 0.14.0b-alt1
- 0.14.0b

* Mon Sep 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.13.0b-alt2
- Blind minor specfile cleanup.

* Mon Sep 3 2001 Andrey Astafiev <andrei@altlinux.ru> 0.13.0b-alt1
- First version of RPM package.
