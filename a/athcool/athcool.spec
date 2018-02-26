Summary: Enabling/disabling Powersaving mode for AMD processors
Name: athcool
Version: 0.3.12
Release: alt1
License: GPL
Group: System/Base
URL: http://members.jcom.home.ne.jp/jacobi/linux/softwares.html
Packager: Mikhail Pokidko <pma@altlinux.ru>
Source0: %name-%version.tar.gz
Source1: athcool.init

# Automatically added by buildreq on Mon Apr 28 2008
BuildRequires: libpci-devel

#BuildRequires: pciutils-devel-static

%description
Athcool is a small utility, enabling/disabling Powersaving mode
for AMD Athlon/Duron processors.

Since enabling Powersaving mode, you can save power consumption,
lower CPU temprature when CPU is idle.

Powersaving works if your kernel support ACPI (APM not work),
because athcool only set/unset "Disconnect enable when STPGNT detected"
bits in the Northbridge of Chipset.
To really save power, someone has to send the STPGNT signal when idle.
This is done by the ACPI subsystem when C2 state entered.

!!!WARNING!!!
Depending on your motherboard and/or hardware components,
enabling powersaving mode may cause that:

 * noisy or distorted sound playback
 * a slowdown in harddisk performance
 * system locks or instability

If you met those problems, you should not use athcool.
Please use athcool AT YOUR OWN RISK.

%prep
%setup -q

%build
%make

%install
%make_install DESTDIR=%buildroot install

install -Dp -m0755 %SOURCE1 %buildroot%_initrddir/athcool

%post
/sbin/chkconfig --add %name

%preun
if [ $1 -eq 0 ]; then
	/sbin/service athcool stop &>/dev/null || :
	/sbin/chkconfig --del athcool
fi

%postun
/sbin/service athcool condrestart &>/dev/null || :

%files
%doc ChangeLog COPYING README
%_man8dir/athcool.8*
%_initdir/%name
%_sbindir/%name

%changelog
* Mon Apr 28 2008 Mikhail Pokidko <pma@altlinux.org> 0.3.12-alt1
- Version up

* Thu Oct 19 2006 Mikhail Pokidko <pma@altlinux.ru> 0.3.11-alt1
- Initial ALT build

* Wed Apr 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.11-1 - 4305/dries
- Updated to release 0.3.11.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.7-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Initial package. (using DAR)
