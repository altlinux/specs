Name:     system-monitoring-center 
Version:  1.43.2
Release:  alt1

Summary:  Multi-featured system monitor
License:  GPLv3+
Group:    Monitoring
Url:      https://github.com/hakandundar34coding/system-monitoring-center

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
%summary

%prep
%setup

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
* Mon May 01 2023 Roman Alifanov <ximper@altlinux.org> 1.43.2-alt1
- Initial build for Sisyphus
