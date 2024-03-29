Name: aqemu
Version: 0.9.2
Release: alt2.1
Epoch: 2

Summary: QEMU GUI written in Qt5
License: GPL-2.0 and Zlib and MIT
Group: Emulators

Url: https://github.com/tobimensch/aqemu
Packager: Boris Savelev <boris@altlinux.org>
Source: %name-%version.tar
# Source-url: https://github.com/tobimensch/aqemu/archive/%version/aqemu-%version.tar.gz
# debian patches
Patch1: 01_qemu_parallel_typo.diff
Patch2: 0002-Remove-VLAN-stuff-QEMU-doesn-t-support-it-anymore.patch
Patch5: 0005-fix-spelling-of-some-words.patch
Patch7: 0007-Fix-crash-because-of-duplicated-widget-name.patch

Requires: qemu qemu-kvm

BuildRequires(pre): cmake rpm-build-ninja
BuildRequires: gcc-c++ libvncserver-devel ImageMagick
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools

ExcludeArch: e2k e2kv4 e2kv5

%description
AQEMU is a QEMU GUI written in Qt5.
It has user-friendly interface and allows to set up the majority of QEMU options.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch5 -p1
%patch7 -p1
# gcc10
sed -i 's|#include <vector>|#include <vector>\n#include <stdexcept>|' src/docopt/docopt_value.h

%build
PATH=%_datadir/qt5/bin:$PATH; export PATH
%cmake_insource \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
#
cmake --build "%_cmake__builddir" -j1

%install
%cmake_install
mkdir -p %buildroot%_desktopdir
install -d %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
convert -size 16x16 ./resources/icons/aqemu.png %buildroot%_miconsdir/%name.png
convert -size 32x32 ./resources/icons/aqemu.png %buildroot%_niconsdir/%name.png
convert -size 48x48 ./resources/icons/aqemu.png %buildroot%_liconsdir/%name.png
rm -rf %buildroot%_datadir/doc/%name

%files
%doc README* AUTHORS* CHANGELOG* TODO*
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_miconsdir/%name.png
%_niconsdir/%name.png
%_man1dir/%{name}*
%_pixmapsdir/*.png

%changelog
* Sat Oct 08 2022 Michael Shigorin <mike@altlinux.org> 2:0.9.2-alt2.1
- E2K: exclude <v6 (no virtualization support)
- minor spec cleanup

* Wed Aug 31 2022 Leontiy Volodin <lvol@altlinux.org> 2:0.9.2-alt2
- Backported to 0.9.2 version.
- Applied patches from debian (ALT #42293):
  + Removed vlan support (it doesn't work anymore).
  + Fixed spelling of some words.
  + Fixed crash because of duplicated widget name.
  + Fixed type when lpt parallel option is selected.

* Tue Mar 29 2022 Leontiy Volodin <lvol@altlinux.org> 1:0.9.4-alt3
- Fixed errors in some settings (ALT #25201).

* Mon Mar 21 2022 Leontiy Volodin <lvol@altlinux.org> 1:0.9.4-alt2
- Fixed segfault on restart (ALT #42188).

* Wed Jan 27 2021 Leontiy Volodin <lvol@altlinux.org> 1:0.9.4-alt1
- 0.9.4 version (more stable).

* Fri Jan 15 2021 Leontiy Volodin <lvol@altlinux.org> 0.9.6-alt0.1.git34ca8ce
- 0.9.6 development version.
- Built with meson instead cmake.

* Sat Oct 22 2016 L.A. Kostis <lakostis@altlinux.ru> 0.9.2-alt0.1
- 0.9.2 release.

* Sat May 28 2016 L.A. Kostis <lakostis@altlinux.ru> 0.9.1-alt0.1
- New version, now with qt5 support.

* Mon Mar 19 2012 Boris Savelev <boris@altlinux.org> 0.8.2-alt1
- new version (0.8.2) with rpmgs script

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1.qa1
- NMU: dropped obsolete menu entry

* Mon Jul 12 2010 Boris Savelev <boris@altlinux.org> 0.8-alt1
- new version (0.8) (Closes: #23758)
- build from upstream git

* Wed Sep 30 2009 Boris Savelev <boris@altlinux.org> 0.7.3-alt1
- new version (0.7.3)

* Sat Jun 27 2009 Boris Savelev <boris@altlinux.org> 0.7.2-alt1
- new version (0.7.2)

* Fri Apr 10 2009 Boris Savelev <boris@altlinux.org> 0.7.1-alt1
- new version (0.7.1)

* Wed Mar 04 2009 Boris Savelev <boris@altlinux.org> 0.7-alt1
- new version (0.7)

* Fri Jan 30 2009 Boris Savelev <boris@altlinux.org> 0.6.1-alt1
- new version (0.6.1)

* Wed Dec 17 2008 Boris Savelev <boris@altlinux.org> 0.6-alt1
- new version

* Thu Nov 13 2008 Boris Savelev <boris@altlinux.org> 0.5.2-alt2
- clean desktop and menu files (fix #17666)

* Fri Oct 17 2008 Boris Savelev <boris@altlinux.org> 0.5.2-alt1
- New Manage QEMU Binary Window
- Minor Interface Rebuilding.
- More Bug Fix

* Thu Sep 18 2008 Boris Savelev <boris@altlinux.org> 0.5.1-alt1
- New Network Option "Hostname".
- New OS Logos Icons (From Qemulator).
- Minor Interface Rebuilding.
- Major Bug Fix.
- Change package group.

* Wed Sep 03 2008 Boris Savelev <boris@altlinux.org> 0.5-alt1
- initial build
