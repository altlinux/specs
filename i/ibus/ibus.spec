%def_disable snapshot
%define api_ver 1.0
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var
%define xdg_name org.freedesktop.IBus

%def_enable gtk2
%def_enable gtk4

%def_enable python
%def_disable python2
%def_enable dconf
%def_enable wayland
%def_enable appindicator
%def_enable emoji_dict
%def_enable unicode_dict
# ibus-engine-switch timed out in hasher
%def_disable check
#src/tests/ibus-desktop-testing-runner.in:
#172     if test $HAVE_GRAPHICS -eq 1 ; then
#173         /usr/libexec/Xorg.wrap -noreset ...
%def_disable installed_tests

Name: ibus
Version: 1.5.28
Release: alt1

Summary: Intelligent Input Bus for Linux OS
License: LGPL-2.1 and Unicode
Group: System/Libraries
Url: https://github.com/ibus/ibus/wiki

%if_disabled snapshot
Source: https://github.com/%name/%name/releases/download/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: ibus-xinput

# fc
Patch10: %name-1385349-segv-bus-proxy.patch

%if_enabled gtk2
%define gtk2_binary_version %(pkg-config --variable=gtk_binary_version gtk+-2.0)
%endif
%define gtk3_binary_version %(pkg-config --variable=gtk_binary_version gtk+-3.0)
%if_enabled gtk4
%define gtk4_binary_version %(pkg-config --variable=gtk_binary_version gtk4)
%endif

%define unicode_ver 15.0

Requires: iso-codes setxkbmap xmodmap
Requires: lib%name = %EVR
Requires: lib%name-gir = %EVR
Requires: %name-dicts = %EVR

Requires(pre): dconf

%if_enabled python
BuildRequires(pre): rpm-build-python3
%add_python3_path %_datadir/%name/setup
%endif

BuildRequires(pre): rpm-build-xdg rpm-build-systemd
%{?_enable_python2:BuildRequires(pre): rpm-build-python}
BuildRequires: vala-tools >= 0.18
%{?_enable_gtk2:BuildRequires: libgtk+2-devel}
BuildRequires: libgtk+3-devel
%{?_enable_gtk4:BuildRequires: libgtk4-devel}
BuildRequires: libdbus-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk-doc
BuildRequires: iso-codes-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gnome-icon-theme-symbolic
BuildRequires: libXi-devel libXtst-devel libXfixes-devel
BuildRequires: xkeyboard-config-devel
BuildRequires: libnotify-devel
%{?_enable_unicode_dict:BuildRequires: unicode-ucd}
%{?_enable_python:BuildRequires: python3-devel python3-module-dbus-devel python3-module-pygobject3-devel}
%{?_enable_python2:BuildRequires: python-devel python-modules-compiler python-module-dbus-devel python-module-pygobject3-devel}
%{?_enable_dconf:BuildRequires: libdconf-devel /proc dbus-tools-gui dconf}
%{?_enable_wayland:BuildRequires: libwayland-client-devel libxkbcommon-devel}
# since 1.5.14
%{?_enable_emoji_dict:BuildRequires: cldr-emoji-annotation-devel >= 42
BuildRequires: unicode-emoji >= %unicode_ver unicode-ucd >= %unicode_ver gir(Gtk) = 3.0}
%{?_enable_appindicator:BuildRequires: qt5-base-devel}
%{?_enable_check:BuildRequires: xvfb-run gnome-desktop-testing}

%define _xinputconf %_sysconfdir/X11/xinit/xinput.d/ibus.conf


%description
IBus means Intelligent Input Bus. It is an input framework for Linux OS.

%package dicts
Summary: IBus dictionaries
Group: Text tools
License: Unicode
BuildArch: noarch

%description dicts
This package provides Unicode %{?_enable_emoji_dict:and Emoji}
dictionaries for IBus.

%package -n lib%name
Summary: IBus libraries
Group: System/Libraries
Requires: dbus

%description -n lib%name
This package contains the libraries for IBus

%package -n lib%name-gir
Summary: GObject introspection data for the IBus library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
This package contains typelib file for the IBus library.

%package gtk2
Summary: IBus im module for gtk2
Group: System/Libraries
Requires(pre): libgtk+2
Requires: lib%name = %EVR

%description gtk2
This package contains IBus im module for gtk2.

%package gtk3
Summary: IBus im module for gtk3
Group: System/Libraries
Requires(pre): libgtk+3
Requires: lib%name = %EVR

%description gtk3
This package contains IBus im module for gtk3.

%package gtk4
Summary: IBus im module for gtk4
Group: System/Libraries
Requires(pre): libgtk4
Requires: lib%name = %EVR

%description gtk4
This package contains IBus im module for gtk4.

%package -n lib%name-devel
Summary: Development tools for ibus
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains the header files for IBus library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for IBus
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-gir-devel
This package contains gir files for IBus library.

%package -n lib%name-devel-docs
Summary: Developer documents for IBus
Group: Development/Other
BuildArch: noarch
Requires: %name = %EVR

%description -n lib%name-devel-docs
This package contains developer documentation for IBus.

%package -n python3-module-ibus-overrides
Summary: IBus Python override library
Group: Development/Python3

%description -n python3-module-ibus-overrides
This package provides Python override library for IBus. The Python files
override some functions in GObject-Introspection.

%if_enabled python2
%package -n python-module-ibus
Summary: IBus im module for python
Group: Development/Python
BuildArch: noarch

%description -n python-module-ibus
This package contains IBus im module for python.

%package -n python-module-ibus-overrides
Summary: IBus Python override library
Group: Development/Python

%description -n python-module-ibus-overrides
This package provides Python override library for IBus. The Python files
override some functions in GObject-Introspection.
%endif

%package tests
Summary: Tests for IBus
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Intelligent Input Bus.

%prep
%setup
%patch10 -p1
%{?_enable_snapshot:touch ChangeLog}

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
    --disable-static \
    %{?_disable_gtk2:--disable-gtk2} \
    --enable-gtk3 \
    %{?_enable_gtk4:--enable-gtk4} \
    --enable-xim \
    %{?_enable_snapshot:--enable-gtk-doc} \
    %if_enabled python
    %{?_disable_python2:--disable-python2} \
    --with-python=%__python3 \
    %{?_enable_python2:--enable-python-library} \
    %endif
    %{subst_enable dconf} \
    %{?_enable_dconf:--disable-schemas-compile} \
    %{subst_enable wayland} \
    --enable-surrounding-text \
    --enable-introspection \
    %{?_disable_emoji_dict:--disable-emoji-dict} \
    %{?_disable_unicode_dict:--disable-unicode-dict} \
    %{subst_enable appindicator} \
    %{?_enable_installed_tests:--enable-install-tests}
%nil
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_localstatedir/cache/%name

# install xinput config file
install -pm 644 -D %SOURCE1 %buildroot%_xinputconf

%find_lang %{name}10

%check
xvfb-run %make -k check VERBOSE=1

%files -f %{name}10.lang
%_xdgconfigdir/Xwayland-session.d/10-%name-x11
%dir %_datadir/%name/
%_bindir/%name
%_bindir/%name-daemon
%_bindir/%name-setup
%_datadir/%name/*
# dicts
%exclude %_datadir/%name/dicts
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_libexecdir/%name-portal
%_libexecdir/%name-ui-gtk3
%_libexecdir/%name-x11
%_libexecdir/%name-engine-simple
%{?_enable_wayland:%_libexecdir/%name-wayland}

%if_enabled emoji_dict
%_libexecdir/%name-extension-gtk3
%_libexecdir/%name-ui-emojier
%_man7dir/%name-emoji.7*
%endif

%if_enabled dconf
%dir %_sysconfdir/dconf/db/%name.d
%_sysconfdir/dconf/db/%name.d/00-upstream-settings
%_sysconfdir/dconf/profile/%name
%_libexecdir/%name-dconf
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.freedesktop.%name.gschema.xml
%endif
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/dbus-1/services/org.freedesktop.portal.IBus.service
%_userunitdir/gnome-session.target.wants/%xdg_name.session.GNOME.service
%_userunitdir/%xdg_name.session.GNOME.service
%_userunitdir/%xdg_name.session.generic.service

%config %_xinputconf
%_localstatedir/cache/%name
%_man1dir/%name-daemon.1.*
%_man1dir/%name-setup.1.*
%_man1dir/%name.1.*
%_man5dir/*
%doc AUTHORS README

%exclude %_datadir/bash-completion/completions/ibus.bash

%files dicts
%dir %_datadir/%name/dicts
%_datadir/%name/dicts/*

%files -n lib%name
%_libdir/lib%name-1.0.so.*

%files -n lib%name-gir
%_typelibdir/IBus-%api_ver.typelib

%if_enabled gtk2
%files gtk2
%_libdir/gtk-2.0/%gtk2_binary_version/immodules/im-ibus.so
%endif

%files gtk3
%_libdir/gtk-3.0/%gtk3_binary_version/immodules/im-ibus.so

%if_enabled gtk4
%files gtk4
%_libdir/gtk-4.0/%gtk4_binary_version/immodules/libim-ibus.so
%endif


%exclude %_libdir/gtk-*.0/*/immodules/*.la

%files -n lib%name-devel
%_libdir/lib*.so
%_pkgconfigdir/*
%_includedir/*
%_datadir/gettext/its/ibus.*
%_vapidir/%name-%api_ver.vapi
%_vapidir/%name-%api_ver.deps

%files -n lib%name-gir-devel
%_girdir/IBus-%api_ver.gir

%files -n lib%name-devel-docs
%_datadir/gtk-doc/html/*

%if_enabled python
%files -n python3-module-ibus-overrides
%python3_sitelibdir/gi/overrides/IBus*
%python3_sitelibdir/gi/overrides/__pycache__/IBus*
%endif

%if_enabled python2
%files -n python-module-ibus
%dir %python_sitelibdir_noarch/ibus
%python_sitelibdir_noarch/ibus/*

%files -n python-module-ibus-overrides
%python_sitelibdir/gi/overrides/IBus.py*
%endif

%if_enabled installed_tests
%files tests
%_bindir/ibus-desktop-testing-runner
%_libexecdir/installed-tests/%name/
%_datadir/installed-tests/%name/
%endif

%changelog
* Tue Feb 21 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.28-alt1
- 1.5.28

* Tue Aug 23 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.27-alt1
- 1.5.27

* Fri Apr 08 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.26-alt2
- "Fix refcounting issues in IBusText & IBusProperty" (upstream patch)

* Mon Mar 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.26-alt1
- 1.5.26

* Sat Aug 21 2021 Yuri N. Sedunov <aris@altlinux.org> 1.5.25-alt1
- 1.5.25

* Mon Feb 22 2021 Yuri N. Sedunov <aris@altlinux.org> 1.5.24-alt1
- 1.5.24
- new -gtk4 subpackage

* Tue Sep 29 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5.23-alt1
- 1.5.23

* Tue Apr 21 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5.22-alt2
- moved dictionaries to separate -dicts subpackage (ALT #38372)

* Tue Mar 17 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5.22-alt1
- 1.5.22

* Fri Aug 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.21-alt1
- 1.5.21
- new -tests subpackage

* Thu Aug 22 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.20-alt3
- rebuilt with Emoji dict
- disabled python2 support

* Sat Apr 06 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.20-alt2
- rebuilt with python3 as default python

* Fri Mar 01 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.20-alt1
- 1.5.20

* Thu Aug 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.19-alt1
- 1.5.19

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5.18-alt1
- 1.5.18

* Thu Oct 26 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.17-alt2
- rebuild with _localstatedir=%%_var

* Mon Oct 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.17-alt1
- 1.5.17

* Wed May 17 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.16-alt1
- 1.5.16

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.15-alt1
- 1.5.15

* Fri Aug 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.14-alt1
- 1.5.14

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.13-alt1
- 1.5.13

* Thu Feb 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.12-alt1
- 1.5.12

* Thu Aug 06 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.11-alt1
- 1.5.11

* Fri Apr 10 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.10-alt1
- 1.5.10

* Thu Oct 09 2014 Yuri N. Sedunov <aris@altlinux.org> 1.5.9-alt1
- 1.5.9
- remove upstreamed patches

* Tue Jul 08 2014 Yuri N. Sedunov <aris@altlinux.org> 1.5.7-alt1
- 1.5.7
- updated fc patchset

* Fri Feb 07 2014 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5
- updated fc patchset

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

