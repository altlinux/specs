%define api_ver 1.0
%define _libexecdir %_prefix/libexec
%define ibus_xkb_ver 1.5.0

%def_enable python
%def_enable dconf
%def_disable gconf
%def_enable xkb
%def_enable wayland

Name: ibus
Version: 1.5.4
Release: alt1

Summary: Intelligent Input Bus for Linux OS
License: LGPLv2+
Group: System/Libraries
Url: http://code.google.com/p/%name/

Source: http://%name.googlecode.com/files/%name-%version.tar.gz
Source1: ibus-xinput
Source2: ibus-xkb-%ibus_xkb_ver.tar.gz

# fedora's patches
Patch1: ibus-810211-no-switch-by-no-trigger.patch
Patch2: ibus-541492-xkb.patch
Patch3: ibus-530711-preload-sys.patch
Patch4: ibus-xx-setup-frequent-lang.patch

Patch10: ibus-1.5.4-up.patch

%define gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)
%define gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)

Requires: iso-codes
Requires: lib%name = %version-%release
Requires: lib%name-gir = %version-%release

%{?_enable_gconf:Requires(post,preun):GConf}
%{?_enable_dconf:Requires: dconf}

BuildRequires: vala-tools >= 0.18
BuildRequires: python-modules-compiler
BuildRequires: rpm-build-python
BuildPreReq: libgtk+2-devel
BuildPreReq: libgtk+3-devel
BuildRequires: libdbus-devel
BuildRequires: python-module-dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk-doc
BuildRequires: python-module-pygobject-devel
BuildRequires: intltool
BuildRequires: iso-codes-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gnome-icon-theme-symbolic
BuildRequires: libXi-devel
BuildRequires: libnotify-devel
%{?_enable_python:BuildRequires: rpm-build-python python-module-pygobject-devel}
%{?_enable_gconf:BuildRequires: libGConf-devel}
# required if autoreconf used
BuildRequires: libGConf-devel
%{?_enable_dconf:BuildRequires: libdconf-devel /proc dbus-tools-gui dconf}
%{?_enable_xkb:BuildRequires: libxkbfile-devel}
%{?_enable_wayland:BuildRequires: libwayland-client-devel libxkbcommon-devel}
# gsettings-schema-convert
BuildRequires: GConf

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
%setup -a2
%patch1 -p1 -b .noswitch

%if_enabled xkb
%patch2 -p1 -b .xkb
rm -f bindings/vala/ibus-%api_ver.vapi
rm -f data/dconf/00-upstream-settings
# merge translations
for po in $(basename -a $(ls ibus-xkb-%ibus_xkb_ver/po/*.po)); do
    msgcat --use-first po/$po ibus-xkb-%ibus_xkb_ver/po/$po -o po/$po
done
%endif
%patch3 -p1
%patch4 -p1
%patch10 -p1

%build
%autoreconf
%configure \
    --disable-static \
    --enable-gtk2 \
    --enable-gtk3 \
    --enable-xim \
    --disable-gtk-doc \
    %{?_enable_python:--enable-python-library} \
    %{subst_enable dconf} \
    %{?_enable_dconf:--disable-schemas-compile} \
    %{subst_enable gconf} \
    %{?_enable_gconf:--disable-schemas-install} \
    %{subst_enable wayland} \
    --enable-surrounding-text \
    --enable-introspection

%if_enabled xkb
make -C ui/gtk3 maintainer-clean-generic
%endif

%make_build

%install
%makeinstall_std

# install xinput config file
install -pm 644 -D %SOURCE1 %buildroot%_xinputconf

%find_lang %{name}10

%check
# FAIL: test-stress
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
%_bindir/%name
%_bindir/%name-daemon
%_bindir/%name-setup
%_datadir/%name/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_libexecdir/%name-ui-gtk3
%_libexecdir/%name-x11
%_libexecdir/%name-engine-simple
%{?_enable_wayland:%_libexecdir/%name-wayland}

%if_enabled gconf
%_libexecdir/%name-gconf
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
%_man1dir/%name-daemon.1.*
%_man1dir/%name-setup.1.*
%_man1dir/%name.1.*
%doc AUTHORS README

%exclude %_datadir/bash-completion/completions/ibus.bash

%files -n lib%name
%_libdir/lib%name-1.0.so.*

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
* Wed Oct 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4
- updated fc patchset

* Mon Sep 02 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3
- updated fc patchset

* Sun May 12 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2
- updated fc patchset

* Wed Mar 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt2
- rebuilt for people/gnome

* Wed Mar 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1
- updated fc patchset

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

