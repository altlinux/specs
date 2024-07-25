%define _unpackaged_files_terminate_build 1

Name: alt-gaming
Version: 0.0.2
Release: alt1

Summary: Easy system setup to optimize for games.

License: MIT
Group: System/Configuration/Other
Url: https://git.altlinux.org/people/fidel/packages/alt-gaming.git

Source: %name-%version.tar

BuildArch: noarch

Requires: %name-esync
Requires: %name-mm-count
Requires: %name-clearcpuid514
Requires: %name-check

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

%prep
%setup

%build

%install
pushd settings
install -D -m 644 95-esync.conf %buildroot%_sysconfdir/security/limits.d/95-esync.conf
install -D -m 644 95-vm.max_map_count.conf %buildroot%_sysconfdir/sysctl.d/95-vm.max_map_count.conf
popd

install -D -m 755 scripts/alt-gaming-check %buildroot%_bindir/alt-gaming-check

%post clearcpuid514
if ! grep -q "clearcpuid=514" /etc/sysconfig/grub2 \
&& sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="/GRUB_CMDLINE_LINUX_DEFAULT="clearcpuid=514 /' /etc/sysconfig/grub2
then
    update-grub || :
fi

%postun clearcpuid514
if sed -i 's/clearcpuid=514 //g' /etc/sysconfig/grub2
then update-grub || :
fi

%files

%files esync
%_sysconfdir/security/limits.d/95-esync.conf

%files mm-count
%_sysconfdir/sysctl.d/95-vm.max_map_count.conf

%files clearcpuid514

%files check
%_bindir/alt-gaming-check

%changelog
* Thu Jul 25 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.2-alt1
- added alt-gaming-clearcpuid514
- added script: alt-gaming-check

* Wed Jul 24 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.1-alt1
- initial build for ALT Sisyphus
- added alt-gaming-esync
- added alt-gaming-mm-count
