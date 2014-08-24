%define oname seafile
Name: libseafile
Version: 3.1.0
Release: alt7
Summary: Seafile client libriary

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/libsearpc
Packager: Konstantin Artyushkin <akv@altlinux.org> 

#Source: http://seafile.com.cn/downloads/seafile-latest.tar.gz
Source: %name-%version.tar

Requires: python-module-mako
Requires: python-module-webpy
Requires: python-module-simplejson

# Automatically added by buildreq on Sun Nov 10 2013
# optimized out: glib2-devel gnu-config libevent-devel libgio-devel libsearpc-devel mariadb-client mariadb-common pkg-config python-base python-devel python-module-distribute python-module-zope python-modules
BuildRequires: libsqlite3-devel intltool libccnet-devel libssl-devel libuuid-devel python-module-mwlib python-module-paste python-module-peak
BuildRequires: zlib-devel libfuse-devel vala libjansson-devel libjson-glib-devel 
BuildRequires: libccnet-devel >= 1.4.2 libsearpc-devel >= 1.2.0

%description
Seafile is a full-fledged document collaboration platform

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Networking/File transfer

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
#Repocop found prefix=/usr/src/tmp/libseafile-buildroot/usr pc file 
%__subst s/\(DESTDIR\)// lib/libseafile.pc.in

%build
%autoreconf
%configure --disable-gui
#%make_build
%make

%install
%makeinstall_std
#find %buildroot -name '*.la' -exec rm -f {} ';'

%find_lang %name

%files -f %name.lang
%_libdir/*.so.*
%_libdir/*.a
%_libdir/python2.7/site-packages/seaserv/
%_bindir/*
#_desktopdir/*
#_iconsdir/hicolor/*/apps/*
#_pixmapsdir/*
%_man1dir/*.1.gz
#_datadir/%oname/*.png
%python_sitelibdir/%oname/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Sun Aug 24 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt7
- one more fix px file

* Sun Aug 24 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt6
- fix pc file

* Fri Aug 22 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt5
-  update buildrequires

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt4
- + libjansson-devel

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt3
 update to 3.1.0 

* Mon Aug 04 2014 Konstantin Artyushkin <akv@altlinux.org> 3.1.0-alt2
 update source 

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.4-alt2
- Fix some error in repository

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.4-alt1
- Initial build libseafile for ALTLinux

