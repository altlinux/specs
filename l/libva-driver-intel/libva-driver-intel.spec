Name: libva-driver-intel
Version: 1.0.18
Release: alt1

Summary: VDPAU-based backend for VA API
License: GPLv2
Group: System/Libraries
Url: http://cgit.freedesktop.org/vaapi/intel-driver/

Conflicts: libva < 1.1.0

Source: %name-%version-%release.tar

BuildRequires: libva-devel libX11-devel libGL-devel

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
* Thu Jun 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.18-alt1
- 1.0.18
