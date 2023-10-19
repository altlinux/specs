Name: udev-rules-usb-autosuspend-on-RTS5129
Version: 1.0
Release: alt1
Summary: Enable autosuspend mode for RTS5129
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
On kernels 5.10 (starting from 5.10.82-alt1), power saving
of usb devices is disabled (usbcore.autosuspend=-1).
In order for connected card detection to work correctly
for the RTS5129 chip, a rule to enable power saving is required.
See https://bugzilla.altlinux.org/48069

%install
mkdir -p %buildroot%_udevrulesdir

cat > %buildroot%_udevrulesdir/10-RTS5129-autosuspend.rules <<EOF
# On kernels 5.10 (starting from 5.10.82-alt1), power saving
# of usb devices is disabled (usbcore.autosuspend=-1).
# In order for connected card detection to work correctly
# for the RTS5129 chip, a rule to enable power saving is required.
# See https://bugzilla.altlinux.org/48069

ACTION=="add" \
, ATTR{idProduct}=="0129" \
, ATTR{idVendor}=="0bda" \
, ATTR{power/autosuspend_delay_ms}="2" \
, ATTR{power/control}="on"
EOF

%files
%_udevrulesdir/10-RTS5129-autosuspend.rules

%changelog
* Thu Oct 19 2023 Dmitry Terekhin <jqt4@altlinux.org> 1.0-alt1
- Initial build
