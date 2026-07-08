Name: netsurf-buildsystem
Version: 1.10
Release: alt1

Summary: Makefiles shared by NetSurf projects
License: MIT
Group: Development/C

Url: https://www.netsurf-browser.org/

BuildArch: noarch

# https://download.netsurf-browser.org/libs/releases/
Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%install
install -d %buildroot%_prefix
make install PREFIX=%buildroot%_prefix

%files
%doc COPYING README
%_datadir/%name

%changelog
* Wed Jul 08 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.10-alt1
- Initial build for ALT Linux.

