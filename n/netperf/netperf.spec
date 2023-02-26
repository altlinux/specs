# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: netperf
Version: 2.7.0
Release: alt2
Summary: Network benchmarking tool
License: MIT
Group: Networking/Other
Url: https://hewlettpackard.github.io/netperf/
Vcs: https://github.com/HewlettPackard/netperf
# Ref: https://cloud.google.com/blog/products/networking/using-netperf-and-ping-to-measure-network-latency

Source: %name-%version.tar

BuildRequires: makeinfo

%description
Netperf is a benchmark that can be used to measure the performance of many
different types of networking. It provides tests for both unidirectional
throughput, and end-to-end latency.

%prep
%setup

%build
./autogen.sh
%add_optflags %(getconf LFS_CFLAGS) -fno-strict-aliasing -fcommon
%configure \
	--enable-burst \
	--enable-dccp \
	--enable-demo \
	--enable-dirty \
	--enable-histogram \
	--enable-intervals \
	--enable-omni \
	--enable-unixdomain
%make_build
pushd doc
makeinfo netperf.texi
popd

%install
%makeinstall_std
install -Dpm644 .gear/netserver.service -t %buildroot%_unitdir
install -Dpm755 .gear/netserver.init       %buildroot%_initdir/netserver

%post
%post_service netserver

%preun
%preun_service netserver

%check
src/netperf -V
src/netperf -t help
src/netserver -D &
sleep 1
src/netperf -t TCP_RR -v 2 -- -o min_latency,mean_latency,max_latency,stddev_latency,transaction_rate
kill %%1

%files
%doc COPYING AUTHORS ChangeLog README doc/examples
%_bindir/netperf
%_bindir/netserver
%_initdir/netserver
%_unitdir/netserver.service
%_infodir/netperf.*
%_man1dir/*.1*

%changelog
* Fri Feb 24 2023 Vitaly Chikunov <vt@altlinux.org> 2.7.0-alt2
- Fix install warning from netperf.info.
- Install sysv init script.

* Fri Feb 24 2023 Vitaly Chikunov <vt@altlinux.org> 2.7.0-alt1
- First import 2.7.0 (with updates until 2021-01-21).
