# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: wayland-logout
Summary: Simple program that sends SIGTERM to a wayland compositor
Version: 1.4
Release: alt1
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/soreau/wayland-logout
Source: %name-%version.tar

BuildRequires: meson >= 0.55

%description
Wayland Logout is an utility designed to kill any wayland compositor
that uses libwayland-server. It looks up the PID for the socket file
by checking the socket path environment variables and sends a SIGTERM
signal. This is useful as a way to logout of a wayland compositor,
as the name implies.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sat Oct 12 2024 Anton Midyukov <antohami@altlinux.org> 1.4-alt1
- initial build
