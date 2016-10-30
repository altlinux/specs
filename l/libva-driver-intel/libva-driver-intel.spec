Name: libva-driver-intel
Version: 1.7.2
Release: alt1

Summary: VDPAU-based backend for VA API
License: GPLv2
Group: System/Libraries
Url: http://cgit.freedesktop.org/vaapi/intel-driver/

Conflicts: libva < 1.1.0

Source: %name-%version-%release.tar

BuildRequires: intel-gen4asm
BuildRequires: libdrm-devel libX11-devel libGL-devel libEGL-devel
BuildRequires: libva-devel >= 1.7.0

%description
Video decode driver for Intel chipsets.
Note that contents of this package were previously in libva package.

%prep
%setup

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
* Sun Oct 30 2016 L.A. Kostis <lakostis@altlinux.ru> 1.7.2-alt1
- 1.7.2.

* Thu Jul 07 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt1
- 1.7.1 released

* Tue Nov 18 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Fri Jan 24 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Thu Jun 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.18-alt1
- 1.0.18
