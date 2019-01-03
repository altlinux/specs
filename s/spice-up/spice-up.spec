%def_enable snapshot
%define _name Spice-up
%define xdg_name com.github.philip-scott.spice-up

Name: spice-up
Version: 1.7.0
Release: alt1

Summary: Desktop presentation application
License: GPLv3
Group: Office
Url: https://github.com/Philip-Scott/%_name

%if_disabled snapshot
Source: https://github.com/Philip-Scott/Spice-up/archive/%version.tar.gz#/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildRequires: cmake gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib-devel
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite) >= 0.3
BuildRequires: pkgconfig(gtk+-3.0) >= 3.18.0
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libsoup-2.4)
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
%add_optflags -D_FILE_OFFSET_BITS=64
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
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/mime/packages/%xdg_name.mime.xml


%changelog
* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- updated to 1.7.0-4-g6c23e27

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt2
- rebuilt against libgranite.so.5

* Mon Feb 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Mon Feb 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sun Jan 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Wed Sep 20 2017 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- built for sisyphus (based on opensuse package by avvissu@yandex.by)
  + special thanks to aris@ for finishing the spec nicely

