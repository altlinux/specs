Name: rtl-sdr
Summary: SDR utilities for Realtek RTL2832 based DVB-T dongles
Version: 2.0.1
Release: alt1
License: GPL-2.0-or-later
Group: Communications
Url: https://sdr.osmocom.org/trac/wiki/rtl-sdr

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake libusb-devel

%description
This package can turn your RTL2832 based DVB-T dongle into a SDR receiver.

%package devel
Summary: Development files for rtl-sdr
Group: Communications
Requires: %name = %EVR

%description devel
Development files for rtl-sdr.

%prep
%setup
rm -f src/getopt/*
rmdir src/getopt

%build
%cmake -DDETACH_KERNEL_DRIVER=ON
%cmake_build

%install
%cmake_install

# remove static libs
rm -f %buildroot%_libdir/*.a

# Fix udev rules and allow access only to users in uucp group
sed -i 's/GROUP="plugdev"/GROUP="uucp"/' rtl-sdr.rules
install -Dpm 644 rtl-sdr.rules %buildroot%_udevrulesdir/10-rtl-sdr.rules

%files
%doc AUTHORS COPYING
%_bindir/*
%_libdir/*.so.*
%_udevrulesdir/10-rtl-sdr.rules

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/rtlsdr
%_pkgconfigdir/*.pc

%changelog
* Fri Nov 10 2023 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Tue Aug 15 2023 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt3.20221118
- new snapshot
- allow only users in group 'uucp' to access rtl-sdr devices
- do not create group 'rtlsdr

* Mon Nov 23 2020 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt2
- Fix Requires (Closes: 39334)

* Tue Dec 25 2018 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt1
- New version 0.6.0

* Mon Oct 30 2017 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt2.20170920.1
- Replace 10-rtl-sdr.rules to _udevrulesdir

* Wed Oct 18 2017 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt1.20170920.1
- Initial build for ALT Sisyphus.
