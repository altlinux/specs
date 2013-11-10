%define oname seafile
Name: libseafile
Version: 2.0.4
Release: alt2
Summary: Seafile client libriary

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/libsearpc
Packager: Denis Baranov <baraka@altlinux.ru>

#Source: http://seafile.com.cn/downloads/seafile-latest.tar.gz
Source: %name-%version.tar

Requires: python-module-mako
Requires: python-module-webpy
Requires: python-module-simplejson

# Automatically added by buildreq on Sun Nov 10 2013
# optimized out: glib2-devel gnu-config libevent-devel libgio-devel libsearpc-devel mariadb-client mariadb-common pkg-config python-base python-devel python-module-distribute python-module-zope python-modules
BuildRequires: libsqlite3-devel intltool libccnet-devel libssl-devel libuuid-devel python-module-mwlib python-module-paste python-module-peak

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
#%__subst /\(DESTDIR\)/d libseafile.pc.in

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
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*
%_man1dir/*.1.gz
%_datadir/%oname/*.png
%python_sitelibdir/%oname/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.4-alt2
- Fix some error in repository

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.4-alt1
- Initial build libseafile for ALTLinux

