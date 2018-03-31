
Name: systemd-settings
Version: 1
Release: alt1
Summary: Settings for systemd
Url: https://packages.altlinux.org/en/Sisyphus/srpms/%name
Group: System/Configuration/Hardware
License: GPLv2+
BuildArch: noarch

Source: %name-%version.tar

%description
This package contains drop-in settings for systemd.

%package disable-kill-user-processes
Summary: Set global KillUserProcesses=no
Group: System/Configuration/Hardware
License: GPLv2+
BuildArch: noarch
Requires: /lib/systemd/systemd-logind

%description disable-kill-user-processes
Set global KillUserProcesses=no

%prep
%setup

%build

%install
mkdir -p %buildroot/lib/systemd/logind.conf.d
install -p -m644 disable-kill-user-processes.conf \
    %buildroot/lib/systemd/logind.conf.d/disable-kill-user-processes.conf

%files disable-kill-user-processes
/lib/systemd/logind.conf.d/disable-kill-user-processes.conf

%changelog
* Sat Mar 31 2018 Alexey Shabalin <shaba@altlinux.ru> 1-alt1
- Initial build

