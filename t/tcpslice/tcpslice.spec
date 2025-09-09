Name: tcpslice
Version: 1.8
Release: alt1

Summary: A tool to merge or split pcap files
License: BSD
Group: Monitoring
Url: https://github.com/the-tcpdump-group/tcpslice

Source: %name-%version-%release.tar

Requires: libpcap0.8 >= 2:1.9.0

BuildRequires: libpcap-devel >= 2:1.9.0

%description
tcpslice concatenates multiple pcap files together, or extracts time slices
from one or more pcap files.

%prep
%setup -n %name-%version-%release

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_mandir/man?/*

%changelog
* Tue Sep 09 2025 Alexander Danilov <admsasha@altlinux.org> 1.8-alt1
- New version 1.8.

* Thu Aug 20 2020 Nikita Ermakov <arei@altlinux.org> 1.3-alt1
- Initial release for ALT Sisyphus.
