Name: frog-protocols
Version: 0.01
Release: alt1

Summary: Faster moving Wayland protocols
License: MIT
Group: Development/Other
URL: https://github.com/misyltoad/frog-protocols
BuildArch: noarch

# This is a development package so add it for convention
Provides: %name-devel = %version-%release

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
%name contains Wayland protocol definitions for protocols
being developed in a more agile fashion to enable shipping
functionality to users more quickly. It is intended to
accelerate development of formal Wayland protocols.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.* LICENSE.*
%_datadir/pkgconfig/%name.pc
%_datadir/%name/

%changelog
* Wed Sep 25 2024 Anton Kurachenko <srebrov@altlinux.org> 0.01-alt1
- Initial build for Sisyphus.
