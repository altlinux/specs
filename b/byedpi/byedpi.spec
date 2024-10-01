%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _user byedpi
%define _home %_localstatedir/%_user

Name: byedpi
Version: 0.14.1.0.8.g322f
Release: alt1

Summary: A local proxy for DPI environments

Group: System/Internationalization
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
mkdir -p %buildroot{/run/%_user,%_home}
install -pD -m755 .gear/%name.init %buildroot%_initdir/%name
install -pD -m644 .gear/%name.conf %buildroot%_sysconfdir/sysconfig/%name

%pre
groupadd -r -f %_user ||:
useradd -g %_user -c 'The byedpi daemon' \
        -d %_home -s /dev/null -r %_user \
        >/dev/null 2>&1 ||:

%files
%_bindir/*
%doc README.md
%dir %attr(0775,root,%_user) /run/%_user
%dir %attr(0770,root,%_user) %_home
%_initdir/%name
%_sysconfdir/sysconfig/%name

%changelog
* Mon Sep 30 2024 Andrew Savchenko <bircoph@altlinux.org> 0.14.1.0.8.g322f-alt1
- Initial version.
