%def_enable snapshot
%define _libexecdir %_prefix/libexec

Name: evisum
Version: 0.5.0
Release: alt1

Summary: The Enlightenment system and process monitor
Group: Graphical desktop/Enlightenment
License: ISC
Url: https://enlightenment.org

%if_disabled snapshot
Source: https://download.enlightenment.org/rel/apps/%name/%name-%version.tar.xz
%else
# VCS: https://git.enlightenment.org/apps/evisum.git
Source: %name-%version.tar
%endif

%define efl_ver 1.22

BuildRequires(pre): meson
BuildRequires: libelementary-devel >= %efl_ver

%description
System and process monitor for Enlightenment

%prep
%setup

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
%_iconsdir/hicolor/*/apps/*.png
%doc AUTHORS NEWS README

%changelog
* Tue Jul 07 2020 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus (v0.5.0-2-gd71b1a2)


