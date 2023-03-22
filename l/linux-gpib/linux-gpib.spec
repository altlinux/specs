Name: linux-gpib
Version: 4.3.4
Release: alt2

Summary: Support package for GPIB (IEEE 488) hardware
Group: System/Kernel and hardware
Url: http://linux-gpib.sourceforge.net/
License: GPLv2

BuildRequires(pre): rpm-build-python3
BuildRequires: rpm-build-kernel docbook-utils
BuildRequires: python3-devel tcl-devel perl-devel
Requires: fxload firmware-gpib

Source0: %name-%version.tar
Source1: %name-kernel-%version.tar.bz2

%description
The Linux GPIB Package is a support package for GPIB (IEEE 488) hardware.
The package contains kernel driver modules, and a C user-space library
with Guile, Perl, PHP, Python and TCL bindings. The API of the C library
is intended to be compatible with National Instrument's GPIB library.

%package devel
Summary: Development files for %name
Group: Development/Other
%description devel
This package contains development files for %name

%package -n python3-module-%name
Summary: Python bindings for %name
Group: Development/Other
%description -n python3-module-%name
This package contains python bindings for %name

%package -n tcl-%name
Summary: Tcl bindings for %name
Group: Development/Other
%description -n tcl-%name
This package contains tcl bindings for %name

%package -n kernel-source-%name
Summary: GPIB modules sources for Linux kernel
Group: Development/Kernel
BuildArch: noarch
Provides: kernel-src-%name = %version-%release
%description -n kernel-source-%name
This package contains GPIB modules sources for Linux kernel.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
# Version in pc-file is set to GPIB_SO_VERSION which is 3:0:3.
# This causes "invalid pkg-config output" error. Replacing it with 3.0.3:
sed -r -i -e '/Version:/s/([0-9]+):/\1./g' %buildroot/%_pkgconfigdir/libgpib.pc

# move doc and example folders
mkdir -p %buildroot%_docdir
mv %buildroot%_datadir/linux-gpib-user %buildroot%_docdir/%name-%version
cp COPYING README doc/linux-gpib.pdf %buildroot%_docdir/%name-%version
cp -r language/tcl/examples  %buildroot%_docdir/%name-%version/tcl-examples

# move udev rules
mkdir -p %buildroot/lib/udev
mv %buildroot/%_sysconfdir/udev/rules.d %buildroot/lib/udev

# install kernel module sources
install -pDm0644 %SOURCE1 %kernel_srcdir/%name-%version.tar.bz2

%_sbindir/groupadd -r -f gpib 2> /dev/null ||:

%files
%dir %_docdir/%name-%version
%dir %_docdir/%name-%version/html
%doc %_docdir/%name-%version/COPYING
%doc %_docdir/%name-%version/README
%doc %_docdir/%name-%version/linux-gpib.pdf
%doc %_docdir/%name-%version/html/*
/lib/udev/rules.d/*
%_libexecdir/udev/*
%config(noreplace) %_sysconfdir/gpib.conf
%_bindir/ibterm
%_bindir/ibtest
%_bindir/findlisteners
%_libdir/libgpib.so.*
%_sbindir/gpib_config

%files devel
%_includedir/gpib/*
%_libdir/libgpib.so
%_pkgconfigdir/*

%files -n python3-module-%name
%python3_sitelibdir/*

%files -n tcl-%name
%doc %_docdir/%name-%version/tcl-examples/*
%doc %_docdir/%name-%version/tcl-examples/.xsetup
%_libdir/libgpib_tcl*

%files -n kernel-source-%name
%kernel_src/%name-%version.tar.bz2

%changelog
* Wed Mar 22 2023 Vladislav Zavjalov <slazav@altlinux.org> 4.3.4-alt2
- install udev rules to /lib/udev/rules.d (new sisyphus_check requirement)

* Tue Apr 06 2021 Vladislav Zavjalov <slazav@altlinux.org> 4.3.4-alt1
- v4.3.4

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.3.0-alt5
- Porting to python3.

* Thu Feb 06 2020 Vladislav Zavjalov <slazav@altlinux.org> 4.3.0-alt3
- fix callback type for driver_find_device for 5.4 kernel

* Thu Feb 06 2020 Vladislav Zavjalov <slazav@altlinux.org> 4.3.0-alt2
- remove unneeded include <asm/segment.h>

* Wed Feb 05 2020 Vladislav Zavjalov <slazav@altlinux.org> 4.3.0-alt1
- v4.3.0

* Thu Mar 28 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 4.2.0-alt3
- fixed to build with 5.0 kernel

* Mon Feb 18 2019 Vladislav Zavjalov <slazav@altlinux.org> 4.2.0-alt2
- fix Repocop warnings: docdir-is-not-owned, buildroot

* Sat Feb 16 2019 Vladislav Zavjalov <slazav@altlinux.org> 4.2.0-alt1
- v4.2.0

