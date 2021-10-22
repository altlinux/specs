Name: tripso
Version: 1.2
Release: alt1

Summary: Translation of IPv4 Security Options (IPSO) Labels
License: GPLv2
Group: System/Kernel and hardware
Requires: iptables

Url: https://github.com/vt-alt/tripso
Source0: %name-%version.tar

BuildPreReq: rpm-build-kernel
BuildRequires: libiptables-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm >= 1.22 kernel-headers-un-def iptables iproute2 net-tools tcpdump tcpreplay kernel-headers-modules-un-def}}

%description
Translate between CISPO and GOST R 58256-2018 security labels (userspace part).

%package -n kernel-source-%name
Summary: Translate between CISPO and GOST R 58256-2018 security labels (source)
Group: Development/Kernel
BuildArch: noarch
%description -n kernel-source-%name
Translate between CISPO and GOST R 58256-2018 security labels (source).

%prep
%setup -q

%build
make libxt_TRIPSO.so VERSION=%version CFLAGS="%optflags"

%install
make install-lib DESTDIR=%buildroot
install -pDm0644 %_sourcedir/%name-%version.tar %kernel_srcdir/kernel-source-%name-%version.tar

%check
# do dummy build of the module
make KDIR=$(echo /lib/modules/*/build) VERSION=%version xt_TRIPSO.ko
timeout 60 \
vm-run --kvm=cond --sbin '
	set -e
	modprobe -a iptable_filter iptable_raw iptable_security ip_tables
	mount -t tmpfs run /var/run
	export XTABLES_LIBDIR=$PWD:/%_lib/iptables
	./tripso_tests.sh retest
'

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar

%files
%doc README.md
/%_lib/iptables/*.so

%changelog
* Tue Oct 19 2021 Vitaly Chikunov <vt@altlinux.org> 1.2-alt1
- Fix unintended dropping of packets.
- spec: Improve testing.

* Wed Feb 05 2020 Vitaly Chikunov <vt@altlinux.org> 1.1-alt1
- Compatibility drop v3.19, add v5.3.

* Tue Oct 01 2019 Vitaly Chikunov <vt@altlinux.org> 1.0-alt3
- Fix build of kernel module.

* Mon Sep 30 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.0-alt2
- Fix debuginfo which did not contain source code
- Build with system CFLAGS

* Tue Mar 06 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0-alt1
- Sisyphus package.
