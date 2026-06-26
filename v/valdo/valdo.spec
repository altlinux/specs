%define _unpackaged_files_terminate_build 1

Name: valdo
Version: 2022.04.14
Release: alt1

Summary: Boilerplate Vala project creator.
License: LGPL-2.1
Group: Development/Tools
Url: https://github.com/vala-lang/valdo
Vcs: https://github.com/vala-lang/valdo

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(json-glib-1.0)

%description
A tool that allows to create a new Vala project from
a local repository of templates.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/valdo
%_datadir/valdo/

%changelog
* Fri Jun 26 2026 Pavel Mitrofanov <cobalt@altlinux.org> 2022.04.14-alt1
- Initial commit.
