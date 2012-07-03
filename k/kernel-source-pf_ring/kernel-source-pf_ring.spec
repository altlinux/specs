Name: kernel-source-pf_ring
Version: 4.4.1
Release: alt1

Summary: Packet capture acceleration by means of a ring buffer
License: GPL
Group: Development/Kernel
Url: http://www.ntop.org/PF_RING.html
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source: %name-%version.tar

BuildArch: noarch
BuildPreReq: kernel-build-tools

%description
PF_RING is a high speed packet capture library that turns a commodity PC into an efficient and cheap
network measurement box suitable for both packet and active traffic analysis and manipulation.
Moreover, PF_RING opens totally new markets as it enables the creation of efficient application such as
traffic balancers or packet filters in a matter of lines of codes.

PF_RING module sources for Linux kernel.

#### KERNEL HEADERS ##########
%package -n kernel-headers-pf_ring
Summary: Header files for the PF_RING module
Group: Development/Kernel
Requires: glibc-kernheaders

%description -n kernel-headers-pf_ring
These are the C header files for the PF_RING modules system,
which define structures and constants that are needed when building
programs that use PF_RING.

%prep
%setup -c -q

%install

mkdir -p %kernel_srcdir
mkdir -p %buildroot%_includedir/linux-default/include/linux
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version
cp -r %name-%version/linux/pf_ring.h %buildroot%_includedir/linux-default/include/linux

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n kernel-headers-pf_ring
%_includedir/linux-default/include/linux/pf_ring.h

%changelog
* Thu Oct 14 2010 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Fri Feb 26 2010 Alexey Shabalin <shaba@altlinux.ru> 4.1.3-alt2
- add kernel-headers-pf_ring package

* Wed Feb 17 2010 Alexey Shabalin <shaba@altlinux.ru> 4.1.3-alt1
- initial build 
