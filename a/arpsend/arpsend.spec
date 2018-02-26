Name: arpsend
Summary: arpsend - tool for network diagnostics and testing
Version: 1.2.2
Release: alt1
License: GPL/BSD/BSD-like
Group: System/Configuration/Networking
URL: http://www.net.princeton.edu/software/arpsend/

# vzctl have own copy of arpsend
Conflicts: vzctl

Packager: Anton Farygin <rider@altlinux.ru>

Source: %name-%version.tar

BuildRequires: libnet2-devel

%description
arpsend sends an Ethernet frame containing an IP ARP request or reply packet
containing fields you specify. This is a diagnostic tool intended for use by
network administrators.

%prep
%setup

%build
%__autoreconf
%configure
%make_build

%install
%__make install DESTDIR=%buildroot

%files
%_bindir/*
%_man8dir/*
%doc COPYING* README NEWS TODO ChangeLog AUTHORS

%changelog
* Fri Dec 19 2008 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- new version

* Wed Dec 20 2006 L.A. Kostis <lakostis@altlinux.ru> 1.1.0-alt1
- First build for ALTLinux.

