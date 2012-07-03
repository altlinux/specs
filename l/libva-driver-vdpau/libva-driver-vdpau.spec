%define upstreamname vdpau-video

Name: libva-driver-vdpau
Version: 0.7.3
Release: alt1
Summary: VDPAU-based backend for VA API
Group: System/Libraries
License: GPLv2
Url: http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/

Source: %upstreamname-%version.tar

BuildRequires: libvdpau-devel libva-devel libX11-devel libGL-devel

%description
Video decode driver for NVIDIA chipsets (VDPAU implementation)

%prep
%setup -q -n %upstreamname-%version

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS NEWS
%_libdir/dri/*.so

%changelog
* Wed Mar 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.7.3-alt1
- 0.7.3 release

* Sat Feb 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.7.3-alt0.pre6
- 0.7.3.pre6

* Tue Jan 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.7.3-alt0.pre4
- 0.7.3.pre4

* Tue Jan 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Wed Aug 25 2010 Konstantin Pavlov <thresh@altlinux.org> 0.6.10-alt1
- 0.6.10 release.

* Thu Mar 18 2010 Konstantin Pavlov <thresh@altlinux.org> 0.6.6-alt1
- 0.6.6 release.

* Thu Jan 28 2010 Konstantin Pavlov <thresh@altlinux.org> 0.6.3-alt1
- 0.6.3 release.

* Wed Jan 27 2010 Konstantin Pavlov <thresh@altlinux.org> 0.6.2-alt1
- 0.6.2 release.

* Fri Oct 09 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1
- 0.5.0 release.

* Tue Sep 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.4.1-alt1
- 0.4.1 release.

* Fri Apr 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.3.1-alt1
- 0.3.1 release.

* Mon Apr 20 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.3.0-alt1
- Initial build for ALT Linux.

