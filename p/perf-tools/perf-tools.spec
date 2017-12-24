Summary:A miscellaneous collection of in-development and unsupported performance analysis tools for Linux ftrace and perf_events (aka the "perf" command).
Name: perf-tools
Version: 1.0
Release: alt2
License: GPLv2
Group: Monitoring
URL: https://github.com/brendangregg/perf-tools
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildArch: noarch

BuildRequires: sh4

%description
A miscellaneous collection of in-development and unsupported
performance analysis tools for Linux ftrace and perf_events (aka the
"perf" command). Both ftrace and perf are core Linux tracing tools,
included in the kernel source. Your system probably has ftrace
already, and perf is often just a package add (see Prerequisites).

These tools are designed to be easy to install (fewest dependencies),
provide advanced performance observability, and be simple to use: do
one thing and do it well. This collection was created by Brendan Gregg
(author of the DTraceToolkit).

Many of these tools employ workarounds so that functionality is
possible on existing Linux kernels. Because of this, many tools have
caveats (see man pages), and their implementation should be considered
a placeholder until future kernel features, or new tracing subsystems,
are added.

These are intended for Linux 3.2 and newer kernels. For Linux 2.6.x,
see Warnings.

%prep
%setup
%patch0 -p1

%build
%install
mkdir -p %buildroot%_man8dir %buildroot%_bindir
cp -va man/man8/*.8 %buildroot%_man8dir
for i in disk/bitesize fs/cachestat execsnoop kernel/funccount kernel/funcgraph kernel/funcslower kernel/functrace iolatency iosnoop killsnoop kernel/kprobe opensnoop misc/perf-stat-hist tools/reset-ftrace syscount net/tcpretrans system/tpoint user/uprobe;do
cp -va $i %buildroot%_bindir
done

%files
%_bindir/bitesize
%_bindir/cachestat
%_bindir/execsnoop
%_bindir/funccount
%_bindir/funcgraph
%_bindir/funcslower
%_bindir/functrace
%_bindir/iolatency
%_bindir/iosnoop
%_bindir/killsnoop
%_bindir/kprobe
%_bindir/opensnoop
%_bindir/perf-stat-hist
%_bindir/reset-ftrace
%_bindir/syscount
%_bindir/tcpretrans
%_bindir/tpoint
%_bindir/uprobe
%_man8dir/*.8.*
%doc README.md examples deprecated

%changelog
* Sun Dec 24 2017 Terechkov Evgenii <evg@altlinux.org> 1.0-alt2
- Fix "iolatency -T" (https://github.com/brendangregg/perf-tools/issues/30)

* Fri Dec 22 2017 Terechkov Evgenii <evg@altlinux.org> 1.0-alt1
- v1.0-17-g98d42a2

* Fri Jan 29 2016 Terechkov Evgenii <evg@altlinux.org> 0.1-alt3
- git-20160129

* Thu Jul  9 2015 Terechkov Evgenii <evg@altlinux.org> 0.1-alt2
- git-20150709

* Tue Mar 24 2015 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
