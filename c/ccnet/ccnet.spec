%def_disable server
Name: ccnet
Version: 6.1.4
Release: alt1

Summary: Framework for writing networked applications in C

Group: Networking/File transfer
License: GPLv2 with permissions for OpenSSL
Url: https://github.com/haiwen/ccnet

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/haiwen/ccnet/archive/v%version.tar.gz
Source: %name-%version.tar

# manually removed: python-module-mwlib 
# Automatically added by buildreq on Fri Sep 06 2013
# optimized out: glib2-devel gnu-config libgio-devel pkg-config python-base python-devel python-module-distribute python-module-zope python-modules
BuildRequires: libevent-devel libssl-devel libuuid-devel python-module-paste python-module-peak

BuildRequires: libsqlite3-devel

BuildRequires: libsearpc-devel >= 3.0.4

BuildRequires: vala >= 0.8

%if_enabled server
# server requirements
BuildRequires: libzdb-devel >= 2.10.2
%endif

Requires: lib%name = %version-%release

%description
Ccnet is a framework for writing networked applications in C.

%package -n lib%name
Summary: Library of framework for writing networked applications in C
Group: Networking/File transfer
Requires: libsearpc >= 3.0.4


%description -n lib%name
Ccnet is a framework for writing networked applications in C.

%package -n lib%name-devel
Summary: Development files for lib%name
Requires: lib%name = %version-%release
Group: Networking/File transfer

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use lib%name.

%package server
Summary: Ccnet server
Requires: lib%name = %version-%release
Requires: %name = %version-%release
Group: Networking/File transfer

%description server
Ccnet server part.
Ccnet is a framework for writing networked applications in C.

%package -n python-module-%name
Summary: Ccnet python module
Requires: lib%name = %version-%release
Group: Networking/File transfer

%description -n python-module-%name
Ccnet python module.

%prep
%setup
%__subst 's/(DESTDIR)//' libccnet.pc.in

%build
%autoreconf
%configure --disable-static \
           %subst_enable server

# smp build does not work
%make_build || %make

%install
%makeinstall_std

%files
%_bindir/ccnet
%_bindir/ccnet-init
#%_bindir/ccnet-tool

%files -n lib%name
%_libdir/*.so.*

%files -n python-module-%name
%python_sitelibdir/%name/

%if_enabled server
%files server
%_bindir/%name-server
%_bindir/%name-servtool
%endif

%files -n lib%name-devel
%doc HACKING
%_includedir/ccnet/
%_includedir/ccnet.h
%_libdir/*.so
%_pkgconfigdir/lib%name.pc

%changelog
* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 6.1.4-alt1
- new version 6.1.4 (with rpmrb script)

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 6.1.3-alt1
- new version 6.1.3 (with rpmrb script)

* Sun Dec 04 2016 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt1
- new version 6.0.0 (with rpmrb script)

* Wed Aug 03 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.4-alt1
- new version 5.1.4 (with rpmrb script)

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.3-alt1
- new version 5.1.3 (with rpmrb script)

* Tue May 17 2016 Vitaly Lipatov <lav@altlinux.ru> 5.1.1-alt1
- new version 5.1.1 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 5.0.5-alt1
- new version 5.0.5 (with rpmrb script)

* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 5.0.4-alt2
- real build 5.0.4

* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 5.0.4-alt1
- new version 5.0.4 (with rpmrb script)

* Fri Nov 21 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.11-alt1
- new version 3.1.11 (with rpmrb script)

* Thu Aug 28 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt1
- new version 3.1.5 (with rpmrb script)

* Mon Aug 25 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt7
- new build for ALT Linux Sisyphus (drop old source tree)
- rename repository and subpackages

* Mon Aug 25 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt6
- new version (3.1.4) with rpmgs script
- cleanup spec, drop extraneous files

* Sun Aug 24 2014 Konstantin Artyushkin <akv@altlinux.org> 1.4.2-alt6
- add ccnet server
- update to 1.4.2

* Fri Nov 08 2013 Denis Baranov <baraka@altlinux.ru> 1.3.6-alt1
- Update to 1.3.6

* Fri Sep 06 2013 Denis Baranov <baraka@altlinux.ru> 1.3.4-alt1
- initial build for ALT Linux Sisyphus
