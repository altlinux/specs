Name: libnetfilter_conntrack
Version: 1.0.6
Release: alt1
Epoch: 1

Summary: Netfilter conntrack userspace library
License: GPLv2+
Group: System/Libraries
Url: http://netfilter.org/projects/libnetfilter_conntrack/

# git://git.netfilter.org/%name
# git://git.altlinux.org/gears/l/%name
Source: %name-%version.tar

BuildRequires: libnfnetlink-devel libmnl-devel

%description
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

%package devel
Summary: Netfilter conntrack userspace library
Group: Development/C
Requires: %name = %EVR

%description devel
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/%name/
%_pkgconfigdir/*.pc

%changelog
* Wed Feb 22 2017 Michael Shigorin <mike@altlinux.org> 1:1.0.6-alt1
- Updated to 1.0.6 including clang/lcc-related pseudo-VLA fix:
  http://www.spinics.net/lists/netfilter-devel/msg43542.html

* Mon Nov 25 2013 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.4-alt1
- Updated to 1.0.4, required by iptables/libxt_connlabel.

* Mon Jun 24 2013 Anton Farygin <rider@altlinux.ru> 1:1.0.3-alt1
- New version

* Thu Aug 23 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1:0.9.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for libnetfilter_conntrack

* Sat Oct 30 2010 Anton Farygin <rider@altlinux.ru> 1:0.9.0-alt1
- New version
- updated build requires

* Sun Mar 01 2009 Avramenko Andrew <liks@altlinux.ru> 1:0.0.99-alt1
- New version
- Fix repocop warnings

* Sat Apr 19 2008 Avramenko Andrew <liks@altlinux.ru> 1:0.0.89-alt1
- New version

* Wed Nov 28 2007 Avramenko Andrew <liks@altlinux.ru> 1:0.0.82-alt1
- New version

* Mon Jul 30 2007 Avramenko Andrew <liks@altlinux.ru> 1:0.0.81-alt1
- New version (bug fixes)

* Fri Jul 06 2007 Avramenko Andrew <liks@altlinux.ru> 1:0.0.80-alt1
- New version

* Wed May 30 2007 Avramenko Andrew <liks@altlinux.ru> 1:0.0.75-alt1
- New version

* Mon May 07 2007 Avramenko Andrew <liks@altlinux.ru> 20070410-alt3
- BuildRequires changed from libnfnetlink to libnfnetlink-devel

* Thu Apr 13 2007 Avramenko Andrew <liks@altlinux.ru> 20070410-alt2
- Add post/postun section
- Split devel package
- Disable static

* Wed Apr 11 2007 Avramenko Andrew <liks@altlinux.ru> 20070410-alt1
- New version build (fix #11443)

* Fri Mar 23 2007 Avramenko Andrew <liks@altlinux.ru> 0.0.31-alt1
- Initial build for Sisyphus
