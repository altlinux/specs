%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _user byedpi
%define _home %_localstatedir/%_user

Name: byedpi
Version: 0.14.1.0.8.g322f
Release: alt3

Summary: A local proxy for DPI environments

Group: Networking/Other
License: MIT
Url: https://github.com/hufrea/byedpi

Source: %name-%version.tar

%description
A local SOCKS proxy for users in DPI environments.

%prep
%setup

%build
%make CC=gcc CFLAGS="%optflags" LDFLAGS="-Wl,-O1,--as-needed"

%install
%makeinstall_std
mkdir -p %buildroot%_home
install -pD -m755 .gear/%name.init    %buildroot%_initdir/%name
install -pD -m644 .gear/%name.service %buildroot%_unitdir/%name.service
install -pD -m644 .gear/%name.conf    %buildroot%_sysconfdir/sysconfig/%name
install -D  -m644 .gear/tmpfiles.conf %buildroot%_tmpfilesdir/%name.conf

%pre
groupadd -r -f %_user ||:
useradd -g %_user -c 'The byedpi daemon' \
        -d %_home -s /dev/null -r %_user \
        >/dev/null 2>&1 ||:

%files
%_bindir/*
%doc README.md
%dir %attr(0770,root,%_user) %_home
%_initdir/%name
%_unitdir/%name.service
%_sysconfdir/sysconfig/%name
%_tmpfilesdir/%name.conf

%changelog
* Sun Oct 27 2024 Andrew Savchenko <bircoph@altlinux.org> 0.14.1.0.8.g322f-alt3
- Add systemd unit file

* Sun Oct 27 2024 Andrew Savchenko <bircoph@altlinux.org> 0.14.1.0.8.g322f-alt2
- Use tmpfilesd (Closes: #51622)
- Add LSB header to the init script

* Mon Sep 30 2024 Andrew Savchenko <bircoph@altlinux.org> 0.14.1.0.8.g322f-alt1
- Initial version.
