Name: fake_remount_rw
Version: 0.0.1
Release: alt1

Summary: Boot from RO root file system (copy all RW parts to tmpfs)

License: %gpl2plus
Group: System/Base
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

%description
%summary

%prep
%setup

%build
%install
install -D -m755 %name %buildroot/sbin/%name

%post
echo "REMOUNT_ROOTFS_RW_COMMAND=/sbin/fake_remount_rw" >> /etc/sysconfig/init

%files
/sbin/%name

%changelog
* Thu Apr 26 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus
