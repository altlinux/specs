%define ver_major 0.3

Name: nautilus-image-converter
Version: %ver_major.1
Release: alt1

Summary: An extension for Nautilus to rotate and resize images
Group: Graphical desktop/GNOME
License: %gpl2plus
Url: http://www.bitron.ch/software/%name.php

Source: %name-%version.tar

Requires: /usr/bin/convert

BuildPreReq: rpm-build-licenses rpm-build-gnome gnome-common

# From configure.ac
BuildRequires: intltool >= 0.35.0
BuildRequires: libnautilus-devel >= 3.0.0
BuildRequires: libgio-devel >= 2.28.0
BuildRequires: libgtk+3-devel >= 3.0.0

%description
This package contains a Nautilus extension makes it easy to open terminal
in current location.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang %name

%files -f %name.lang
%doc AUTHORS README NEWS
%nautilus_extdir/lib%name.so
%dir %_datadir/%name
%_datadir/%name/*.ui

%exclude %nautilus_extdir/*.la

%changelog
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

