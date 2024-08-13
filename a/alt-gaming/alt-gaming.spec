%define _unpackaged_files_terminate_build 1

%define limitsdir %_sysconfdir/security/limits.d
%define sysctldir %_sysconfdir/sysctl.d
%define schemasdir %_datadir/glib-2.0/schemas

Name: alt-gaming
Version: 0.0.5
Release: alt1

Summary: Easy system setup to optimize for games.

License: MIT
Group: System/Configuration/Other
Url: https://git.altlinux.org/people/fidel/packages/alt-gaming.git

Source: %name-%version.tar

BuildArch: noarch

Requires: %name-check
Requires: %name-esync
Requires: %name-mm-count
Requires: %name-clearcpuid514
Requires: %name-tcp-mtu-probing
Requires: %name-alive-timeout

%description
%summary

%package esync
Group: System/Configuration/Other
Summary: Enable esync support.
%description esync
Enable esync support. Improves productivity many games that use wine,
especially those that are heavily depend on multithreading.

%package mm-count
Group: System/Configuration/Other
Summary: Reduce operating system mmap restrictions.
%description mm-count
Reduce operating system mmap restrictions. Required for some games.

%package clearcpuid514
Group: System/Configuration/Other
Summary: Disable UMIP support.
%description clearcpuid514
Disable UMIP support. (Required to run some games, such as Overwatch and
Hogwards Legacy on Ryzen 3xxx processors and higher)

%package check
Group: System/Configuration/Other
Summary: Checking alt-gaming settings.
%description check
Use alt-gaming-check in the terminal to check if the optimizations are working.

%package tcp-mtu-probing
Group: System/Configuration/Other
Summary: Use net.ipv4.tcp_mtu_probing = 1 by default.
%description tcp-mtu-probing
Use net.ipv4.tcp_mtu_probing = 1 by default.
Fixed connection to some game servers and launchers. (For example: UBISOFT)

%package alive-timeout
Group: System/Configuration/Other
Summary: Override check-alive-timeout=15 seconds for GNOME
%description alive-timeout
Override check-alive-timeout=uint32 15000 (only for GNOME)
Increases application keepalive timeout to 15 seconds.
Fixes problems with some games.

%prep
%setup

%build

%install
pushd settings
install -D -m 644 95-esync.conf %buildroot%limitsdir/95-esync.conf
install -D -m 644 95-vm.max_map_count.conf %buildroot%sysctldir/95-vm.max_map_count.conf
install -D -m 644 95-tcp_mtu_probing.conf %buildroot%sysctldir/95-tcp_mtu_probing.conf
install -D -m 644 95-gnome-gschema.override %buildroot%schemasdir/95-gnome-gschema.override
popd

install -D -m 755 scripts/alt-gaming-check %buildroot%_bindir/alt-gaming-check

%post clearcpuid514
if ! grep -q "clearcpuid=514" /etc/sysconfig/grub2 ; then
    if grep -q "GRUB_CMDLINE_LINUX_DEFAULT=\"" /etc/sysconfig/grub2 ; then
        sed -i "s/GRUB_CMDLINE_LINUX_DEFAULT=\"/GRUB_CMDLINE_LINUX_DEFAULT=\"clearcpuid=514 /" /etc/sysconfig/grub2
    elif grep -q "GRUB_CMDLINE_LINUX_DEFAULT='" /etc/sysconfig/grub2 ; then
        sed -i "s/GRUB_CMDLINE_LINUX_DEFAULT='/GRUB_CMDLINE_LINUX_DEFAULT='clearcpuid=514 /" /etc/sysconfig/grub2
    fi
    update-grub || :
fi

%postun clearcpuid514
if sed -i 's/clearcpuid=514 //g' /etc/sysconfig/grub2
then update-grub || :
fi

%files

%files esync
%limitsdir/95-esync.conf

%files mm-count
%sysctldir/95-vm.max_map_count.conf

%files tcp-mtu-probing
%sysctldir/95-tcp_mtu_probing.conf

%files clearcpuid514

%files check
%_bindir/alt-gaming-check

%files alive-timeout
%schemasdir/95-gnome-gschema.override

%changelog
* Tue Aug 13 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.5-alt1
- fixed alt-gaming-check: alive-timeout for GNOME

* Thu Aug 01 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.4-alt1
- added alt-gaming-alive-timeout (thanx @boria138)
- updated alt-gaming-check

* Mon Jul 29 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.3-alt1
- fixed CMDLINE for clearcpuid514
- added tcp-mtu-probing (thanx @boria138)
- added error check to alt-gaming-check

* Thu Jul 25 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.2-alt1
- added alt-gaming-clearcpuid514
- added script: alt-gaming-check

* Wed Jul 24 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.1-alt1
- initial build for ALT Sisyphus
- added alt-gaming-esync
- added alt-gaming-mm-count
