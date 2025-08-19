Name: udev-rules-goodix-touchpad
Version: 2
Release: alt1
Summary: Fix orientation of touchscreen in Anbernic RG Arc D
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
BuildRequires(pre): rpm-macros-systemd
AutoReq: no
ExclusiveArch: aarch64

Source: %name-%version.tar


%description
%summary.

%prep
%setup -n %name-%version

%install

install -Dm0755 arc-d-udev-rule %buildroot%_bindir/arc-d-udev-rule

install -Dm0644 arc-d-touchscreen.service %buildroot%_unitdir/arc-d-touchscreen.service

mkdir -p %buildroot%_presetdir
install -m 0644 20-udev-rules-goodix-touchscreen.preset %buildroot%_presetdir/

%post
%post_service arc-d-touchscreen.service

%preun
%preun_service arc-d-touchscreen.service

%files
#%%_udevrulesdir/99-goodix-touchscreen.rules
%_bindir/arc-d-udev-rule
%_unitdir/arc-d-touchscreen.service
%_presetdir/20-udev-rules-goodix-touchscreen.preset

%changelog
* Tue Aug 19 2025 Artyom Bystrov <arbars@altlinux.org> 2-alt1
- Total rework of package:
- change cat method to systemd service with run device check

* Mon Aug 18 2025 Artyom Bystrov <arbars@altlinux.org> 1.1-alt1
- Set model with cuustom variable

* Wed Oct 30 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt6.1
- Fix mistype in the name of device

* Mon Oct 28 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt6
- Change name of device to name of model

* Wed Oct 23 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt5
- Update rule

* Fri Oct 11 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt4
- Change number of kernel event.

* Thu Sep  5 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt3
- Remove product attribute (broke rule)

* Mon Aug 19 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt2
- Fix rule for touchscreen

* Mon May 13 2024 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for ALT.
