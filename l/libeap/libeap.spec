Name: libeap
Version: 0.7.2
Release: alt1

Summary: EAP Peer shared library
License: GPL/BSD
Group: System/Libraries

Url: http://hostap.epitest.fi/

Source: %name-%version-%release.tar

BuildRequires: libssl-devel

%description
%summary

%package devel
Summary: %name development files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides %name development files.

%prep
%setup

%build
make -C eap_peer

%install
%make_install DESTDIR=%buildroot LIBDIR=%_libdir install -C eap_peer

%files
%_libdir/libeap.so.*

%files devel
%_libdir/libeap.so
%_includedir/eap_peer
%_pkgconfigdir/*.pc

%changelog
* Mon Oct 25 2010 Alexey I. Froloff <raorn@altlinux.org> 0.7.2-alt1
- updated to 0.7.2

* Sun Sep 12 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.10-alt1
- initial build
