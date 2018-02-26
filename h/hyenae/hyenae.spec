Name: hyenae
Version: 0.36
Release: alt1
License: GPLv3
Summary: %name is a highly flexible and platform independent network packet generator
Group: Networking/Other
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
URL: http://sourceforge.net/projects/hyenae/
Source: %name-%version-1.tar.gz
Patch: hyenae-0.36-1-remove_restriction.patch

BuildRequires: libpcap-devel libdnet-devel

%description
%name is a highly flexible and platform independent network packet generator.
It allows you to reproduce low level ethernet attack scenarios (such as MITM,
DoS and DDoS) to reveal potential security vulnerabilities of your network.
Besides smart wildcard-based address randomization, a highly customizable
packet generation control and an interactive attack assistant, Hyenae comes
with a clusterable remote daemon for setting up distributed attack networks.

%package daemon
Summary: %name-daemon is a clusterable remote daemon for setting up distributed attack network
Group: Networking/Other

%description daemon
%name-daemon is a clusterable remote daemon for setting up distributed attack network

%prep
%setup -n %name-%version-1
%patch -p0

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README HOWTO LICENSE THANKS TODO
%_bindir/%name
%_man1dir/%name.*

%files daemon
%_bindir/hyenaed
%_man1dir/hyenaed.*

%changelog
* Sun Dec 26 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.36-alt1
- Build for ALT
