Name: udev-rules-da280-accelerometer
Version: 1.0
Release: alt1
Summary: Set orientation of DA280 accelerometer
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_udevrulesdir

cat > %buildroot%_udevrulesdir/99-da280-accelerometer.rules <<EOF
SUBSYSTEM=="iio", ENV{IIO_SENSOR_PROXY_TYPE}=="iio-poll-accel", ENV{ACCEL_MOUNT_MATRIX}="0,-1,0;1,0,0;0,0,1"
EOF

%files
%_udevrulesdir/99-da280-accelerometer.rules

%changelog
* Tue Oct 14 2025 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
