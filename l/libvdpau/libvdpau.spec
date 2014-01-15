%define docdir %_docdir/%name

Name: libvdpau
Version: 0.7
Release: alt1
Epoch: 1
Group: System/Libraries
Summary: VDPAU library
Url: http://cgit.freedesktop.org/~aplattner/libvdpau
License: Nvidia Free

Source: %name-%version.tar

Provides: libvdpau1 = %version-%release
Obsoletes: libvdpau1

# Automatically added by buildreq on Wed Jan 15 2014 (-bi)
# optimized out: elfutils fontconfig fonts-type1-urw ghostscript-common libX11-devel libstdc++-devel libwayland-client libwayland-server pkg-config python-base ruby ruby-stdlibs tex-common texlive-base texlive-base-bin texlive-common texlive-latex-base xorg-xproto-devel
#BuildRequires: doxygen fonts-ttf-google-droid-kufi fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif gcc-c++ ghostscript-classic glibc-devel-static graphviz libXext-devel rpm-build-ruby xorg-dri2proto-devel
BuildRequires: doxygen gcc-c++ ghostscript-classic glibc-devel graphviz libXext-devel xorg-dri2proto-devel
BuildRequires: /usr/bin/pdftex

%description
This package contains the libvdpau wrapper library and the
libvdpau_trace debugging library. To actually use a VDPAU device, you
need a vendor-specific implementation library.  Currently, this is
always libvdpau_nvidia.  You can override the driver name by setting the
VDPAU_DRIVER environment variable.

%package devel
Group: Development/C
Summary: Development files for VDPAU library
Requires: %name = %{?epoch:%epoch:}%version-%release
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

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING
%config(noreplace) %_sysconfdir/vdpau_wrapper.cfg
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
* Mon Sep 02 2013 Sergey V Turchin <zerg@altlinux.org> 1:0.7-alt1
- new version

* Mon Jul 22 2013 Sergey V Turchin <zerg@altlinux.org> 1:0.6-alt1
- new version

* Mon Nov 19 2012 Sergey V Turchin <zerg@altlinux.org> 1:0.5-alt0.M60P.2
- built for M60P

* Mon Nov 19 2012 Sergey V Turchin <zerg@altlinux.org> 1:0.5-alt1
- new version

* Tue Aug 28 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1:0.4.1-alt2.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for libvdpau

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

