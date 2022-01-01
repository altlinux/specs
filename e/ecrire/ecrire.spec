%def_disable snapshot
%define _libexecdir %_prefix/libexec
%define beta %nil

Name: ecrire
Version: 0.2.0
Release: alt1

Summary: The Enlightenment Text Editor
Group: Graphical desktop/Enlightenment
License: GPL-3.0
Url: https://www.enlightenment.org/about-ecrire

%if_disabled snapshot
Source: http://download.enlightenment.org/rel/apps/%name/%name-%version%beta.tar.xz
%else
Vcs: https://git.enlightenment.org/apps/ecrire.git
Source: %name-%version%beta.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libelementary-devel >= 1.26.0

%description
Ecrire is a simple Notepad-like text editor for Enlightenment desktop.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/%name.*
%_iconsdir/hicolor/*/apps/%name.*
%doc AUTHORS README TODO

%changelog
* Sat Jan 01 2022 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus


