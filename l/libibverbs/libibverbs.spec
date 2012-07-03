Name: libibverbs
Version: 1.1.4
Release: alt3

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Summary: A library for direct userspace use of InfiniBand

Group: System/Libraries
License: GPL/BSD

Url: http://openib.org/
# git://git.kernel.org/pub/scm/libs/infiniband/libibverbs.git
Source: %name-%version.tar.gz
#Patch: verbs_man_page.patch
#Patch1: XRC_man_pages.patch
#Patch2: XRC_base_implementation.patch
#Patch3: XRC_RCV_QP.patch
#Patch4: pthread_cond_t_fields.patch

Patch1: verbs_man_page.patch
Patch2: XRC_man_pages.patch
Patch3: XRC_base_implementation.patch
Patch4: XRC_RCV_QP.patch
Patch5: pthread_cond_t_fields.patch
Patch6: rocee_link_layer.patch
Patch7: rocee_kernel_accept_link_layer.patch
Patch8: rocee_get_mac.patch
Patch9: rocee_examples.patch
Patch10: qpt_raw_eth.patch
Patch11: configure_in-AC_PROG_LIBTOOL-for-automake.patch

# Automatically added by buildreq on Mon Aug 20 2007
BuildRequires: gcc-c++ glibc-devel libsysfs-devel

%description
libibverbs is a library that allows userspace processes to use
InfiniBand "verbs" as described in the InfiniBand Architecture
Specification.  This includes direct hardware access for fast path
operations.

For this library to be useful, a device-specific plug-in module should
also be installed.

%package devel
Summary: Development files for the libibverbs library
Group: Development/C
Requires: %name = %version-%release
Requires: libsysfs-devel

%description devel
Development libraries and header files for the libibverbs library.

%package devel-static
Summary: Static libraries for the libibverbs library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libraries for the libibverbs library.

%package utils
Summary: Examples for the libibverbs library
Group: System/Base
Requires: %name = %version-%release

%description utils
Useful libibverbs1 example programs such as ibv_devinfo, which
displays information about InfiniBand devices.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
touch NEWS
./autogen.sh
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -d %buildroot%_sysconfdir/%name.d/

%files
%doc AUTHORS COPYING ChangeLog README
%dir %_sysconfdir/%name.d/
%_libdir/*.so.*

%files devel
%_man3dir/*
%_man7dir/*
%_libdir/lib*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%files utils
%_bindir/*
%_man1dir/*

%changelog
* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt3
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt2
- Rebuilt for soname set-versions

* Tue Aug 17 2010 Andriy Stepanov <stanv@altlinux.ru> 1.1.4-alt1
- Version 1.1.4 (OFED 1.5.1)

* Tue Nov 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20091030
- Version 1.1.3

* Wed Jul 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Replace build from tar by build from upstream git repository

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Thu Apr 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt3
- Add static library (NMU)

* Fri Sep 19 2008 Stanislav Ievlev <inger@altlinux.org> 1.1.1-alt1.M41.1
- build for 4.1

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.1.1-alt2
- OFED 1.3.1

* Tue Aug 21 2007 Stanislav Ievlev <inger@altlinux.org> 1.1.1-alt1
- 1.1.1
- add plugin directory to package

* Mon Aug 20 2007 Stanislav Ievlev <inger@altlinux.org> 1.0.4-alt1
- Initial build
