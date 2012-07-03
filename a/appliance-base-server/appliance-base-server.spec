Name: appliance-base-server
Summary: Virtual package for server appliance
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

# System
Requires: appliance-base-admin-hn
Requires: appliance-ntp-autosync ntpdate
Requires: appliance-base-sshd

Requires: iptables iputils etcnet-full

Requires: crontab-control
Requires: openssh-clients libssl
Requires: osec osec-cronjob osec-mailreport

Requires: quota

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

