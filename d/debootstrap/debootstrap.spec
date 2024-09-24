Name: debootstrap
Version: 1.0.137
Release: alt1
Summary: Debian GNU/Linux bootstrapper

Group: System/Base
License: MIT
Url: http://code.erisian.com.au/Wiki/debootstrap

# Repacked http://ftp.debian.org/debian/pool/main/d/debootstrap/%{name}_%version.tar.gz
Source: %name-%version.tar
Patch1: debootstrap-alt-mask-optional-reqs.patch

BuildArch: noarch

Requires: wget, tar

%description
debootstrap is used to create a Debian base system from scratch, without
requiring the availability of dpkg or apt.  It does this by downloading
.deb files from a mirror site, and carefully unpacking them into a
directory which can eventually be chrooted into.

This might be often useful coupled with virtualization techniques to run
Debian GNU/Linux guest system.

%prep
%setup
%patch1 -p2

%install
install -d %buildroot%_datadir/debootstrap/scripts/
install -d %buildroot%_sbindir
install -d %buildroot%_man8dir
install -p -m 0644 debootstrap.8 %buildroot%_man8dir
%makeinstall_std \
       VERSION="%version-%release" \
       DSDIR=%buildroot%_datadir/debootstrap
# correct the debootstrap script timestamp
touch -r debootstrap  %buildroot%_sbindir/debootstrap

%files
%_datadir/debootstrap
%_sbindir/debootstrap
%_man8dir/debootstrap.8*
%doc debian/changelog debian/copyright README

%changelog
* Mon Sep 23 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.137-alt1
- Updated to 1.0.137.

* Wed Jan 24 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.134-alt1
- Updated to 1.0.134.

* Wed Dec 20 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.133-alt1
- Updated to 1.0.133.

* Sat Sep 02 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.132-alt1
- Updated to 1.0.132.

* Sun Aug 20 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.131-alt1
- Updated to 1.0.131.

* Sun Aug 20 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.130-alt1
- Updated to 1.0.130.

* Tue Jul 18 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.128.nmu5-alt1
- Updated to 1.0.128+nmu5.

* Tue Nov 16 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.126-alt1
- Updated to 1.0.126.

* Fri Aug 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.115-alt1
- Updated to 1.0.115.

* Fri May 10 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.114-alt1
- Updated to 1.0.114.

* Fri Oct 14 2011 Denis Baranov <baraka@altlinux.ru> 1.0.36-alt2
- add devices.tar.gz in package

* Fri Oct 14 2011 Denis Baranov <baraka@altlinux.ru> 1.0.36-alt1
- initial build for ALT Linux Sisyphus

* Mon Aug 22 2011 Jan Vcelak <jvcelak@redhat.com> 1.0.36-1
- new upstream release:
  + use md5sum for 'sarge'
  + improve error message when decompressing command is not available
  + add more information regarding the version and architecture in case a download fails
  + do not use --arch when we specifically care about the host architecture
  + guess host OS based on uname for non-Debian systems
  + clarify "target" in usage message
  + search PATH for programs, rather than checking hardcoded locations
  + various fixes for installing kFreeBSD

* Mon Jun 20 2011 Jan Vcelak <jvcelak@redhat.com> 1.0.32-1
- new upstream release:
  + use md5sums for 'woody' and 'potato'

* Mon May 23 2011 Jan Vcelak <jvcelak@redhat.com> 1.0.31-1
- bootstrapping Ubuntu systems:
  + recommend ubuntu-keyring instead of debian-archive-keyring
  + check signatures when ubuntu-keyring package is installed

* Fri May 20 2011 Jan Vcelak <jvcelak@redhat.com> 1.0.30-1
- new upstream release:
  + support bootstraping Debian oldstable
  + Ubuntu Oneiric symlink to Gutsy
  + removed --boot-floppies switch and mode
  + various fixes in package GPG signatures checking

* Tue Mar 08 2011 Jan Vcelak <jvcelak@redhat.com> 1.0.28-1
- new upstream release:
  + fix: bug in the ar extractor for non-gz data.tar in .debs (Debian #598729)
  + remove 5 second sleeps when debootstrap finds additional required dependencies
  + use SHA checksums instead of MD5
  + avoid new warning from dpkg about missing Maintainer field

* Wed Feb 09 2011 Jan Vcelak <jvcelak@redhat.com> 1.0.27-1
- new upstream release (typo in --private-key, improve Hurd support)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Jan Vcelak <jvcelak@redhat.com> 1.0.26-1
- new upstream release (fix typos and remove old workaround for md5sum)

* Mon Oct 25 2010 Jan Vcelak <jvcelak@redhat.com> 1.0.25-1
- new upstream release (support for HTTPS, added Ubuntu Nanty, added Debian Wheezy)

* Wed May 26 2010 Jan Zeleny <jzeleny@redhat.com> - 1.0.23-1
- rebased to 1.0.23 (Add ${misc:Depends}, Add (Ubuntu) maverick as symlink to gutsy)

* Fri Mar 05 2010 Jan Zeleny <jzeleny@redhat.com> - 1.0.22-1
- rebased to 1.0.22

* Wed Sep 30 2009 Adam Goode <adam@spicenitz.org> - 1.0.19-2
- Make sure to create /dev/console in devices.tar.gz

* Wed Sep 30 2009 Adam Goode <adam@spicenitz.org> - 1.0.19-1
- New upstream release
   + Many bugfixes
   + Support for new distributions
- Arch patch no longer needed
- Rebase other patches

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Lubomir Rintel <lkundrak@v3.sk> - 1.0.10-1
- New upstream version

* Sun Jun 15 2008 Adam Goode <adam@spicenitz.org> - 1.0.9-1
- 1.0.9

* Fri Feb 22 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1.0.8-1
- 1.0.8

* Sun Nov 18 2007 Patrice Dumas <pertusus@free.fr> 1.0.7-2
- keep timestamps
- use rpm macros instead of hardcoded paths

* Sat Nov 17 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.7-1
- Version bump

* Thu Nov 15 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-2
- Some more fixes, thanks to Patrice Dumas (#329291)

* Fri Oct 12 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-1
- Incorporating advises from Patrice Dumas (#329291) in account

* Fri Oct 12 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.3.3.2etch1-1
- Initial package
