Name: libva-driver-intel
Version: 1.8.3
Release: alt2%ubt

Summary: VA-API (Video Acceleration API) user mode driver for Intel GEN Graphics family
License: GPLv2
Group: System/Libraries
Url: http://cgit.freedesktop.org/vaapi/intel-driver/

Conflicts: libva < 1.1.0

Source: %name-%version.tar

BuildRequires: intel-gen4asm
BuildRequires: libdrm-devel libX11-devel libGL-devel libEGL-devel
BuildRequires: libva-devel >= 1.7.0
BuildRequires(pre): rpm-build-ubt

%description
Video decode driver for Intel chipsets.

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
* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.8.3-alt2%ubt
- fixed summary (closes: #33639)

* Thu Jul 06 2017 Anton Farygin <rider@altlinux.ru> 1.8.3-alt1%ubt
- 1.8.3

* Thu Jun 01 2017 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- new version

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
