Name: coldreboot
Version: 0.2
Release: alt2

Summary: Tool to halt and reboot very fast
License: GPL
Group: System/Configuration/Other

Packager: Lenar Shakirov <snejok@altlinux.org>

Source: %name-%version.tar

%description
Tool to halt and reboot very fast

Provides %_sbindir/cold{halt,reboot}.

%prep
%setup

%build
make

%install
%makeinstall_std

%files
%_sbindir/coldreboot
%_sbindir/coldhalt
%_sysconfdir/rc.d/rc.halt
%_sysconfdir/rc.d/rc.reboot

%changelog
* Tue Jun 01 2010 Lenar Shakirov <snejok@altlinux.ru> 0.2-alt2
- Spec cleaned: thanks to rpmcs

* Tue Mar 30 2010 Lenar Shakirov <snejok@altlinux.ru> 0.2-alt1
- Emulation of SysVinit-usermode was deleted

* Mon Dec 29 2008 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt5
- Unmounting /dev/hd* and /dev/sd* devices

* Mon Oct 20 2008 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt4
- Unmounting only /mnt/hd*

* Mon Oct 20 2008 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt3
- Unmounting /mnt/root/* and /mnt/hd*

* Mon Oct 20 2008 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt2
- Cleaned up spec
  + New packager: me
  + New summary
  + New description

* Tue Oct 24 2006 Alex V. Myltsev <avm@altlinux.ru> 0.1-alt1
- Initial build

