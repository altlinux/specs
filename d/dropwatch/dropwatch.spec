%define _unpackaged_files_terminate_build 1

Name: dropwatch
Version: 1.5.5
Release: alt1

Summary: Kernel dropped packet monitor
License: GPL-2.0
Group: Monitoring
Url: https://github.com/nhorman/dropwatch
Vcs: https://github.com/nhorman/dropwatch

Source: %name-%version.tar

BuildRequires: libnl-devel
BuildRequires: libreadline-devel
BuildRequires: libpcap-devel
BuildRequires: binutils-devel

%description
Dropwatch is an utility to interface to the kernel to monitor for dropped
network packets.

%prep
%setup

%build
%autoreconf
%configure
%make_build CFLAGS="%optflags" LDFLAGS="%optflags"

%install
%make_install install DESTDIR=%buildroot PREFIX=%prefix

%files
%doc README.md COPYING
%_bindir/%name
%_bindir/dwdump
%_man1dir/dropwatch.1*
%_man1dir/dwdump.1*

%changelog
* Tue Nov 17 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 1.5.5-alt1
- Initial build for Sisyphus.

