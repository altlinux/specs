Name: altocation
Version: 1.0
Release: alt1

Summary: Generator of vacation applications.

License: MIT
Group: Other
Url: https://en.altlinux.org/Main_Page

Packager: Nikita Ermakov <arei@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%description
%summary

%prep
%setup

%install
install -Dm755 -t %buildroot/%_bindir %name.sh

%files
%_bindir/*

%changelog
* Fri Aug 30 2019 Nikita Ermakov <arei@altlinux.org> 1.0-alt1
- Initial build for ALT Linux Sisyphus.
