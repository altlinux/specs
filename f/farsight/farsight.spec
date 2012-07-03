Name: farsight
Version: 0.1.28
Release: alt3.1

Summary: A audio/video conferencing framework
Group: System/Libraries
License: LGPLv2+
URL: http://farsight.freedesktop.org/wiki/

Source0: http://farsight.freedesktop.org/releases/farsight/farsight-%{version}.tar.gz

Patch0: farsight-0.1.25-alt-unresolved.patch
Patch1: farsight-%version-alt-gst-feature.patch

Packager: Afanasov Dmitry <ender@altlinux.org>

# Automatically added by buildreq on Thu Jul 03 2008
BuildRequires: gcc-c++ gst-plugins-devel gtk-doc libjingle-devel

%description
FarSight is an audio/video conferencing framework specifically designed
for Instant Messengers. It aims to provide a code structure that will be
able to absorb as many video conferencing protocols as possible. It also
offers an interface to those Instant Messengers, allowing them to embed
the video feeds and controls into them.

FarSight is not a standalone application. It provides two APIs, one for
interfacing with the different "protocol modules" and one for interfacing
with the Instant Messenger GUI.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Requires: libjingle-devel >= 0.3.11
Requires: gst-plugins-devel

%description	devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-sequence-diagrams \
	--disable-sofia-sip \
	--disable-gnet \
	--disable-msnwebcam \
	--disable-yahoowebcam \
	--enable-gtk-doc \
	--enable-jingle-p2p \
	--enable-rtp

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc COPYING AUTHORS
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/gstelements.conf
%config(noreplace) %_sysconfdir/%name/gstcodecs.conf
%_libdir/lib*.so.*
%dir %_libdir/%name-0.1-3
%_libdir/%name-0.1-3/*.so
%_libdir/%name-0.1-3/*.la
#%exclude %_libdir/%name-0.1-3/*.la

%files devel
%_libdir/lib%name-0.1.so
%_libdir/pkgconfig/%name-0.1.pc
%_includedir/%name-0.1/
%_datadir/gtk-doc/html/%name

%changelog
* Mon Dec 22 2008 Afanasov Dmitry <ender@altlinux.org> 0.1.28-alt3.1
- rebuild with libjingle-0.3.12

* Tue Nov 25 2008 Afanasov Dmitry <ender@altlinux.org> 0.1.28-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Oct 27 2008 Afanasov Dmitry <ender@altlinux.org> 0.1.28-alt2
- fix build error (_m4_divert_diversion on m4/gst-feature.m4)

* Tue Jul 08 2008 Igor Zubkov <icesik@altlinux.org> 0.1.28-alt1
- 0.1.25 -> 0.1.28

* Thu Jul 03 2008 Igor Zubkov <icesik@altlinux.org> 0.1.25-alt2
- buildreq

* Fri Sep 28 2007 Igor Zubkov <icesik@altlinux.org> 0.1.25-alt1
- build for Sisyphus

* Sun Sep 16 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.25-1
- Update to 0.1.25.

* Wed Aug 22 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.24-1
- Update to 0.1.24.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.23-3
- Rebuild.

* Fri Aug 10 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.23-2
- Add new conf file.
- Add BR on check-devel.

* Fri Aug 10 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.23-1
- Update to 0.1.23.

* Thu Aug  2 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.21-2
- Update license tag.

* Mon Jul 30 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.21-1
- Update to 0.1.21.

* Fri Jun 15 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.20-2
- Add min version of libjingle needed.

* Thu Jun 14 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.20-1
- Update to 0.1.20.

* Sun May 20 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.19-2
- use correct libdir.

* Sun May 20 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.19-1
- Update to 0.1.19.

* Mon Apr 16 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.17-1
- Update to 0.1.17.

* Tue Mar 27 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.15-1
- Update to 0.1.15.
- Update URL & Source to new locations.

* Sun Dec  3 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.1.10-2
- Add requires for gstreamer-devel & gstreamer-plugins-base-devel to devel package.

* Wed Nov 22 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.1.8-3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.1.8-2
- Use correct license (LGPL).

* Wed Sep 13 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.1.8-1
- Intial FE spec.

