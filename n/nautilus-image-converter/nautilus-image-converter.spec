%define ver_major 0.4

Name: nautilus-image-converter
Version: %ver_major.0
Release: alt1

Summary: An extension for Nautilus to rotate and resize images
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://gitlab.gnome.org/coreyberla/nautilus-image-converter
Source: %name-%version.tar

Requires: /usr/bin/convert

BuildRequires(pre): meson
BuildRequires: pkgconfig(glib-2.0) >= 2.28.0
BuildRequires: pkgconfig(gtk4) >= 4.6.0
BuildRequires: pkgconfig(libnautilus-extension-4)

%description
This package contains a Nautilus extension makes it easy to open terminal
in current location.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS ChangeLog NEWS COPYING
%_libdir/nautilus/extensions-4/libnautilus-image-converter.so
%dir %_datadir/nautilus-image-converter
%_datadir/nautilus-image-converter/nautilus-image-resize.ui
%_datadir/nautilus-image-converter/nautilus-image-rotate.ui

%changelog
* Thu Jan 05 2023 Roman Alifanov <ximper@altlinux.org> 0.4.0-alt1
- changed upstream
- updated to 0.4.0

* Tue Jun 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- upstream snapshot

* Thu Jul 02 2009 Alexey Rusakov <ktirf@altlinux.org> 0.3.0-alt4
- Make ImageMagick dependency even more specific (Requires:
  /usr/bin/convert, since it is literally the thing that gets called).
  (Closes ALT Bug #20641).

* Tue Jun 30 2009 Alexey Rusakov <ktirf@altlinux.org> 0.3.0-alt3
- Replace dependency on ImageMagick with ImageMagick-tools
  (closes ALT Bug 20641).

* Sat Sep 13 2008 Alexey Rusakov <ktirf@altlinux.org> 0.3.0-alt2
- Fixed a blunder in the specfile.
- Added a patch that fixes building with 'warnings as errors' option set.

* Wed May 14 2008 Alexey Rusakov <ktirf@altlinux.org> 0.3.0-alt1
- New version (0.3.0).

* Thu Dec 27 2007 Alexey Rusakov <ktirf@altlinux.org> 0.2.1-alt1
- New version (0.2.1).

* Mon Sep 03 2007 Alexey Rusakov <ktirf@altlinux.org> 0.0.9-alt1
- Initial Sisyphus package

