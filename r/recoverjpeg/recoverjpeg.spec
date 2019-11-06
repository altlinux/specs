Name: recoverjpeg
Version: 2.6.3
Release: alt2

Summary: Recover jpeg pictures and mov movies from damaged devices
License: GPLv2
Group: File tools

Url: http://www.rfc1149.net/devel/recoverjpeg
Source0: http://www.rfc1149.net/download/%name/%name-%version.tar.gz
Source1: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++

%add_findreq_skiplist  %_bindir/sort-pictures

%description
recoverjpeg tries to recover JFIF (JPEG) pictures
and MOV movies (using recovermov) from a peripheral.
This may be useful if you mistakenly overwrite
a partition or if a device such as a digital camera
memory card is bogus.

NB: sort-pictures(1) requires ImageMagick-tools, exif
    which aren't included into package dependencies
    so as to keep it X-free for minimal rescue images

%prep
%setup

sed -i 's|#! /usr/bin/python|#!/usr/bin/python3|' scripts/remove-duplicates

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/recovermov
%_bindir/remove-duplicates
%_bindir/sort-pictures
%_bindir/%name
%_man1dir/*.1*


%changelog
* Wed Nov 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.6.3-alt2
- python2 -> python3

* Mon Sep 17 2018 Michael Shigorin <mike@altlinux.org> 2.6.3-alt1
- new version (watch file uupdate)

* Tue Apr 03 2018 Michael Shigorin <mike@altlinux.org> 2.6.2-alt1
- new version (watch file uupdate)

* Sat Nov 12 2016 Michael Shigorin <mike@altlinux.org> 2.6.1-alt1
- new version (watch file uupdate)

* Mon Oct 12 2015 Michael Shigorin <mike@altlinux.org> 2.6-alt1
- new version (watch file uupdate)

* Tue Sep 22 2015 Michael Shigorin <mike@altlinux.org> 2.4-alt1
- new version (watch file uupdate)

* Mon Aug 10 2015 Michael Shigorin <mike@altlinux.org> 2.3-alt1
- new version (watch file uupdate)

* Tue Apr 22 2014 Michael Shigorin <mike@altlinux.org> 2.2.3-alt1
- initial build for ALT Linux Sisyphus based on fedora package

* Mon May 27 2013 Christopher Meng <rpm@cicku.me> - 2.2.3-2
- SPEC cleanup.

* Wed May 01 2013 Christopher Meng <rpm@cicku.me> - 2.2.3-1
- New upstream release with minor fixes.

* Sun Apr 14 2013 Christopher Meng <rpm@cicku.me> - 2.2.2-1
- Initial Package.
