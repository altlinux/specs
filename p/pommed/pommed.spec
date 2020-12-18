Name: pommed
Version: 1.39
Release: alt9

Summary: Apple laptops hotkeys event handler
License: GPL-2.0
Group: System/Kernel and hardware

# Upstream is dead.
#Url: http://alioth.debian.org/projects/pommed

Source0: %name-%version.tar.gz
Source1: %name.init
Source2: %name.service

Patch0: pommed-1.39-alt-build.patch
Patch1: pommed-1.22-alt-fix-desktop-files.patch
Patch2: pommed-1.39-alt-rpm_opt_flags.patch
Patch3: pommed-1.39-alt-add-kbd.patch
Patch4: pommed-fix-ftbfs.patch
Patch5: pommed-MacBookPro91.patch

# http://alioth.debian.org/tracker/download.php/31066/412713/313891/5185/0001-Add-support-for-LCD-back-light-on-latest-kernels.patch
Patch10: 0001-Add-support-for-LCD-back-light-on-latest-kernels.patch

Packager: Alexey Gladkov <legion@altlinux.ru>

ExclusiveArch: x86_64

BuildRequires:  libalsa-devel libaudiofile-devel libconfuse-devel libdbus-devel libpci-devel

%description
pommed handles the hotkeys found on the Apple MacBook Pro, MacBook and
PowerBook laptops and adjusts the LCD backlight, sound volume, keyboard
backlight or ejects the CD-ROM drive accordingly.

pommed also monitors the ambient light sensors to automatically
light up the keyboard backlight on the MacBook Pro and PowerBook.

Optional support for the Apple Remote control is available.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%patch10 -p1

%build
%make_build pommed

%install
# Install pommed
mkdir -p %buildroot%_initdir/
install -p -m0755 %SOURCE1 %buildroot%_initdir/pommed

mkdir -p %buildroot%_unitdir/
install -p -m0644 %SOURCE2 %buildroot%_unitdir/

mkdir -p %buildroot%_sbindir/
cp pommed/pommed %buildroot%_sbindir/
mkdir -p %buildroot%_datadir/pommed/
cp pommed/data/*.wav %buildroot%_datadir/pommed/

mkdir -p %buildroot%_sysconfdir/dbus-1/system.d
cp pommed.conf.mactel %buildroot%_sysconfdir/pommed.conf
cp dbus-policy.conf %buildroot%_sysconfdir/dbus-1/system.d/pommed.conf

%post
%post_service pommed

%preun
%preun_service pommed

%files
%doc AUTHORS ChangeLog INSTALL README TODO
%config(noreplace) %_sysconfdir/pommed.conf
%config(noreplace) %_sysconfdir/dbus-1/system.d/pommed.conf
%attr(755,root,root) %config(noreplace) %_initdir/pommed
%_unitdir/pommed.service
%_sbindir/pommed
%dir %_datadir/pommed
%_datadir/pommed/click.wav
%_datadir/pommed/goutte.wav

%changelog
* Fri Dec 18 2020 Alexey Gladkov <legion@altlinux.ru> 1.39-alt9
- Add support for MacBookPro9,1.
- Fix ftbfs with GCC-10.
- Drop gpomme, wmpomme.

* Wed May 06 2015 Michael Shigorin <mike@altlinux.org> 1.39-alt8
- NMU: patched to add yet another keyboard ID (closes: #27230, #30285)

* Sun Jun 23 2013 Igor Zubkov <icesik@altlinux.org> 1.39-alt7
- Add lsb header to init file

* Sun Jun 23 2013 Igor Zubkov <icesik@altlinux.org> 1.39-alt6
- Fix desktop files

* Sat Jun 22 2013 Igor Zubkov <icesik@altlinux.org> 1.39-alt5
- Add systemd service file

* Thu Jun 06 2013 Igor Zubkov <icesik@altlinux.org> 1.39-alt4
- Add support for LCD back-light on latest kernels

* Tue May 08 2012 Igor Zubkov <icesik@altlinux.org> 1.39-alt3
- use RPM_OPT_FLAGS

* Tue May 08 2012 Igor Zubkov <icesik@altlinux.org> 1.39-alt2
- Add ExclusiveArch: x86_64 %%ix86

* Mon Apr 16 2012 Igor Zubkov <icesik@altlinux.org> 1.39-alt1
- 1.31 -> 1.39

* Mon Jan 18 2010 Igor Zubkov <icesik@altlinux.org> 1.31-alt1
- 1.30 -> 1.31

* Sat Oct 31 2009 Igor Zubkov <icesik@altlinux.org> 1.30-alt1
- 1.28 -> 1.30

* Thu Oct 01 2009 Igor Zubkov <icesik@altlinux.org> 1.28-alt1
- 1.27 -> 1.28

* Sun Sep 13 2009 Igor Zubkov <icesik@altlinux.org> 1.27-alt1
- 1.26 -> 1.27

* Fri Mar 27 2009 Igor Zubkov <icesik@altlinux.org> 1.26-alt2
- apply patch from repocop

* Tue Mar 24 2009 Igor Zubkov <icesik@altlinux.org> 1.26-alt1
- 1.23 -> 1.26

* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 1.23-alt1
- 1.22 -> 1.23

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 1.22-alt1
- 1.18 -> 1.22
- buildreq

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 1.18-alt3
- apply patch from repocop

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 1.18-alt2
- fix desktop files

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 1.18-alt1
- 1.17 -> 1.18

* Wed Apr 23 2008 Michael Shigorin <mike@altlinux.org> 1.17-alt1.1
- NMU: rebuilt against libpci-3.0.0

* Sat Apr 19 2008 Igor Zubkov <icesik@altlinux.org> 1.17-alt1
- 1.16 -> 1.17

* Thu Apr 03 2008 Igor Zubkov <icesik@altlinux.org> 1.16-alt2
- fix rebuild

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 1.16-alt1
- 1.15 -> 1.16

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 1.15-alt3
- fix rebuild with fresh pciutils
- buildreq

* Tue Feb 26 2008 Igor Zubkov <icesik@altlinux.org> 1.15-alt2
- add modprobe applesmc before start pommed

* Fri Feb 22 2008 Igor Zubkov <icesik@altlinux.org> 1.15-alt1
- 1.14 -> 1.15

* Sun Dec 16 2007 Igor Zubkov <icesik@altlinux.org> 1.14-alt1
- 1.13 -> 1.14

* Fri Dec 07 2007 Igor Zubkov <icesik@altlinux.org> 1.13-alt1
- 1.12 -> 1.13

* Sat Dec 01 2007 Igor Zubkov <icesik@altlinux.org> 1.12-alt1
- 1.10 -> 1.12

* Sun Oct 21 2007 Igor Zubkov <icesik@altlinux.org> 1.10-alt1
- build for Sisyphus

