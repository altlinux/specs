Name: arpsend
Summary: arpsend - tool for network diagnostics and testing
Version: 1.2.3
Release: alt1
License: GPL/BSD/BSD-like
Group: System/Configuration/Networking
URL: http://www.net.princeton.edu/software/arpsend/
# vzctl have own copy of arpsend
Conflicts: vzctl
Source: %name-%version.tar
BuildRequires: libnet2-devel

%description
arpsend sends an Ethernet frame containing an IP ARP request or reply packet
containing fields you specify. This is a diagnostic tool intended for use by
network administrators.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std


%files
%_bindir/*
%_man8dir/*
%doc COPYING* README NEWS TODO ChangeLog AUTHORS

%changelog
* Tue Oct 16 2018 Anton Farygin <rider@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Dec 19 2008 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- new version

* Wed Dec 20 2006 L.A. Kostis <lakostis@altlinux.ru> 1.1.0-alt1
- First build for ALTLinux.

