%define _unpackaged_files_terminate_build 1

Name:    qman
Version: 1.4.1
Release: alt1

Summary: A more modern man page viewer for our terminals
License: BSD-2-Clause
Group:   Documentation
Url:     https://github.com/plp13/qman

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: python3-module-cogapp
BuildRequires: cmake
BuildRequires: pkgconfig(cunit)
BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(inih)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(liblzma)

%description
Linux manual pages are lovely. They are concise, well-written, complete,
and downright useful. However, the standard way of accessing them from
the command-line hasn't changed since the early days.

Qman aims to change that. It's a modern, full-featured manual page
viewer featuring hyperlinks, web browser like navigation, a table of
contents for each page, incremental search, on-line help, and more.
It also strives to be fast and tiny, so that it can be used everywhere.
For this reason, it's been written in plain C and has only minimal
dependencies.

%prep
%setup
sed -i "s|/screenshots/|screenshots/|g" README.md

%build
%meson
%meson_build

%install
%meson_install

rm -vfr %{buildroot}%_datadir/doc/qman

%files
%doc README.md PACKAGING.md TESTING.md screenshots config
%_bindir/*
%_man1dir/*
%dir %_sysconfdir/xdg/%name
%_sysconfdir/xdg/%name/*

%changelog
* Sat Apr 12 2025 Nikolay Strelkov <snk@altlinux.org> 1.4.1-alt1
- New version 1.4.1.

* Wed Feb 26 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.1-alt2
- Added XZ-support from devel-branch (commit hash 2a23f6c)

* Sun Feb 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
