Name: libmarblepq
Version: 2.0.0
Release: alt3.gitf240b2e

Summary: A collection of useful functions and reusable GTK widgets.
License: GPL-3.0
Group: System/Libraries

Url: https://gitlab.com/raggesilver/marble
Source: %name-%version.tar
Packager: Vladimir Didenko <cow@altlinux.org>

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: libgio-devel
BuildRequires: libgtk4-devel libgtk4-gir-devel
BuildRequires: gobject-introspection-devel

%description
A collection of useful functions and reusable GTK widgets.

%package devel
Summary: Development libraries and header files for MarblePQ
Group: Development/C
Requires: %name = %version-%release

%description devel
This package package includes the libraries and header files
for the MarblePQ library.

%package gir
Summary: GObject introspection data for the MarblePQ library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the MarblePQ library.

%package gir-devel
Summary: GObject introspection devel data for the MarblePQ library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the MarblePQ library.


%package vala
Summary: Vala language bindings for the MarblePQ library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for the MarblePQ library.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc COPYING README.md
%_libdir/*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir

%files vala
%_vapidir/*.vapi
%_vapidir/*.deps

%changelog
* Thu Aug 31 2023 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt3.gitf240b2e
- revert build fix for gtk css provider (fixed in new vala)

* Mon Aug 14 2023 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt2.gitf240b2e
- build fix for gtk css provider

* Mon Sep 19 2022 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1.gitf240b2e
- new version with the rename marble -> marblepq

* Mon Sep 19 2022 Vladimir Didenko <cow@altlinux.org> 42-alt1.git6dcc6fe
- new version
