Name: kqemu
Version: 1.4.0
Release: alt0.1.pre1
%define upstream_version	1.4.0pre1

Summary: QEMU x86 virtualization module
License: GPL
Group: Emulators
URL: http://fabrice.bellard.free.fr/qemu/kqemu-doc.html
Packager: Sergey Vlasov <vsu@altlinux.ru>
BuildArch: noarch

Source0: %name-%upstream_version.tar

Source1: %name-extra-%version-%release.tar

BuildPreReq: kernel-build-tools

%package common
Summary: QEMU x86 virtualization module - support files and documentation
Group: System/Configuration/Other
# due to new_summary function and is_builtin_mode bugfix
PreReq: control >= 0.7.2-alt1
PreReq: shadow-utils
# due to /bin/mountpoint (SysVinit >= 2.86-alt1)
PreReq: sysvinit-utils

%package -n kernel-source-%name
Summary: QEMU x86 virtualization module - sources
Group: Development/Kernel

%description
QEMU Accelerator (KQEMU) is a driver allowing the QEMU PC emulator to
run much faster when emulating a PC on an x86 host.

%description common
QEMU Accelerator (KQEMU) is a driver allowing the QEMU PC emulator to
run much faster when emulating a PC on an x86 host.

This package contains scripts and other support files which are
required to use the kqemu kernel module in the ALT Linux system.
The kernel module itself is not included - you need to install the
appropriate kernel-modules-kqemu-* package for your kernel.

This package also contains documentation for the kqemu kernel module.

%description -n kernel-source-%name
QEMU Accelerator (KQEMU) is a driver allowing the QEMU PC emulator to
run much faster when emulating a PC on an x86 host.

This package contains sources for building the kqemu kernel module.

%prep
%setup -c -q -a 1
mv %name-%upstream_version kernel-source-%name-%version
cd kernel-source-%name-%version
cd ..

%install
mkdir -p %kernel_srcdir
tar --owner=root --group=root --mode=u+w,go-w,go+rX -cjf \
	%kernel_srcdir/kernel-source-%name-%version.tar.bz2 \
	kernel-source-%name-%version

install -Dp %name-extra/%name.control %buildroot%_controldir/%name
install -Dp %name-extra/%name.init %buildroot%_initdir/%name
install -Dp -m644 %name-extra/%name.rules \
	%buildroot%_sysconfdir/udev/rules.d/90-%name.rules

%pre common
/usr/sbin/groupadd -r -f kqemu
%pre_control %name

%post common
%post_control -s kqemu %name
%post_service %name

%preun common
%preun_service %name

%triggerin common -- dev
# If using static /dev, select the same status again to fix permissions
mountpoint -q /dev || {
	status="`/usr/sbin/control %name status`" || status=
	[ -n "$status" ] && /usr/sbin/control %name "$status" ||:
}

%files common
%_controldir/%name
%_initdir/%name
%config %_sysconfdir/udev/rules.d/90-%name.rules
%doc %name-extra/README.ALT
%doc kernel-source-%name-%version/LICENSE
%doc kernel-source-%name-%version/Changelog
%doc kernel-source-%name-%version/*.html

%files -n kernel-source-%name
%_usrsrc/*

%changelog
* Mon Oct 06 2008 Michail Yakushin <silicium@altlinux.ru> 1.4.0-alt0.1.pre1
- 1.4.0.pre1 

* Mon Apr 28 2008 Sergey Vlasov <vsu@altlinux.ru> 1.3.0-alt0.3.pre11
- Require sysvinit-utils instead of versioned SysVinit.

* Fri Mar 02 2007 Sergey Vlasov <vsu@altlinux.ru> 1.3.0-alt0.2.pre11
- Added PreReq: SysVinit >= 2.86-alt1 for /bin/mountpoint (#10984).
- Fixed PreReq: control: require control >= 0.7.2-alt1 for new_summary function
  and is_builtin_mode bugfix.

* Sun Feb 25 2007 Sergey Vlasov <vsu@altlinux.ru> 1.3.0-alt0.1.pre11
- 1.3.0pre11.
- Moved to git.
- Spec file cleanup.
- Fixed Version/Release format.
- Renamed main package to kqemu; now two binary packages are built:
   + kqemu-common - documentation and support scripts required by all
     kernel-modules-kqemu-* packages;
   + kernel-source-kqemu - sources required for building the kernel module.
- Added initscript to the kqemu-common package (handles loading of the kqemu
  module at startup; automatic loading on /dev/kqemu access is no longer
  possible with dynamic device numbers).
- Added udev rule file to the kqemu-common package.
- Added control(8) support to control /dev/kqemu permissions:
   + public - 0666 root:root;
   + kqemu - 0660 root:kqemu (default after new install);
   + restricted - 0600 root:root (initial state in the packaged files).
- Added kqemu group creation to %%pre to handle systems installed before
  setup-2.2.7-alt1 (#7149).
- Added %%triggerin on the dev package to restore /dev/kqemu permissions
  after dev upgrade when using static /dev.

* Tue Feb 06 2007 Michael Shigorin <mike@altlinux.org> 1.3.0pre10-alt0.1
- NMU: 1.3.0pre10
- License: changed to GPL

* Tue Oct 10 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 1.3.0pre9-alt1
- initial revision from kernel-source-qvm86
