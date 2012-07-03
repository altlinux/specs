%def_enable static

Name: libusb
Version: 1.0.9
Release: alt2
Summary: Libusb is a library which allows userspace access to USB devices
License: LGPL
Group: System/Libraries
Url: http://sourceforge.net/projects/libusb/
Packager: Alexander Bokovoy <ab@altlinux.org>

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: docbook-dtds docbook-style-dsssl docbook-utils doxygen graphviz openjade sgml-common gcc-c++

%description
Libusb is a library which allows userspace access to USB devices

%package devel
Summary: Libusb is a library which allows userspace access to USB devices
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains header files needed for the development of programs that
use libusb

%package devel-static
Summary: Libusb is a library which allows userspace access to USB devices
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package provides static libraries to use libusb

%package doc
Summary: Libusb is a library which allows userspace access to USB devices
Group: Development/C
BuildArch: noarch
Requires: %name = %version-%release

%description doc
This package contains documentation for %name

%prep
%setup -q
%patch -p1

mkdir -p m4

%build
%autoreconf
%configure \
	%{subst_enable static}
%make_build
%make -C doc docs

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/lib*.so; do
	t=$(readlink "$f")
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/lib*.so.* %buildroot/%_lib/

%files
/%_lib/%name-*.so.*
%doc AUTHORS README NEWS THANKS TODO

%files devel
%_libdir/%name-*.so
%_includedir/*
%_pkgconfigdir/%name-*.pc

%if_enabled static
%files devel-static
%_libdir/%name-*.a
%endif

%files doc
%doc doc/html

%changelog
* Sat Apr 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt2
- 1.0.9

* Fri Dec 02 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.9-alt1.rc3
- 1.0.9-rc3
- disabled symbol versioning

* Fri Mar 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt3
- rebuild for debuginfo

* Wed Nov 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt2
- rebuild

* Fri May 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Sun Apr 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Thu Feb 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Thu Dec 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Wed May 20 2009 Alexander Bokovoy <ab@altlinux.org> 1.0.1-alt1
- 1.0.1
- Include fixes from git.alt:/people/shrek/packages/libusb.git of 1.0-alt3
- libusb-1.0.so.* library now is in /lib. 
- Compatibility library is left in secondary system library path

* Wed May 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt3
- relocate libusb-1.0.so.* to /lib

* Sun Mar 29 2009 Alexander Bokovoy <ab@altlinux.org> 1.0-alt2
- 1.0
- Include ALT-specific fixes

* Sat Nov 22 2008 Alexander Bokovoy <ab@altlinux.org> 0.9.4-alt2.0
- Fixed:
  + Memory leaks in processing active configuration descriptors

* Sat Nov 22 2008 Alexander Bokovoy <ab@altlinux.org> 0.9.4-alt1.0
- Update to 0.9.4 and libusb-compat-0.1-beta3

* Wed Oct 01 2008 Alexander Bokovoy <ab@altlinux.org> 0.9.3-alt3.0
- Fixed:
  + Work around bad code in KDE that attempts to close non-opened USB devices for now
  + Issue a warning about a frivolous use of usb_close(NULL) at application level which
    was tolerated by libusb 0.1. Should fix #17352

* Thu Sep 18 2008 Alexander Bokovoy <ab@altlinux.org> 0.9.3-alt2.0
- Add x86_64 support

* Sun Sep 14 2008 Alexander Bokovoy <ab@altlinux.org> 0.9.3-alt1.0
- New version
- Package libusb-compat-0.1 to keep compatibility with old code

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.12-alt1.0
- Automated rebuild.

* Fri Apr 28 2006 Anton Farygin <rider@altlinux.ru> 0.1.12-alt1
- new version

* Tue Sep 13 2005 Anton Farygin <rider@altlinux.ru> 0.1.10a-alt3
- enabled devel-static packages

* Thu Sep 08 2005 Anton Farygin <rider@altlinux.ru> 0.1.10a-alt2
- new version, with specfile from wrar@ (#7580, #7579)

* Sat Aug 06 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.10a-alt1
- 0.1.10a
- removed outdated docs, packaged bundled docs (#7580)

* Mon Apr 26 2004 Anton Farygin <rider@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Sun Dec 14 2003 Rider <rider@altlinux.ru> 0.1.7-alt2
- removed .la files

* Mon Jan 06 2003 Rider <rider@altlinux.ru> 0.1.7-alt1
- 0.1.7
- added build requires 

* Mon Sep 16 2002 Rider <rider@altlinux.ru> 0.1.6a-alt2
- gcc 3.2 rebuild

* Sat Aug 24 2002 Rider <rider@altlinux.ru> 0.1.6a-alt1
- 0.1.6a

* Sun Feb 10 2002 Rider <rider@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Thu Dec 06 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.1.4-alt1
- 0.1.4
- Added documentation

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.1.3b-alt2
- Fixed requires
- Added devel-static package

* Fri Aug 24 2001 Rider <rider@altlinux.ru> 0.1.3b-alt1
- First build for ALT

* Thu Mar  1 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1.3b-1mdk
- Initial Mandrake release
