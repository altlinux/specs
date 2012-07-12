Name: walinuxagent
Version: 20120625
Release: alt1
Summary: Windows Azure Linux Agent

Group: System/Configuration/Boot and Init
License: Apache 2.0
Url: https://www.windowsazure.com/en-us/manage/downloads/

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel

Requires: SysVinit net-tools logrotate fdisk sfdisk openssl openssh-server iptables
Requires: /etc/sudoers.d

%py_requires pyasn1

%description
The Windows Azure Linux Agent (waagent) manages VM interaction with the Windows
Azure Fabric Controller.

%prep
%setup

%build

%install
install -pD -m0755 waagent %buildroot/%_sbindir/waagent

%files
%doc README
%_sbindir/waagent

%changelog
* Mon Jun 25 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 20120625-alt1
- initial


