%def_enable snapshot

%define _name spiel
%define ver_major 1.0
%define api_ver 1.0
%define namespace Spiel
%define xdg_name org.freedesktop.Speech.%namespace


%def_enable system_speechprovider
%def_enable introspection
%def_enable docs
%def_enable check

Name: lib%_name
Version: %ver_major.3
Release: alt0.1

Summary: A library for speech synthesis clients
Group: System/Libraries
License: Apache-2.0
Url: https://github.com/project-spiel/libspiel

Vcs: https://github.com/project-spiel/libspiel.git

%define VER %(echo %version|tr . _)

%if_disabled snapshot
Source: %url/archive/SPIEL_%VER/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
%{?_disable_system_speechprovider:Source1: libspeechprovider-%version.tar}

%define meson_ver 0.64
%define glib_ver 2.76

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson >= %meson_ver
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) /usr/bin/g-ir-scanner
%{?_enable_system_speechprovider:BuildRequires: pkgconfig(speech-provider-1.0)}
%{?_enable_docs:BuildRequires: gi-docgen}

%description
This client library is designed to provide an ergonomic interface to the
myriad of potential speech providers that are installed in a given
session. The API is inspired by the W3C Web Speech API.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %namespace library.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for Dex library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for %namespace library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %EVR

%description devel-doc
This package contains development documentation for Dex library.

%prep
%setup -n %name-%version %{?_disable_system_speechprovider:-a1
mv libspeechprovider-%version subprojects/libspeechprovider}

%build
%meson \
    %{subst_enable_meson_bool docs docs}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%_name
%_libdir/lib%_name-%api_ver.so
%_datadir/glib-2.0/schemas/org.monotonous.libspiel.gschema.xml
%doc README*

%files devel
%_includedir/%_name/
#%_libdir/lib%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

#%if_enabled docs
#%files devel-doc
#%_datadir/doc/%name/
#%endif

%changelog
* Tue Dec 10 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt0.1
- first build for Sisyphus

