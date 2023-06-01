Name:    wsdd
Version: 0.7.1
Release: alt1

Summary: A Web Service Discovery host daemon
License: MIT
Group:   System/Servers
URL:     https://github.com/christgau/wsdd

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source: %name-%version.tar
Source1: %name.conf

%description
wsdd implements a Web Service Discovery host daemon. This enables (Samba)
hosts, like your local NAS device, to be found by Web Service Discovery Clients
like Windows.

It also implements the client side of the discovery protocol which allows to
search for Windows machines and other devices implementing WSD. This mode of
operation is called discovery mode.

%prep
%setup -n %name-%version
subst 's|^EnvironmentFile=.*$|EnvironmentFile=%_sysconfdir/sysconfig/wsdd|' etc/systemd/wsdd.service
subst 's|=wsdd|=_wsdd|' etc/systemd/wsdd.service

%install
install -Dpm0755 src/wsdd.py %buildroot%_bindir/%name
install -Dpm0644 etc/systemd/wsdd.defaults %buildroot%_sysconfdir/sysconfig/wsdd
install -Dpm0644 etc/systemd/wsdd.service %buildroot%_unitdir/%name.service
install -Dpm0644 man/wsdd.8 %buildroot%_man8dir/wsdd.8
install -Dpm0644 %SOURCE1 %buildroot%_tmpfilesdir/%name.conf

%pre
getent group _%name > /dev/null || /usr/sbin/groupadd -r _%name
getent passwd _%name > /dev/null || \
%_sbindir/useradd -M -r -g _%name -c 'Web Service Discovery host daemon' \
     -d / -s /sbin/nologin _%name 2> /dev/null ||:

%preun
%preun_service %name

%post
%post_service %name

%files
%doc AUTHORS README.md CHANGELOG.md
%_bindir/%name
%config(noreplace) %_sysconfdir/sysconfig/wsdd
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%_man8dir/wsdd.8*

%changelog
* Thu Jun 01 2023 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
