Name:           nftables
Epoch:          1
Version:        0.8.4
Release:        alt1
Summary:        nftables is the project that aims to replace the existing {ip,ip6,arp,eb}tables framework
Group:          System/Libraries
License:        LGPLv2.1+
URL:            http://netfilter.org/projects/nftables
# git://git.netfilter.org/nftables
Source:        %name-%version.tar
BuildRequires: libmnl-devel libnftnl-devel flex bison libgmp-devel libreadline-devel
BuildPreReq: docbook2X

#TODO
# docbook-utils-print dblatex

%description
libnftnl is a userspace library providing a low-level netlink programming interface (API) to the
in-kernel nf_tables subsystem. The library libnftnl has been previously known as libnftables.
This library is currently used by nftables.

%prep
%setup

%build
%autoreconf
%configure --enable-debug --disable-pdf-doc
%make_build

%check
make check

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/nftables
cp files/examples/* %buildroot%_sysconfdir/nftables/

%files
%doc COPYING
#%%doc %_docdir/%name
%dir %_sysconfdir/nftables
%attr(644,root,root) %config %_sysconfdir/nftables/*
%_libdir/lib%name.so.*
%_sbindir/*
%_man8dir/*


%changelog
* Wed May 02 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.4-alt1
- Version 0.8.4

* Sun Mar 04 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.3-alt1
- Version 0.8.3
- Remove dblatex from BR

* Mon Feb 05 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.2-alt1
- Version 0.8.2

* Fri Jan 19 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.1-alt1
- Version 0.8.1

* Fri Oct 13 2017 Alexei Takaseev <taf@altlinux.org> 1:0.8-alt1
- Version 0.8
- disable pdf

* Wed Dec 21 2016 Alexei Takaseev <taf@altlinux.org> 1:0.7-alt1
- Version 0.7

* Fri Jun 03 2016 Alexei Takaseev <taf@altlinux.org> 1:0.6-alt1
- Version 0.6

* Mon Dec 21 2015 Alexei Takaseev <taf@altlinux.org> 1:0.5-alt1
- Version 0.5

* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.3-alt1.git20140915
- Version 0.3

* Tue Jan 21 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.100-alt1
- first build for ALT Linux
