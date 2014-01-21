Name:           nftables
Version:        0.100
Release:        alt1
Summary:        nftables is the project that aims to replace the existing {ip,ip6,arp,eb}tables framework
Group:          System/Libraries
License:        LGPLv2.1+
URL:            http://netfilter.org/projects/nftables
Source:        %name-%version.tar
BuildRequires: libmnl-devel libnftnl-devel flex bison libgmp-devel libreadline-devel

#TODO
# docbook-utils-print

%description
libnftnl is a userspace library providing a low-level netlink programming interface (API) to the
in-kernel nf_tables subsystem. The library libnftnl has been previously known as libnftables.
This library is currently used by nftables.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%check
#make check

%install
%makeinstall_std

%files
%doc COPYING TODO
%dir %_sysconfdir/nftables
%config %_sysconfdir/nftables/*
%_sbindir/*


%changelog
* Tue Jan 21 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.100-alt1
- first build for ALT Linux
