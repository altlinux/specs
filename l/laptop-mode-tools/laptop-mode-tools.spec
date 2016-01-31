Name: 	  laptop-mode-tools
Version:  1.68.1
Release:  alt1

Summary:  Tools for power savings based on battery/AC status
License:  GPL
Group:    System/Base
URL:      http://www.samwel.tk/laptop_mode
Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
# VCS:    https://github.com/rickysarraf/laptop-mode-tools

BuildArch: noarch
%filter_from_requires /^\/lib\/udev\/hotplug\.functions/d

%description
Laptop mode is a Linux kernel feature that allows your laptop to save
considerable power, by allowing the hard drive to spin down for longer
periods of time. This package contains the userland scripts that are
needed to enable laptop mode. It includes support for automatically
enabling laptop mode when the computer is working on batteries. In
addition, it provides a set of modules which allow you to apply
various other power savings.

%prep
%setup -q

%build
DESTDIR=%buildroot INIT_D=%buildroot%_initdir MAN_D=%_mandir INSTALL=install ./install.sh

%preun
%preun_service laptop-mode

%post
%post_service laptop-mode

%files
%doc COPYING Documentation/*.txt README.md
%_sbindir/*
%config %_sysconfdir/acpi/actions/lm_*.sh
%config %_sysconfdir/acpi/events/lm_*
%config(noreplace) %_sysconfdir/laptop-mode/
%config %_initdir/laptop-mode
%_unitdir/*.service
%_unitdir/*.timer
/lib/udev/lmt-udev
/lib/udev/rules.d/99-laptop-mode.rules
%_sysconfdir/apm/event.d/*
%_sysconfdir/power/scripts.d/*
%_sysconfdir/power/event.d/*
%_datadir/laptop-mode-tools/modules/*
%_datadir/laptop-mode-tools/module-helpers/*
%_libexecdir/pm-utils/sleep.d/*
%_libexecdir/tmpfiles.d/laptop-mode.conf
%_man8dir/*

%changelog
* Sun Jan 31 2016 Andrey Cherepanov <cas@altlinux.org> 1.68.1-alt1
- Inital build in Sisyphus

