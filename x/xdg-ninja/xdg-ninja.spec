%define _unpackaged_files_terminate_build 1

Name: xdg-ninja
Version: 0.2.0.2
Release: alt1

Summary: A shell script which checks your $HOME for unwanted files and directories.
License: MIT
Group: System/Configuration/Other

Url: https://github.com/b3nj5m1n/xdg-ninja
VCS: https://github.com/b3nj5m1n/xdg-ninja.git
Source: %name-%version.tar
BuildArch: noarch
Requires: jq

%description
The script is designed to provide change recommendations and does not make any
modifications to the system itself.
This program has optional runtime dependencies that can modify and improve the
visual output. The recommended dependency for best results is glow.

%prep
%setup

%install
%makeinstall_std PREFIX=%_prefix
rm -rf %{buildroot}%{_defaultdocdir}

%files
%doc README.md
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_man1dir/*

%changelog
* Tue Aug 04 2026 Andrey Alekseev <parovoz@altlinux.org> 0.2.0.2-alt1
- initial build for ALT Sisyphus
