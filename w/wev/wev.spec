%define _unpackaged_files_terminate_build 1

Name: wev
Version: 1.1.0
Release: alt1

Summary: Debug wayland events
License: MIT
Group: Development/Debug

Url: https://git.sr.ht/~sircmpwn/wev
Vcs: https://git.sr.ht/~sircmpwn/wev
Source: %name-%version.tar

BuildRequires: scdoc
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)

%description
This is a tool for debugging events on a Wayland window, analagous to the X11
tool xev.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%_bindir/%name
%_man1dir/%name.1.*
%doc README.md

%changelog
* Mon Aug 25 2025 Alexander Davydzik <paladindev@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Apr 03 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0.0-alt1
- initial build
