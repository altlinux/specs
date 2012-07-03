Name: radiusclient-ng
Version: 0.5.6
Release: alt1

Summary: Utility programs for RADIUS client library
License: BSD
Group: Networking/Other
URL: http://developer.berlios.de/projects/%name/
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: http://download.berlios.de/%name/%name-%version.tar.gz
Patch: radiusclient-ng-0.5.6-fedora-etc-install.patch

Requires: lib%name = %version-%release
BuildRequires: gcc-c++
%def_disable static

%package -n lib%name
Summary: RADIUS client shared library
Group: System/Libraries

%description -n lib%name
This package contains RADIUS client shared library.

%package -n lib%name-devel
Summary: RADIUS client development library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains RADIUS client development library.

%description
This package contains utility programs for RADIUS client library.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%_sbindir/*
%doc BUGS CHANGES COPYRIGHT doc/instop.html

%files -n lib%name
%_libdir/lib%name.so.*
%config(noreplace) %_sysconfdir/%name/
%_datadir/%name/

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name.h

%changelog
* Wed Jul 13 2011 Dmitry V. Levin <ldv@altlinux.org> 0.5.6-alt1
- Updated to 0.5.6.
- Fixed packaging.

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.5.3-alt4.1
- rebuild (with the help of girar-nmu utility)

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.5.3-alt4
- cleanup spec

* Tue Feb 26 2008 Denis Smirnov <mithraen@altlinux.ru> 0.5.3-alt3
- fix building

* Sun Jul 09 2006 Denis Smirnov <mithraen@altlinux.ru> 0.5.3-alt2
- fix requres (-devel not requires radiusclient-ng)
- move lib%name.so.2 to lib%name from lib%name-devel

* Tue May 23 2006 Denis Smirnov <mithraen@altlinux.ru> 0.5.3-alt1
- first build for Sisyphus

