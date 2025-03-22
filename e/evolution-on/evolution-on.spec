%define _unpackaged_files_terminate_build 1

Name: evolution-on
Version: 3.24.2
Release: alt2

Summary: Tray plugin for the GNOME Evolution email client
License: GPL-2.0
Group: Networking/Mail
Url: https://github.com/acidrain42/evolution-on

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: gnome-common
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: evolution-devel

Requires: evolution

%description
Plugin which allow Evolution to be hidden as tray icon, so one could
receive notification while main Evolution window is hidden.

%prep
%setup
%patch -p1
sed -i '/AM_GCONF_SOURCE_2/d' configure.ac
NOCONFIGURE=1 ./autogen.sh

%build
CFLAGS="%{optflags} -Wno-implicit-function-declaration -Wno-unused-function"
%configure
%make

%install
%makeinstall_std

rm -vf %buildroot/%_libdir/evolution/plugins/*.la

%check
%make_build check

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/evolution/plugins/*
%_datadir/GConf/gsettings/%{name}.convert
%_datadir/glib-2.0/schemas/org.gnome.evolution.plugin.evolution-on.gschema.xml

%changelog
* Sat Mar 22 2025 Nikolay Strelkov <snk@altlinux.org> 3.24.2-alt2
- Fixed FTBFS

* Sun Mar 02 2025 Nikolay Strelkov <snk@altlinux.org> 3.24.2-alt1
- Initial build for Sisyphus
