
%ifndef _environmentdir
%define _environmentdir /lib/environment.d
%endif
%ifndef _userunitdir
%define _userunitdir %_prefix/lib/systemd/user
%endif

Name: systemd-ssh-agent
Version: 1.3
Release: alt1

Requires: ssh-provider-openssh-clients
#Requires: openssh-clients
#Requires: /usr/bin/ssh-agent

Group: System/Configuration/Other
Summary: Systemd unit for SSH agent
Url: https://altlinux.org
License: GPL-3.0-only

BuildArch: noarch

Source0: ssh-agent.service
Source1: ssh_auth_socket.conf

%description
Systemd startup unit and configuration for SSH agent.

%prep
%setup -T -c -n %name-%version

%install
mkdir -p %buildroot/%_userunitdir/
install -m 0644 %SOURCE0 %buildroot/%_userunitdir/ssh-agent.service
mkdir -p %buildroot/%_environmentdir
install -m 0644 %SOURCE1 %buildroot/%_environmentdir/30-ssh_auth_socket.conf

%files
%_environmentdir/30-ssh_auth_socket.conf
%_userunitdir/ssh-agent.service

%changelog
* Tue Jan 16 2024 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- add systemd support for wayland

* Thu Oct 19 2023 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- update requires

* Tue Oct 10 2023 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- update requires

* Mon Dec 19 2022 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
