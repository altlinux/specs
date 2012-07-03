%define __strip %_mingw32_strip
%define __objdump %_mingw32_objdump

Name: mingw32-libpng
Version: 1.2.37
Release: alt1
Summary: MinGW Windows Libpng library

License: zlib
Url: http://www.libpng.org/pub/png/
Packager: Boris Savelev <boris@altlinux.org>

Source: ftp://ftp.simplesystems.org/pub/png/src/libpng-%version.tar.bz2
Patch: libpng-multilib.patch
Patch1: libpng-pngconf.patch

Group: System/Libraries

BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-zlib

Requires: pkgconfig

%description
MinGW Windows Libpng library.

%prep
%setup -q -n libpng-%version
%patch0 -p1
%patch1 -p1

%build
%_mingw32_configure
%make

%install
%makeinstall_std

rm %buildroot%_mingw32_libdir/libpng.a

# No need to distribute manpages which appear in the Fedora
# native packages already.
rm -rf %buildroot%_mingw32_mandir

%files
%doc ANNOUNCE CHANGES KNOWNBUG LICENSE README TODO Y2KINFO
%_mingw32_bindir/libpng-3.dll
%_mingw32_bindir/libpng-config
%_mingw32_bindir/libpng12-0.dll
%_mingw32_bindir/libpng12-config
%_mingw32_includedir/libpng12
%_mingw32_includedir/png.h
%_mingw32_includedir/pngconf.h
%_mingw32_libdir/libpng.dll.a
%_mingw32_libdir/libpng.la
%_mingw32_libdir/libpng12.a
%_mingw32_libdir/libpng12.dll.a
%_mingw32_libdir/libpng12.la
%_mingw32_libdir/pkgconfig/libpng.pc
%_mingw32_libdir/pkgconfig/libpng12.pc

%changelog
* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 1.2.37-alt1
- intial build

* Tue Jun  9 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.37-1
- New upstream version 1.2.37 to fix SECURITY bug RHBZ#504782.

* Wed Feb 25 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.35-1
- Update to libpng 1.2.35, to fix CVE-2009-0040 (Tom Lane).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.34-3
- Rebuild for mingw32-gcc 4.4

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.34-2
- Depend on mingw32-filesystem >= 40 so we can still build in F-10.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.34-1
- Rebase to 1.2.34 and patches from Fedora.
- Requires pkgconfig.
- Add documentation.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.31-5
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 1.2.31-4
- Add patches from rawhide RPM

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.31-3
- Don't duplicate Fedora native manpages.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.31-2
- Remove static library.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 1.2.31-1
- Initial RPM release
