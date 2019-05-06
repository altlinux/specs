Name: libfprint
Version: 0.7.0
Release: alt2

Summary: Tool kit for fingerprint scanner
License: LGPLv2+
Group: System/Libraries

Url: http://www.freedesktop.org/wiki/Software/fprint/libfprint
# git://anongit.freedesktop.org/libfprint/libfprint
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libusb-devel libnss-devel glib2-devel libImageMagick-devel libXv-devel libpixman-devel
BuildRequires: gcc-c++ doxygen

%description
The fprint project aims to support for consumer fingerprint reader
devices.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1
mkdir -p m4

%build
%ifarch %e2k
# lcc 1.23.12's frontend is more strict...
sed -i 's,int main(void),&;,' configure.ac
%endif
%autoreconf
%configure \
	--disable-static \
	--enable-udev-rules \
	--with-udev-rules-dir=%_sysconfdir/udev/rules.d \
	--enable-examples-build \
	--enable-x11-examples-build
%make_build
pushd doc
%make docs
popd

%install
%makeinstall_std

%files
%doc COPYING INSTALL NEWS TODO THANKS AUTHORS README
%_libdir/*.so.*
%_sysconfdir/udev/rules.d/60-fprint-autosuspend.rules

%files devel
%doc HACKING doc/html
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- fix build on e2k with lcc
- minor spec cleanup

* Fri Aug 18 2017 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1
- new version

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 0.4.0-alt3
- Rebuild with new libImageMagick

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 0.4.0-alt2
- Rebuild with new libImageMagick

* Thu Oct 25 2012 Ivan Ovcherenko <asdus@altlinux.org> 0.4.0-alt1
- 0.4.0 with git updates

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.2.0-alt3
- Rebuild with new libImageMagick

* Mon Sep 13 2010 Anton Farygin <rider@altlinux.ru> 0.2.0-alt2
- rebuild with new libImageMagick

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 0.2.0-alt1
- new version

* Sat Jun 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt0.pre2
- 0.1.0-pre2

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt0.pre1
- 0.1.0-pre1

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.6-alt2
- rebuild with libMagickCore.so.1

* Sat May 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.6-alt1
- initial release

