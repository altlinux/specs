%define _unpackaged_files_terminate_build 1

Name: suru-icon-theme
Version: 2026.03.0
Release: alt1

Summary: Suru Icon Theme for Lomiri Operating Environment
License: CC-BY-SA-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/suru-icon-theme

Source: %name-%version.tar

BuildArch: noarch

%description
Lomiri Operating Environment is a convergent work shell designed
for use cases on phone, tablet or desktop devices.

This package contains Lomiri's Suru icon theme.

%prep
%setup

%build
# nothing to build here

%install

mkdir -pv %buildroot%_iconsdir
cp -aprv suru %buildroot%_iconsdir/

%files
%doc AUTHORS ChangeLog COPYING NEWS
%dir %_iconsdir/suru
%_iconsdir/suru/*

%changelog
* Tue Mar 31 2026 Nikolay Strelkov <snk@altlinux.org> 2026.03.0-alt1
- New version 2026.03.0.

* Thu Jul 17 2025 Nikolay Strelkov <snk@altlinux.org> 2025.05.0-alt1
- Initial build for Sisyphus
