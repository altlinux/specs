%define _unpackaged_files_terminate_build 1

Name: alt-gaming
Version: 0.0.1
Release: alt1

Summary: Easy system setup to optimize for games.

License: MIT
Group: System/Configuration/Other
Url: https://git.altlinux.org/people/fidel/packages/alt-gaming.git

Source: %name-%version.tar

BuildArch: noarch

Requires: %name-esync
Requires: %name-mm-count

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
Summary: Reduce operating system mmap restrictions. Required for some games.
%description mm-count
%summary


%prep
%setup

%build

%install
pushd settings
install -D -m 644 95-esync.conf %buildroot%_sysconfdir/security/limits.d/99-esync.conf
install -D -m 644 95-vm.max_map_count.conf %buildroot%_sysconfdir/sysctl.d/99-vm.max_map_count.conf
popd

%files

%files esync
%_sysconfdir/security/limits.d/99-esync.conf

%files mm-count
%_sysconfdir/sysctl.d/99-vm.max_map_count.conf

%changelog
* Wed Jul 24 2024 Mikhail Tergoev <fidel@altlinux.org> 0.0.1-alt1
- initial build for ALT Sisyphus
- added alt-gaming-esync
- added alt-gaming-mm-count
