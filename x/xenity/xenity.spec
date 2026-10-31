%define _unpackaged_files_terminate_build 1

Name: xenity
Version: 3.44.6
Release: alt1

Summary: Drop-in replacement for Zenity 3.44 (GTK3)
License: LGPL-2.1-or-later
Group: Graphical desktop/Other
Url: https://github.com/xapp-project/xenity

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc README.md
%_bindir/xenity
%_man1dir/xenity.1.*
%dir %_datadir/xenity
%_datadir/xenity/*.png
%_datadir/xenity/*.ui

%changelog
* Sat Oct 31 2026 Nikolay Strelkov <snk@altlinux.org> 3.44.6-alt1
- Initial build for Sisyphus
