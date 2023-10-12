%define sover 0

Name: touche
Version: 2.0.10
Release: alt1

Summary: The desktop application to configure Touchegg

License: GPLv3
Group: System/Configuration/Other
Url: https://github.com/JoseExposito/touche

# Source-url: https://github.com/JoseExposito/touche/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from etersoft-build-utils
Source1: %name-development-%version.tar

Requires: lib%name%sover = %EVR
Requires: lib%name-gir = %EVR
Requires: touchegg
Requires: typelib(Adw) = 1

BuildRequires: rpm-macros-nodejs
BuildRequires: rpm-build-gir
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: meson
BuildRequires: npm
BuildRequires: libgjs-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libX11-devel
BuildRequires: node-webpack
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
Easily configure your touchpad and touchscreen multi-touch gestures
using Touchegg with this GTK graphical user interface

%package -n lib%name%sover
Summary: Shared library for Touche
Group: System/Libraries

%description -n lib%name%sover
Easily configure your touchpad and touchscreen multi-touch gestures
using Touchegg with this GTK graphical user interface

This package provides shared library required for Touche to work.

%package -n lib%name-devel
Summary: Development files and libraries for Touche
Group: Development/C++
Requires: lib%name%sover = %EVR

%description -n lib%name-devel
Easily configure your touchpad and touchscreen multi-touch gestures
using Touchegg with this GTK graphical user interface

This package provides files and library required to develop applications
that use lib%name

%package -n lib%name-gir
Summary: GObject introspection data for the Touche
Group: System/Libraries
Requires: lib%name%sover = %EVR

%description -n lib%name-gir
GObject introspection data for the Touche

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Touche
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the Touche

%prep
%setup -q -n %name-%version
%setup -a 1

%build
%meson
%meson_build

%install
%meson_install
%find_lang com.github.joseexposito.touche
desktop-file-validate %buildroot%_desktopdir/com.github.joseexposito.touche.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/appdata/com.github.joseexposito.touche.appdata.xml
( cd %buildroot%_bindir
  ln -s com.github.joseexposito.touche touche
)

%files -f com.github.joseexposito.touche.lang
%doc README.md
%_bindir/com.github.joseexposito.touche
%_bindir/touche
%_datadir/com.github.joseexposito.touche/
%_desktopdir/com.github.joseexposito.touche.desktop
%_datadir/glib-2.0/schemas/com.github.joseexposito.touche.gschema.xml
%_iconsdir/hicolor/*/apps/com.github.joseexposito.touche.svg
%_datadir/appdata/com.github.joseexposito.touche.appdata.xml

%files -n lib%name%sover
%_libdir/libtouche.so.%sover

%files -n lib%name-devel
%_includedir/touche.h
%_libdir/libtouche.so

%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir

%changelog
* Thu Oct 12 2023 Anton Midyukov <antohami@altlinux.org> 2.0.10-alt1
- new version (2.0.10) with rpmgs script

* Mon May 16 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 2.0.5-alt1
- new version (2.0.5) with rpmgs script
- Removed unneeded patches (Accepted by upstream)

* Mon Apr 04 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.0.7-alt4
- Added touchegg to Requires

* Wed Nov 17 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.0.7-alt3
- add russian translation

* Wed Nov 10 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.0.7-alt2
- add soname to libtouch library
- packing library files into subpackages

* Wed Nov 10 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.0.7-alt1
- Initial build in Sisyphus
