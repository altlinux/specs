Name:    apt-updatecache
Version: 1.2
Release: alt2

Summary: Service for update APT cache on boot and every 4 hours
License: GPL-3.0+ 
Group:   System/Configuration/Packaging
URL:     http://altlinux.org/apt-updatecache

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
Service for update APT cache on boot and every 4 hours.

%prep
%setup

%install
install -pD -m644 %name.service %buildroot%systemd_unitdir/%name.service
install -pD -m644 %name.timer %buildroot%systemd_unitdir/%name.timer

%files
%config(noreplace) %systemd_unitdir/*

%changelog
* Wed Nov 10 2021 Andrey Cherepanov <cas@altlinux.org> 1.2-alt2
- Remove postun/post macros for service file.

* Sat Jul 10 2021 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Fix run on startup (ALT #40423).
- Add Requires=network-online.target to service file.
- Remove randomized run of timer.

* Thu Jul 08 2021 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Add [Install] section in service file.

* Thu Jul 08 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
