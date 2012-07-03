
Name: openconnect
Version: 3.20
Release: alt1
Summary: Open client for Cisco AnyConnect VPN

Group: Networking/Remote access
License: LGPLv2.1+
Url: http://www.infradead.org/openconnect.html

Source: %name-%version.tar
Patch0: openconnect-snapshot.patch
Patch1: %name-%version-alt-fix.patch

Requires: lib%name = %version-%release

BuildRequires: libssl-devel >= 0.9.8l-alt4
BuildRequires: libxml2-devel libproxy-devel zlib-devel
BuildRequires: vpnc-script
BuildRequires: python-modules python-modules-xml groff-extra
Requires: vpnc-script
Requires: openssl >= 0.9.8l-alt4

%description
This package provides a client for Cisco's "AnyConnect" VPN, which uses
HTTPS and DTLS protocols.

%package -n lib%name
Group: System/Libraries
Summary: Shared libraries for %name

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure --enable-static=no
echo "const char *openconnect_version_str = \"v%version\";" > version.c
%make_build

%install
make DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%doc TODO COPYING.LGPL
%_sbindir/%name
%_man8dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 3.20-alt1
- 3.20

* Wed Nov 16 2011 Alexey Shabalin <shaba@altlinux.ru> 3.14-alt1
- 3.14

* Thu Sep 15 2011 Alexey Shabalin <shaba@altlinux.ru> 3.12-alt1
- 3.12

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 3.02-alt1
- 3.02

* Wed Apr 20 2011 Alexey Shabalin <shaba@altlinux.ru> 2.26-alt2
- update BR:

* Fri Nov 12 2010 Alexey Shabalin <shaba@altlinux.ru> 2.26-alt1
- 2.26

* Tue Oct 12 2010 Alexey Shabalin <shaba@altlinux.ru> 2.25-alt2
- pre 2.26

* Sun May 16 2010 Alexey Shabalin <shaba@altlinux.ru> 2.25-alt1
- 2.25

* Mon Mar 15 2010 Alexey Shabalin <shaba@altlinux.ru> 2.22-alt1.git9b782
- git snapshot 9b782af3aa4d2fb3b238bbfdd12b217db80f83cd
- rebuild with new libproxy-0.4.0

* Wed Mar 03 2010 Alexey Shabalin <shaba@altlinux.ru> 2.21-alt2.git357c85
- git snapshot 357c85e8db1949565e99695b17cf5dadbc679269

* Sat Jan 16 2010 Alexey Shabalin <shaba@altlinux.ru> 2.21-alt1
- Initial packaging
