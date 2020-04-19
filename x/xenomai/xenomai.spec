%define _unpackaged_files_terminate_build 1

Name: xenomai
Version: 3.1
Release: alt1
Source0: %name-%version.tar
Summary: Real-Time Framework for Linux (Cobalt) (%version)
License: GPL-2.0+ and LGPL-2.0+ and LGPL-2.1 and MIT
Group: System/Kernel and hardware
Url: http://www.xenomai.org
Vcs: https://gitlab.denx.de/Xenomai/xenomai.git
ExclusiveArch: x86_64

BuildRequires: libiniparser-devel
#BuildRequires: doxygen asciidoc asciidoc-a2x w3m

%description
Xenomai is a Free Software project in which engineers from a wide
background collaborate to build a versatile real-time framework for
the Linux platform.

The main project goal is to help migrating industrial applications
from proprietary real-time systems to Linux.

Xenomai is about making various real-time operating system APIs
available to Linux-based platforms. When the target Linux kernel
cannot meet the requirements with respect to response time
constraints, Xenomai can also supplement it for delivering stringent
real-time guarantees based on an original dual kernel approach.

%package -n libxenomai1
Summary: Xenomai (Cobalt) system libraries (v%version)
Group: System/Libraries

%description -n libxenomai1
System libraries for Xenomai (Cobalt)

%package -n libxenomai-devel
Summary: Xenomai development headers (v%version)
Group: Development/C
Requires: libxenomai1 = %EVR
AutoReqProv: nocpp

%description -n libxenomai-devel
Header files for Xenomai Libraries

%package -n libxenomai-devel-static
Summary: Xenomai static libraries (Cobalt) (v%version)
Group: Development/C
Requires: libxenomai-devel = %EVR

%description -n libxenomai-devel-static
Static libraries for Xenomai (Cobalt)

%package -n xenomai-kernel-source
Summary: Xenomai (Cobalt) patch for Linux kernel (v%version)
Group: Development/Kernel
BuildArch: noarch
AutoReqProv: no

%description -n xenomai-kernel-source
This package is used only internally to build Xenomai kernel.

%prep
%setup

%build
%autoreconf
export CFLAGS=-fno-omit-frame-pointer
%configure \
	--with-core=cobalt \
	--includedir=/usr/include/xenomai \
	--with-testdir=%_libdir/xenomai/testsuite \
	--enable-smp \
	--enable-lazy-setsched \
	--enable-debug=symbols \
	--enable-dlopen-libs \

%make_build -s

%install
%makeinstall_std -s SUDO=false
rm -rf %buildroot/usr/src/debug
rm -rf %buildroot/usr/lib/debug
rm -rf %buildroot/usr/demo
mkdir -p %buildroot/usr/src/xenomai-kernel-source/config
cp -Ra	scripts	\
	include	\
	kernel	%buildroot/usr/src/xenomai-kernel-source/
cp config/version-{code,label} \
		%buildroot/usr/src/xenomai-kernel-source/config/
mv %buildroot/usr/sbin/version %buildroot/usr/sbin/xeno-version
mkdir -p %buildroot/etc/udev/rules.d
for f in kernel/cobalt/udev/*.rules; do
  cp $f %buildroot/etc/udev/rules.d/
done

# Only .so is required for dlopen test
rm -f %_libdir/xenomai/testsuite/*.a

# smokey should be non-stripped at all, stripping just
# debug is not enough.
%brp_strip_none %_libdir/xenomai/testsuite/smokey

%pre
%_sbindir/groupadd -r -f xenomai 2> /dev/null ||:

%files
%doc README
/etc/*.conf
/etc/udev/rules.d/*.rules
%_bindir/*
%exclude %_bindir/xeno-config
%exclude %_bindir/wrap-link.sh
%_sbindir/*
%dir %_libdir/xenomai
%_libdir/xenomai/testsuite

%files -n libxenomai1
%_libdir/lib*.so.*

%files -n libxenomai-devel
%_includedir/xenomai
%_libdir/*.so
%_bindir/xeno-config
%_bindir/wrap-link.sh
%_libdir/*.wrappers
%_libdir/dynlist.ld
%dir %_libdir/xenomai
%_libdir/xenomai/*.o

%files -n libxenomai-devel-static
%_libdir/lib*.a*

%files -n xenomai-kernel-source
%_usrsrc/xenomai-kernel-source

%changelog
* Sun Apr 19 2020 Vitaly Chikunov <vt@altlinux.org> 3.1-alt1
- Update to v3.1 (ABI r17).

* Sat Aug 24 2019 Vitaly Chikunov <vt@altlinux.org> 3.0.9.0.9.ge71785fe0-alt1
- Update to v3.0.9-9-ge71785fe0.

* Fri Jun 28 2019 Vitaly Chikunov <vt@altlinux.org> 3.0.8-alt3
- Add udev rules and groupadd.

* Thu Jun 27 2019 Vitaly Chikunov <vt@altlinux.org> 3.0.8-alt2
- Make proper -devel package.

* Fri Jun 21 2019 Vitaly Chikunov <vt@altlinux.org> 3.0.8-alt1
- Update to 3.0.8.
- Add xenomai-kernel-source package

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.4.8-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jun 02 2009 Michail Yakushin <silicium@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Mon May 18 2009 Michail Yakushin <silicium@altlinux.ru> 2.4.7-alt1
- intial build for ALT

