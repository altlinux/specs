%define _unpackaged_files_terminate_build 1

%def_with check

Name: unfold
Version: 1.0.2
Release: alt1

Summary: Archive Manager for Linux Desktops
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/xapp-project/unfold

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): meson

BuildRequires: rpm-build-python3

Requires: python3-module-pygobject3
Requires: python3(cairo)
Requires: xapp-symbolic-icons
Requires: /usr/bin/7z

%description
%summary.

Create, browse and extract archives: zip, 7z, tar and its compressed
variants, rar and more, including password protected ones.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%_bindir/unfold
%_desktopdir/org.x.unfold.desktop
%python3_sitelibdir_noarch/unfold
%_iconsdir/hicolor/scalable/apps/unfold.svg
%_datadir/nemo/actions/unfold-compress-visible
%_datadir/nemo/actions/unfold-compress.nemo_action
%_datadir/nemo/actions/unfold-extract-here.nemo_action
%_datadir/nemo/actions/unfold-extract-to.nemo_action
%dir %_datadir/unfold
%_datadir/unfold/unfold.svg

%changelog
* Sun Oct 18 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
