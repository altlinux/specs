%define _libexecdir %_prefix/libexec
%define libname libfeedback
%define _version 0.0.0+git20210426
%define ver_major 0.0.0
%define api_ver 0.0
%define ver_minor .git20210426

%def_enable introspection
%def_enable vala
%def_enable check

Name: feedbackd
Version: %ver_major
Release: alt0.1%ver_minor

Summary: Feedback library for GNOME
Group: System/Servers
License: GPL-3.0-or-later
Url: https://source.puri.sm/Librem5/feedbackd

Vcs: https://source.puri.sm/Librem5/feedbackd.git
Source: https://source.puri.sm/Librem5/%name/-/archive/v%_version/%name-v%_version.tar.gz

Requires: %libname = %EVR

%define glib_ver 2.50
%define gudev_ver 232

BuildRequires(pre): meson rpm-build-gir
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gsound)
BuildRequires: pkgconfig(gudev-1.0) >= %gudev_ver
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(systemd)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_check:BuildRequires: dbus-tools-gui}

%description
feedbackd provides a DBus daemon (feedbackd) to act on events to provide
haptic, visual and audio feedback. It offers a library (libfeedback) and
GObject introspection bindings to ease using it from applications.

%package -n %libname
Summary: Library for %name
Group: System/Libraries

%description -n %libname
The lib%name package contains libraries for %name

%package -n %libname-devel
Summary: Development files for %libname
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
%setup -n %name-v%_version

%build
%meson \
    %{?_disable_introspection:-Dintrospection=disabled} \
    %{?_disable_vala:-Dvapi=false}
%nil
%meson_build

%install
%meson_install
install -D -m644 debian/%name.udev %buildroot%_udevrulesdir/90-%name.rules

%check
%__meson_test

%files
%_bindir/fbcli
%_libexecdir/%name
%_libexecdir/fbd-ledctrl
%_udevrulesdir/90-%name.rules
%_datadir/dbus-1/interfaces/org.sigxcpu.Feedback.xml
%_datadir/dbus-1/services/org.sigxcpu.Feedback.service
%_datadir/%name/
%_datadir/glib-2.0/schemas/org.sigxcpu.feedbackd.gschema.xml

%files -n %libname
%_libdir/%libname-%api_ver.so.*

%files -n %libname-devel
%_includedir/%libname-%api_ver/
%_libdir/%libname-%api_ver.so
%_pkgconfigdir/%libname-%api_ver.pc
%{?_enable_vala:%_datadir/vala/vapi/%libname-%api_ver.*}

%if_enabled introspection
%files -n %libname-gir
%_typelibdir/Lfb-%api_ver.typelib

%files -n %libname-gir-devel
%_girdir/Lfb-%api_ver.gir
%endif

%changelog
* Fri Jul 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.0.0-alt0.1.git20210426
- first build for Sisyphus

