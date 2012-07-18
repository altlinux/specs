Name: florence
Version: 0.5.1
Release: alt1.1

Summary: Extensible scalable virtual keyboard for GNOME
Url: http://florence.sourceforge.net/  

Source: %name-%version.tar
Patch: florence-0.5.1-alt-glib2.patch
License: GPLv2+

Group: System/X11 

BuildRequires: glib2-devel libgtk+2-devel gnome-doc-utils
BuildRequires: libGConf-devel gettext-devel intltool
BuildRequires: librsvg-devel libnotify-devel libXtst-devel libat-spi2-core-devel
BuildPreReq: libxml2-devel

%description
Florence is primarily intended to be used with the GNOME desktop,
although it can be used on any desktop environment.


%prep
%setup
%patch -p2

%build
./autogen.sh
%configure --without-panelapplet

%make_build

%install
%makeinstall
%find_lang %name

%post
/usr/sbin/gconf_install_schema florence

%preun
if [ $1 = 0 ]; then
/usr/sbin/gconf_uninstall_schema florence
fi

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_datadir/gnome/help/florence/
/etc/gconf/schemas/*
%_datadir/applications/florence.desktop
%_datadir/omf/florence/
%_datadir/pixmaps/florence.svg

%changelog
* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.1
- Fixed build

* Wed Dec 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5.1-alt1
- first build for Sisyphus

