%define mname ipt_NETFLOW
Name: kernel-src-%mname
Version: 1.8.2
Release: alt2
Summary: Netflow iptables module for Linux kernel
Group: Development/Kernel
BuildArch: noarch
License: GPLv3+
URL: http://http://sourceforge.net/projects/ipt-netflow
Source: ipt-netflow-%version.tar
Patch: ipt-netflow-%version-%release.patch
Provides: kernel-source-%mname = %version-%release

BuildRequires: rpm-build-kernel

%description
%mname is very fast and effective Netflow exporting module for Linux kernel.
Designed for Linux router with heavy network load.
This is netfilter/iptables module adding support for NETFLOW target.


%prep
%setup -q -n ipt-netflow-%version
%patch -p1


%build
install -d -m 0755 %mname-%version
cd %mname-%version
ln -sf ../{%mname.[ch],murmur3.h} ./
echo "obj-m = %mname.o" > Makefile


%install
install -d -m 0755 %buildroot%kernel_src
tar -chJf %buildroot%kernel_src/%mname-%version.tar.xz %mname-%version


%files
%_usrsrc/kernel


%changelog
* Mon Oct 21 2013 Led <led@altlinux.ru> 1.8.2-alt2
- upstream fixes

* Mon Oct 14 2013 Led <led@altlinux.ru> 1.8.2-alt1
- initial build
