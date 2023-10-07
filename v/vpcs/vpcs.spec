Name: vpcs
Version: 0.8.3
Release: alt1

Summary: Virtual PC Simulator
License: BSD-2-Clause
Group: Networking/Other
Url: https://github.com/GNS3/vpcs

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
The VPCS can simulate up to 9 PCs. You can ping/traceroute them, or ping/traceroute
the other hosts/routers from the virtual PCs when you study the Cisco routers in
the Dynamips. VPCS is not the traditional PC, it is just a program running on the
Linux or Windows, and only few network commands can be used in it. But VPCS can
give you a big hand when you study the Cisco devices in the Dynamips. VPCS can
replace the routers or VMware boxes which are used as PCs in the Dynamips network.

Try VPCS, it can save your CPU/Memory. It is very small.

Now, VPCS can be run in udp or ether mode. In the udp mode, VPCS sends or receives
the packets via udp. In the ether mode, via /dev/tap, not support on the Windows. 

%prep
%setup
%patch0 -p1

%build
pushd src
export CFLAGS="%optflags -fno-strict-aliasing -fcommon"
%make_build -f Makefile.linux CPUTYPE=%_target_cpu
popd

mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_man1dir
install -m0755 src/vpcs %buildroot/%_bindir/%name
xz man/vpcs.1
cp man/vpcs.1.xz %buildroot/%_man1dir/

%files
%doc readme.txt README.md
%_bindir/%name
%_man1dir/*.1.*

%changelog
* Sat Oct 07 2023 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt1
- new version 0.8.3
- clean Packager
- fix License (BSD -> BSD-2-Clause)

* Fri Jan 07 2022 Anton Midyukov <antohami@altlinux.org> 0.8.2-alt1
- new version 0.8.2

* Thu Dec 10 2020 Anton Midyukov <antohami@altlinux.org> 0.8-alt3.20171012
- Set CFLAGS+=-fcommon to workaround gcc10 errors

* Tue Oct 16 2018 Anton Midyukov <antohami@altlinux.org> 0.8-alt2.20171012
- first build for aarch64
- drop ubt

* Sun Jun 03 2018 Anton Midyukov <antohami@altlinux.org> 0.8-alt1.20171012%ubt
- New snapshot
- Fix FTBFS

* Mon Aug 08 2016 Anton Midyukov <antohami@altlinux.org> 0.8-alt1.20160225
- Initial build for ALT Linux Sisyphus.
