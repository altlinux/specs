%define _unpackaged_files_terminate_build 1

%define appname com.cassidyjames.dippi

Name: dippi
Version: 4.2.0
Release: alt1

Summary: Calculate display info like DPI and aspect ratio
License: GPL-3.0-or-later
Group: Other
Url: https://github.com/cassidyjames/dippi

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)

%description
Analyze any display. Input a few simple details and figure out the
aspect ratio, DPI, and other details of a particular display. Great for
deciding which laptop or external monitor to purchase, and if it would
be considered HiDPI.

Lots of handy features:

* Find out if a display is a good choice based on its size and resolution
* Get advice about different densities
* Learn the logical resolution
* Differentiate between laptops and desktop displays
* Stupid simple: all in a cute li'l window

Tells you if a display's density is:

* Very Low DPI,
* Fairly Low DPI,
* Ideal for LoDPI,
* Potentially Problematic,
* Ideal for HiDPI,
* Fairly High for HiDPI, or
* Too High DPI

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc AUTHORS COPYING dpi.md README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%_iconsdir/hicolor/symbolic/apps/%{appname}-symbolic.svg
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus
