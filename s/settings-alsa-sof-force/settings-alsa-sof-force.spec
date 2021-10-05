Name:    settings-alsa-sof-force
Version: 1.0
Release: alt1

Summary: Kernel settings for force sof usage for some souncards
License: ALT-Public-Domain
Group:   System/Kernel and hardware
Url:     http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
install -Dm 0644 %name.conf %buildroot%_sysconfdir/modprobe.d/%name.conf

%files
%_sysconfdir/modprobe.d/%name.conf

%changelog
* Tue Oct 05 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build.
