# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

# NEON support is by default disabled on ARMs
# building with --with=neon will enable auto detection
%def_with neon

%ifarch %arm aarch64
%if ! %{with neon}
%global have_neon -DHAVE_ARM_NEON_H=0
%endif
%endif

Name: uhd
Url: http://code.ettus.com/redmine/ettus/projects/uhd/wiki
Version: 3.11.0.0
Release: alt1
License: GPLv3+
Group: Engineering
Summary: Universal Hardware Driver for Ettus Research products
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source1: %name-limits.conf
Source2: http://files.ettus.com/binaries/images/uhd-images_003.010.002.000-release.tar.xz

BuildRequires: ctest cmake
BuildRequires: boost-interprocess-devel gcc-c++ boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-program_options-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel, libusb-devel, python-module-cheetah libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel libgps-devel libudev-devel
BuildRequires: python-module-docutils python-module-docutils-compat doxygen libpcap-devel libwiretap-devel
BuildRequires: python-module-mako
Requires(pre):  shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils
Requires: tkinter

%description
The UHD is the universal hardware driver for Ettus Research products.
The goal of the UHD is to provide a host driver and API for current and
future Ettus Research products. It can be used standalone without GNU Radio.

%package firmware
Group: Engineering
Summary: Firmware files for UHD
Requires: %name = %version-%release
BuildArch: noarch

%description firmware
Firmware files for the Universal Hardware driver (UHD).

%package devel
Group: Engineering
Summary: Development files for UHD
Requires: %name = %version-%release

%description devel
Development files for the Universal Hardware Driver (UHD).

%package doc
Group: Engineering
Summary: Documentation files for UHD
BuildArch: noarch

%description doc
Documentation for the Universal Hardware Driver (UHD).

%package tools
Group: Engineering
Summary: Tools for working with / debugging USRP device
Requires: %name = %version-%release

%description tools
Tools that are useful for working with and/or debugging USRP device.

%prep
%setup
mkdir -p images/images
tar -xJf %SOURCE2 -C images/images --strip-components=4
rm -f images/images/{LICENSE.txt,*.tag}

%build

pushd host
%cmake %{?have_neon} \
        -DENABLE_GPSD=ON \
        -DENABLE_E100=ON \
        -DENABLE_E300=ON
%cmake_build
popd

# tools
pushd tools/uhd_dump
%make_build
popd

%check
pushd host/BUILD
make test
popd

%install
pushd host
%cmakeinstall_std
popd

# Fix udev rules and use dynamic ACL management for device
%__subst 's/BUS==/SUBSYSTEM==/;s/SYSFS{/ATTRS{/;s/MODE:="0666"/MODE:="0660", ENV{ID_SOFTWARE_RADIO}="1"/' %buildroot%_libdir/uhd/utils/uhd-usrp.rules
mkdir -p %buildroot%_udevrulesdir
mv %buildroot%_libdir/uhd/utils/uhd-usrp.rules %buildroot%_udevrulesdir/10-usrp-uhd.rules

# Remove tests, examples binaries
rm -rf %buildroot%_libdir/uhd/{tests,examples}

# Move the utils stuff to libexec dir
mkdir -p %buildroot%_libexecdir/uhd
mv %buildroot%_libdir/uhd/utils/* %buildroot%_libexecdir/uhd

# Package base docs to base package
mkdir _tmpdoc
mv %buildroot%_docdir/%name/{LICENSE,README.md} _tmpdoc

install -m 644 -D %SOURCE1 %buildroot%_sysconfdir/security/limits.d/99-usrp.conf

# firmware
mkdir -p %buildroot%_datadir/uhd/images
cp -r images/images/* %buildroot%_datadir/uhd/images

# remove win stuff
rm -rf %buildroot%_datadir/uhd/images/winusb_driver

# convert hardlinks to symlinks (to not package the file twice)
pushd %buildroot%_bindir
for f in usrp_n2xx_simple_net_burner usrp_x3xx_fpga_burner;
do
  unlink $f
  ln -s ../..%_libexecdir/uhd/$f
done
popd

# tools
install -Dpm 0755 tools/usrp_x3xx_fpga_jtag_programmer.sh %buildroot%_bindir/usrp_x3xx_fpga_jtag_programmer.sh
install -Dpm 0755 tools/uhd_dump/chdr_log %buildroot%_bindir/chdr_log

%files
%exclude %_docdir/%name/doxygen
%exclude %_datadir/uhd/images
%doc _tmpdoc/*
%_bindir/*
%_udevrulesdir/10-usrp-uhd.rules
%config(noreplace) %_sysconfdir/security/limits.d/*.conf
%_libdir/lib*.so.*
%_libexecdir/uhd
%_man1dir/*.1*
%_datadir/uhd

%files firmware
%_datadir/uhd/images

%files devel
%_includedir/*
%_libdir/lib*.so
%dir %_libdir/cmake/uhd
%_libdir/cmake/uhd/*.cmake
%_pkgconfigdir/*.pc

%files doc
%doc %_docdir/%name/doxygen

%files tools
%doc tools/README.md
%_bindir/usrp_x3xx_fpga_jtag_programmer.sh
%_bindir/chdr_log

%changelog
* Sun Mar 18 2018 Anton Midyukov <antohami@altlinux.org> 3.11.0.0-alt1
- new version 3.11.0.0

* Sun Oct 22 2017 Anton Midyukov <antohami@altlinux.org> 3.10.2.0-alt1
- Initial build ALT Sisyphus.
