Name: systemd-settings
Version: 1
Release: alt2
Summary: Settings for systemd
Url: https://packages.altlinux.org/en/Sisyphus/srpms/%name
Group: System/Configuration/Boot and Init
License: GPLv2+
BuildArch: noarch

Source: %name-%version.tar

%description
This package contains drop-in settings for systemd.

%package disable-user-systemd-for-selinux
Summary: Disable user systemd --user  for ALT selinux systems
Group: System/Configuration/Boot and Init
License: GPLv2+
BuildArch: noarch

%package disable-kill-user-processes
Summary: Set global KillUserProcesses=no
Group: System/Configuration/Boot and Init
License: GPLv2+
BuildArch: noarch
Requires: /lib/systemd/systemd-logind
Conflicts: %name-enable-kill-user-processes

%package enable-kill-user-processes
Summary: Set global KillUserProcesses=yes
Group: System/Configuration/Boot and Init
License: GPLv2+
BuildArch: noarch
Requires: /lib/systemd/systemd-logind
Conflicts: %name-disable-kill-user-processes

%description disable-kill-user-processes
Set global KillUserProcesses=no

%description enable-kill-user-processes
Set global KillUserProcesses=yes

%description disable-user-systemd-for-selinux
Disabling user@.service, which attempts to start
systemd for user sessions, not needed or allowed
in ALT selinux systems.

%prep
%setup

%build

%install
mkdir -p %buildroot/lib/systemd/logind.conf.d
mkdir -p %buildroot/lib/systemd/system/user@.service.d

install -p -m644 disable-kill-user-processes.conf \
    %buildroot/lib/systemd/logind.conf.d/disable-kill-user-processes.conf
install -p -m644 enable-kill-user-processes.conf \
    %buildroot/lib/systemd/logind.conf.d/enable-kill-user-processes.conf
install -p -m644 disable-user-systemd-for-selinux.conf \
    %buildroot/lib/systemd/system/user@.service.d/disable-user-systemd-for-selinux.conf

%files disable-kill-user-processes
/lib/systemd/logind.conf.d/disable-kill-user-processes.conf

%files enable-kill-user-processes
/lib/systemd/logind.conf.d/enable-kill-user-processes.conf

%files disable-user-systemd-for-selinux
/lib/systemd/system/user@.service.d/disable-user-systemd-for-selinux.conf

%changelog
* Thu Apr 05 2018 Denis Medvedev <nbr@altlinux.org> 1-alt2
- Added ALT selinux settings as additional packages. Changed
package group.

* Sat Mar 31 2018 Alexey Shabalin <shaba@altlinux.ru> 1-alt1
- Initial build

