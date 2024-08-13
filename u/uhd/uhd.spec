# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
# Build artifact directory path sometimes affects documentation generation.
%define _cmake__builddir BUILD

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

# NEON support is by default disabled on ARMs
# building with --with=neon will enable auto detection
%ifarch %arm
%def_without neon
%else
%def_with neon
%endif

%ifarch %arm aarch64
%if ! %{with neon}
%global have_neon -DNEON_SIMD_ENABLE:BOOL=OFF
%endif
%endif

Name: uhd
Url: https://github.com/EttusResearch/uhd
Version: 4.7.0.0
Release: alt1
License: GPL-3.0-or-later
Group: Engineering
Summary: Universal Hardware Driver for Ettus Research products

Source: %name-%version.tar
Source1: %name-limits.conf
# Download command firmware:
# uhd_images_downloader --types "(fpga|fw)_default" -i images
# Source2-url: https://github.com/EttusResearch/uhd/releases/download/v%version/uhd-images_%version.tar.xz
Source2: images.tar

# Tests fail on i586, armh
ExcludeArch: %ix86 %arm

Patch: uhd-4.3.0.0-python3-fix.patch
Patch1: disable-uhd_image_downloader_test.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: ctest cmake
BuildRequires: boost-interprocess-devel gcc-c++ boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-program_options-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-polygon-devel boost-program_options-devel boost-python3-devel boost-signals-devel boost-wave-devel libusb-devel libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel libgps-devel libudev-devel
BuildRequires: dpdk-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-Cheetah
BuildRequires: python3-module-docutils
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libpcap-devel
BuildRequires: python3-module-mako
Requires(pre): shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils
Requires: lib%name = %EVR
Requires: python3-module-%name = %EVR
Requires: python3-module-usrp_mpm = %EVR
Requires: %name-firmware = %EVR

%description
The UHD is the universal hardware driver for Ettus Research products.
The goal of the UHD is to provide a host driver and API for current and
future Ettus Research products. It can be used standalone without GNU Radio.

%package firmware
Summary: Firmware files for UHD
Group: Engineering
BuildArch: noarch

%description firmware
Firmware files for the Universal Hardware driver (UHD).

%package -n lib%name
Group: Engineering
Summary: Libraries for UHD

%description -n lib%name
Libraries for the Universal Hardware driver (UHD).

%package devel
Group: Development/Other
Summary: Development files for UHD
Requires: lib%name = %EVR

%description devel
Development files for the Universal Hardware Driver (UHD).

%package doc
Group: Documentation
Summary: Documentation files for UHD
BuildArch: noarch

%description doc
Documentation for the Universal Hardware Driver (UHD).

%package tools
Group: Engineering
Summary: Tools for working with / debugging USRP device
Requires: %name = %EVR

%description tools
Tools that are useful for working with and/or debugging USRP device.

%package -n python3-module-%name
Group: Development/Python3
Summary: Python 3 API for %name
Requires: lib%name = %EVR

%description -n python3-module-%name
Python 3 API for %name

%package -n python3-module-usrp_mpm
Group: Development/Python3
Summary: Python 3 module for usrp (part %name)
Requires: lib%name = %EVR
%add_python3_req_skip usrp_mpm.libpyusrp_periphs
%add_python3_req_skip usrp_mpm.chips.ic_reg_maps.x4xx_rfdc_regmap

# self-provide from %python3_sitelibdir/uhd/libpyuhd.cpython-311.so
%add_python3_req_skip uhd.libpyuhd.paths

%add_python3_self_prov_path %buildroot%python3_sitelibdir/usrp_mpm/

%description -n python3-module-usrp_mpm
Python 3 module for usrp (part %name)

%prep
%setup
%autopatch -p1

# fix python shebangs
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%__python3|' {} \;

# Disable -march=native on ppc64le
%ifarch ppc64le
find . -type f -name 'CMakeLists.txt' -print0 |
	xargs -r0 sed -i -e's![ \t]*-march=native!!g'
%endif

%build
pushd host
%cmake %{?have_neon} \
        %_cmake_skip_rpath \
        -DENABLE_GPSD=ON \
        -DENABLE_E300=ON \
        -DENABLE_PYTHON_API=ON
%cmake_build
popd

# tools
pushd tools/uhd_dump
%make_build
popd

%check
pushd host
%cmake_build --target test || :
popd

%install
pushd host
%cmake_install
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
tar -xf %SOURCE2 -C %buildroot%_datadir/uhd/

# remove win stuff
rm -rf %buildroot%_datadir/uhd/images/winusb_driver

# convert hardlinks to symlinks (to not package the file twice)
pushd %buildroot%_bindir
for f in uhd_images_downloader usrp2_card_burner
do
  unlink $f
  ln -s ../..%_libexecdir/uhd/${f}.py $f
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
#exclude %_bindir/aurora_bist_test.py
%exclude %_bindir/chdr_log
#exclude %_bindir/e320_bist
#exclude %_bindir/usrp_update_fs
%exclude %_bindir/usrp_x3xx_fpga_jtag_programmer.sh
%_udevrulesdir/10-usrp-uhd.rules
%config(noreplace) %_sysconfdir/security/limits.d/*.conf
%_libexecdir/uhd
%_man1dir/*.1*
%_datadir/uhd

%files -n lib%name
%_libdir/lib*.so.*

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
#_bindir/aurora_bist_test.py
%_bindir/chdr_log
#_bindir/e320_bist
#_bindir/usrp_update_fs
%_bindir/usrp_x3xx_fpga_jtag_programmer.sh

%files -n python3-module-%name
%python3_sitelibdir/%name/

%files -n python3-module-usrp_mpm
%python3_sitelibdir/usrp_mpm/

%changelog
* Sun Aug 11 2024 Anton Midyukov <antohami@altlinux.org> 4.7.0.0-alt1
- New version 4.7.0.0.

* Sat May 04 2024 Anton Midyukov <antohami@altlinux.org> 4.6.0.0-alt2
- fix compilation with boost 1.85
- convert License to SPDX

* Thu Apr 11 2024 Alexey Shabalin <shaba@altlinux.org> 4.6.0.0-alt1
- NMU: 4.6.0.0
- fix build with DPDK 23.11 LTS

* Thu Aug 17 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 4.4.0.0-alt3.1
- NMU: ingored unmet dependency

* Tue Jul 25 2023 Alexey Shabalin <shaba@altlinux.org> 4.4.0.0-alt3
- fix build with DPDK v22.11 LTS

* Fri Jun 23 2023 Anton Midyukov <antohami@altlinux.org> 4.4.0.0-alt2
- fix build with gcc13

* Thu Jun 15 2023 Anton Midyukov <antohami@altlinux.org> 4.4.0.0-alt1
- New version 4.4.0.0.

* Sat Jan 28 2023 Anton Midyukov <antohami@altlinux.org> 4.3.0.0-alt1
- new version 4.3.0.0
- disable -march=native on ppc64le to fix build

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 4.1.0.3-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Thu Sep 23 2021 Anton Midyukov <antohami@altlinux.org> 4.1.0.3-alt1
- New version 4.1.0.3
- New subpackages: lib%name, python3-module-usrp_mpm
- ExcludeArch: %ix86 %arm

* Sat Jul 03 2021 Anton Midyukov <antohami@altlinux.org> 4.1.0.0-alt1
- New version 4.1.0.0

* Sun May 30 2021 Arseny Maslennikov <arseny@altlinux.org> 3.15.0.0-alt6.1
- NMU: spec: adapted to new cmake macros.

* Wed May 19 2021 Anton Midyukov <antohami@altlinux.org> 3.15.0.0-alt6
- Drop requires tkinter

* Tue May 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.15.0.0-alt5
- Rebuilt with boost-1.76.0.

* Mon Sep 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.15.0.0-alt4
- Rebuilt without neon on armh.

* Thu Jun 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.15.0.0-alt3
- Rebuilt with boost-1.73.0.

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.15.0.0-alt2
- Fixed build with numpy.

* Sat Jan 11 2020 Anton Midyukov <antohami@altlinux.org> 3.15.0.0-alt1
- New version 3.15.0.0

* Wed Dec 25 2019 Anton Midyukov <antohami@altlinux.org> 3.14.1.1-alt3
- fix python3 shebang and syntax for utils
- fix Group

* Tue Dec 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.14.1.1-alt2
- Fixed shebang for installed scripts.
- Rebuilt with boost-1.71.0.

* Sat Oct 19 2019 Anton Midyukov <antohami@altlinux.org> 3.14.1.1-alt1.1
- fix shebang for setup.py

* Thu Oct 17 2019 Anton Midyukov <antohami@altlinux.org> 3.14.1.1-alt1
- New version 3.14.1.1
- fix Url
- switch to python 3 (thanks Aleksey Borisenkov)

* Sat Sep 21 2019 Anton Midyukov <antohami@altlinux.org> 3.13.0.2-alt5
- add BuildRequires: python-module-setuptools (Fix FTBFS)

* Tue Apr 09 2019 Anton Midyukov <antohami@altlinux.org> 3.13.0.2-alt4
- update buildrequires

* Sun Jan 20 2019 Anton Midyukov <antohami@altlinux.org> 3.13.0.2-alt3
- rebuild with new wireshark-devel (fix FTBFS)

* Tue Jan 01 2019 Anton Midyukov <antohami@altlinux.org> 3.13.0.2-alt2
- Update firmaware (Closes: 35831)
- Enable Python API

* Sat Dec 29 2018 Anton Midyukov <antohami@altlinux.org> 3.13.0.2-alt1
- New version 3.13.0.2

* Fri Aug 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.0.0-alt5
- NMU: updated build dependencies.

* Thu Aug 09 2018 Anton Farygin <rider@altlinux.ru> 3.11.0.0-alt4
- build for aarch64

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.0.0-alt3
- NMU: rebuilt with boost-1.67.0.

* Fri Mar 30 2018 Anton Midyukov <antohami@altlinux.org> 3.11.0.0-alt2
- Fix buildrequires

* Sun Mar 18 2018 Anton Midyukov <antohami@altlinux.org> 3.11.0.0-alt1
- new version 3.11.0.0

* Sun Oct 22 2017 Anton Midyukov <antohami@altlinux.org> 3.10.2.0-alt1
- Initial build ALT Sisyphus.
