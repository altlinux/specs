%define geany_ver 1.22
Name: geany-plugins
Version: 1.22
Release: alt1

Summary: Plugins for Geany

License: GPLv2
Group: Development/Tools
Url: http://plugins.geany.org/

Source: %name-%version.tar.bz2
Obsoletes: geanygdb

BuildRequires(pre): geany geany-devel intltool

Requires: geany-plugins-vc

# Automatically added by buildreq on Thu Jul 26 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgpg-error-devel libgtk+2-devel libjavascriptcoregtk2-devel libpango-devel libsoup-devel perl-XML-Parser pkg-config xorg-xproto-devel zlib-devel
BuildRequires: geany-devel intltool libGConf-devel libcheck-devel libenchant-devel libgpgme-devel libgtkspell-devel liblua5-devel libvte-devel libwebkitgtk2-devel libwnck-devel libxml2-devel vala

%description
This is Geany plugin collection

%package common
Group: Development/Tools
Requires: geany = %geany_ver
Summary: localization for geany-plugins

%description common
Common files of geany-plugins, including localization

%package vc
Group: Development/Tools
Requires: geany-plugins-common = %version-%release
Summary: Geany VC integration plugin

%description vc
Various VCS integration (Git, SVN, ...) for Geany

%prep
%setup

%build
%configure --enable-geanygdb
%make_build

%install
%makeinstall_std --silent --no-print-directory
%find_lang %name

%files
%doc %_defaultdocdir/%name
%_libdir/geany/*
%_libdir/geany-plugins/*
%_datadir/geany-plugins/*
%dir %_libexecdir/geany-plugins
%_libexecdir/geany-plugins/*
%_iconsdir/hicolor/*/apps/gproject*
%exclude %_libdir/geany/geanyvc*
%exclude %_libdir/geany/*.la
%exclude %_libdir/geany-plugins/*/*.la

%files common -f %name.lang
%files vc
%_libdir/geany/geanyvc*
%exclude %_libdir/geany/*.la

%changelog
* Thu Jul 26 2012 Fr. Br. George <george@altlinux.ru> 1.22-alt1
- Autobuild version bump to 1.22
- Update BuildRequires for more plugins to build

* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 0.21.1-alt2
- Remove release dependency

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 0.21.1-alt1
- Autobuild version bump to 0.21.1

* Fri Jan 14 2011 Fr. Br. George <george@altlinux.ru> 0.20-alt1
- Autobuild version bump to 0.20
- Add unpackaged files

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt4
- trying to fix build

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt3
- split by plugins

* Sun Jan 09 2011 Mykola Grechukh <gns@altlinux.ru> 0.19-alt2
- first build for ALT Linux
