Name: livecd-backlight-max
Version: 0.1
Release: alt1

Summary: Set backlight to maximum in LiveCD
License: GPL-2.0-or-later
Group: System/Base

Url: https://altlinux.org
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-systemd

%description
%summary.

%prep
%setup

%install
install -pDm0755 livecd-backlight-max.sh %buildroot%_prefix/libexec/livecd-backlight-max
install -pDm0755 livecd-backlight-max.service %buildroot%_unitdir/livecd-backlight-max.service

%files
%_prefix/libexec/livecd-backlight-max
%_unitdir/livecd-backlight-max.service

%changelog
* Fri Jul 11 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial build
