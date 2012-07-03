%def_enable dconf
%def_disable gconf

Name: ibus
Version: 1.4.0
Release: alt4

Summary: Intelligent Input Bus for Linux OS
License: LGPLv2+
Group: System/Libraries
Url: http://code.google.com/p/%name/

Source: http://%name.googlecode.com/files/%name-%version.tar.gz
Source1: xinput-ibus

%define gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)
%define gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)

Requires: iso-codes
Requires: python-module-%name = %version-%release
Requires: lib%name = %version-%release
%{?_enable_gconf:Requires(post,preun):GConf}
%{?_enable_dconf:Requires: dconf}

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
%{?_enable_gconf:BuildRequires: libGConf-devel}
# required if autoreconf used
BuildRequires: libGConf-devel
%{?_enable_dconf:BuildRequires: libdconf-devel /proc dbus-tools-gui dconf}

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
Requires: lib%name = %version-%release

%description gtk2
This package contains IBus im module for gtk2.

%package gtk3
Summary: IBus im module for gtk3
Group: System/Libraries
Requires: lib%name = %version-%release

%description gtk3
This package contains IBus im module for gtk3.

%package -n python-module-ibus
Summary: IBus im module for python
Group: Development/Python
BuildArch: noarch

%description -n python-module-ibus
This package contains IBus im module for python.

%package -n lib%name-devel
Summary: Development tools for ibus
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files for IBus library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for IBus
Group: Development/Other
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
This package contains gir files for IBus library.

%package -n lib%name-devel-docs
Summary: Developer documents for IBus
Group: Development/Other
Requires: %name = %version-%release
Requires: gtk-doc

%description -n lib%name-devel-docs
This package contains developer documentation for IBus.

%prep
%setup

%build
%autoreconf
%configure \
    --disable-static \
    --enable-gtk2 \
    --enable-gtk3 \
    --enable-xim \
    --disable-gtk-doc \
    %{subst_enable dconf} \
    %{?_enable_dconf:--disable-schemas-compile} \
    %{subst_enable gconf} \
    %{?_enable_gconf:--disable-schemas-install} \
    --enable-introspection

# make -C po update-gmo
%make_build

%install
%make DESTDIR=%buildroot install

# install xinput config file
install -pm 644 -D %SOURCE1 %buildroot%_xinputconf

# install .desktop files
mkdir -p %buildroot%_sysconfdir/xdg/autostart/
install -m0640 bus/ibus.desktop %buildroot%_sysconfdir/xdg/autostart/

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

%files -f %{name}10.lang
%dir %_datadir/ibus/
%_bindir/ibus-daemon
%_bindir/ibus-setup
%_datadir/ibus/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_libexecdir/ibus-ui-gtk
%_libexecdir/ibus-x11
%_sysconfdir/xdg/autostart/ibus.desktop

%if_enabled gconf
%_libexecdir/ibus-gconf
%_sysconfdir/gconf/schemas/ibus.schemas
%endif

%if_enabled dconf
%_sysconfdir/dconf/db/%name
%_sysconfdir/dconf/profile/%name
%_libexecdir/%name-dconf
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.freedesktop.%name.gschema.xml
%endif

%config %_xinputconf
%doc AUTHORS README

%files -n python-module-ibus
%dir %python_sitelibdir_noarch/ibus
%python_sitelibdir_noarch/ibus/*

%files -n lib%name
%_libdir/libibus-1.0.so.*

%files -n lib%name-gir
%_libdir/girepository-1.0/IBus-1.0.typelib

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
%_datadir/gir-1.0/IBus-1.0.gir

%files -n lib%name-devel-docs
%_datadir/gtk-doc/html/*

%changelog
* Thu Jan 19 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt4
- fixed GConf support, made it optional
- really built with dconf support

* Fri Dec 16 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3
- gir subpackages separated

* Wed Nov 30 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2
- lib%name-devel dependences fixed

* Tue Nov 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1
- build for Sisyphus, based on upstream spec

