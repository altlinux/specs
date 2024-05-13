Name: volumes-profile-alt-server-v
Version: 1.1
Release: alt1

Summary: Volumes description for ALT Server-V distribution
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
%define hook1dir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hook1dir
install -pm755 10-*.sh %buildroot%hook1dir/

%files
%hook1dir/*

%changelog
* Mon May 13 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.1-alt1
- change root size to fit swap into limit

* Wed Apr 12 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt1
- fork from installer-distro-alt-server-v

