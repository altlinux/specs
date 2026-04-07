Name: udev-rules-goodix-touchscreen
Version: 7
Release: alt1
Summary: Fix orientation of Goodix touchscreen on number of devices
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
BuildRequires(pre): rpm-macros-systemd
AutoReq: no
ExclusiveArch: aarch64 x86_64

Source: %name-%version.tar

Conflicts: udev-rules-MIG-goodix-touchpad udev-rules-goodix-touchpad
Obsoletes: udev-rules-MIG-goodix-touchpad udev-rules-goodix-touchpad
Provides: udev-rules-MIG-goodix-touchpad = %EVR udev-rules-goodix-touchpad = %EVR

%description
%summary.

%prep
%setup -n %name-%version

%install

install -Dm0755 goodix-udev-rule %buildroot%_bindir/goodix-udev-rule

install -Dm0644 goodix-touchscreen.service %buildroot%_unitdir/goodix-touchscreen.service

mkdir -p %buildroot%_presetdir
install -m 0644 20-udev-rules-goodix-touchscreen.preset %buildroot%_presetdir/

# uninstall old udev rules
%triggerin -- %name <= 6
rm -f %_udevrulesdir/90-goodix-*.rules

%post
%post_service goodix-touchscreen.service

%preun
%preun_service goodix-touchscreen.service

%files
#%%_udevrulesdir/99-goodix-touchscreen.rules
%_bindir/goodix-udev-rule
%_unitdir/goodix-touchscreen.service
%_presetdir/20-udev-rules-goodix-touchscreen.preset

%changelog
* Tue Apr  7 2026 Artyom Bystrov <arbars@altlinux.org> 7-alt1
- Add Anbernic RG DS support

* Fri Mar 20 2026 Artyom Bystrov <arbars@altlinux.org> 6-alt1
- Change default path of udev rules (closes: #58220)

* Fri Mar 13 2026 Artyom Bystrov <arbars@altlinux.org> 5-alt1
- Fix accepting udev rule on MIG tablet

* Tue Oct  7 2025 Artyom Bystrov <arbars@altlinux.org> 4-alt1
- Ready to replace udev-rules-MIG-goodix-touchpad and udev-rules-goodix-touchpad

* Thu Sep 18 2025 Artyom Bystrov <arbars@altlinux.org> 3-alt3
- minor fixes

* Thu Sep 18 2025 Artyom Bystrov <arbars@altlinux.org> 3-alt2
- Fix checking model of device for x86_64 CPU

* Fri Sep 12 2025 Artyom Bystrov <arbars@altlinux.org> 3-alt1
- Change name to more correct variant
- Improve binary for case if card was inserted in the another device
- Rename files of package
- Add MIG T8S tablet support

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
