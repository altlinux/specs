%define mname ipt_NETFLOW
Name: kernel-src-%mname
Version: 2.0
Release: alt1
Summary: Netflow iptables module for Linux kernel
Group: Development/Kernel
BuildArch: noarch
License: GPLv3+
URL: http://http://sourceforge.net/projects/ipt-netflow
Source: ipt-netflow-%version.tar
#Patch: ipt-netflow-%version-%release.patch
Provides: kernel-source-%mname = %version-%release

BuildRequires: rpm-build-kernel

%description
%mname is very fast and effective Netflow exporting module for Linux kernel.
Designed for Linux router with heavy network load.
This is netfilter/iptables module adding support for NETFLOW target.


%prep
%setup -q -n ipt-netflow-%version
#patch -p1


%build
install -d -m 0755 %mname-%version
cd %mname-%version
ln -sf ../{%mname.[ch],murmur3.h} ./
cat > Makefile <<__EOF__
obj-m = %mname.o
EXTRA_CFLAGS += -DENABLE_DEBUGFS -DSNMP_RULES
__EOF__


%install
install -d -m 0755 %buildroot%kernel_src
tar -chJf %buildroot%kernel_src/%mname-%version.tar.xz %mname-%version


%files
%_usrsrc/kernel


%changelog
* Thu Aug 14 2014 Led <led@altlinux.ru> 2.0-alt1
- 2.0

* Thu Jul 10 2014 Led <led@altlinux.ru> 1.8.3-alt4
- upstream updates and fixes

* Sun Jun 15 2014 Led <led@altlinux.ru> 1.8.3-alt3
- upstream updates and fixes

* Mon Jun 09 2014 Led <led@altlinux.ru> 1.8.3-alt2
- upstream updates

* Thu Jun 05 2014 Led <led@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Wed Jan 08 2014 Led <led@altlinux.ru> 1.8.2-alt9
- upstream fixes

* Mon Dec 16 2013 Led <led@altlinux.ru> 1.8.2-alt8
- upstream fixes

* Sat Nov 30 2013 Led <led@altlinux.ru> 1.8.2-alt7
- upstream fixes

* Fri Nov 29 2013 Led <led@altlinux.ru> 1.8.2-alt6
- upstream updates and fixes

* Tue Nov 12 2013 Led <led@altlinux.ru> 1.8.2-alt5
- upstream updates and fixes

* Fri Nov 01 2013 Led <led@altlinux.ru> 1.8.2-alt4
- upstream fixes

* Fri Nov 01 2013 Led <led@altlinux.ru> 1.8.2-alt3
- upstream updates and fixes

* Mon Oct 21 2013 Led <led@altlinux.ru> 1.8.2-alt2
- upstream fixes

* Mon Oct 14 2013 Led <led@altlinux.ru> 1.8.2-alt1
- initial build
