
Name: maliit-framework
Version: 2.3.0
Release: alt1
%define sover 2
%define libmaliit libmaliit%sover
%define libmaliit_glib libmaliit-glib%sover
%define xinputconfdir %_sysconfdir/X11/xinit/xinput.d

Group: System/Libraries
Summary: Maliit Input Method Framework
Url: http://www.maliit.org
License: LGPL-2.1-only
%K5init no_altplace

Source0: %name-%version.tar
Source1: maliit.conf

# Automatically added by buildreq on Fri Jun 04 2021 (-bi)
# optimized out: cmake-modules debugedit elfutils fontconfig gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libatk-devel libcairo-devel libcairo-gobject-devel libctf-nobfd0 libgdk-pixbuf-devel libgio-devel libglvnd-devel libgpg-error libharfbuzz-devel libpango-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-waylandclient libsasl2-3 libssl-devel libstdc++-devel libudev-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-server-devel libxcb-devel libxkbcommon-devel pkg-config python-modules python2-base python3 python3-base python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-python3 sh4 wayland-devel xz
#BuildRequires: cmake doxygen fonts-ttf-dejavu fonts-ttf-gnu-freefont-mono fonts-ttf-google-droid-sans graphviz libXfixes-devel libgtk+3-devel libwayland-cursor-devel libwayland-egl-devel python-modules-encodings python3-dev python3-module-mpl_toolkits qt5-base-devel-static qt5-svg-devel qt5-wayland-devel qt5-webengine-devel wayland-protocols
BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake doxygen graphviz libgtk+3-devel
BuildRequires: pkgconfig(xkbcommon) pkgconfig(xfixes)
BuildRequires: wayland-protocols libwayland-cursor-devel libwayland-egl-devel
BuildRequires: qt5-base-devel-static qt5-svg-devel qt5-wayland-devel

%description
Core server and libraries for the Maliit Input Methods Framework

%package devel
Summary: Maliit Input Method Framework Development Package
Group: System/Libraries
Provides: libmaliit-devel = %EVR
Obsoletes: libmaliit-devel < %EVR
Provides: libmaliit-glib-devel = %EVR
Obsoletes: libmaliit-glib-devel < %EVR
%description devel
This package contains the files necessary to develop
input method plugins for Maliit, and applications using the libmaliit
extension library.

%package -n %libmaliit
Summary: Maliit Framework Input Method library
Group: System/Libraries
%description -n %libmaliit
Maliit toolkit support extension library for Qt applications

%package -n %libmaliit_glib
Summary: Maliit Framework Input Method library
Group: System/Libraries
%description -n %libmaliit_glib
Maliit toolkit support extension library for Gtk+ applications

%package -n libmaliit-glib-gir
Summary: GObject introspection data for the Maliit Framework
Group: System/Libraries
Requires: %libmaliit_glib
%description -n libmaliit-glib-gir
GObject introspection data for the Maliit Framework Input Method library

%package doc
Summary: Maliit Framework Documentation
Group: Development/Other
Requires: %name = %version-%release
BuildArch: noarch
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

%package -n maliit-inputcontext-qt5
Summary: Maliit Input Context Plugin for Qt
Group: Accessibility
Requires: %name = %version-%release
%description -n maliit-inputcontext-qt5
%name input context plugin for Qt toolkit support

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

# avoid depending on python 2
#sed -i '1s=^#!/usr/bin/env python=#!/usr/bin/python3=' examples/apps/gtk3-python/maliit-exampleapp-gtk3-python.py

%build
export PATH=%_qt5_bindir:$PATH
%K5build \
    -DMALIIT_SERVER_ARGUMENTS="" \
    -Denable-dbus-activation:BOOL=ON \
    -Denable-qt5-inputcontext:BOOL=ON \
    -Denable-wayland-gtk=ON \
    -Denable-wayland=ON \
    -Denable-xcb=ON \
    -Denable-glib=ON \
    -Denable-tests:BOOL=OFF \
    -Denable-examples:BOOL=OFF \
    #
#    CONFIG+=disable-gtk-cache-update \

%install
#K5install
%make -C BUILD DESTDIR=%buildroot install

# install xinput config file
mkdir -p %buildroot/%xinputconfdir
install -pm 644 -D %SOURCE1 %buildroot/%xinputconfdir/

mkdir -p %buildroot/%_libdir/maliit/plugins/factories

# cleanup
rm -rf %buildroot/%_docdir/maliit-framework-doc


%post -n maliit-inputcontext-gtk2
%_bindir/gtk-query-immodules-2.0 > /etc/gtk-2.0/gtk.immodules 2>>/dev/null ||:
%post -n maliit-inputcontext-gtk3
%_bindir/gtk-query-immodules-3.0 --update-cache >/dev/null 2>&1 ||:

%files
%doc README* LICENSE* NEWS
%dir %_libdir/maliit/
%dir %_libdir/maliit/plugins*/
%dir %_libdir/maliit/plugins*/factories
%_bindir/maliit-server
%_qt5_plugindir/platforminputcontexts/libmaliitplatforminputcontextplugin.so
%_qt5_plugindir/wayland-shell-integration/libinputpanel-shell.so
#%_libdir/gtk-3.0/3.0.0/immodules/libim-wayland.so
#%config %xinputconfdir/*
%_datadir/dbus-1/services/org.maliit.server.service

#%files settings
#%_bindir/maliit-exampleapp-settings-python3.py

#%files examples
#%_bindir/maliit-example*
#%exclude %_bindir/maliit-exampleapp-settings-python3.py

%files devel
%_includedir/maliit-2/
%_libdir/libmaliit-*.so
%_libdir/pkgconfig/maliit-*.pc
%_qt5_archdatadir/mkspecs/features/maliit-*.prf
%_libdir/cmake/MaliitGLib/
%_libdir/cmake/MaliitPlugins/

%files -n %libmaliit
%_libdir/libmaliit-plugins.so.%sover
%_libdir/libmaliit-plugins.so.*

%files -n %libmaliit_glib
%_libdir/libmaliit-glib.so.%sover
%_libdir/libmaliit-glib.so.*

#%files -n libmaliit-glib-gir
#%_typelibdir/Maliit-*.typelib

%files doc
%doc BUILD/doc/html

#%files sdk
#%_bindir/maliit-sdk
#%_defaultdocdir/maliit-framework-%version/maliit-sdk

#%files tests
#%_libdir/maliit-framework-tests/

#%files -n maliit-inputcontext-qt5
#%_qt5_plugindir/inputmethods/*.so

#%files -n maliit-inputcontext-gtk2
#%_libdir/gtk-2.0/2.10.0/immodules/libim-maliit.so*

#%files -n maliit-inputcontext-gtk3
#%_libdir/gtk-3.0/3.0.0/immodules/libim-maliit.so*

%changelog
* Tue Jan 24 2023 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt1
- new version

* Wed Jan 12 2022 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version

* Thu Nov 18 2021 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt3
- don't package xinput config

* Wed Jun 30 2021 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt2
- don't add custom argumetrs to maliit-server startup

* Fri Jun 04 2021 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- new version

* Tue Feb 25 2020 Sergey V Turchin <zerg@altlinux.org> 0.94.2-alt5
- fix to build with new compilers
- build without python2

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.94.2-alt4.2.qa1
- NMU: applied repocop patch

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.94.2-alt4.2
- (NMU) rebuild with python3.6

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
