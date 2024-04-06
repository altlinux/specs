Name:           stunserver
Version:        1.2.16
Release:        alt1
Summary:        An open source STUN server/client
Group:          Networking/Other
URL:            https://stunprotocol.org/
License:        Apache-2.0
Source:         %name-%version.tar

# Automatically added by buildreq on Sat Mar 23 2024
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libstdc++-devel python3 python3-base sh5
BuildRequires: boost-devel-headers gcc-c++ libssl-devel pandoc python3-dev

%description
STUNTMAN is an open source implementation of the STUN protocol (Session
Traversal Utilities for NAT) as specified in RFCs 5389, 5769, and 5780.
It also includes backwards compatibility for RFC 3489. Source code
distribution includes a high performance STUN server, a client
application, and a set of code libraries for implementing a STUN client
within an application.

%prep
%setup
# Typo hack
sed -i 's/^#\([^ ]\)/# \1/' resources/stunclient.md
sed -i 's/^#\([^ ]\)/# \1/' resources/stunserver.md

%build
%make_build
%make -C resources manpages

%install
install -D stunserver %buildroot%_bindir/stunserver
install -D stunclient %buildroot%_bindir/stunclient
install -D -m644 resources/stunserver.1 %buildroot%_man1dir/stunserver.1
install -D -m644 resources/stunclient.1 %buildroot%_man1dir/stunclient.1

%files
%doc README 
%_bindir/*
%_man1dir/*

%check
./stuntestcode

%changelog
* Sat Mar 23 2024 Fr. Br. George <george@altlinux.org> 1.2.16-alt1
- Initial build for ALT
