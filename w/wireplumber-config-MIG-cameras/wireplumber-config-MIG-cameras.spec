%define _wireplumberdir %_datadir/wireplumber/wireplumber.conf.d
Name: wireplumber-config-MIG-cameras
Version: 1.0
Release: alt1
Summary: Fix rotation and mirroring of cameras for MIG T8X tablet
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_wireplumberdir

cat > %buildroot%_wireplumberdir/wireplumber-config-MIG-T8X-cameras.conf << EOF
monitor.v4l2.rules = [
  {
    matches = [
      {
        # Rear cam
        node.name = "v4l2_input.pci-0000_00_14.0-usb-0_6_1.0",
        device.product.id = "0x6360",
        device.vendor.id = "0x0c45",
      }
    ]
    actions = {
      update-props = {
        meta.videotransform.transform = "Flipped"
      }
    }
  },
  {
    matches = [
      {
        # Front cam
        node.name = "v4l2_input.pci-0000_00_14.0-usb-0_5_1.0",
        device.product.id = "0x636d",
        device.vendor.id = "0x0c45",
      }
    ]
    actions = {
      update-props = {
        meta.videotransform.transform = "0"
      }
    }
  }
]
EOF

%files
%_wireplumberdir/wireplumber-config-MIG-T8X-cameras.conf

%changelog
* Tue May  5 2026 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for ALT
