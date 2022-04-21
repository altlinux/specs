Name: docker-systemctl-replacement
Version: 1.5.4505.9.g9cbe1a0
Release: alt1

Summary: Run systemd-controlled containers without starting an systemd daemon
License: EUPL-1.2
Group: System/Base

Url: https://github.com/gdraheim/docker-systemctl-replacement/
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-python3

%description
daemonless "systemctl" command to manage services without systemd
"systemctl" is a replacement command to control system daemons without
systemd. "systemctl" is useful in application containers where systemd is
not available to start/stop services.

%package -n systemctl-replacement
Summary: %summary
Group: System/Base
BuildArch: noarch

%description -n systemctl-replacement
daemonless "systemctl" command to manage services without systemd
"systemctl" is a replacement command to control system daemons without
systemd. "systemctl" is useful in application containers where systemd is
not available to start/stop services.

This script can also be run as init of an application container (i.e. the
main "CMD" on PID 1) where it will automatically bring up all enabled
services in the "multi-user.target" and where it will reap all zombies
from background processes in the container. When stopping such a container
it will also bring down all configured services correctly before exit.

%prep
%setup

%install
install -D -m 755 files/docker/journalctl3.py %buildroot/bin/journalctl.py
install -D -m 755 files/docker/systemctl3.py %buildroot/bin/systemctl.py

%files -n systemctl-replacement
/bin/*

%files

%changelog
* Thu Apr 21 2022 Alexey Gladkov <legion@altlinux.ru> 1.5.4505.9.g9cbe1a0-alt1
- First build for ALT Linux.
