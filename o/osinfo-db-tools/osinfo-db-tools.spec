
Summary: Tools for managing the osinfo database
Name: osinfo-db-tools
Version: 1.7.0
Release: alt1
License: GPLv2+
Group: Development/Tools
Source: %name-%version.tar
Url: http://libosinfo.org/

BuildRequires(pre): meson >= 0.49.0
BuildRequires: gettext >= 0.19.8
BuildRequires: gtk-doc
BuildRequires: pkgconfig(glib-2.0) >= 2.44 pkgconfig(gobject-2.0) pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires: pkgconfig(libxslt) >= 1.0.0
BuildRequires: pkgconfig(libarchive) >= 3.0.0
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsoup-2.4)

BuildRequires: perl-podlators
BuildRequires: python3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-requests

Conflicts: libosinfo < 1.0.0

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

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
%doc NEWS README
%_bindir/*
%_man1dir/*

%changelog
* Wed Dec 04 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.0-alt1
- new version 1.7.0

* Fri Aug 23 2019 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- new version 1.6.0

* Wed May 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Sat Mar 02 2019 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- new version 1.4.0

* Sat Feb 02 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Dec 30 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0
- fix License

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0

