Name: xtables-addons
Version: 1.42
Release: alt1
Summary: IP tables addons
Group: System/Kernel and hardware

URL: http://xtables-addons.sourceforge.net/
License: GPLv2

# git://xtables-addons.git.sf.net/gitroot/xtables-addons/xtables-addons.git
# git://git.altlinux.org/gears/x/xtables-addons.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%define _libexecdir /usr/libexec

BuildRequires: libiptables-devel libmnl-devel perl-Text-CSV_XS
Requires: iptables
ExclusiveArch: %ix86 x86_32 x86_64

%description
Xtables-addons is the proclaimed successor to patch-o-matic(-ng).
It contains extensions that were not accepted in the main Xtables

%package ipset
Summary: Tools for managing sets of IP or ports with iptables
License: GPLv2
Group: System/Kernel and hardware
Requires: libipset = %version-%release
Conflicts: ipset

%description ipset
IP sets are a framework inside the Linux 2.4.x and 2.6.x kernel,
which can be administered by the ipset utility.
Depending on the type, currently an IP set may store IP addresses,
(TCP/UDP) port numbers or IP addresses with MAC addresses in a way,
which ensures lightning speed when matching an entry against a set.

ipset may be the proper tool for you, if you want to
 * store multiple IP addresses or port numbers and match against the
   collection by iptables at one swoop;
 * dynamically update iptables rules against IP addresses or ports
   without performance penalty;
 * express complex IP address and ports based rulesets with one single
   iptables rule and benefit from the speed of IP sets

%package -n libipset
Summary: Linux ipset library
License: GPLv2
Group: System/Libraries

%description -n libipset
ipset library

%package -n libipset-devel
Summary: Linux ipset library
License: GPLv2
Group: Development/C
Requires: libipset = %version-%release

%description -n libipset-devel
ipset library

%package geoip-utils
Summary: Tools for build and update geoip data
License: GPLv2
Group: System/Kernel and hardware
BuildArch: noarch

%description geoip-utils
Tools for build and update geoip data

%package -n kernel-source-%name
Summary: xtables module sources
Group: Development/Kernel
BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description -n kernel-source-%name
XTable addons module sources for Linux kernel.

%prep
%setup
%patch -p1
%autoreconf
%configure --libdir=/%_lib --with-kbuild=no --with-xtlibdir=/%_lib/iptables

%build
%make_build

%install
%makeinstall_std
tar -xf %SOURCE0
mv %name-%version/extensions kernel-source-%name-%version
cp mconfig kernel-source-%name-%version/mconfig
cp kernel-source-%name-%version/Mbuild kernel-source-%name-%version/Makefile
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/kernel-source-%name-%version.tar.bz2 kernel-source-%name-%version

%files
%doc README
%_sbindir/iptaccount
%attr(0755,root,root) /%_lib/libx*.so*
/%_lib/iptables/*.so*
%_man8dir/xtables-addons*

%files geoip-utils
%_man1dir/*
%_libexecdir/xtables-addons/*

%files -n kernel-source-%name
%kernel_src/*

%changelog
* Fri May 25 2012 Dmitry V. Levin <ldv@altlinux.org> 1.42-alt1
- Fixed build.
- Built with libxtables.so.7.
- Blind update to v1.42-3-g1e8da7c.
- No more ipset-related subpackages, the feature was removed in v1.42~1.

* Mon Oct 10 2011 Anton Farygin <rider@altlinux.ru> 1.39-alt1
- new version

* Sun Mar 06 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.33-alt1
- Update new version

* Sun Jan 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.32-alt1
- Update new version
- Add ipset subpackage and libipset

* Wed Oct 13 2010 Anton Farygin <rider@altlinux.ru> 1.30-alt1
- Initial build for Sisyphus, thanls to Sergei Epiphanov for specfile
