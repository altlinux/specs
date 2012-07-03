Name: shake
Version: 0.99
Release: alt2

Summary: Userspace filesystem defragmenter

License: GPL
Group: System/Configuration/Hardware
Url: http://vleu.net/shake/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.twaren.net/Unix/NonGNU/shake/%name-%version.tar.bz2

# Automatically added by buildreq on Fri Jan 02 2009
BuildRequires: ccmake gcc-c++ help2man libattr-devel

%description
Shake is a defragmenter that runs in userspace and works on a live system.
It just works by rewriting fragmented files. But it has some heuristics that
could make it more efficient than other tools, including defrag and, maybe,
xfs_fsr.

See
http://mydebianblog.blogspot.com/2008/05/linux_19.html

%prep
%setup

%build
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

%files
%_bindir/shake
%_bindir/unattr
%_man8dir/*

%changelog
* Wed Nov 25 2009 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt2
- build with new cmake macro

* Tue Apr 28 2009 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt1
- new version 0.99 (with rpmrb script)

* Fri Jan 02 2009 Vitaly Lipatov <lav@altlinux.ru> 0.31-alt1
- initial build for ALT Linux Sisyphus

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.29-4mdv2009.0
+ Revision: 260648
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.29-3mdv2009.0
+ Revision: 252386
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Nov 21 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.29-1mdv2008.1
+ Revision: 111001
- import shake

* Wed Nov 21 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.29-1mdv2008.1
- initial release
