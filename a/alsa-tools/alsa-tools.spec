%define basever 1.1.0

Name: alsa-tools
Version: 1.1.5
Release: alt2

Summary: Advanced Linux Sound Architecture (ALSA) tools
License: GPL
Group: System/Kernel and hardware

Url: http://www.alsa-project.org/
Source0: %name-%version.tar
Source1: 90-alsa-tools-firmware.rules
Patch: %name-%version-%release.patch
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Obsoletes: hda-verb < 0.4
Obsoletes: alsa2-tools < 0.9.4
Provides: alsa2-tools = %version
Requires: libalsa >= %basever
# echomixer
Requires: fonts-bitmap-misc
# due to %%_bindir/as10k1
Conflicts: emu10k1-tools
# someone remind me how to cheat SourceIfExists clones
Provides: /etc/default/ld10k1

BuildRequires: gcc-c++ libgtk+2-devel libgtk+3-devel
BuildRequires: libalsa-devel >= %basever

%define udevdir /lib/udev

Summary(ru_RU.UTF-8): Инструменты ALSA
Summary(uk_UA.UTF-8): Інструменти ALSA

%description
Advanced Linux Sound Architecture (ALSA) tools. Modularized architecture
with support for a large range of ISA and PCI cards. Fully compatible
with OSS/Lite but contains many enhanced features.

You may install this package if you really want use this low-level utils
with some audio cards.

%description -l ru_RU.UTF-8
Пакет содержит инструменты ALSA (современной звуковой подсистемы Linux),
предназначенные для низкоуровневой работы с некоторыми звуковыми картами
(на чипах Envy24, EMU10K1).

%description -l uk_UA.UTF-8
Пакунок містить інструменти ALSA (сучасної звукової підсистеми Linux),
що застосовуються для низькорівневої роботи із деякими звуковими
картками (на чіпах Envy24, EMU10K1).

%package -n hwmixvolume
Summary: Control individual streams volume on hardware-mixing soundcards
Group: System/Kernel and hardware
BuildArch: noarch

%description -n hwmixvolume
This tool allows you to control the volume of individual streams
on sound cards that use hardware mixing, i.e., those based on the
following chips:
* Creative Emu10k1 (SoundBlaster Live!) (driver: snd-emu10k1)
* VIA VT823x southbridge (driver: snd-via82xx)
* Yamaha DS-1 (YMF-724/740/744/754) (driver: snd-ymfpci)

It is recommended to use at least Linux kernel 2.6.32
or alsa-driver 1.0.22; otherwise, the name of the program
that is using a stream cannot be shown.

%package -n hdajackretask
Summary: ALSA soundcard jack task manipulation tool
Group: System/Kernel and hardware

%description -n hdajackretask
Most HDA Intel soundcards are to some degree retaskable, i.e. can
be used for more than one thing. This tool is a GUI to make it
easy to retask your jacks - e g, turn your Mic jack into an extra
Headphone, or why not make them both line outs and connect them
to your surround receiver?

%package -n ld10k1
Summary: EMU10K1 patch loader/linker
Group: System/Kernel and hardware

%description -n ld10k1
EMU10K1 patch loader/linker, see also as10k1

%package -n liblo10k1
Summary: lo10k1 library
Group: System/Libraries

%description -n liblo10k1
lo10k1 library

%package -n liblo10k1-devel
Summary: lo10k1 library, development part
Group: Development/C

%description -n liblo10k1-devel
lo10k1 library, development part

%prep
%setup
%patch -p1

mv seq/sbiload sbiload
rm -rf {seq,hdsp*,qlo10k1}

%build
export PATH=$PATH:$(pwd)/as10k1
for d in *; do
	if [ -d $d ]; then
		cd $d
		%autoreconf
		%configure
		%make_build
		cd ..
	fi
done

%install
for d in *; do
	if [ -d $d ]; then
		cd $d
		%makeinstall_std
		cd ..
	fi
done

# convert hotplug stuff to udev
rm -f %buildroot%_sysconfdir/hotplug/usb/tascam_fw.usermap
mkdir -p %buildroot{%udevdir,%_udevrulesdir}
mv %buildroot%_sysconfdir/hotplug/usb/* %buildroot%udevdir/
install -pm644 %SOURCE1 %buildroot%_udevrulesdir/

%files
%exclude %_bindir/hdajackretask
%exclude %_bindir/hwmixvolume
%exclude %_bindir/lo10k1
%_bindir/*
%_datadir/sounds/opl3
%_man1dir/*
%_udevrulesdir/*.rules
%udevdir/tascam_fpga
%udevdir/tascam_fw

%files -n hdajackretask
%_bindir/hdajackretask

%files -n hwmixvolume
%_bindir/hwmixvolume

%files -n ld10k1
%_bindir/lo10k1
%_sbindir/*
%_datadir/ld10k1

%files -n liblo10k1
%_libdir/liblo10k1.so.*

%files -n liblo10k1-devel
%_includedir/lo10k1
%_libdir/liblo10k1.so
%_datadir/aclocal/ld10k1.m4

# TODO:
# - consider http://cvs.fedoraproject.org/viewvc/rpms/alsa-tools/devel/

%changelog
* Sat Dec 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt2
- NMU: added Obsoletes: hda-verb

* Wed Nov 22 2017 Michael Shigorin <mike@altlinux.org> 1.1.5-alt1
- 1.1.5

* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 1.1.3-alt1
- 1.1.3

* Mon Nov 09 2015 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- 1.1.0

* Mon Mar 02 2015 Michael Shigorin <mike@altlinux.org> 1.0.29-alt2
- moved 90-alsa-tools-firmware.rules file
  from %_sysconfdir/udev/rules.d/
    to %_udevrulesdir/

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 1.0.29-alt1
- 1.0.29

* Wed Jun 18 2014 Michael Shigorin <mike@altlinux.org> 1.0.28-alt1
- 1.0.28

* Sat Apr 13 2013 Michael Shigorin <mike@altlinux.org> 1.0.27-alt2
- retag

* Sat Apr 13 2013 Michael Shigorin <mike@altlinux.org> 1.0.27-alt1
- 1.0.27

* Fri Sep 07 2012 Michael Shigorin <mike@altlinux.org> 1.0.26.1-alt4
- fixed udev rules (closes: #27623)

* Fri Sep 07 2012 Michael Shigorin <mike@altlinux.org> 1.0.26.1-alt3
- merge gears repo

* Fri Sep 07 2012 Michael Shigorin <mike@altlinux.org> 1.0.26.1-alt2
- retag

* Thu Sep 06 2012 Michael Shigorin <mike@altlinux.org> 1.0.26.1-alt1
- 10.26.1
- added hdajackretask subpackage (requires GTK3)

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.24.1-alt2.1.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Michael Shigorin <mike@altlinux.org> 1.0.24.1-alt2.1
- hwmixvolume made noarch

* Fri Jun 24 2011 Michael Shigorin <mike@altlinux.org> 1.0.24.1-alt2
- moved hwmixvolume into a subpackage of its own (requires pygtk)
  + thanks sr@ for bringing attention to this

* Wed Feb 16 2011 Michael Shigorin <mike@altlinux.org> 1.0.24.1-alt1
- 1.0.24.1

* Thu Oct 21 2010 Michael Shigorin <mike@altlinux.org> 1.0.23-alt1
- 1.0.23

* Thu Dec 17 2009 Michael Shigorin <mike@altlinux.org> 1.0.22-alt2
- adapted hotplug->udev tascam handling from fedora spec
- added fonts-bitmap-misc dependency for echomixer (RH#503284)

* Thu Dec 17 2009 Michael Shigorin <mike@altlinux.org> 1.0.22-alt1
- 1.0.22

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt3
- fixed firmware path

* Sun May 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt2
- rebuild

* Thu May 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt1
- 1.0.20

* Mon Jan 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.19-alt1
- 1.0.19

* Wed Oct 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.18-alt1
- 1.0.18

* Wed Jul 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt1
- 1.0.17

* Thu May 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.16-alt1
- 1.0.16

* Sun Jan 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.15-alt1
- 1.0.15
- qlo10k1 build
- spec cleanup
- update build dependencies

* Tue Sep 18 2007 Kirill A. Shutemov <kas@altlinux.ru> 1.0.14-alt1.1
- NMU
- Drop BuildRequires: kernel-headers-std. Use glibc-kernheaders instead.

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.0.14-alt1
- 1.0.14
- updated buildrequires
- set _unpackaged_files_terminate_build

* Mon Oct 16 2006 Michael Shigorin <mike@altlinux.org> 1.0.13-alt1
- 1.0.13 (codename Dirty Hack)
- s/2\.4/2.6/
- disabled new-and-ugly qlo10k1 build for now
- worked around echomixer, envy24control, rmedigicontrol
  build regressions with --as-needed
- split off ld10k1, liblo10k1{,devel} subpackages

* Wed Apr 19 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt1
- 1.0.11

* Wed Apr 05 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt0.4
- 1.0.11rc4
- spec cleanup

* Sat Mar 04 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt0.3
- 1.0.11rc3

* Sun Feb 05 2006 Michael Shigorin <mike@altlinux.org> 1.0.10-alt2
- s/XFree86-devel-static/XFree86-devel/

* Wed Nov 16 2005 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- 1.0.10

* Thu Jun 23 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1
- 1.0.9
- NB: %_datadir/emu10k1 asm files renamed in upstream
- found echomixer, adding menufile. :)

* Thu Jun 09 2005 Michael Shigorin <mike@altlinux.ru> 1.0.9-alt0
- 1.0.9
- removed gcc34 patch

* Wed Feb 23 2005 Michael Shigorin <mike@altlinux.ru> 1.0.8-alt2
- rebuilt with gcc3.4 (and gentoo patch for that matter)

* Thu Jan 13 2005 Michael Shigorin <mike@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Thu Dec 16 2004 Michael Shigorin <mike@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Sat Jun 26 2004 Michael Shigorin <mike@altlinux.ru> 1.0.5-alt2
- fixed thinko in Conflicts:
- added ru/uk package info
- renamed %_menudir/*.menu to drop ".menu" suffix
- updated kernel headers version

* Mon May 31 2004 Michael Shigorin <mike@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sat Apr 03 2004 Michael Shigorin <mike@altlinux.ru> 1.0.4-alt1
- 1.0.4
- added menufiles for envy24control and hdspconf, thanks to Sergey Pinaev (dfo@)
  for notifyin' and buggin' till it was done :-)

* Sun Mar 21 2004 Michael Shigorin <mike@altlinux.ru> 1.0.3-alt2
- got back missing envy24control binary
  (thanks to Sergey Pinaev <dfo antex ru> for noticing)
- added Conflicts: emu10k1-tools

* Tue Mar 02 2004 Michael Shigorin <mike@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Jan 29 2004 Michael Shigorin <mike@altlinux.ru> 1.0.2-alt2
- 1.0.2, Final Upload by ALSA Project (TM) 20040129 18:35 +0200
- thanks to Sergey Vlasov (vsu@) for alerting about re-uploads

* Wed Jan 28 2004 Michael Shigorin <mike@altlinux.ru> 1.0.2-alt1
- 1.0.2
- removed "alsa" dependency for the time being
- spec cleanup: cycle over found targets instead of copy/paste blocks
  (also fixes #3230)
- revamped docs unclash/installation
- refreshed build deps
- fixed CLAGS typo

* Thu Jan 15 2004 Michael Shigorin <mike@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Oct 22 2003 Michael Shigorin <mike@altlinux.ru> 0.9.8-alt1
- 0.9.8
- updated buildrequires
- spec cleanup

* Fri Sep 26 2003 Michael Shigorin <mike@altlinux.ru> 0.9.7-alt1
- 0.9.7
- updated --with-soundbase value to reflect unified alsa headers location

* Wed Jul 30 2003 Michael Shigorin <mike@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Tue Jul 15 2003 Michael Shigorin <mike@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Mon Jun 23 2003 Michael Shigorin <mike@altlinux.ru> 0.9.4-alt1
- 0.9.4
- renamed to alsa-tools

* Wed Apr 02 2003 Michael Shigorin <mike@altlinux.ru> 0.9.1-alt0.1
- 0.9.1 (unofficial build)

* Tue Feb 04 2003 Rider <rider@altlinux.ru> 0.9.0rc7-alt2
- 0.9.0rc7

* Mon Jan 20 2003 Rider <rider@altlinux.ru> 0.9.0rc6-alt2
- build requires fix (autoconf & automake)

* Tue Nov 26 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0rc6-alt1
- 0.9.0rc6
- Rebuilt in new environment

* Mon Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0rc1-alt1
- 0.9.0rc1

* Thu Feb 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta12-alt1
- 0.9.0beta12

* Wed Dec 26 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta10-alt1
- 0.9.0beta10
- Removed as10k1 to avoid conflicts with emu10k1-utils

* Wed Nov 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta9-alt1
- 0.9.0beta9

* Fri Oct 12 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta8-alt1
- 0.9.0beta8

* Fri Sep 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta7-alt1
- First build for Sisyphus
