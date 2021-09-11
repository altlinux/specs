Name: udptunnel
Version: 1.1
Release: alt1

Summary: Tunnels UDP over a TCP connection

License: BSD-like
Url: http://www1.cs.columbia.edu/~lennox/udptunnel/
Group: Networking/Other

# see also https://github.com/Inqb8r/udptunnel-advanced

# Source-url: http://www1.cs.columbia.edu/~lennox/udptunnel/%name-%version.tar.gz
Source: %name-%version.tar
Source1: %name.1

Patch0: %name-no-explicit-nis.patch

%description
UDPTunnel is a small program which can tunnel UDP packets
bi-directionally over a TCP connection. Its primary purpose (and
original motivation) is to allow multi-media conferences to traverse a
firewall which allows only outgoing TCP connections. Works most
probably only with RTP traffic.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -Dp %SOURCE1 %buildroot%_man1dir/udptunnel.1

%files
%doc COPYRIGHT README udptunnel.html
%_bindir/udptunnel
%_man1dir/udptunnel.1*

%changelog
* Sat Sep 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Sisyphus

