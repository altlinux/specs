Name: dnstop
Version: 20110502
Release: alt1

Summary: Displays various tables of DNS traffic on your network
License: BSD
Group: Monitoring

Url: http://dnstop.measurement-factory.com/
Source: http://dns.measurement-factory.com/tools/dnstop/src/dnstop-%version.tar.gz

# Automatically added by buildreq on Wed May 04 2011
# optimized out: libtinfo-devel
BuildRequires: libncurses-devel libpcap-devel

%description
dnstop is a libpcap application (ala tcpdump) that displays various tables of
DNS traffic on your network, including tables of source and destination IP
addresses, query types, top level domains and second level domains.

%prep
%setup

%build
%configure
%make_build

%install
install -pD -m755 dnstop %buildroot%_bindir/dnstop
install -pD -m644 dnstop.8 %buildroot%_man8dir/dnstop.8

%files
%_bindir/*
%_man8dir/*

%changelog
* Wed May 04 2011 Victor Forsiuk <force@altlinux.org> 20110502-alt1
- 20110502

* Wed Feb 02 2011 Victor Forsiuk <force@altlinux.org> 20110127-alt1
- version released 2011-01-27.

* Thu Jan 13 2011 Victor Forsiuk <force@altlinux.org> 20110107-alt1
- version released 2011-01-07.

* Thu Dec 30 2010 Victor Forsiuk <force@altlinux.org> 20101227-alt1
- Version released 2010-12-27.

* Mon Feb 09 2009 Victor Forsyuk <force@altlinux.org> 20090128-alt1
- Version released 2009-01-28.

* Thu May 15 2008 Victor Forsyuk <force@altlinux.org> 20080502-alt1
- Version from 2008-05-02.

* Tue Jun 19 2007 Victor Forsyuk <force@altlinux.org> 20070510-alt1
- Initial build.
