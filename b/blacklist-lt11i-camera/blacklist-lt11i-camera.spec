Name: blacklist-lt11i-camera
Version: 0.1
Release: alt1
Summary: Disable camera on MIG lt11i Tablet
License: GPL-2.0-or-later
Group: System/Kernel and hardware

ExclusiveArch: aarch64

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/modprobe.d
cat > %buildroot%_sysconfdir/modprobe.d/blacklist-lt11i-camera.conf << EOF
blacklist vvcam-isp
blacklist vvcam-dwe
blacklist vvcam-video
blacklist imx8-media-dev
EOF

%files
%_sysconfdir/modprobe.d/blacklist-lt11i-camera.conf

%changelog
* Wed Aug 21 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build

