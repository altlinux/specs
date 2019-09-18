Name:     rteval
Version:  2.14.0.27.g5ed68ae
Release:  alt1

Summary:  Evaluate the performance of a realtime Linux kernel
License:  GPL-2.0-or-later
Group:    System/Kernel and hardware
# https://git.kernel.org/pub/scm/linux/kernel/git/clrkwllms/rteval.git/
Url:      https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/rteval

BuildRequires: python-module-setuptools python-module-ethtool python-module-lxml python-module-libxml2
BuildRequires: python-dmidecode

# hackbench and cyclictest
Requires: linux-rt-tests
# taskset
Requires: schedutils
# --loaddir=
Requires: kernel-source-4.9
# something to build the kernel
Requires: gcc gcc-c++ make binutils util-linux e2fsprogs bc perl flex
Requires: lzma-utils libelf-devel

Source:   %name-%version.tar
BuildArch: noarch

%description
Rteval is a python program written to evaluate the performance of a
realtime Linux kernel on a particular hardware platform. The program
unpacks source code for two loads: hackbench and a Linux kernel
compile, then loops running hackbench and a parallel build of the
Linux kernel. While the loads are running, the cyclictest program is
run to measure realtime performance under load. When the specified run
duration is met, the loads are stopped and cyclictest outputs measured
timer latency values in histogram format, which is analyzed by
rteval. Rteval then writes an XML file to disk with information about
the system (gotten through DMI tables), the raw histogram data
collected during the run and the statistical analysis of the run.

%prep
%setup

%build

%install
make DESTDIR=%buildroot install_rteval

%check
# vm-run --mem=4G --overlay=tmpfs:/usr/src/RPM/BUILD make runit

%files
%doc COPYING README doc/rteval.txt
%_sysconfdir/rteval.conf
%_bindir/rteval
%python_sitelibdir_noarch/%name-*
%python_sitelibdir_noarch/%name
%_datadir/%name
%_man8dir/*

%changelog
* Tue Sep 17 2019 Vitaly Chikunov <vt@altlinux.org> 2.14.0.27.g5ed68ae-alt1
- Initial build of v2.14-27-g5ed68ae.
