Name: wondershaper
Version: 1.4.1
Release: alt1

Summary: Helps to maintain interactive latency on modem/ADSL/cable
License: GPL
Group: System/Servers
Url: http://lartc.org/%name
BuildArch: noarch
Packager: Andy Gorev <horror@altlinux.ru>
Requires:       iproute2

Source: %url/%name-%version.tar.bz2
# PATCH-FIX-OPENSUSE wondershaper-fix-conf-path.patch -- Use /etc/wondershaper for wondershaper.conf place
Patch0:         wondershaper-fix-conf-path.patch
# PATCH-FIX-OPENSUSE wondershaper-systemd-hardening.patch -- Added hardening to systemd service(s) (bsc#1181400)
Patch1:         wondershaper-systemd-hardening.patch

%description
This package attempts to implement
+ Maintain low latency for interfactive traffic at all times.
+ Allow 'surfing' at reasonable speeds while up or downloading.
+ Make sure uploads don't harm downloads, and the other way around.
+ Have the ability to mark certain hosts/ports as 'low priority'.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%install
install -pDm 755 %{name} %{buildroot}/%{_sbindir}/%{name}
install -pDm 644 %{name}.service %{buildroot}/%{_unitdir}/%{name}.service
install -pDm 644 %{name}.conf %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf

%files

%doc COPYING ChangeLog README.bhubert README.md VERSION
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/%{name}.conf

%changelog
* Mon Sep 18 2023 Artyom Bystrov <arbars@altlinux.org> 1.4.1-alt1
- Update version

* Tue Oct 14 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1a-alt1
- Initial revision.
