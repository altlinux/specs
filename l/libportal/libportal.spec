%def_enable snapshot

%define ver_major 0.1
%define soname %ver_major.1

%def_enable gtk_doc

Name: libportal
Version: %ver_major
Release: alt1
Epoch: 1

Summary: Flatpak portal library
Group: System/Libraries
License: LGPLv2
Url: https://github.com/flatpak/libportal

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.38

BuildRequires(pre): meson
BuildRequires: libgio-devel >= %glib_ver gtk-doc

%description
%name provides GIO-style async APIs for most Flatpak portals.

%package devel
Summary: Development files and libraries for %name
Group: Development/C
Requires: %name = %EVR

%description devel
%name provides GIO-style async APIs for most Flatpak portals.

This package provides files for development with %name.

%package devel-doc
Summary: Development documentaion for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %EVR

%description devel-doc
%name provides GIO-style async APIs for most Flatpak portals.

This package provides development documentations for %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -f %name.lang
%_libdir/%name.so.*
%doc README*

%files devel
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%name
%endif


%changelog
* Thu Nov 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1:0.1-alt1
- 0.1

* Sun Nov 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1:0.0.2-alt1
- first build for Sisyphus

