%define _unpackaged_files_terminate_build 1

# Add option to build without examples
%def_without examples
# Add option to build without tools
%def_with tools
%def_disable docs

%def_enable afxdp


Name: dpdk
Version: 22.11.3
Release: alt1
Url: http://dpdk.org
License: BSD-3-Clause AND GPL-2.0-only AND LGPL-2.1-only
Summary: Set of libraries and drivers for fast packet processing
Group: System/Libraries

Source: %name-%version.tar

Patch0001: 0001-Do-not-redefine-strlcpy-and-strlcat.patch

#
# The DPDK is designed to optimize througput of network traffic using, among
# other techniques, carefully crafted assembly instructions.  As such it
# needs extensive work to port it to other architectures.
#
ExclusiveArch: x86_64 %{ix86} aarch64 ppc64le riscv64

BuildRequires(pre): meson >= 0.53.2
BuildRequires(pre): rpm-build-python3
BuildRequires: glibc-kernheaders libpcap-devel zlib-devel libssl-devel
BuildRequires: libnuma-devel libelf-devel libfdt-devel libjansson-devel
BuildRequires: rdma-core-devel libmnl-devel python3(elftools)
%{?_enable_afxdp:BuildRequires: libbpf-devel}
%{?_enable_docs:BuildRequires: doxygen /usr/bin/sphinx-build python3-module-sphinx_rtd_theme}
Requires: lib%name = %EVR

%description
The Data Plane Development Kit is a set of libraries and drivers for
fast packet processing in the user space.

%package -n lib%name
Summary: Data Plane Development Kit runtime libraries
Group: System/Libraries

%description -n lib%name
This package contains the runtime libraries needed for 3rd party application
to use the Data Plane Development Kit.

%package devel
Summary: Data Plane Development Kit development files
Group: System/Libraries
Requires: %name = %EVR
Provides: lib%name-devel = %EVR

%description devel
This package contains the headers and other files needed for developing
applications with the Data Plane Development Kit.

%package doc
Summary: Data Plane Development Kit API documentation
Group: System/Libraries
BuildArch: noarch

%description doc
API programming documentation for the Data Plane Development Kit.

%package tools
Summary: Tools for setting up Data Plane Development Kit environment
Group: Development/Documentation
Requires: %name = %EVR
Requires: kmod pciutils findutils iproute
AutoReqProv: yes, nopython

%description tools
%summary

%package examples
Summary: Data Plane Development Kit example applications
Group: Development/Tools
BuildRequires: libvirt-devel

%description examples
Example applications utilizing the Data Plane Development Kit, such
as L2 and L3 forwarding.

%define sdkdir %_datadir/%name
%define docdir %_docdir/%name
%define incdir %_includedir/%name
%define pmddir %name-pmds

%prep
%setup
%patch0001 -p2

%build
%add_optflags -fcommon
%meson --includedir=include/dpdk \
       -Ddrivers_install_subdir=%pmddir \
       -Dmachine=default \
       %{?_with_examples:-Dexamples=all} \
       %{?_enable_docs:-Denable_docs=true} \
       --default-library=shared

%meson_build

%install
%meson_install
rm -f %buildroot%_libdir/*.a

%files
# BSD
%_bindir/dpdk-dumpcap
%_bindir/dpdk-testpmd
%_bindir/dpdk-proc-info

%files -n lib%name
%_libdir/*.so.*
%_libdir/%pmddir

%if_enabled docs
%files doc
#BSD
%docdir
%endif

%files devel
#BSD
%incdir/
%sdkdir
%if_with examples
%exclude %sdkdir/examples/
%endif
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_with tools
%files tools
%_bindir/dpdk-pdump
%_bindir/dpdk-test
%_bindir/dpdk-test-*
%_bindir/dpdk-*.py
%endif

%if_with examples
%files examples
%_bindir/dpdk_example_*
%doc %sdkdir/examples
%endif

%changelog
* Tue Oct 10 2023 Alexey Shabalin <shaba@altlinux.org> 22.11.3-alt1
- Update to LTS release 22.11.3.

* Fri Jul 07 2023 Alexey Shabalin <shaba@altlinux.org> 22.11.2-alt1
- Update to LTS release 22.11.2.

* Fri Jul 07 2023 Alexey Shabalin <shaba@altlinux.org> 21.11.4-alt1
- Update to LTS release 21.11.4.

* Wed May 03 2023 Alexey Shabalin <shaba@altlinux.org> 21.11.3-alt1
- Update to LTS release 21.11.3.
- Fixes for the following security vulnerabilities:
  + CVE-2022-28199 mlx5 driver error recovery handling vulnerability
  + CVE-2022-2132 vhost: discard too small descriptor chains

* Tue Nov 23 2021 Alexey Shabalin <shaba@altlinux.org> 20.11.3-alt1
- Update to LTS release 20.11.3.

* Thu May 27 2021 Alexey Shabalin <shaba@altlinux.org> 19.11.8-alt1
- Update to LTS release 19.11.8.

* Sun Mar 14 2021 Alexey Shabalin <shaba@altlinux.org> 19.11.6-alt1
- Update to LTS release 19.11.6.

* Wed Dec 16 2020 Alexey Shabalin <shaba@altlinux.org> 19.11.5-alt1
- Update to LTS release 19.11.5
- Add libdpdk package
- Fixes for the following security vulnerabilities:
  + CVE-2020-14374 vhost/crypto: fix data length check
  + CVE-2020-14378 vhost/crypto: fix incorrect descriptor deduction
  + CVE-2020-14376, CVE-2020-14377 vhost/crypto: fix missed request check for copy mode
  + CVE-2020-14375 vhost/crypto: fix possible TOCTOU attack

* Thu Aug 13 2020 Alexey Shabalin <shaba@altlinux.org> 19.11.3-alt1
- Update to LTS release 19.11.3
- Fixes for the following security vulnerabilities:
  + CVE-2020-10722 vhost: check log mmap offset and size overflow
  + CVE-2020-10723 vhost: fix translated address not checked
  + CVE-2020-10724 vhost/crypto: validate keys lengths
  + CVE-2020-10725 vhost: fix potential memory space leak
  + CVE-2020-10726 vhost: fix potential fd leak, fix vring index check

* Thu Aug 13 2020 Alexey Shabalin <shaba@altlinux.org> 18.11.9-alt1
- Update to LTS release 18.11.9

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 18.11.8-alt1
- Update to LTS release 18.11.8 (Fixes: CVE-2020-10722, CVE-2020-10723, CVE-2020-10724)

* Fri Dec 27 2019 Alexey Shabalin <shaba@altlinux.org> 18.11.5-alt1
- Update to LTS release 18.11.5 (Fixes: CVE-2019-14818)
- Rename testbbdev to dpdk-test-bbdev
- Fixed broken symlinks in %%pmddir

* Fri Nov 01 2019 Alexey Shabalin <shaba@altlinux.org> 18.11.3-alt1
- Update to latest LTS release 18.11.3

* Wed Jun 05 2019 Alexey Shabalin <shaba@altlinux.org> 18.11.1-alt1
- Update to latest LTS release 18.11.1
- switch to use python3

* Tue Mar 12 2019 Alexey Shabalin <shaba@altlinux.org> 18.11-alt1
- 18.11

* Wed Feb 13 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 18.08-alt2
- Fixed build on ppc64le (patch by Christian Ehrhardt).

* Tue Oct 30 2018 Alexey Shabalin <shaba@altlinux.org> 18.08-alt1
- 18.08
- build with Mellanox nic support

* Fri Jun 01 2018 Anton Farygin <rider@altlinux.ru> 18.02.1-alt1
- 18.02.1

* Wed Apr 26 2017 Alexey Shabalin <shaba@altlinux.ru> 16.11.1-alt1
- 16.11.1

* Thu Dec 08 2016 Lenar Shakirov <snejok@altlinux.ru> 16.11-alt1
- Initial build for ALT (based on 16.11-1.fc26.src)

