%global __strip %_mingw32_strip
%global __objdump %_mingw32_objdump

Name: mingw32-pixman
Version: 0.15.10
Release: alt1
Summary: MinGW Windows Pixman library

License: MIT
Url: http://xorg.freedesktop.org/
Group: System/Libraries

Packager: Boris Savelev <boris@altlinux.org>

Source: http://xorg.freedesktop.org/archive/individual/lib/pixman-%version.tar.gz
Source1: make-pixman-snapshot.sh

BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-dlfcn

Requires: pkgconfig

%description
MinGW Windows Pixman library.

%package static
Summary: Static version of the MinGW Windows Pixman library
Requires: %name = %version-%release
Group: System/Libraries

%description static
Static version of the MinGW Windows Pixman library.

%prep
%setup -q -n pixman-%version

%build
# Uses GTK for its testsuite, so disable this otherwise
# we have a chicken & egg problem on mingw
%_mingw32_configure --disable-gtk --enable-static --enable-shared
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%_mingw32_bindir/libpixman-1-0.dll
%_mingw32_includedir/pixman-1
%_mingw32_libdir/libpixman-1.dll.a
%_mingw32_libdir/libpixman-1.la
%_mingw32_libdir/pkgconfig/pixman-1.pc

%files static
%_mingw32_libdir/libpixman-1.a

%changelog
* Fri Jul 31 2009 Boris Savelev <boris@altlinux.org> 0.15.10-alt1
- initial build

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.15.10-1
- Update to 0.15.10
- Use %%global instead of %%define
- Dropped pixman-0.13.2-license.patch as freedesktop bug #19582 is resolved

* Fri Apr  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.13.2-5
- Fixed %%defattr line
- Added -static subpackage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 0.13.2-3
- Rebuild for mingw32-gcc 4.4

* Thu Jan 15 2009 Richard W.M. Jones <rjones@redhat.com> - 0.13.2-2
- Include LICENSE file (freedesktop bug 19582).

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 0.13.2-1
- Resynch with Fedora package (0.13.2).
- Disable static library for speed.
- Use _smp_mflags.
- Requires pkgconfig.
- Depends on dlfcn.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 0.12.0-2
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 0.12.0-1
- Update to 0.12.0 release

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 0.11.10-2
- Remove static library.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 0.11.10-1
- Initial RPM release
