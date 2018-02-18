#
# spec file for package spice-up
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%define xdg_name com.github.philip-scott.spice-up

Name: spice-up
Version: 1.3.0
Release: alt1

Summary: Desktop presentation application
License: GPLv3
Group: Office

Url: https://github.com/Philip-Scott/Spice-up
Source: https://github.com/Philip-Scott/Spice-up/archive/%version.tar.gz#/Spice-up-%version.tar.gz

BuildRequires: cmake gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib-devel
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite) >= 0.3
BuildRequires: pkgconfig(gtk+-3.0) >= 3.18.0
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libevdev)
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: vala-tools vapi(granite)
BuildRequires: libgee0.8-gir libgee0.8-gir-devel

Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Requires: gsettings-desktop-schemas

%description
Spice-up is a desktop presentation application
based upon SpiceOfDesign's presentation concept.

%prep
%setup -n Spice-up-%version

%build
%cmake_insource -DGSETTINGS_COMPILE=OFF
%make_build

%install
%makeinstall_std
ln -s %xdg_name %buildroot%_bindir/%name

%find_lang --output=%name.lang %xdg_name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_bindir/%xdg_name
%_datadir/%xdg_name/
%_datadir/applications/*.%name.desktop
%_datadir/icons/hicolor/*/apps/*%name.??g
%_datadir/icons/hicolor/*/mimetypes/*spiceup.??g
%_datadir/glib-2.0/schemas/*.%name.gschema.xml
%_datadir/metainfo/*.%name.appdata.xml
%_datadir/mime/packages/*%name.mime.xml


%changelog
* Mon Feb 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sun Jan 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Wed Sep 20 2017 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- built for sisyphus (based on opensuse package by avvissu@yandex.by)
  + special thanks to aris@ for finishing the spec nicely

