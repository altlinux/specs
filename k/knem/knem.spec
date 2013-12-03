%def_disable debug
%def_disable hwloc
%define _group rdma

%define Name KNEM
Name: knem
Summary: High-Performance Intra-Node MPI Communication
Version: 1.1.0
Release: alt6
License: BSD
Group: System/Kernel and hardware
URL: http://runtime.bordeaux.inria.fr/%name
Source: %url/download/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-kernel
%{?_enable_hwlock:BuildRequires: pkgconfig(libhwloc)}
BuildRequires: unifdef

%description
%Name is a Linux kernel module enabling high-performance intra-node MPI
communication for large messages. %Name offers support for asynchronous
and vectorial data transfers as well as offloading memory copies on to
Intel I/OAT hardware.


%package tools
Summary: %Name High-Performance Intra-Node MPI Communication tools
Group: System/Kernel and hardware

%description tools
%Name is a Linux kernel module enabling high-performance intra-node MPI
communication for large messages. %Name offers support for asynchronous
and vectorial data transfers as well as offloading memory copies on to
Intel I/OAT hardware.


%package devel
Summary: Files for build with %Name
Group: Development/C
BuildArch: noarch

%description devel
%Name is a Linux kernel module enabling high-performance intra-node MPI
communication for large messages. %Name offers support for asynchronous
and vectorial data transfers as well as offloading memory copies on to
Intel I/OAT hardware.

This package contains header file for build with %Name.


%package devel-doc
Summary: Files for build with %Name
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
%Name is a Linux kernel module enabling high-performance intra-node MPI
communication for large messages. %Name offers support for asynchronous
and vectorial data transfers as well as offloading memory copies on to
Intel I/OAT hardware.

This package contains API docs for build with %Name.


%package -n kernel-source-%name
Summary: %Name module sources for Linux kernel
Group: Development/Kernel
BuildArch: noarch
Provides: kernel-src-%name = %version-%release

%description -n kernel-source-%name
%Name is a Linux kernel module enabling high-performance intra-node MPI
communication for large messages. %Name offers support for asynchronous
and vectorial data transfers as well as offloading memory copies on to
Intel I/OAT hardware.
This package contains %Name module sources for Linux kernel.


%prep
%setup
%patch -p1
install -d -m 0755 %name-%version
cat > %name-%version/Makefile <<"__EOF__"
obj-m += knem.o
knem-objs := knem_main.o

KSRC ?= /lib/modules/`uname -r`/build
KHDR ?= $(KSRC)
KREL ?= dummy

knem.ko: knem_checks.h knem_io.h knem_hal.h knem_config.h knem_main.c
	$(MAKE) -C $(KSRC) M=$(CURDIR) EXTRA_CFLAGS="-include $(CURDIR)/knem_checks.h --include $(CURDIR)/knem_config.h" modules

knem_checks.h: check_kernel_headers.sh
	sh check_kernel_headers.sh knem_checks.h $(KSRC) $(KHDR) $(KREL)
__EOF__
ln -sr driver/linux/*.{c,h,sh} %name-%version/
unifdef -D__KERNEL__ -o %name-%version/%{name}_io.h common/%{name}_io.h || [ $? = 1 ]
unifdef -U__KERNEL__ -o common/%{name}_io.h common/%{name}_io.h  || [ $? = 1 ]


%build
./autogen.sh
%configure \
	--sysconfdir=%_sysconfdir/udev/rules.d \
	%{subst_enable debug} \
	%{subst_enable hwloc} \
	--without-linux \
	--disable-silent-rules
%make_build

ln -s ../common/%{name}_config.h %name-%version/

gzip -9c ChangeLog > ChangeLog.gz


%install
%makeinstall_std docdir=%_docdir/%name-%version
rm -rf %buildroot%_sbindir

install -d -m 0755 %kernel_srcdir
install -p -m 0644 AUTHORS COPYING ChangeLog.* README REPORTING-BUGS TODO %buildroot%_docdir/%name-%version/

tar -cJhf %kernel_srcdir/%name-%version.tar.xz %name-%version


%if 0
%post
%_sbindir/groupadd -r -f %_group &> /dev/null ||:
%endif


%files tools
%doc %_docdir/%name-%version
%exclude %_docdir/%name-%version/%name-api.html
%exclude %_docdir/%name-%version/ChangeLog.*
%_bindir/*
%exclude %_sysconfdir/udev/rules.d/*


%files devel
%_includedir/*


%files devel-doc
%dir %doc %_docdir/%name-%version
%doc %_docdir/%name-%version/%name-api.html
%doc %_docdir/%name-%version/ChangeLog.*


%files -n kernel-source-%name
%_usrsrc/kernel


%changelog
* Tue Dec 03 2013 Led <led@altlinux.ru> 1.1.0-alt6
- upstream updates

* Tue Nov 26 2013 Led <led@altlinux.ru> 1.1.0-alt5
- upstream fixes

* Fri Sep 27 2013 Led <led@altlinux.ru> 1.1.0-alt4
- upstream fixes

* Sun Sep 08 2013 Led <led@altlinux.ru> 1.1.0-alt3
- upstream updates

* Sun Aug 11 2013 Led <led@altlinux.ru> 1.1.0-alt2
- upstream updates

* Wed Jul 31 2013 Led <led@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sat Jul 06 2013 Led <led@altlinux.ru> 1.0.90-alt1
- 1.0.90
- updated summary and description of kernel-source-%name

* Thu Jun 27 2013 Led <led@altlinux.ru> 1.0.0-alt2
- cleaned up spec

* Thu Jan 24 2013 Led <led@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Mon May 14 2012 Led <led@massivesolutions.co.uk> 0.9.8-cx2
- driver: make sure the singleuse flag is consistent when finding a region
- added kernel-source-%%name package

* Tue Feb 21 2012 Led <led@massivesolutions.co.uk> 0.9.8-cx1
- 0.9.8

* Fri Jul 29 2011 Led <led@massivesolutions.co.uk> 0.9.7-cx1
- 0.9.7

* Tue May 10 2011 Led <led@altlinux.ru> 0.9.6.90-cx0.1
- initial build
