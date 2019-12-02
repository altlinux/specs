Name: kgdb-agent-proxy
Version: 1.97
Release: alt1

Summary: kgdb serial console helpers (agent-proxy and kdmx)
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://git.kernel.org/pub/scm/utils/kernel/kgdb/agent-proxy.git
Source: %name-%version.tar

%description
This is a simple, small proxy which was intended for use with kgdb, or
gdbserver type connections where you want to share a text console and a debug
session.

The idea is that you use the agent-proxy to connect to a serial port directly
or to a remote terminal server.

kdmx is a program designed to split GDB packets and other trafic coming from a
target on a serial line into 2 separate pseudo-ttys.

The most common use of this is to run kgdb and console on a single serial port,
but should be usable for alternating gdbserver or console over a serial line as
well.

%prep
%setup

%build
%make_build
%make_build -C kdmx

%install
install -D agent-proxy %buildroot/%_bindir/agent-proxy
install -D kdmx/kdmx %buildroot/%_bindir/kdmx

%files
%doc README.TXT kdmx/README-KDMX.txt
%_bindir/agent-proxy
%_bindir/kdmx

%changelog
* Mon Dec 02 2019 Vitaly Chikunov <vt@altlinux.org> 1.97-alt1
- First build for ALT.
