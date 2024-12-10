%def_enable snapshot

%define _name speech-provider
%define ver_major 1.0
%define api_ver 1.0
%define xdg_name org.freedesktop.Speech.Provider
%define namespace SpeechProvider

%def_enable introspection
%def_enable docs
%def_enable check

Name: libspeechprovider
Version: %ver_major.3
Release: alt0.1

Summary: Speech Provider Resources
Group: System/Libraries
License: Apache-2.0
Url: https://github.com/project-spiel/libspeechprovider

Vcs: https://github.com/project-spiel/libspeechprovider.git

%define VER %(echo %version|tr . _)

%if_disabled snapshot
Source: %url/archive/SPEECHPROVIDER_%VER/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define meson_ver 0.64
%define glib_ver 2.76

BuildRequires(pre): rpm-macros-meson %{?_enable_introspection:rpm-build-gir}
BuildRequires: meson >= %meson_ver
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
%{?_enable_introspection:BuildRequires: pkgconfig(gobject-introspection-1.0) /usr/bin/g-ir-scanner}
%{?_enable_docs:BuildRequires: gi-docgen}

%description
%summary

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
%setup -n %name-%version

%build
%meson \
    %{subst_enable_meson_bool introspection introspection} \
    %{subst_enable_meson_bool docs docs}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_libdir/lib%_name-%api_ver.so
%_datadir/speech-provider/%xdg_name.xml
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

