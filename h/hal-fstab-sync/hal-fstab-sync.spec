Name: hal-fstab-sync
Version: 0.0.1
Release: alt7

Summary: Update the /etc/fstab file in response to HAL events
License: GPL
Group: System/Servers
#Url: http://www.piware.de/projects.shtml

Source: %name-%version.tar

BuildPreReq: libhal-devel >= 0.5.7, libdbus-devel >= 0.61, libdbus-glib-devel >= 0.61, pkgconfig
Provides: hal-fstab-sync = %version-%release
Conflicts: hal <= 0.5.7-alt4, fstab-sync

# Automatically added by buildreq on Fri Jun 23 2006
BuildRequires: glib2-devel libhal-devel libpopt-devel linux-libc-headers pkg-config

%description
This program serves one major purpose: Update the  file  systems  table
file /etc/fstab and create/remove mount points in /media in response to
HAL events. This program is usually never run directly  from  a  shell;
instead it is invoked as a callout by the HAL daemon.

Sample configs for filesystem options in %_docdir/%name-%version.


%prep
%setup -q

%build
%configure
%make

%install
%make DESTDIR=%buildroot PREFIX=/usr install

%__mkdir_p %buildroot%_datadir/hal/scripts

# Make wrapper for hal-fstab-sync to HAL
cat > %buildroot%_datadir/hal/scripts/hal-fstab-sync << EOF
#!/bin/sh

forceUnMountDevice() {
    local aDevice=\$1 ; shift

    [ -r /proc/mounts ] || return 0
    [ -x /bin/umount ] || return 0

    local vDevice
    local vMountpoint
    local vFsType
    local vOptions
    local vDump
    local vOrder

    while read vDevice vMountpoint vFsType vOptions vDump vOrder ; do
        if [ "\${vDevice}" = "\${aDevice}" ] ; then
            /bin/umount -fl \${vMountpoint}
        fi
    done < /proc/mounts
    return 0
}

if [[ "\${HALD_ACTION}" = "remove" ]] ; then
    forceUnMountDevice \${HAL_PROP_BLOCK_DEVICE}
    sleep .5
elif [[ "\${HALD_ACTION}" = "add" ]] ; then
    if [[ "\${HAL_PROP_INFO_UDI}" != "/org/freedesktop/Hal/devices/computer" ]] ; then
        sleep .5
    fi
fi

exec %_sbindir/hal-fstab-sync "\$@"
EOF
%__chmod 0755 %buildroot%_datadir/hal/scripts/hal-fstab-sync

%__mkdir_p %buildroot%_sysconfdir/hal/fdi/policy
cp fdi/10-fstab-sync-mount-options-utf8.fdi \
   %buildroot%_sysconfdir/hal/fdi/policy/10-fstab-sync-mount-options.fdi
cp fdi/91-fstab-sync-dont-use-storage.fdi \
   %buildroot%_sysconfdir/hal/fdi/policy/91-fstab-sync-dont-use-storage.fdi

%find_lang %name

%files -f %name.lang
%doc README COPYING AUTHORS ChangeLog NEWS TODO fdi/10-fstab-sync-mount-options-*.fdi fdi/91-fstab-sync-dont-use-storage.fdi
%ghost %config(missingok) %_sysconfdir/hal/fdi/policy/10-fstab-sync-mount-options.fdi
%_sbindir/hal-fstab-sync
%_mandir/*/*
%_datadir/hal/scripts/hal-fstab-sync
%config %_datadir/hal/fdi/policy/10osvendor/*.fdi
%config %_sysconfdir/hal/fdi/policy/*.fdi

%changelog
* Mon Sep  7 2009 Sergey Sukiyazov <corwin@altlinux.ru> 0.0.1-alt7
- commit into git.alt
- rename executibles to hal-fstab-sync instead fstab-sync
- add norock as default for iso9660

* Fri Aug 14 2009 Sergey Sukiyazov <corwin@altlinux.ru> 0.0.1-alt6
- fix fdi files for cdrom/dvd device rules

* Wed Aug 5 2009 Sergey Sukiyazov <corwin@altlinux.ru> 0.0.1-alt6
- fix device processing order on boot

* Wed Jul 15 2009 Sergey Sukiyazov <corwin@altlinux.ru> 0.0.1-alt4
- fix fstab-sync invoction script for correctly removing unmounted volumes
- add conflict with hal-fstab-sync package

* Tue Jul 14 2009 Sergey Sukiyazov <corwin@altlinux.ru> 0.0.1-alt3
- updates
- change package name to fstab-sync to avoid conflicts with hal rpm

* Mon Dec 25 2006 Igor Zubkov <icesik@altlinux.org> 0.0.1-alt2.2.1
- NMU
- rebuild with new dbus

* Thu Jun 22 2006 Sergey A. Sukiyazov <corwin@altlinux.ru> 0.0.1-alt2.2
- renamed to hal-fstab-sync
- conflicts with hal <= 0.5.7-alt4

* Fri Jun 02 2006 Sergey A. Sukiyazov <corwin@altlinux.ru> 0.0.1-alt2
- first build for ALT Linux
