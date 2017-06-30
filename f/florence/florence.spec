Name: florence
Version: 0.6.0
Release: alt2

Summary: Extensible scalable virtual keyboard for GNOME
Url: http://florence.sourceforge.net/  

Source: %name-%version.tar
License: GPLv2+

Group: System/X11 

BuildRequires: glib2-devel libgtk+3-devel gnome-doc-utils
BuildRequires: libGConf-devel gettext-devel intltool
BuildRequires: librsvg-devel libnotify-devel libXtst-devel libat-spi2-core-devel
BuildRequires: gstreamer-devel libXcomposite-devel
BuildPreReq: libxml2-devel
BuildPreReq: trang

%description
Florence is primarily intended to be used with the GNOME desktop,
although it can be used on any desktop environment.


%prep
%setup

%build
./autogen.sh
%configure \
	--without-panelapplet \
	-with-at-spi

%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_datadir/gnome/help/florence/
%_datadir/glib-2.0/schemas/org.florence.gschema.xml
%_datadir/applications/florence.desktop
%_datadir/omf/florence/
%_datadir/pixmaps/florence.svg
%_man1dir/*.1.*

%exclude %_man1dir/florence_applet.1.*

%changelog
* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt2
- Updated build spec to support any man page compression

* Fri Mar 29 2013 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Drop obsoleted patch.
- Updated to 0.6.0.

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.1
- Fixed build

* Wed Dec 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5.1-alt1
- first build for Sisyphus

