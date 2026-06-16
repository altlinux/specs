Name: ktls-utils
Version: 1.4.0
Release: alt2

Summary: TLS handshake utilities for in-kernel TLS consumers
License: GPLv2
Group: Networking/Other
Url: https://github.com/oracle/ktls-utils/

Source: %name-%version.tar

BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libkeyutils)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libnl-genl-3.0)
BuildRequires: pkgconfig(yaml-0.1)

%description
In-kernel TLS consumers need a mechanism to perform TLS handshakes on a
connected socket to negotiate TLS session parameters that can then be
programmed into the kernel's TLS record protocol engine.
This package of software provides a TLS handshake user agent that listens
for kernel requests and then materializes a user space socket endpoint
on which to perform these handshakes. The resulting negotiated session
parameters are passed back to the kernel via standard kTLS socket options.

%prep
%setup

%build
%autoreconf
%configure --with-systemd=%_unitdir --enable-session-tags
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING NEWS README
%dir %_sysconfdir/tlshd
%dir %_sysconfdir/tlshd/tags.d
%_sysconfdir/tlshd/tags.d/tags.example
%config(noreplace) %_sysconfdir/tlshd/config
%_sbindir/tlshd
%_unitdir/tlshd.service
%_man5dir/tlshd.conf.5*
%_man7dir/tls-session-tags.7*
%_man8dir/tlshd.8*

%changelog
* Tue Jun 16 2026 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt2
- NMU: explicitly specified %%_unitdir for systemd unit installation

* Thu Apr 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.0-alt1
- 1.4.0 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.0-alt1
- 1.3.0 released

* Mon Jul 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.1-alt1
- 1.2.1 released

* Mon Jul 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.0-alt1
- 1.2.0 released

* Wed Jun 04 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.0-alt1
- 1.1.0 released

* Tue May 06 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt1
- 1.0.0 released
