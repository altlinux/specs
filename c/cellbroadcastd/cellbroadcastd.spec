%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define _name cellbroadcastd
%define libname libcellbroadcast
%define xdg_name org.freedesktop.cbd
%define ver_major 0.0
%define namespace Lcb
%define api_ver 0.0

%define gvdb_ver 4758f6f

%def_enable introspection
%def_enable vala
%def_disable man
%def_disable gtk_doc
%ifarch %ix86
%def_disable check
%else
%def_enable check
%endif


Name: %_name
Version: %ver_major.3
Release: alt1

Summary: Cell broadcast daemon
Group: System/Servers
License: GPL-3.0-or-later and LGPL-2.1-or-later
Url: https://gitlab.freedesktop.org/devrtz/cellbroadcastd

Vcs: https://gitlab.freedesktop.org/devrtz/cellbroadcastd.git

%if_disabled snapshot
Source: https://gitlab.freedesktop.org/devrtz/cellbroadcastd/-/archive/v%version/%name-v%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: gvdb-%gvdb_ver.tar

%define glib_ver 2.76
%define gudev_ver 232
%define gmobile_ver 0.4.0
%define mm_ver 1.24.0

# daemon is linked statically for now
#Requires: %libname = %EVR
Requires: ModemManager >= %mm_ver
Requires: mobile-broadband-provider-info

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-macros-systemd
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gmobile) >= %gmobile_ver
BuildRequires: pkgconfig(mm-glib) >= %mm_ver
BuildRequires: pkgconfig(mobile-broadband-provider-info)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_man:BuildRequires: /usr/bin/rst2man}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: dbus-tools-gui}

%description
cellbroadcastd provides a DBus daemon that manages cell broadcast
messages received via ModemManager. It provides a storage for them
and allows configuring channels for the modem to watch out for. It
offers a library (libcellbroadcast) and GObject introspection bindings
to ease using it from applications.

%package -n %libname
Summary: Library for %name
License: LGPL-2.1-or-later
Group: System/Libraries

%description -n %libname
The lib%name package contains libraries for %name

%package -n %libname-devel
Summary: Development files for %libname
License: LGPL-2.1-or-later
Group: Development/C
Requires: %libname = %EVR

%description -n %libname-devel
The %name-devel package contains libraries and header files for
developing applications that use %libname.

%package -n %libname-gir
Summary: GObject introspection data for %libname
Group: System/Libraries
Requires: %libname = %EVR

%description -n %libname-gir
GObject introspection data for %libname

%package -n %libname-gir-devel
Summary: GObject introspection devel data for %libname
Group: Development/Other
BuildArch: noarch
Requires: %libname-gir = %EVR
Requires: %libname-devel = %EVR

%description -n %libname-gir-devel
GObject introspection devel data for %libname

%prep
%setup -n %name-%{?_disable_snapshot:v}%version -a1
mv gvdb-%gvdb_ver subprojects/gvdb
# install gir-files
sed -i 's/install: false/install: true/' %libname/meson.build

%build
%meson \
    -Dsystemd_user_unit_dir=%_userunitdir \
    %{subst_enable_meson_feature introspection introspection} \
    %{subst_enable_meson_bool check tests}
%nil
%meson_build

%install
%meson_install
rm -f %buildroot%_libdir/*.a

%check
%__meson_test

%files
%_bindir/cbcli
%_libexecdir/%name
%_userunitdir/%name.service
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/interfaces/%xdg_name.xml
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.enums.xml
%{?_enable_man:%_man1dir/fbcli.1.*
%_man1dir/cbcli.1.*
%_man8dir/%name.8.*}
%doc README* NEWS

%files -n %libname
%_libdir/%libname-%api_ver.so.*
%doc README* NEWS

%files -n %libname-devel
%_includedir/%libname-%api_ver/
%_libdir/%libname-%api_ver.so
%_pkgconfigdir/%libname-%api_ver.pc
%{?_enable_vala:%_datadir/vala/vapi/%libname-%api_ver.*}

%if_enabled introspection
%files -n %libname-gir
%_typelibdir/%namespace-%api_ver.typelib

%files -n %libname-gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%changelog
* Wed Oct 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt1
- 0.0.3

* Fri Jun 27 2025 Yuri N. Sedunov <aris@altlinux.org> 0.0.2-alt1
- 0.0.2

* Thu Jun 26 2025 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt1
- 0.0.1

* Wed Jun 25 2025 Yuri N. Sedunov <aris@altlinux.org> 0.0.0-alt0.1
- first build for Sisyphus (4818d8d)

