%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: proxychains-ng
Version: 4.17
Release: alt1

Summary: Redirects the connections through SOCKS4a/5 or HTTP proxies

License: GPL-2.0-or-later
Group: Networking/Other
Url: https://github.com/rofl0r/proxychains-ng

Source: %name-%version.tar

%description
ProxyChains is a UNIX program, that hooks network-related libc functions
in DYNAMICALLY LINKED programs via a preloaded DLL (dlsym(), LD_PRELOAD)
and redirects the connections through SOCKS4a/5 or HTTP proxies.
It supports TCP only (no UDP/ICMP etc).

%package -n proxychains
Summary: Proxychains backward compatible executable name
Group: Networking/Other
Requires: %name = %EVR

%description -n proxychains
%summary.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%configure
%make_build

%install
%makeinstall_std install-config
install -Dm 0755 src/proxyresolv %buildroot%_bindir/proxyresolv4
install -Dpm644 completions/zsh/_proxychains4 -t %buildroot%_datadir/zsh/site-functions
ln -s proxychains4 %buildroot%_bindir/proxychains

%files
%doc AUTHORS COPYING README
%config(noreplace) %_sysconfdir/proxychains.conf
%_bindir/proxychains4
%_bindir/proxychains4-daemon
%_bindir/proxyresolv4
%_libdir/libproxychains4.so
%_datadir/zsh/site-functions/_proxychains4

%files -n proxychains
%_bindir/proxychains

%changelog
* Sun Apr 27 2025 Vitaly Chikunov <vt@altlinux.org> 4.17-alt1
- Update to v4.17 (2024-01-21).

* Sun Jul 24 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.16.0.9.git060801d-alt1
- Updated to v4.16-9-g060801d.
- Fixed watch file.

* Mon Jan 24 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.16-alt1
- Updated to 4.16.

* Tue Sep 21 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.15-alt1
- Initial built for ALT Sisyphus.
