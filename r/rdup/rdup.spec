# TODO: send patches to mainstream
Name: rdup
Version: 0.6.3
Release: alt1

Summary: prints filenames for backup

License: GPL
Group: File tools
Url: http://www.miek.nl/projects/rdup/index.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.miek.nl/projects/%name/%name-%version.tar.bz2
Patch: %name-0.6.2.patch
#AutoReq: yes, noperl

# manually removed: rpm-build-java rpm-build-mono rpm-build-seamonkey rpm-macros-fillup xorg-sdk
# Automatically added by buildreq on Thu Dec 11 2008 (-bi)
BuildRequires: glib2-devel libpcre-devel

%description
rdup is a utility inspired by rsync and the plan9 way of doing backups.
rdup it self does not backup anything, it only print a list of absolute
filenames to standard output. Auxilary scripts are needed that act on
this list and implement the backup strategy.

%prep
%setup -q
%patch

%build
%configure
%make_build

%install
mkdir -p %buildroot%_bindir
%makeinstall_std

%files
%doc AUTHORS DEPENDENCIES ChangeLog README DESIGN todo
%_bindir/rdup
%_man1dir/*
%_datadir/%name/


%changelog
* Thu Dec 11 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script)

* Mon Jul 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Wed Nov 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt0.1
- new version 0.3.0
- update buildreq, disable perl autoreq

* Sat May 27 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.13-alt0.1
- new version 0.2.13
- enable make_build
- add new directories to doc

* Fri Mar 17 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt0.1
- new version 0.2.5 (with rpmrb script)

* Sat Mar 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt0.1
- new version 0.2.4
- fix objects order for ld(v)

* Thu Mar 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt0.1
- new version 0.2.3 (with rpmrb script)

* Fri Feb 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt0.1
- new version 0.2.2 (with rpmrb script)

* Fri Feb 17 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt0.1
- initial build for ALT Linux Sisyphus
