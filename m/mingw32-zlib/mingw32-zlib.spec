%define __strip %_mingw32_strip
%define __objdump %_mingw32_objdump

Name: mingw32-zlib
Version: 1.2.3
Release: alt1
Summary: MinGW Windows zlib compression library

License: zlib
Group: System/Libraries
Url: http://www.zlib.net/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://www.zlib.net/zlib-%version.tar.gz
Patch3: zlib-1.2.3-autotools.patch
Patch6: minizip-1.2.3-malloc.patch
BuildArch: noarch

# MinGW-specific patches.
Patch100: zlib-win32.patch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils

%description
MinGW Windows zlib compression library.

%package static
Summary: Static libraries for mingw32-zlib development
Group: System/Libraries
Requires: mingw32-zlib = %version-%release

%description static
The mingw32-zlib-static package contains static library for mingw32-zlib development.

%package -n mingw32-minizip
Summary: Minizip manipulates files from a .zip archive
Group: System/Libraries
Requires: mingw32-zlib = %version-%release

%description -n  mingw32-minizip
MinGW Minizip manipulates files from a .zip archive.

%prep
%setup -q -n zlib-%version
%patch100 -p1
cd ..
cp -a zlib-%version x
mv x zlib-%version
cd zlib-%version
%patch3 -p1 -b .atools
# patch cannot create an empty dir
mkdir m4
%patch6 -p1 -b .mal
iconv -f windows-1252 -t utf-8 <ChangeLog >ChangeLog.tmp
mv ChangeLog.tmp ChangeLog
cp Makefile Makefile.old

%build
pushd x
CC=%_mingw32_cc \
CFLAGS="%_mingw32_cflags" \
RANLIB=%_mingw32_ranlib \
./configure

make -f win32/Makefile.gcc \
  CFLAGS="%_mingw32_cflags" \
  CC=%_mingw32_cc \
  AR=%_mingw32_ar \
  RC=%_mingw32_target-windres \
  DLLWRAP=%_mingw32_target-dllwrap \
  STRIP=%_mingw32_strip \
  all
popd

autoreconf --install;
%_mingw32_configure
%make_build libz.la
perl -i -pe 's,libz-1.dll,zlib1.dll,' libz.la
rm -f libz.dll.a
cp x/libzdll.a libz.dll.a
cp x/zlib1.dll .
rm -f .libs/libz.dll.a
cp x/libzdll.a .libs/libz.dll.a
cp x/zlib1.dll .libs/
%make_build

%install
%makeinstall_std

rm -rf %buildroot%_mingw32_mandir

rm -f %buildroot%_mingw32_bindir/libz-1.dll
install x/zlib1.dll %buildroot%_mingw32_bindir/

%files
%_mingw32_includedir/zconf.h
%_mingw32_includedir/zlib.h
%_mingw32_libdir/libz.dll.a
%_mingw32_bindir/zlib1.dll
%_mingw32_libdir/libz.la

%files static
%_mingw32_libdir/libz.a

%files -n mingw32-minizip
%doc contrib/minizip/ChangeLogUnzip
%_mingw32_libdir/libminizip.dll.a
%_mingw32_libdir/libminizip.la
%_mingw32_bindir/libminizip-1.dll
%dir %_mingw32_includedir/minizip
%_mingw32_includedir/minizip/*.h
%_mingw32_libdir/pkgconfig/minizip.pc

%changelog
* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 1.2.3-alt1
- initial build

* Fri Jun 12 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-18
- Cannot copy current directory into itself, so fix the copy command
  which creates 'x' subdirectory.

* Thu May  1 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.3-17
- BR autoconf, automake, libtool

* Thu Apr 30 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.2.3-16
- use autotools build system from native package

* Mon Mar  3 2009 W. Pilorz <wpilorz at gmail.com> - 1.2.3-15
- Add static subpackage.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-13
- Rebuild for mingw32-gcc 4.4

* Mon Jan 19 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-12
- Force rebuild to test maintenance account.

* Thu Dec 18 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-11
- Pass correct CFLAGS to build.

* Thu Oct 16 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-10
- Consider native patches.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-9
- Rename mingw -> mingw32.

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-8
- Remove manpage.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-7
- Remove static library.

* Fri Sep  5 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-5
- Fix misnamed file: zlibdll.a -> zlib.dll.a
- Explicitly provide mingw(zlib1.dll).

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-3
- Initial RPM release, largely based on earlier work from several sources.
