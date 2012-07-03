%define __strip %_mingw32_strip
%define __objdump %_mingw32_objdump

# Build the programs like cjpeg, etc.
# https://bugzilla.redhat.com/show_bug.cgi?id=467401c7
%define build_programs 0

Name: mingw32-libjpeg
Version: 6b
Release: alt1
Summary: MinGW Windows Libjpeg library

License: IJG
Url: http://www.ijg.org/
Group: System/Libraries
Packager: Boris Savelev <boris@altlinux.org>

Source: ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v%version.tar.gz
Source1: configure.in

Patch1: jpeg-c++.patch
Patch4: libjpeg-cflags.patch
Patch5: libjpeg-buf-oflo.patch
Patch6: libjpeg-autoconf.patch

Patch100: jpeg-mingw32.patch

BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-libpng
BuildRequires: mingw32-zlib

%description
MinGW Windows Libjpeg library.

%prep
%setup -q -n jpeg-6b

%patch1 -p1 -b .c++
%patch4 -p1 -b .cflags
%patch5 -p1 -b .oflo
%patch6 -p1

%patch100 -p1

# For long-obsolete reasons, libjpeg 6b doesn't ship with a configure.in.
# We need to re-autoconf though, in order to update libtool support,
# so supply configure.in.
cp %SOURCE1 configure.in

# libjpeg 6b includes a horribly obsolete version of libtool.
# Blow it away and replace with build system's version.
rm -f config.guess config.sub ltmain.sh ltconfig aclocal.m4

cat %_datadir/libtool/aclocal/libtool.m4 > aclocal.m4
# If this is the new libtool 2.x, we need to append some additional
# files.  Rather than hard-coding a version of libtool, just test
# if the files exist and append them:
for f in \
%_datadir/libtool/aclocal/ltoptions.m4 \
%_datadir/libtool/aclocal/ltversion.m4 \
%_datadir/libtool/aclocal/ltsugar.m4 \
%_datadir/libtool/aclocal/lt~obsolete.m4; do
  if [ -f $f ]; then cat $f >> aclocal.m4; fi
done

# Now we can run libtool.
libtoolize

# Automake can fail - we only need this to get config.sub and config.guess.
automake -a ||:

autoconf

%build
%_mingw32_configure --enable-shared --disable-static
%make_build

%install
mkdir -p %buildroot%_mingw32_bindir
mkdir -p %buildroot%_mingw32_includedir
mkdir -p %buildroot%_mingw32_libdir
mkdir -p %buildroot%_mingw32_mandir/man1

%_mingw32_makeinstall

# Remove manual pages which duplicate Fedora native.
rm -rf %buildroot%_mingw32_mandir

pushd %buildroot%_mingw32_bindir
# Rename or remove win32 native binaries
for i in cjpeg djpeg jpegtran rdjpgcom wrjpgcom ; do
%if %build_programs
   mv $i $i.exe
%else
   rm $i
%endif
done
popd

%files
%doc README
%if %build_programs
%_mingw32_bindir/cjpeg.exe
%_mingw32_bindir/djpeg.exe
%_mingw32_bindir/jpegtran.exe
%_mingw32_bindir/rdjpgcom.exe
%_mingw32_bindir/wrjpgcom.exe
%endif
%_mingw32_bindir/libjpeg-62.dll
%_mingw32_includedir/jconfig.h
%_mingw32_includedir/jerror.h
%_mingw32_includedir/jmorecfg.h
%_mingw32_includedir/jpeglib.h
%_mingw32_libdir/libjpeg.dll.a
%_mingw32_libdir/libjpeg.la

%changelog
* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 6b-alt1
- initial build

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 6b-9
- Rebuild for mingw32-gcc 4.4

* Wed Jan 28 2009 Richard W.M. Jones <rjones@redhat.com> - 6b-8
- Exclude the binaries.
- Rename the binaries to *.exe (Levente Farkas).

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 6b-7
- Disable static libraries.
- Use _smp_mflags.
- Update for new libtool 2.
- +BR mingw32-dlfcn.
- Added documentation (README includes the license).

* Thu Nov 20 2008 Richard W.M. Jones <rjones@redhat.com> - 6b-6
- Don't set libdir in the make step.
- Fix path to mandir.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 6b-5
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 6b-4
- Switch to tar.bz2 source, and rename configure.in

* Sun Sep 21 2008 Daniel P. Berrange <berrange@redhat.com> - 6b-3
- Fix URL.
- Remove manpages which duplicate Fedora native.

* Wed Sep 10 2008 Daniel P. Berrange <berrange@redhat.com> - 6b-2
- Rename configure.in with a prefix.
- Remove static library.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 6b-1
- Initial RPM release
