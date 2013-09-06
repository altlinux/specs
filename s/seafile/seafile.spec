Name: seafile
Version: 1.7.0
Release: alt3
Summary: Seafile client

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/libsearpc
Packager: Denis Baranov <baraka@altlinux.ru>

#Source: http://seafile.com.cn/downloads/seafile-latest.tar.gz
Source: %name-%version.tar

Requires: python-module-mako
Requires: python-module-webpy
Requires: python-module-simplejson

# Automatically added by buildreq on Fri Sep 06 2013
# optimized out: ccnet fontconfig fontconfig-devel glib2-devel gnu-config libatk-devel libcairo-devel libevent-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libsearpc-devel libwayland-client libwayland-server pkg-config python-base python-devel python-module-distribute python-module-zope python-modules
BuildRequires: libccnet-devel glibc-devel-static intltool libgtk+2-devel libnotify-devel libsqlite3-devel libssl-devel libuuid-devel python-module-mwlib python-module-paste python-module-peak

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
%configure --disable-static --enable-client --disable-server
#%make_build
%make

%install
%makeinstall_std
#find %buildroot -name '*.la' -exec rm -f {} ';'

%find_lang %name

%files -f %name.lang
%_libdir/*.so.*
%_libdir/python2.7/site-packages/seaserv/
%_bindir/*
%python_sitelibdir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*
%_datadir/%name/
%_man1dir/*.1.gz

%files devel
%_includedir/*
%_libdir/*.so
#%_pkgconfigdir/lib%name.pc

%changelog
* Fri Sep 06 2013 Denis Baranov <baraka@altlinux.ru> 1.7.0-alt3
- Fix name for requires

* Fri Sep 06 2013 Denis Baranov <baraka@altlinux.ru> 1.7.0-alt2
- Rename require package

* Fri Sep 06 2013 Denis Baranov <baraka@altlinux.ru> 1.7.0-alt1
- initial build for ALT Linux Sisyphus

* Tue Jun 18 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.7.0-1
- updated to 1.7.0
* Thu May 30 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-1
- added description from github
- moved to seafile 1.6.1
* Mon Jan 28 2013 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-1
- Initial package
