Name: libtext-engine
Version: 0.1.1
Release: alt1

Summary: A lightweight rich text framework for GTK
License: LGPL-2.1-or-later AND MPL-2.0
Group: Other
Url: https://github.com/mjakeman/text-engine

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(glib-2.0)

%description
Text Engine is a rich-text editing framework for GTK 4. 
The primary user of this library is bluetype but it can be used wherever rich text display and editing is needed.

%package devel
Summary:  Development files for %name
Group:    Development/GNOME and GTK+
Requires: %name = %EVR

%description devel
This package contains the pkg-config file and development headers for %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/text-engine-demo
%_libdir/libtext-engine-0.1.so

%files devel
%_includedir/text-engine/
%_pkgconfigdir/text-engine-0.1.pc

%changelog
* Mon Jun 26 2023 Roman Alifanov <ximper@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
