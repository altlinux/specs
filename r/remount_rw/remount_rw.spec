Name: remount_rw
Version: 0.6
Release: alt1

Summary: Bind at startup to RO root file system unionfs/aufs

License: %gpl2plus
Group: System/Base
Source: %name.tar
BuildArch: noarch

Packager: Stepanov Andrew <stanv@altlinux.org>
BuildRequires(pre): rpm-build-licenses

%description
Remount Read Only root file system with aufs.
Mostly useful in LiveCD distros.

%prep
%setup -n %name

%build
%make

%post
/sbin/chkconfig --add livecd-save-state ||:

%preun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del livecd-save-state
fi

%install
install -pD -m0755 "remount_rw" "%buildroot/%_sysconfdir/rc.d/init.d/remount_rw"
install -pD -m0644 "remount_rw.mo" "%buildroot/%_datadir/locale/ru/LC_MESSAGES/remount_rw.mo"
mkdir -p %buildroot%_initdir/
install -pD -m0755 livecd-save-state %buildroot%_initdir/livecd-save-state

%files
%_sysconfdir/rc.d/init.d/remount_rw
%_datadir/locale/ru/LC_MESSAGES/remount_rw.mo
%doc README
%_initdir/livecd-save-state

%changelog
* Wed Apr 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- /boot added to rw dirs list

* Wed Mar 02 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- untaring Metadata/live-overlay*.tar removed (unusable)
- added mounting overlays from ISOs on NFS

* Fri Feb 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- untar Metadata/live-overlay*.tar to $rwroot

* Fri Dec 03 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt2
- dependance on race condition in udev removed

* Wed Nov 24 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- automagical read/write live when on isohybrided flash

* Tue Jun 30 2009 Andriy Stepanov <stanv@altlinux.ru> 0.2-alt1
- Stack of squashfs images (/proc/cmdline)

* Thu Jun 18 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt5
- udevinfo -> udevadm info

* Mon Jun 08 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt4
- Remove any information messages, because `remount_rw' called as parameter to
  `action' function in /etc/rc.d/rc.sysinit.

* Mon Jun 08 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt3
- Add 'carriage return' for each startup message.

* Fri Feb 06 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- s/unionfs/aufs

* Mon Feb 02 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt1
- Initial build for ALTLinux

