Name: spice-protocol
Version: 0.10.1
Release: alt1
Summary: Spice protocol header files
Group: Development/C
License: BSD
Url: http://www.spice-space.org/

Source: http://www.spice-space.org/download/releases/%name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

%description
Header files describing the spice protocol and the para-virtual graphics card QXL.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%doc COPYING NEWS
%_includedir/spice-1
%_datadir/pkgconfig/*.pc

%changelog
* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Thu Nov 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue May 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt2
- upstream/0.8 snapshot with fixes from upstream/master

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Wed Jan 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Sat Nov 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALT Linux Sisyphus
