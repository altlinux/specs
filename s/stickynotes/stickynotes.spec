%define _unpackaged_files_terminate_build 1

Name: stickynotes
Version: 1.1
Release: alt1

Summary: Program that simulates the Sticky Notes for the MATE Desktop
License: GPL-2.0
Group: Graphical desktop/MATE
Url: https://github.com/vlastavesely/stickynotes

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtksourceview-3.0)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: rpm-build-python3

%description
This is a program that simulates the Sticky Notes for the Mate Desktop
Environment. From the user's perspective, it works the same way as the 
MATE applet: it allows you to create, view, and maintain sticky notes on your desktop. However, under the hood, there are some changes:

- independent on MATE Desktop;
- does not resize the notes when the text is too long (forces scrolling
  instead);
- highlights selected text properly;
- has ability to perform some basic synchronisation (using GSettings).

%prep
%setup
%patch -p1

%build
./autogen.sh
%configure \
            --prefix=%buildroot/%_prefix \
            --bindir=%buildroot/%_bindir \
            --mandir=%buildroot/%_mandir
%make_build

%install
%makeinstall_std

%files
%doc COPYING README
%_bindir/*
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/*/apps/*
%_man1dir/*
%_datadir/glib-2.0/schemas/*.gschema.xml

%changelog
* Sat Mar 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.1-alt1
- Initial build for Sisyphus
