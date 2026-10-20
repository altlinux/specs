%define module_name promethean

Name: activdriver
Version: 5.18.19
Release: alt1.1

Summary: Driver for Promethean ActivBoard and ActivHub
License: GPL-2.0
Group: Development/Kernel
URL: https://support.prometheanworld.com/product/activdriver

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source: %name-%version.tar
# udev rules, X11 config and udev helper from activdriver_5.18.19-0~Ubuntu~1804_amd64.deb
Source1: extra.tar
Patch0: promethean-linux-6.12-6.18.patch
Patch1: promethean-stop-timer-on-disconnect.patch
Patch2: promethean-sh-activlc-path.patch

BuildRequires(pre): rpm-build-kernel

%description
%{summary}.

%package -n kernel-source-%module_name
Summary: The kernel mode drivers for Promethean ActivBoard and ActivHub
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%module_name
%{summary}.

%prep
%setup -c -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
rm -v kernel/promethean.ko

%build
make KERN_INC=.. BUILD=release -C activlc

%install
install -Dpm0755 activlc/release/activlc %buildroot%_bindir/activlc
install -Dpm0755 extra/promethean.sh %buildroot%_bindir/promethean.sh
install -Dpm0644 extra/10-board.rules %buildroot%_udevrulesdir/10-board.rules
install -Dpm0644 extra/66-xorg-promethean.rules %buildroot%_udevrulesdir/66-xorg-promethean.rules
install -Dpm0644 extra/50-promethean.conf %buildroot%_datadir/X11/xorg.conf.d/50-promethean.conf
mkdir -p %kernel_srcdir
mkdir kernel-source-%module_name-%version
cp -a inc kernel kernel-source-%module_name-%version
tar -cjf %kernel_srcdir/kernel-source-%module_name-%version.tar.bz2 kernel-source-%module_name-%version

%files
%_bindir/activlc
%_bindir/promethean.sh
%_udevrulesdir/10-board.rules
%_udevrulesdir/66-xorg-promethean.rules
%_datadir/X11/xorg.conf.d/50-promethean.conf

%files -n kernel-source-%module_name
%attr(0644,root,root) %kernel_src/kernel-source-%module_name-%version.tar.bz2

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 5.18.19-alt1.1
- NMU:
- Fix build of the module with Linux 6.12 and 6.18
- Stop the pen state timer on device disconnect
- Remove prebuilt promethean.ko from kernel-source-promethean
- Package udev rules, X11 config and udev helper from the vendor deb

* Thu Mar 11 2021 Andrey Cherepanov <cas@altlinux.org> 5.18.19-alt1
- Initial build for Sisyphus.
