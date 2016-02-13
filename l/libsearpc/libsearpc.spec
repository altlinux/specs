Name: libsearpc
Version: 3.0.7
Release: alt2

Summary: RPC library for Seafile

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/libsearpc

Packager: Konstantin Artyushkin <akv@altlinux.org>

# Source-url: https://github.com/haiwen/libsearpc/archive/v%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Sun Aug 24 2014
# optimized out: libcloog-isl4 pkg-config python-base python-devel python-module-distribute python-module-zope python-modules python3-base
BuildRequires: glib2-devel glibc-devel libjansson-devel
# python-module-cmd2 python-module-mwlib python-module-protobuf

BuildRequires: libgio-devel

%description
Searpc is a simple C language RPC framework based on GObject system.
Searpc handles the serialization/deserialization part of RPC, the transport part is left to users.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Networking/File transfer

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%__subst 's/(DESTDIR)//' libsearpc.pc.in

%build
%autoreconf
%configure --disable-static --disable-compile-demo --enable-server-pkg
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README.markdown
%_libdir/*.so.*
%python_sitelibdir/pysearpc/

%files devel
%_bindir/searpc-codegen.py
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 3.0.7-alt2
- move searpc-codegen.py to devel subpackage
- fix build requires

* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 3.0.7-alt1
- new version 3.0.7 (with rpmrb script)

* Sun Aug 24 2014 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt1
- new version (3.0.4) with rpmgs script
- cleanup spec, drop extraneous files

* Sun Aug 03 2014 Konstantin Artyushkin <akv@altlinux.org> 1.2.0-alt3
- plus libjansson

* Sun Aug 03 2014 Konstantin Artyushkin <akv@altlinux.org> 1.2.0-alt2
- update to 1.2.2

* Fri Sep 06 2013 Denis Baranov <baraka@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

* Tue Jun 18 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-2
- updated for seafile 1.7.0

* Thu May 30 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-1
- added description from github
- moved to 1.1.0 from seafile 1.6.1

* Mon Jan 28 2013 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-1
- Initial package
