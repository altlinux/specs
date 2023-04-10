Name: volumes-profile-alt-server
Version: 1.1
Release: alt1

Summary: Volumes description for ALT Server distribution
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%install
%define hook1dir %_datadir/install2/initinstall.d
%define hook2dir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hook1dir
install -pm755 10-*.sh %buildroot%hook1dir/
mkdir -p %buildroot%hook2dir
install -pm755 20-*.sh %buildroot%hook2dir/

%files
%hook1dir/*
%hook2dir/*

%changelog
* Mon Apr 10 2023 Dmitry Terekhin <jqt4@altlinux.org> 1.1-alt1
- 10-vm-profile.sh: Change Ext2/3 to Ext4

* Thu Jun 30 2022 Dmitry Terekhin <jqt4@altlinux.org> 1-alt1
- fork from volumes-profile-cliff-server-0.18-alt1
- reasonable swap = RAM
