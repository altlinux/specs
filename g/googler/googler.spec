%global _unpacked_files_terminate_build 1

Name:    googler
Version: 3.3
Release: alt1

Summary: Google Search, Google Site Search, Google News from the terminal
License: GPL-3.0
Group:   Networking/Other
URL:     https://github.com/jarun/googler

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%install
make disable-self-upgrade
make install PREFIX=%buildroot%_prefix

%files
%doc README.md
%_bindir/%name
%_man1dir/*
%_docdir/%name/*

%changelog
* Wed Aug 02 2017 Mikhail Gordeev <obirvalger@altlinux.org> 3.3-alt1
- Initial build for Sisyphus
