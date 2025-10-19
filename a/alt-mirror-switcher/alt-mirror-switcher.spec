Name: alt-mirror-switcher
Version: 0.1
Release: alt1

Summary: Simple local mirror switcher for ALT

License: GPLv2+
Group: Other

Url: https://altlinux.space/aleksandershad/alt-mirror-switcher

BuildArch: noarch

Source: %name-%version.tar

%add_python3_path %_datadir/%name

BuildRequires(pre): rpm-build-python3

%description
%summary.

%prep
%setup

%build
%install
install -d %buildroot
%make_install \
    SHAREDIR=%buildroot%_datadir \
    PREFIXBIN=%buildroot%_bindir

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%doc README.md

%changelog
* Sun Oct 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1-alt1
- Initial build for ALT Linux.
