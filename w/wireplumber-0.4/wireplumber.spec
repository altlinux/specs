%define _unpackaged_files_terminate_build 1

%def_enable doc
%def_enable introspection
%def_disable systemd

# These come from meson.build.
%define apiversion 0.4
%define soversion 0

# This is used as the pkgconfig ID and as the library name
# to pass after `cc -l`.
%define libname wireplumber-%apiversion

Name: wireplumber-0.4
Version: 0.4.17
Release: alt2

Summary: a modular session/policy manager for PipeWire (0.4 compat library)

License: MIT
Group: Sound
URL: https://pipewire.pages.freedesktop.org/wireplumber/

BuildRequires(pre): meson >= 0.56
BuildRequires: pkgconfig(gobject-2.0) >= 2.62
BuildRequires: pkgconfig(gmodule-2.0) >= 2.62
BuildRequires: pkgconfig(gio-2.0) >= 2.62
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.62
BuildRequires: pkgconfig(libpipewire-0.3) >= 0.3.68
BuildRequires: liblua5.3-devel
%if_enabled introspection
BuildRequires(pre): gobject-introspection-devel
%endif
%if_enabled doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-breathe
BuildRequires: python3(sphinx_rtd_theme)
BuildRequires: python3-module-setuptools
BuildRequires: python3(lxml)
BuildRequires: doxygen >= 1.8.0
%endif
%if_enabled systemd
# Like so many other programs, WirePlumber implements logind integration via
# libsystemd for no reason. :(
BuildRequires: pkgconfig(systemd)
%endif

Source: %name-%version.tar

%package doc
Summary: docs for the client library for WirePlumber
Group: Documentation

%package -n lib%libname
Summary: the client library for WirePlumber
Group: System/Libraries
Conflicts: libwireplumber < 0.4.17-alt2
Obsoletes: libwireplumber < 0.4.17-alt2

%package -n lib%libname-devel
Summary: development files of the client library for WirePlumber
Group: Development/C

%if_enabled introspection
%package -n lib%libname-gir
Summary: GObject introspection data for lib%libname
Group: System/Libraries
Requires: lib%libname = %EVR

%package -n lib%libname-gir-devel
Summary: GObject introspection development data for lib%libname
Group: Development/Other
BuildArch: noarch
Requires: lib%libname-gir = %EVR
Requires: lib%libname-devel = %EVR

%endif

%description
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

%description doc
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains documentation for WirePlumber.

%description -n lib%libname
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains the client library.

%description -n lib%libname-devel
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains the development files for the client library.

%if_enabled introspection
%description -n lib%libname-gir
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains GObject introspection data for lib%libname.

%description -n lib%libname-gir-devel
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains GObject introspection development data for lib%libname.

%endif

%prep
%setup
# Make the relevant subdir() statements no-ops.
if [ -f src/meson.build ]; then : > src/meson.build; fi
if [ -f po/meson.build ]; then : > po/meson.build; fi
if [ -f tests/wplua/meson.build ]; then : > tests/wplua/meson.build; fi

%build
%meson \
    -Dsystem-lua=true \
%if_enabled doc
    -Ddoc=enabled \
%endif
%if_enabled systemd
    -Dsystemd=enabled \
%endif
%if_enabled introspection
    -Dintrospection=enabled \
%endif
    #

%meson_build

%install
%meson_install

# %%doc does not work for multiple subpackages as of 2021 Oct 18.
# We implement its functionality by hand as closely as possible.
%define docdir() %_defaultdocdir/%1-%version
%if 0
mkdir -p %buildroot%{docdir %name}/
cp -v NEWS.rst README.rst %buildroot%{docdir %name}/
%endif
mkdir -p %buildroot%{docdir %name-doc}/
mv -v %buildroot%_datadir/doc/wireplumber %buildroot%{docdir %name-doc}

%find_lang %name

%if 0
%files -f %name.lang
%define docdir() %_defaultdocdir/%1-%version
%{docdir %name}
%_bindir/wireplumber
%_bindir/wpctl
%_bindir/wpexec
%_datadir/wireplumber
%_datadir/zsh/site-functions/_wpctl
%if_enabled systemd
%_user_unitdir/wireplumber.service
%_user_unitdir/wireplumber@.service
%endif
%endif

%files doc
%define docdir() %_defaultdocdir/%1-%version
# Quoting docs/meson.build.
%{docdir %name-doc}

%files -n lib%libname
%_libdir/lib%libname.so.%soversion.*
%_libdir/lib%libname.so.%soversion
# plugins
%_libdir/%libname

%files -n lib%libname-devel
%_pkgconfigdir/%libname.pc
%_libdir/lib%libname.so
%_includedir/%libname

%if_enabled introspection
%files -n lib%libname-gir
%_typelibdir/Wp-%apiversion.typelib

%files -n lib%libname-gir-devel
%_girdir/Wp-%apiversion.gir
%endif

%changelog
* Tue Jul 30 2024 Arseny Maslennikov <arseny@altlinux.org> 0.4.17-alt2
- Built library and modules only for compatibility with some other packages in
  the presence of 0.5.

* Mon Dec 04 2023 Arseny Maslennikov <arseny@altlinux.org> 0.4.17-alt1
- 0.4.15 -> 0.4.17.

* Mon Oct 16 2023 Michael Shigorin <mike@altlinux.org> 0.4.15-alt2
- Added explicit BR: python3-module-setuptools to fix ftbfs on e2k.

* Sun Oct 15 2023 Arseny Maslennikov <arseny@altlinux.org> 0.4.15-alt1
- 0.4.14 -> 0.4.15.

* Sun Jun 25 2023 Arseny Maslennikov <arseny@altlinux.org> 0.4.14-alt2
- Fixed FTBFS.

* Wed Mar 22 2023 Arseny Maslennikov <arseny@altlinux.org> 0.4.14-alt1
- 0.4.13 -> 0.4.14.

* Thu Dec 15 2022 Arseny Maslennikov <arseny@altlinux.org> 0.4.13-alt1
- 0.4.12 -> 0.4.13.

* Thu Oct 20 2022 Arseny Maslennikov <arseny@altlinux.org> 0.4.12-alt1
- 0.4.9 -> 0.4.12.

* Sun Mar 27 2022 Arseny Maslennikov <arseny@altlinux.org> 0.4.9-alt1
- 0.4.8 -> 0.4.9.

* Mon Feb 07 2022 Arseny Maslennikov <arseny@altlinux.org> 0.4.8-alt1
- 0.4.7 -> 0.4.8.

* Fri Jan 14 2022 Arseny Maslennikov <arseny@altlinux.org> 0.4.7-alt1
- 0.4.6 -> 0.4.7.

* Fri Jan 07 2022 Arseny Maslennikov <arseny@altlinux.org> 0.4.6-alt1
- 0.4.5-37-g0ff9ea9 -> 0.4.6.

* Mon Dec 20 2021 Arseny Maslennikov <arseny@altlinux.org> 0.4.5.37.g0ff9ea9-alt1
- 0.4.5 -> 0.4.5-37-g0ff9ea9.

* Fri Nov 12 2021 Arseny Maslennikov <arseny@altlinux.org> 0.4.5-alt1
- 0.4.4-9-g44a0c55 -> 0.4.5.

* Fri Oct 22 2021 Arseny Maslennikov <arseny@altlinux.org> 0.4.4.9.g44a0c55-alt1
- 0.4.4 -> 0.4.4-9-g44a0c55.
- Built with -Dsystemd=enabled; this includes logind integration (by means of
  libsystemd) and installs unit files.

* Sun Oct 17 2021 Arseny Maslennikov <arseny@altlinux.org> 0.4.4-alt1
- 0.4.3 -> 0.4.4.

* Fri Oct 08 2021 Arseny Maslennikov <arseny@altlinux.org> 0.4.3-alt1
- 0.4.2 -> 0.4.3.

* Sun Oct 03 2021 Arseny Maslennikov <arseny@altlinux.org> 0.4.2-alt1
- 0.3.96 -> 0.4.2.

* Sat Jun 05 2021 Arseny Maslennikov <arseny@altlinux.org> 0.3.96-alt1
- 0.3.60.103.g9609a79903ab -> 0.3.96.

* Thu Mar 18 2021 Arseny Maslennikov <arseny@altlinux.org> 0.3.60.103.g9609a79903ab-alt1
- 0.3.60.63.g24a260030bab -> 0.3.60.103.g9609a79903ab.

* Sun Feb 21 2021 Arseny Maslennikov <arseny@altlinux.org> 0.3.60.63.g24a260030bab-alt1
- Initial build for ALT Sisyphus.
