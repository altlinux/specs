Name: udevd-final
Version: 1.0
Release: alt1
Summary: Perform final udevd startup steps
Url: https://packages.altlinux.org/en/Sisyphus/srpms/%name
Group: System/Configuration/Hardware
License: GPL-2.0-or-later
Requires(pre,preun): udev >= 1:238-alt4
BuildArch: noarch

Conflicts: udev-rule-generator < 2:1.6

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build

%install
mkdir -p %buildroot%_initdir %buildroot%_unitdir
install -p -m755 udevd-final.init %buildroot%_initdir/udevd-final
install -p -m644 udevd-final.service %buildroot%_unitdir/udevd-final.service

%post
%post_service udevd-final

%preun
%preun_service udevd-final

%files
%_initdir/udevd-final
%_unitdir/udevd-final.service

%changelog
* Tue Aug 29 2023 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build
