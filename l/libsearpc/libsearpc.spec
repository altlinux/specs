Name: libsearpc
Version: 1.2.0
Release: alt3

Summary: RPC library for Seafile

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/libsearpc

Packager: Konstantin Artyushkin <akv@altlinux.org> 

# Source-url: https://seafile.googlecode.com/files/seafile-latest.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Fri Sep 06 2013
# optimized out: glib2-devel gnu-config pkg-config python-base python-devel python-module-distribute python-module-zope python-modules
BuildRequires: libgio-devel python-module-mwlib python-module-paste python-module-peak
BuildRequires: libjansson-devel

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
%__subst /\(DESTDIR\)/d libsearpc.pc.in

%build
%autoreconf
%configure --disable-static --disable-compile-demo
%make_build

%install
%makeinstall_std
#find %buildroot -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS README.markdown
%_libdir/*.so.*
%_bindir/searpc-codegen.py
%python_sitelibdir/pysearpc/

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Sun Aug 03 2014 Konstantin Artyushkin <akv@altlinux.org> 1.2.0-alt3
- plus libjansson

* Sun Aug 03 2014 Konstantin Artyushkin <akv@altlinux.org> 1.2.0-alt2
 update to 1.2.2

* Fri Sep 06 2013 Denis Baranov <baraka@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

* Tue Jun 18 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-2
- updated for seafile 1.7.0
* Thu May 30 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-1
- added description from github
- moved to 1.1.0 from seafile 1.6.1
* Mon Jan 28 2013 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-1
- Initial package
