

%define libver 1.0
%define libsover 0
Name: maliit-framework
Version: 0.94.2
Release: alt4.1
%define libmaliit libmaliit%libver-%libsover
%define libmaliit_glib libmaliit-glib%libver-%libsover
%define xinputconfdir %_sysconfdir/X11/xinit/xinput.d

Group: System/Libraries
Summary: Maliit Input Method Framework
Url: http://www.maliit.org
License: LGPLv2

Source0: %name-%version.tar
Source1: maliit.conf
Patch1: maliit-framework-focusworkaround.diff

# Automatically added by buildreq on Thu Oct 18 2012 (-bi)
# optimized out: at-spi2-atk docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glib-networking glib2-devel gobject-introspection libX11-devel libXext-devel libXfixes-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libpango-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-script libqt4-sql libqt4-svg libqt4-test libqt4-xml libqt4-xmlpatterns libstdc++-devel libwayland-client libwayland-server pkg-config python-base python-module-distribute python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-xml rpm-build-gir ruby xml-common xml-utils xorg-compositeproto-devel xorg-damageproto-devel xorg-fixesproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xproto-devel xsltproc
#BuildRequires: cups-filters doxygen fonts-type1-urw gcc-c++ gdb glibc-devel-static gobject-introspection-devel graphviz gtk-doc gvfs libGConf libXcomposite-devel libXdamage-devel libdbus-glib-devel libgtk+2-devel libgtk+3-devel libudev-devel phonon-devel python3 rpm-build-ruby time xdg-utils
BuildRequires: gcc-c++
BuildRequires: doxygen glibc-devel graphviz gtk-doc
BuildRequires: libXcomposite-devel libXdamage-devel libudev-devel
BuildRequires: pkgconfig(gobject-introspection-1.0) pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtDeclarative)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: rpm-build-python python-devel
BuildRequires: rpm-build-python3 python3-devel

%description
Core server and libraries for the Maliit Input Methods Framework

%package devel
Summary: Maliit Input Method Framework Development Package
Group: System/Libraries
#Requires: %name = %version-%release
Requires: libmaliit-glib-gir
%description devel
This package contains the files necessary to develop
input method plugins for Maliit, and applications using the libmaliit
extension library.

%package -n %libmaliit
Summary: Maliit Framework Input Method library
Group: System/Libraries
%description -n %libmaliit
Maliit toolkit support extension library for Qt applications

%package -n libmaliit-devel
Summary: Maliit Framework Input Method library development files
Group: System/Libraries
%description -n libmaliit-devel
Development files for the Maliit toolkit support extension library
for Qt applications

%package -n %libmaliit_glib
Summary: Maliit Framework Input Method library
Group: System/Libraries
%description -n %libmaliit_glib
Maliit toolkit support extension library for Gtk+ applications

%package -n libmaliit-glib-devel
Summary: Maliit Framework Input Method library development files
Group: System/Libraries
%description -n libmaliit-glib-devel
Development files for the Maliit toolkit support extension library
for Gtk+ applications

%package -n libmaliit-glib-gir
Summary: GObject introspection data for the Maliit Framework
Group: System/Libraries
Requires: %libmaliit_glib = %EVR
Conflicts: libmaliit-glib-devel <= 0.94.0-alt1
%description -n libmaliit-glib-gir
GObject introspection data for the Maliit Framework Input Method library

%package doc
Summary: Maliit Framework Documentation
Group: Development/Other
Requires: %name = %version-%release
%description doc
Documentation for the Maliit Input Method Framework

%package sdk
Summary: Maliit Framework SDK
Group: Development/Other
Requires: %name = %version-%release
Requires: %name-doc
%description sdk
SDK environment for Maliit

%package tests
Summary: Maliit Framework Input Method Tests Package
Group: Development/Other
Requires: %name = %version-%release
%description tests
This package contains the files necessary to test
the Maliit input method framework

%package examples
Summary: Maliit Framework Input Method Examples
Group: Development/Other
Requires: %name = %version-%release
%description examples
This package contains examples applications for
the Maliit input method framework

%package settings
Summary: Maliit Framework settings utitlity
Group: System/Configuration/Other
Requires: libmaliit-glib-gir
Conflicts: maliit-framework-examples <= 0.94.0-alt1
%description settings
This package contains settings utitlity for
the Maliit input method framework

%package -n maliit-inputcontext-qt4
Summary: Maliit Input Context Plugin for Qt 4
Group: Accessibility
Requires: %name = %version-%release
%description -n maliit-inputcontext-qt4
%name input context plugin for Qt 4 toolkit support

%package -n maliit-inputcontext-gtk2
Summary: Maliit Input Context Plugin for Gtk+2
Group: Accessibility
Requires: %name = %version-%release
%description -n maliit-inputcontext-gtk2
%name input context plugin for basic Gtk+ version 2 toolkit support

%package -n maliit-inputcontext-gtk3
Summary: Maliit Input Context Plugin for Gtk+3
Group: Accessibility
Requires: %name = %version-%release
%description -n maliit-inputcontext-gtk3
%name input context plugin for basic Gtk+ version 3 toolkit support

%prep
%setup -n %name-%version
%patch1 -p1

%build
%qmake_qt4 -r \
    MALIIT_VERSION=%version \
    MALIIT_SERVER_ARGUMENTS="-software -bypass-wm-hint" \
    PREFIX=%prefix \
    BINDIR=%_bindir \
    LIBDIR=%_libdir \
    INCLUDEDIR=%_includedir \
    CONFIG+=notests \
    CONFIG+=enable-dbus-activation \
    CONFIG+=disable-gtk-cache-update
#    MALIIT_ENABLE_MULTITOUCH=false \
#    CONFIG+=enable-qdbus \
#    CONFIG+=disable-background-translucency \

%make_build

%install
%make install INSTALL="install -p" INSTALL_ROOT=%buildroot

# install xinput config file
mkdir -p %buildroot/%xinputconfdir
install -pm 644 -D %SOURCE1 %buildroot/%xinputconfdir/

# workaround against tests linking check
#    %buildroot/%_qt4dir/plugins/inputmethods/lib*.so \
#    %buildroot/%_libdir/maliit-framework-tests/plugins/lib*.so \
#for l in \
#    %buildroot/%_libdir/maliit/plugins*/factories/lib*.so
#do
#    libname=`basename $l`
#    ln -s \
#	`relative $l %buildroot/%_libdir/$libname` \
#	%buildroot/%_libdir/$libname
#done

# install docs
mv %buildroot/%_defaultdocdir/maliit-framework %buildroot/%_defaultdocdir/maliit-framework-%version
install -m 0644 README LICENSE.LGPL NEWS %buildroot/%_defaultdocdir/maliit-framework-%version/

%post -n maliit-inputcontext-gtk2
%_bindir/gtk-query-immodules-2.0 > /etc/gtk-2.0/gtk.immodules 2>>/dev/null ||:
%post -n maliit-inputcontext-gtk3
%_bindir/gtk-query-immodules-3.0 --update-cache >/dev/null 2>&1 ||:

%files
%dir %_defaultdocdir/maliit-framework-%version
%doc %_defaultdocdir/maliit-framework-%version/README
%doc %_defaultdocdir/maliit-framework-%version/LICENSE.LGPL
%doc %_defaultdocdir/maliit-framework-%version/NEWS
%dir %_libdir/maliit/
%dir %_libdir/maliit/plugins*/
%dir %_libdir/maliit/plugins*/factories
%_bindir/maliit-server
%_libdir/maliit/plugins*/factories/libmaliit-plugins-quick-factory*.so
%config %xinputconfdir/*
%_datadir/dbus-1/services/org.maliit.server.service

%files settings
%_bindir/maliit-exampleapp-settings-python3.py

%files examples
%_bindir/maliit-example*
%exclude %_bindir/maliit-exampleapp-settings-python3.py

%files devel
%dir %_includedir/maliit/
%dir %_includedir/maliit/framework/
%dir %_includedir/maliit/framework/maliit/
%_includedir/maliit/connection/
%_includedir/maliit/framework/maliit/*.h
%_includedir/maliit/plugins/
%_includedir/maliit/plugins-quick/
%_includedir/maliit/server/
%_libdir/libmaliit-connection.so
%_libdir/libmaliit-plugins.so
%_libdir/libmaliit-plugins-quick.so
#%_libdir/libmaliit-plugins-quick-factory.so
%_libdir/pkgconfig/maliit-connection.pc
%_libdir/pkgconfig/maliit-framework.pc
%_libdir/pkgconfig/maliit-plugins.pc
%_libdir/pkgconfig/maliit-plugins-quick.pc
%_libdir/pkgconfig/maliit-server.pc
%_datadir/qt4/mkspecs/features/maliit-*.prf

%files -n %libmaliit
%_libdir/libmaliit.so.*
%_libdir/libmaliit-connection.so.*
%_libdir/libmaliit-plugins.so.*
%_libdir/libmaliit-plugins-quick.so.*
%_libdir/libmaliit-settings.so.*

%files -n libmaliit-devel
%_libdir/libmaliit.so
%_libdir/libmaliit-settings.so
%_includedir/maliit/maliit/
%_libdir/pkgconfig/maliit.pc
%_libdir/pkgconfig/maliit-settings.pc

%files -n %libmaliit_glib
%_libdir/libmaliit-glib.so.*

%files -n libmaliit-glib-gir
%_typelibdir/Maliit-*.typelib

%files -n libmaliit-glib-devel
%_girdir/Maliit-*.gir
%_libdir/libmaliit-glib.so
%_includedir/maliit/maliit-glib/
%_libdir/pkgconfig/maliit-glib.pc

%files doc
%doc %_defaultdocdir/maliit-framework-%version/html

#%files sdk
#%_bindir/maliit-sdk
#%_defaultdocdir/maliit-framework-%version/maliit-sdk

#%files tests
#%_libdir/maliit-framework-tests/

%files -n maliit-inputcontext-qt4
%_qt4dir/plugins/inputmethods/*.so

%files -n maliit-inputcontext-gtk2
%_libdir/gtk-2.0/2.10.0/immodules/libim-maliit.so*

%files -n maliit-inputcontext-gtk3
%_libdir/gtk-3.0/3.0.0/immodules/libim-maliit.so*

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.94.2-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Sep 11 2013 Sergey V Turchin <zerg@altlinux.org> 0.94.2-alt4
- add focus workaround from Plasma Active developers

* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 0.94.2-alt3
- rebuilt with new rpm-build-python3

* Mon Apr 01 2013 Sergey V Turchin <zerg@altlinux.org> 0.94.2-alt2
- rebuilt with new glib

* Fri Mar 29 2013 Sergey V Turchin <zerg@altlinux.org> 0.94.2-alt1
- new version

* Thu Jan 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.94.0-alt1
- new version

* Fri Oct 19 2012 Sergey V Turchin <zerg@altlinux.org> 0.92.5.1-alt1
- initial build
