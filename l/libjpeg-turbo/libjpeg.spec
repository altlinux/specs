
%def_enable profiling

Name: libjpeg-turbo
Version: 2.1.5.1
Release: alt1.1
Epoch: 2

Summary: A SIMD-accelerated library for manipulating JPEG image format files
License: BSD-3-Clause
Group: System/Libraries
Url: http://sourceforge.net/projects/%name/

# http://download.sourceforge.net/%name/%name-%version.tar.gz
Source: %name-%version-%release.tar
Source2: http://jpegclub.org/jpegexiforient.c
Source3: exifautotran
Source4: jpeginfo.c

Patch0: libjpeg-turbo-alt-rdjpgcom-i18n.patch
Patch1: libjpeg-turbo-alt-versioning.patch
Patch2: libjpeg-turbo-fedora-noinst.patch
Patch2000: %name-e2k-simd.patch

# why it should be enabled?
%def_disable static

BuildRequires: cmake ctest

%ifarch %ix86 x86_64
BuildRequires: nasm
%endif

%package -n libjpeg
Summary: A library for manipulating JPEG image format files
Group: System/Libraries

%package -n libjpeg-devel
Summary: Development tools for programs which will use the libjpeg library
Group: Development/C
Requires: libjpeg = %epoch:%version-%release
%ifnarch %ix86
Provides: libjpeg-mmx-devel
%endif

%package -n libjpeg-devel-static
Summary: Static libjpeg library
Group: Development/C
Requires: libjpeg-devel = %epoch:%version-%release
%ifnarch %ix86
Provides: libjpeg-mmx-devel-static
%endif

%package -n libjpeg-utils
Summary: Programs for manipulating JPEG format image files
Group: Graphics
Requires: libjpeg = %epoch:%version-%release

%package -n libturbojpeg
Summary: A turbojpeg library
Group: System/Libraries
Requires: libjpeg = %epoch:%version-%release

%package -n libturbojpeg-devel
Summary: Development files for the turbojpeg library
Group: Development/C
Requires: libturbojpeg = %epoch:%version-%release

%description
libjpeg-turbo is a derivative of libjpeg which uses SIMD instructions
(MMX, SSE2, etc.) to accelerate baseline JPEG compression and
decompression on x86 and x86-64 systems.  On such systems, libjpeg-turbo
is generally 2-4x as fast as the unmodified version of libjpeg, all else
being equal.

%description -n libjpeg
This package contains a shared library of functions for loading,
manipulating and saving JPEG format image files.

%description -n libjpeg-devel
This package includes development files necessary for developing
programs which will manipulate JPEG files using the jpeg library.

%description -n libjpeg-devel-static
This package includes static library necessary for developing statically
linked programs which will manipulate JPEG files using the jpeg library.

%description -n libjpeg-utils
This package contains simple client programs for accessing the
libjpeg functions.  Libjpeg client programs include cjpeg, djpeg,
jpegtran, rdjpgcom and wrjpgcom.  Cjpeg compresses an image file
into JPEG format.  Djpeg decompresses a JPEG file into a regular
image file.  Jpegtran can perform various useful transformations
on JPEG files.  Rdjpgcom displays any text comments included in
a JPEG file.  Wrjpgcom inserts text comments into a JPEG file.

%description -n libturbojpeg
This package contains a turbojpeg shared library.

%description -n libturbojpeg-devel
This package contains development files for the turbojpeg library.

%prep
%setup -n %name-%version-%release
%patch0 -p2
%patch1 -p1
%patch2 -p2
%ifarch %e2k
%patch2000 -p1
%endif

install -pm644 %_sourcedir/{jpegexiforient,jpeginfo}.c .
install -pm755 %_sourcedir/exifautotran .

# restrict list of global symbols exported by the library.
echo -e '{\nglobal:' > libjpeg.sym
sed -En '/^EXTERN/ s,^.+\)\s+([^(]+).+$,\1;,p' jpeglib.h jpegint.h \
	| egrep -v '^(jinit_|jzero_far)' >> libjpeg.sym
# extra symbols required by packages
cat >> libjpeg.sym <<'EOF'
jinit_c_master_control;
jinit_color_converter;
jinit_master_decompress;
jinit_downsampler;
jpeg_std_message_table;
local: *;
};
EOF

%build
# using PGO makes the code about 10%% faster
# up to 50%% on e2k for progressive JPEG decoding
%if_enabled profiling
%add_optflags -fprofile-generate
%cmake -G'Unix Makefiles' \
%if_disabled static
-DENABLE_STATIC=FALSE
%endif
%nil
%cmake_build
# it's better not to do it in parallel
( cd %_cmake__builddir ; make -k test ; make clean )
%remove_optflags -fprofile-generate
%ifarch %e2k
%add_optflags -fprofile-use=%_builddir/%name-%version-%release/%_cmake__builddir/eprof.sum
eprof -d %_cmake__builddir -s %_cmake__builddir/eprof.sum
%else
%add_optflags -fprofile-use
%endif
%endif

%cmake -G'Unix Makefiles'
%cmake_build
make jpegexiforient
bzip2 -9fk libjpeg.txt structure.txt usage.txt

%check
LD_LIBRARY_PATH=%buildroot%_libdir %cmake_build -t test -- -k
LD_LIBRARY_PATH=%buildroot%_libdir ./jpeginfo %_cmake__builddir/*.jpg >/dev/null

%install
%cmake_install
%__cc %optflags -D_GNU_SOURCE -I%buildroot%_includedir jpeginfo.c -L%buildroot%_libdir -ljpeg -o jpeginfo
install -pm755 exifautotran jpegexiforient jpeginfo %buildroot%_bindir/
# do not package unwanted libturbojpeg files
find %buildroot -name 'libturbojpeg.*a' -delete

%define docdir %_docdir/%name
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
install -pm644 README* change.log \
	coderules.txt libjpeg.txt.bz2 structure.txt.bz2 usage.txt.bz2 wizard.txt \
	%buildroot%docdir/

%files -n libjpeg
%_libdir/libjpeg.so.*
%dir %docdir
%docdir/[CLR]*

%files -n libjpeg-utils
%_bindir/*
%_mandir/man?/*

%files -n libjpeg-devel
%_libdir/libjpeg.so
%_includedir/j*
%dir %docdir
%docdir/[^CLR]*
%_pkgconfigdir/libjpeg.pc
%_libdir/cmake/libjpeg-turbo

%if_enabled static
%files -n libjpeg-devel-static
%_libdir/libjpeg.a
%endif #static

%files -n libturbojpeg
%_libdir/libturbojpeg.so.*

%files -n libturbojpeg-devel
%_libdir/libturbojpeg.so
%_includedir/turbojpeg.h
%_pkgconfigdir/libturbojpeg.pc

%changelog
* Mon Nov 13 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2:2.1.5.1-alt1.1
- e2k patch update

* Tue Nov 07 2023 L.A. Kostis <lakostis@altlinux.ru> 2:2.1.5.1-alt1
- 2.1.5.1.
- .spec: Escape unparseable symbols.
- .spec: Disable static build (cmake often prefer -static over shared which
         is not desired way).

* Sat May 28 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2:2.1.2-alt1.2
- improved SIMD patch for Elbrus
- e2k: also need to specify a directory with profiles

* Wed May 25 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2:2.1.2-alt1.1
- updated SIMD patch for Elbrus
- e2k: fixed compiler hang when using profile

* Thu Feb 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:2.1.2-alt1
- 2.1.2 released

* Mon Aug 30 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:2.0.6-alt4
- rebuilt with lto on

* Tue Jun 29 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2:2.0.6-alt3
- added PGO (profile-guided optimization)

* Thu May 27 2021 Arseny Maslennikov <arseny@altlinux.org> 2:2.0.6-alt2.1
- NMU: spec: adapted to new cmake macros.

* Tue May 25 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2:2.0.6-alt2
- added SIMD patch for Elbrus

* Wed Feb 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:2.0.6-alt1
- 2.0.6 released (fixes: CVE-2020-13790)

* Wed Apr 10 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:2.0.2-alt1
- 2.0.2 released

* Tue Apr 09 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:1.5.3-alt1
- 1.5.3 released

* Wed Jun 21 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2:1.5.1-alt1
- 1.5.1 released

* Thu Dec 26 2013 Dmitry V. Levin <ldv@altlinux.org> 2:1.3.1-alt0.1
- Updated to 1.3.1 r1092 (fixes CVE-2013-6629, CVE-2013-6630).

* Wed Jul 18 2012 Dmitry V. Levin <ldv@altlinux.org> 2:1.2.1-alt1
- Updated to 1.2.1 (fixes CVE-2012-2806).

* Tue Jul 19 2011 Dmitry V. Levin <ldv@altlinux.org> 2:1.1.1-alt1
- Updated to 1.1.1 (closes: #25369).

* Tue Feb 15 2011 Dmitry V. Levin <ldv@altlinux.org> 2:1.0.1-alt3
- Packaged libturbojpeg.

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 2:1.0.1-alt2
- Rebuilt for debuginfo.

* Wed Oct 20 2010 Dmitry V. Levin <ldv@altlinux.org> 2:1.0.1-alt1
- Switched to libjpeg-turbo-1.0.1.
- Restricted the list of global symbols exported by the library.

* Tue Oct 12 2010 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt11
- Rebuilt for soname set-versions.

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt10
- Fixed libtoolize simulation.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt9
- exifautotran: Applied fix from Alexei V. Mezin (closes: #17399).
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Mon Apr 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt8
- Enabled devel-static packaging (#10468).

* Mon Mar 06 2006 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt7
- Fixed build with --as-needed.

* Fri Feb 17 2006 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt6
- Disabled build and packaging of static library by default.
- Provide libjpeg-mmx-devel for non-ix86 architectures (#9094).

* Wed May 11 2005 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt5
- Fixed definition of INT32 in jmorecfg.h (SuSE, closes #6533).

* Wed Oct 13 2004 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt4
- Added home-bred jpeginfo utility.

* Tue Oct 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt3
- Added jpegexiforient utility from http://jpegclub.org/.
- Added exifautotran utility based on
  http://jpegclub.org/exifautotran.sh.

* Mon Oct 11 2004 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt2
- Applied lossless-crop patch from
  http://jpegclub.org/croppatch.tar.gz
- Merged patches from debian package.
- Fixed docs packaging.

* Wed Nov 26 2003 Dmitry V. Levin <ldv@altlinux.org> 1:6b-alt1
- Do not package .la files.
- Additional convention enforcement on patch file names.

* Wed Sep 04 2002 Stanislav Ievlev <inger@altlinux.ru> 6b-ipl18mdk
- rebuild with new gcc3

* Thu Aug 16 2001 Dmitry V. Levin <ldv@altlinux.ru> 6b-ipl17mdk
- Moved static library to devel-static subpackage.
- Aadded some C++ tweaks to the headers (rh).

* Sat Jan 06 2001 Dmitry V. Levin <ldv@fandra.org> 6b-ipl16mdk
- RE adaptions.

* Wed Jan  3 2001 <yduret@mandrakesoft.com> 6b-16mdk
- macroization
- added URL:, %%doc
- split into libjpeg, libjpeg-utils and libjpeg-devel

* Fri Jul 26 2000 <adussart@mandrakesoft.com> 6b-15mdk
- Updated %%files section.

* Thu May 04 2000 <adussart@mandrakesoft.com> 6b-14mdk
- Fixed HAVE_STDLIB_H redefine bug.

* Tue Apr 18 2000 Warly <warly@mandrakesoft.com> 6b-13mdk
- New group

* Thu Jan 13 2000 Pixel <pixel@mandrakesoft.com>
- libtoolize --force
- fix strange ./libtool needed by forcing LIBTOOL=libtool

* Wed Nov  3 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 9)

* Wed Jan 13 1999 Cristian Gafton <gafton@redhat.com>
- patch to build on arm
- build for glibc 2.1

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries

* Mon Aug  3 1998 Jeff Johnson <jbj@redhat.com>
- fix buildroot problem.

* Tue Jun 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Jun 04 1998 Marc Ewing <marc@redhat.com>
- up to release 4
- remove patch that set (improper) soname - libjpeg now does it itself

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- fixed build on manhattan

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 6b

* Wed Oct 08 1997 Donnie Barnes <djb@redhat.com>
- new package to remove jpeg stuff from libgr and put in it's own package
