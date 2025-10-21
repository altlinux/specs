Name: xtruss
Version: 20250428
Release: alt1
Summary: Trace X protocol exchanges, in the manner of strace
License: X11
Group: System/X11
Source: %name-%version.tar.gz
Url: http://www.chiark.greenend.org.uk/~sgtatham/xtruss/

# Automatically added by buildreq on Tue Oct 21 2025
# optimized out: bash5 cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libp11-kit libsasl2-3 perl pkg-config python2-base python3 python3-base sh5
BuildRequires: cmake halibut xorg-xcbproto-devel rpm-build-python3

# TODO is the provided generator handy?
%description
XTruss is a utility which logs everything that passes between
the X server and one or more X client programs. In this it is
similar to xmon(1), but intended to combine xmon's basic
functionality with an interface much more similar to strace(1).

%prep
%setup

%build
%cmake -DUSING_XTRGEN=Yes
%cmake_build
rm %name.1
halibut --man=%name.1 doc/man-xtruss.but

%install
%cmakeinstall_std
install -D xtrgen.py %buildroot%_bindir/xtrgen.py

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Tue Oct 21 2025 Fr. Br. George <george@altlinux.org> 20250428-alt1
- Autobuild version bump to 20250428
- Introduce generated XCB proto profile

* Tue Jun 21 2022 Fr. Br. George <george@altlinux.org> 20211025-alt1
- Autobuild version bump to 20211025

* Thu Jan 28 2021 Fr. Br. George <george@altlinux.ru> 20200918-alt1
- Autobuild version bump to 20200918

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 20181001-alt1
- Autobuild version bump to 20181001

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 20150926-alt1
- Autobuild version bump to 20150926

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 20150529-alt1
- Autobuild version bump to 20150529

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 20150103-alt1
- Autobuild version bump to 20150103

* Thu Dec 11 2014 Fr. Br. George <george@altlinux.ru> 20141026-alt1
- Autobuild version bump to 20141026

* Mon Sep 29 2014 Fr. Br. George <george@altlinux.ru> 10272-alt1
- Autobuild version bump to 10272
- Fix upstream versioning

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 10030-alt1
- Autobuild version bump to 10030

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 9879-alt1
- Autobuild version bump to 9879

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 9854-alt1
- Autobuild version bump to 9854

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 9490-alt1
- Autobuild version bump to 9490

* Wed Sep 01 2010 Fr. Br. George <george@altlinux.ru> 8615-alt2
- Homepage URL added

* Mon Aug 23 2010 Fr. Br. George <george@altlinux.ru> 8615-alt1
- Initial build for ALT

