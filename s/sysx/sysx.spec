%define _unpackaged_files_terminate_build 1

Name: sysx
Version: 1.0.0
Release: alt1

Summary: A simple commandline tool for running rommands as systemd services
License: MIT
Group: System/Configuration/Other
Url: https://github.com/krau/sysx
Vcs: https://github.com/krau/sysx

Source: %name-%version.tar

BuildRequires: gcc-c++

%description
sysx is a lightweight command-line tool written in C that simplifies running
commands as systemd services on Linux. It automatically creates a systemd
service file for any command you want to run in the background and manages the
service using systemctl.

%prep
%setup

%build
%make

%install
install -Dm 0755 sysx %buildroot%_bindir/sysx

%files
%_bindir/sysx

%changelog
* Wed Aug 26 2026 Pavel Petrykin <silverducks@altlinux.org> 1.0.0-alt1
- Initial build for Alt Linux.
