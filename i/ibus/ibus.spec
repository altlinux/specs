%define snapshot 20121006
%define api_ver 1.0

%def_enable python
%def_enable dconf
%def_disable gconf
%def_enable xkb

Name: ibus
Version: 1.4.99.%snapshot
Release: alt1

Summary: Intelligent Input Bus for Linux OS
License: LGPLv2+
Group: System/Libraries
Url: http://code.google.com/p/%name/

Source: http://%name.googlecode.com/files/%name-%version.tar.gz
Source1: xinput-ibus
# fedora's patches
Patch1: ibus-810211-no-switch-by-no-trigger.patch
Patch2: ibus-541492-xkb.patch
Patch3: ibus-530711-preload-sys.patch
Patch4: ibus-xx-setup-frequent-lang.patch

# Workaround to disable preedit on gnome-shell until bug 658420 is fixed.
# https://bugzilla.gnome.org/show_bug.cgi?id=658420
Patch92: ibus-xx-g-s-disable-preedit.patch
# Hide nonused properties in f17.
Patch94: ibus-xx-no-use.diff
# Workaround since f18 vala is old.
Patch95: ibus-xx-f18-build.patch

%define gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)
%define gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)

Requires: iso-codes
Requires: lib%name = %version-%release
%{?_enable_gconf:Requires(post,preun):GConf}
%{?_enable_dconf:Requires: dconf}

BuildRequires: vala-tools >= 0.18
BuildRequires: python-modules-compiler
BuildRequires: rpm-build-python
BuildPreReq: libgtk+2-devel
BuildPreReq: libgtk+3-devel
BuildRequires: libdbus-glib-devel
BuildRequires: python-module-dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk-doc
BuildRequires: python-module-pygobject-devel
BuildRequires: intltool
BuildRequires: iso-codes-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gnome-icon-theme-symbolic
BuildRequires: libXi-devel
%{?_enable_python:BuildRequires: rpm-build-python python-module-pygobject-devel}
%{?_enable_gconf:BuildRequires: libGConf-devel}
# required if autoreconf used
BuildRequires: libGConf-devel
%{?_enable_dconf:BuildRequires: libdconf-devel /proc dbus-tools-gui dconf}
%{?_enable_xkb:BuildRequires: libxkbfile-devel libgnomekbd-devel libgnomekbd-gir-devel}

%define _xinputconf %_sysconfdir/X11/xinit/xinput.d/ibus.conf

%description
IBus means Intelligent Input Bus. It is an input framework for Linux OS.

%package -n lib%name
Summary: IBus libraries
Group: System/Libraries
Requires: dbus

%description -n lib%name
This package contains the libraries for IBus

%package -n lib%name-gir
Summary: GObject introspection data for the IBus library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
This package contains typelib file for the IBus library.

%package gtk2
Summary: IBus im module for gtk2
Group: System/Libraries
PreReq: libgtk+2
Requires: lib%name = %version-%release

%description gtk2
This package contains IBus im module for gtk2.

%package gtk3
Summary: IBus im module for gtk3
Group: System/Libraries
PreReq: libgtk+3
Requires: lib%name = %version-%release

%description gtk3
This package contains IBus im module for gtk3.

%package -n lib%name-devel
Summary: Development tools for ibus
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files for IBus library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for IBus
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
This package contains gir files for IBus library.

%package -n lib%name-devel-docs
Summary: Developer documents for IBus
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release
Requires: gtk-doc

%description -n lib%name-devel-docs
This package contains developer documentation for IBus.

%if_enabled python
%package -n python-module-ibus
Summary: IBus im module for python
Group: Development/Python
BuildArch: noarch

%description -n python-module-ibus
This package contains IBus im module for python.
%endif

%prep
%setup
#%%patch92 -p1 -b .g-s-preedit
#cp client/gtk2/ibusimcontext.c client/gtk3/ibusimcontext.c ||
%patch1 -p1 -b .noswitch

%if_enabled xkb
%patch2 -p1 -b .xkb
rm -f bindings/vala/ibus-%api_ver.vapi
rm -f data/dconf/00-upstream-settings
%endif
%patch3 -p1
%patch4 -p1
%patch94 -p1 -b .no-used
%patch95 -p1 -b .f18

%build
%autoreconf
%configure \
    --disable-static \
    --enable-gtk2 \
    --enable-gtk3 \
    --enable-xim \
    --disable-gtk-doc \
    %{subst_enable dconf} \
    %{?_enable_python:--enable-python-library} \
    %{?_enable_dconf:--disable-schemas-compile} \
    %{subst_enable gconf} \
    %{subst_enable xkb} \
    %{?_enable_xkb:--enable-libgnomekbd} \
    %{?_enable_gconf:--disable-schemas-install} \
    --enable-introspection

%make_build

%install
%make DESTDIR=%buildroot install

# install xinput config file
install -pm 644 -D %SOURCE1 %buildroot%_xinputconf

# install .desktop files
mkdir -p %buildroot%_sysconfdir/xdg/autostart/
install -m 644 bus/ibus.desktop %buildroot%_sysconfdir/xdg/autostart/

%find_lang %{name}10

%check
#%%make check

%if_enabled gconf
%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi
%endif

%post gtk2
%_bindir/gtk-query-immodules-2.0 > %_sysconfdir/gtk-2.0/gtk.immodules

%postun gtk2
%_bindir/gtk-query-immodules-2.0 > %_sysconfdir/gtk-2.0/gtk.immodules

%post gtk3
%_bindir/gtk-query-immodules-3.0 --update-cache || :

%postun gtk3
%_bindir/gtk-query-immodules-3.0 --update-cache || :

%files -f %{name}10.lang
%dir %_datadir/ibus/
%_bindir/%name
%_bindir/ibus-daemon
%_bindir/ibus-setup
%_datadir/ibus/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_libexecdir/ibus-ui-gtk3
%_libexecdir/ibus-x11
%{?_enable_xkb:%_libexecdir/ibus-xkb}
%_libexecdir/%name-engine-simple
%_sysconfdir/xdg/autostart/ibus.desktop

%if_enabled gconf
%_libexecdir/ibus-gconf
%_sysconfdir/gconf/schemas/ibus.schemas
%endif

%if_enabled dconf
%dir %_sysconfdir/dconf/db/%name.d
%_sysconfdir/dconf/db/%name.d/00-upstream-settings
%_sysconfdir/dconf/profile/%name
%_libexecdir/%name-dconf
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.freedesktop.%name.gschema.xml
%endif

%config %_xinputconf
%doc AUTHORS README

%exclude %_sysconfdir/bash_completion.d/ibus.bash

%files -n lib%name
%_libdir/libibus-1.0.so.*

%files -n lib%name-gir
%_typelibdir/IBus-%api_ver.typelib

%files gtk2
%_libdir/gtk-2.0/%gtk2_binary_version/immodules/im-ibus.so

%files gtk3
%_libdir/gtk-3.0/%gtk3_binary_version/immodules/im-ibus.so

%exclude %_libdir/gtk-*.0/*/immodules/*.la

%files -n lib%name-devel
%_libdir/lib*.so
%_pkgconfigdir/*
%_includedir/*
%_datadir/vala/vapi/ibus-1.0.vapi
%_datadir/vala/vapi/ibus-1.0.deps

%files -n lib%name-gir-devel
%_girdir/IBus-%api_ver.gir

%files -n python-module-ibus
%dir %python_sitelibdir_noarch/ibus
%python_sitelibdir_noarch/ibus/*

%files -n lib%name-devel-docs
%_datadir/gtk-doc/html/*

%changelog
* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.99.20121006-alt1
- updated to 1.4.99.20121006

* Tue Oct 02 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.99.20120917-alt1
- 1.4.99.20120917

* Thu Jul 19 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Jan 19 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt4
- fixed GConf support, made it optional
- really built with dconf support

* Fri Dec 16 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3
- gir subpackages separated

* Wed Nov 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2
- lib%name-devel dependences fixed

* Tue Nov 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1
- build for Sisyphus, based on upstream spec

