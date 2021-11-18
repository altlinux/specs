
%define _unpackaged_files_terminate_build 1

Name:     headsetcontrol
Version:  2.6
Release:  alt1

Summary:  A tool to control certain aspects of USB-connected headsets on Linux
License:  GPL-3.0
Group:    System/Configuration/Hardware
Url:      https://github.com/Sapd/HeadsetControl

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildRequires: cmake ctest libhidapi-devel

%description
A tool to control certain aspects of USB-connected headsets on
Linux.  Currently, support is provided for adjusting sidetone,
getting battery state, controlling LEDs, and setting the inactive
time.  Supported headsets include Logitech G930, G533, G633, G933,
SteelSeries Arctis 1/7/9/PRO 2019, Corsair VOID (Pro) and others.

%prep
%setup
%autopatch -p1

%build
%cmake -D udev_rules_dir=%_udevrulesdir
%cmake_build

%install
%cmakeinstall_std

%check
%cmake_build -t check

%files
%_bindir/%name
%_udevrulesdir/70-headsets.rules
%doc README.md

%changelog
* Tue Nov 16 2021 Ivan A. Melnikov <iv@altlinux.org> 2.6-alt1
- 2.6

* Wed May 26 2021 Ivan A. Melnikov <iv@altlinux.org> 2.4-alt1.git0a1c2ef
- initial build
  + build from snapshot for Steelseries Arctics 1 battery support
