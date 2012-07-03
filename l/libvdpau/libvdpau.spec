%define docdir %_docdir/%name

Name: libvdpau
Version: 0.4.1
Release: alt2.qa1
Epoch: 1
Group: System/Libraries
Summary: VDPAU library
Url: http://cgit.freedesktop.org/~aplattner/libvdpau
License: Nvidia Free

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Buildrequires: libX11-devel libXext-devel gcc-c++ doxygen graphviz tetex-core xorg-dri2proto-devel
Provides: libvdpau1 = %version-%release
Obsoletes: libvdpau1

%description
This package contains the libvdpau wrapper library and the
libvdpau_trace debugging library. To actually use a VDPAU device, you
need a vendor-specific implementation library.  Currently, this is
always libvdpau_nvidia.  You can override the driver name by setting the
VDPAU_DRIVER environment variable.

%package devel
Group: Development/C
Summary: Development files for VDPAU library
Requires: %name = %version-%release
Provides: libvdpau1-devel = %version-%release
Obsoletes: libvdpau1-devel

%description devel
Development files needed to build VDPAU applications

%package devel-doc
Group: Development/C
Summary: Documentation for VDPAU library
Requires: %name-devel = %version
BuildArch: noarch
Provides: libvdpau1-doc = %version-%release
Obsoletes: libvdpau1-doc

%description devel-doc
Documentation for VDPAU library

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING
%dir %_libdir/vdpau
%_libdir/vdpau/*.so*
%_libdir/libvdpau*.so.*

%files devel
%_includedir/vdpau
%_libdir/libvdpau*.so
%_pkgconfigdir/*.pc

%files devel-doc
%dir %docdir
%docdir/html

%changelog
* Fri May 13 2011 Andrey Cherepanov <cas@altlinux.org> 1:0.4.1-alt2.qa1
- Obsoletes libvdpau1

* Wed Mar 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.1-alt2
- rebuild

* Tue Jan 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.4.1-alt1
- 0.4.1

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1:0.4-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Thu Feb 18 2010 L.A. Kostis <lakostis@altlinux.ru> 1:0.4-alt1
- New version.

* Wed Dec 02 2009 L.A. Kostis <lakostis@altlinux.ru> 1:0.3-alt1
- New version.
- Add documentation, remove soname hack (better track soname changes
  manually).

* Thu Oct 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 1:0.2-alt1
- Initial build for Sisyphus.

