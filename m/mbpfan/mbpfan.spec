Name:    mbpfan
Version: 2.4.0
Release: alt1

Summary: A simple daemon to control fan speed on all MacBook/MacBook Pros
License: GPL-3.0
Group:   System/Configuration/Hardware
Url:     https://github.com/linux-on-mac/mbpfan

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

ExclusiveArch: x86_64

%description
This is an enhanced version of Allan McRae mbpfan

mbpfan is a daemon that uses input from coretemp module and sets the
fan speed using the applesmc module. This enhanced version assumes any
number of processors and fans (max. 10).

* It only uses the temperatures from the processors as input.
* It requires coretemp and applesmc kernel modules to be loaded.
* It requires root use
* It daemonizes or stays in foreground
* Verbose mode for both syslog and stdout
* Users can configure it using the file /etc/mbpfan.conf

%prep
%setup

%build
%make_build
gunzip %name.8.gz

%install
install -Dpm 0755 bin/%name %buildroot%_sbindir/%name
install -Dpm 0755 bin/%name-tests %buildroot%_sbindir/%name-tests
install -Dpm 0644 %name.conf %buildroot%_sysconfdir/%name.conf
install -Dpm 0644 %name.service %buildroot%_unitdir/%name.service
install -Dpm 0644 %name.8 %buildroot%_man8dir/%name.8

%preun
%preun_service %name

%post
%post_service %name

%files
%doc README.md AUTHORS
%config(noreplace) %_sysconfdir/%name.conf
%_sbindir/%name
%_sbindir/%name-tests
%_unitdir/%name.service
%_man8dir/%name.8*

%changelog
* Mon Apr 03 2023 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Tue Apr 26 2022 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus.
