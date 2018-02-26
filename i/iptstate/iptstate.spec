Name: iptstate
Version: 2.2.3
Release: alt1

Summary: Display iptables state table information in a "top"-like interface
License: zlib/libpng license
Group: Monitoring

URL: http://www.phildev.net/iptstate/
Source: http://downloads.sourceforge.net/iptstate/iptstate-%version.tar.bz2

# Automatically added by buildreq on Mon Apr 04 2011
BuildRequires: gcc-c++ libncurses-devel libnetfilter_conntrack-devel

%description
IP Tables State (iptstate) was originally written to implement the
"state top" feature of IP Filter in iptables. "State top" displays
the states held by your stateful firewall in a top-like manner.

%prep
%setup

%build
make CXXFLAGS="%optflags %optflags_nocpp"

%install
make PREFIX="%buildroot/usr" install

%files
%doc BUGS CONTRIB Changelog LICENSE README WISHLIST
%_sbindir/*
%_man8dir/*

%changelog
* Mon Apr 04 2011 Victor Forsiuk <force@altlinux.org> 2.2.3-alt1
- 2.2.3

* Sat Oct 30 2010 Anton Farygin <rider@altlinux.ru> 2.2.2-alt1.1
- NMU: rebuild with new libnetfilter_conntrack

* Fri Oct 09 2009 Victor Forsyuk <force@altlinux.org> 2.2.2-alt1
- 2.2.2

* Tue Oct 28 2008 Victor Forsyuk <force@altlinux.org> 2.2.1-alt4
- Fix FTBFS with gcc4.3.

* Mon Apr 23 2007 Victor Forsyuk <force@altlinux.org> 2.2.1-alt3
- Update buildreqs due to changes in libnetfilter_conntrack packaging.

* Thu Apr 12 2007 Victor Forsyuk <force@altlinux.org> 2.2.1-alt2
- Build with libnetfilter_conntrack.

* Fri Mar 23 2007 Victor Forsyuk <force@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Oct 20 2006 Victor Forsyuk <force@altlinux.org> 2.1-alt1
- 2.1

* Thu Oct 05 2006 Victor Forsyuk <force@altlinux.org> 2.0-alt1
- 2.0

* Mon Apr 18 2005 Victor Forsyuk <force@altlinux.ru> 1.4-alt1
- 1.4

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.3-alt1.1
- Rebuilt with libstdc++.so.6.

* Sat Jun 14 2003 Victor Forsyuk <force@altlinux.ru> 1.3-alt1
- New URL and source location.
- Better Summary.
- Better optimization: add "-fno-exceptions -fno-rtti".

* Wed Oct 30 2002 Victor Forsyuk <force@altlinux.ru> 1.2.1-alt1
- Initial build for Sisyphus.
