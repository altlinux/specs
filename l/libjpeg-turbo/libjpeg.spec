Name: libjpeg-turbo
Version: 1.1.1
Release: alt1
Epoch: 2

Summary: A SIMD-accelerated library for manipulating JPEG image format files
License: wxWidgets
Group: System/Libraries
Url: http://sourceforge.net/projects/%name/

# http://download.sourceforge.net/%name/%name-%version.tar.gz
Source: %name-%version.tar
Source2: http://jpegclub.org/jpegexiforient.c
Source3: exifautotran
Source4: jpeginfo.c

Patch1: libjpeg-6b-suse-int32.patch
Patch2: libjpeg-turbo-fedora-jpgtest.patch
Patch3: libjpeg-turbo-alt-rdjpgcom-i18n.patch
Patch4: libjpeg-turbo-alt-versioning.patch
Patch5: libjpeg-turbo-alt-libturbojpeg.patch
Patch6: libjpeg-turbo-alt-warnings.patch

%def_enable static

# for jpgtest.cxx
BuildRequires: gcc-c++

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
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

install -pm644 %_sourcedir/{jpegexiforient,jpeginfo}.c .
install -pm755 %_sourcedir/exifautotran .

# restrict list of global symbols exported by the library.
sed -n 's/^EXTERN([^()]*)[[:space:]]*\([^[:space:]]\+\).*/\1/p' jpeglib.h \
	> libjpeg.sym
sed -n 's/^EXTERN([^()]*)[[:space:]]*\([^[:space:]]\+\).*/\1/p' jpegint.h \
	| egrep -v '^(jinit_|jzero_far)' >> libjpeg.sym
# extra symbols required by packages
cat >> libjpeg.sym <<'EOF'
jpeg_std_message_table
EOF
sort -u -o libjpeg.sym{,}

%build
%autoreconf
%configure --enable-shared %{subst_enable static}
%make_build
make jpegexiforient
%__cc $CPPFLAGS -D_GNU_SOURCE jpeginfo.c -L.libs -ljpeg -o jpeginfo
bzip2 -9fk libjpeg.txt structure.txt usage.txt

%check
LD_LIBRARY_PATH=%buildroot%_libdir make -k test
LD_LIBRARY_PATH=%buildroot%_libdir ./jpeginfo *.jpg >/dev/null

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_includedir,%_man1dir}
%makeinstall_std
install -pm755 exifautotran jpegexiforient jpeginfo %buildroot%_bindir/
# do not package unwanted libturbojpeg files
find %buildroot -name 'libturbojpeg.*a' -delete

%define docdir %_docdir/%name
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
install -pm644 README* ChangeLog.txt LICENSE.txt change.log example.c \
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

%if_enabled static
%files -n libjpeg-devel-static
%_libdir/libjpeg.a
%endif #static

%files -n libturbojpeg
%_libdir/libturbojpeg.so.*

%files -n libturbojpeg-devel
%_libdir/libturbojpeg.so
%_includedir/turbojpeg.h

%changelog
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
