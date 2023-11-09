%define _unpackaged_files_terminate_build 1

Name: lisgd
Version: 0.3.7
Release: alt1

Summary: Libinput synthetic gesture daemon
License: MIT
Url: https://git.sr.ht/~mil/lisgd
Group: Graphical desktop/Other

Source: %name-%version.tar

BuildRequires: libwayland-client-devel
BuildRequires: libX11-devel libinput-devel

%description
Lisgd (libinput synthetic gesture daemon) lets you bind gestures based on
libinput touch events to run specific commands to execute.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/%{name}*
%_man1dir/%{name}*

%changelog
* Sun Oct 08 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus
