%define _unpackaged_files_terminate_build 1
%def_enable check

Name: tau-helium
Version: 1.8.24
Release: alt1

Summary: tauOS GTK/GNOME Shell Themes
License: LGPL-2.1
Group: Development/GNOME and GTK+

Url: https://github.com/tau-OS/libhelium
Vcs: https://github.com/tau-OS/libhelium
Source: %name-%version.tar

BuildArch: noarch

Patch0: tau-helium-1.8.24-alt-gtk-3.0_func_work_with_sassc.patch
Patch1: tau-helium-1.8.24-alt-gtk-4.0_func_work_with_sassc.patch
Patch2: tau-helium-1.8.24-alt-gtk-4.0_meson_build_work_with_sassc.patch
Patch3: tau-helium-1.8.24-alt-meson_build_work_with_sassc.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: sassc
BuildRequires: fdupes
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

%description
A set of GTK/GNOME Shell Themes for tauOS

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%meson
%meson_build

%install
%meson_install
fdupes -s %buildroot%_datadir/themes/

%check
%meson_test

%files
%_datadir/themes/Helium/*
%_datadir/themes/Helium-dark/*
%doc README.md

%changelog
* Tue Nov 21 2024 Semen Fomchenkov <armatik@altlinux.org> 1.8.24-alt1
- Initial build.
