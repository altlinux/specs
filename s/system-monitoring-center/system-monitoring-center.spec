Name:     system-monitoring-center 
Version:  1.43.6
Release:  alt1

Summary:  Multi-featured system monitor
License:  GPLv3+
Group:    Monitoring
Url:      https://github.com/hakandundar34coding/system-monitoring-center

BuildArch: noarch
Source: %name-%version.tar

Patch1: system-monitoring-center-1.43.6-fix-typos-alt.patch
Patch2: system-monitoring-center-1.43.6-uid500-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
%summary

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%_bindir/%name
%_datadir/%{name}*
%python3_sitelibdir/*.egg-info/
%_iconsdir/*/*/*/*.svg
%_man1dir/*
%_datadir/polkit-1/actions/io.github.hakandundar34coding.%name.policy
%_desktopdir/*

%changelog
* Thu Jun 29 2023 Roman Alifanov <ximper@altlinux.org> 1.43.6-alt1
- new version 1.43.6 (with rpmrb script)
- fix typos in .desktop file (ALT bug 46167)
- fix uid (ALT bug 46164)

* Mon May 01 2023 Roman Alifanov <ximper@altlinux.org> 1.43.2-alt1
- Initial build for Sisyphus
