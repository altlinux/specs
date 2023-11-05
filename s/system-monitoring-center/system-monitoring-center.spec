Name:     system-monitoring-center 
Version:  2.26.0
Release:  alt1

Summary:  Multi-featured system monitor
License:  GPLv3+
Group:    Monitoring
Url:      https://github.com/hakandundar34coding/system-monitoring-center

BuildArch: noarch

# Source-url: https://github.com/hakandundar34coding/system-monitoring-center/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: gtk4-update-icon-cache

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_datadir/%{name}*
%_datadir/appdata/io.*.appdata.xml
%_iconsdir/*/*/*/*.svg
%_man1dir/*
%_desktopdir/*

%changelog
* Sat Nov 04 2023 Roman Alifanov <ximper@altlinux.org> 2.26.0-alt1
- new version 2.26.0 (with rpmrb script)
- added rpm-build-gir to pre req for more correct dependencies

* Sun Oct 15 2023 Roman Alifanov <ximper@altlinux.org> 2.25.1-alt1
- new version 2.25.1 (gtk4 ver) (ALT bug 47606)
- move to tarball
- remove uid500 patch (not relevant for sisyphus)

* Sat Aug 05 2023 Roman Alifanov <ximper@altlinux.org> 1.43.10-alt1
- new version 1.43.10 (with rpmrb script)

* Thu Jun 29 2023 Roman Alifanov <ximper@altlinux.org> 1.43.6-alt1
- new version 1.43.6 (with rpmrb script)
- fix typos in .desktop file (ALT bug 46167)
- fix uid (ALT bug 46164)

* Mon May 01 2023 Roman Alifanov <ximper@altlinux.org> 1.43.2-alt1
- Initial build for Sisyphus
