Name: gsql
Version: 0.2.2
Release: alt1.1

Summary: Integrated database development tool for GNOME

License: GPL
Group: Databases
Packager: Boris Savelev <boris@altlinux.org>

Source: http://gsql.googlecode.com/files/%name-%version.tar
Url: http://gsql.org/

# Automatically added by buildreq on Tue Jul 26 2011
# optimized out: GConf ORBit2-devel fontconfig fontconfig-devel glib2-devel gnome-vfs gnome-vfs-devel libGConf-devel libICE-devel libSM-devel libX11-devel libart_lgpl-devel libatk-devel libavahi-glib libbonobo-devel libbonoboui-devel libcairo-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgnome-devel libgnome-keyring libgnomecanvas-devel libgpg-error libgtk+2-devel libpango-devel libpopt-devel pkg-config
BuildRequires: glibc-devel-static libglade-devel libgnomeui-devel libgtksourceview-devel libmysqlclient-devel libnotify-devel libssh-devel libvte-devel

BuildRequires: gtk-doc librarian rpm-build-gnome rpm-build-compat

%description
Architecturely GSQL is designed so that the database
interfaces are arranged into modules linked to the
platform by engine API. It allows to implement new
engines independently. GSQL provides developers with a rich API.
To extend the functions of GSQL engines, we suggest loadable plugins API.

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
Library for %name

%package -n lib%name-devel
Summary: lib%name development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for lib%name

%prep
%setup
%__subst "s|message, NULL, NULL|message, NULL|g" libgsql/notify.c
%build
%undefine __libtoolize
%configure --disable-static

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std
install -D -m644 %name.desktop %buildroot%_desktopdir/%name.desktop

%find_lang %name
rm -f %buildroot/usr/share/doc/gsql/AUTHORS

%files -f %name.lang
%doc INSTALL AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%gconf_schemasdir/%{name}*
%_pixmapsdir/%name
%_man1dir/%name.*
%dir %_libdir/%name/engines
%dir %_libdir/%name/plugins
%_libdir/%name/engines/*
%_libdir/%name/plugins/*
%_iconsdir/hicolor/scalable/apps/gsql.svg
%_liconsdir/%name.png
# %_gtkdocdir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/lib%name
%_pkgconfigdir/*.pc
# %gnome_helpdir/%name
# %_omfdir/%name

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.1
- Remove bad RPATH

* Tue Jul 26 2011 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- new version 0.2.2 (with rpmrb script)

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Fri Jan 30 2009 Boris Savelev <boris@altlinux.org> 0.2.1-alt1
- new version (0.2.1)

* Sun Jan 11 2009 Boris Savelev <boris@altlinux.org> 0.2.0-alt2
- fix buildreq

* Tue Dec 09 2008 Boris Savelev <boris@altlinux.org> 0.2.0-alt1
- initial build for Sisyphus

