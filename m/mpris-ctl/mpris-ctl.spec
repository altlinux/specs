Name: mpris-ctl
Version: 0.9.100
Release: alt1

Summary: CLI tool for controlling MPRIS-enabled audio players
License: MIT
Group: Sound
Url: https://github.com/mariusor/mpris-ctl

Source: %name-%version-%release.tar

BuildRequires: /usr/bin/scdoc
BuildRequires: pkgconfig(dbus-1)

%description
Minimalistic cli tool for controlling audio players exposing a MPRIS DBus
interface, targeted at keyboard based WMs.

%prep
%setup

%build
CC=gcc make release

%install
make DESTDIR=%buildroot INSTALL_PREFIX=%_prefix install

%files
%doc README* LICENSE
%_bindir/mpris-ctl
%_man1dir/mpris-ctl.1*

%changelog
* Tue May 21 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.100-alt1
- 0.9.100 released

* Mon May 13 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.99.1-alt1
- 0.9.99.1 released

* Tue Jan 09 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.98-alt1
- 0.9.98 released

* Mon Oct 09 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.96-alt1
- 0.9.96 released

* Fri Oct 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.95-alt1
- 0.9.95 released

* Mon Sep 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- 0.9 released

* Fri Sep 01 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.6-alt1
- 0.8.6 released

* Mon Feb 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.5-alt1
- 0.8.5 released

* Mon Aug 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.4-alt1
- 0.8.4 released
