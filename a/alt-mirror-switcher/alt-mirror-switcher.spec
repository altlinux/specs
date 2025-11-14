Name: alt-mirror-switcher
Version: 0.4.0
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
* Fri Nov 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.0-alt1
- 0.3.1 -> 0.4.0 (ALT #56850)

* Sat Nov 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1

* Wed Oct 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.0-alt1
- 0.2.1 -> 0.3.0:
  + add: labels and protocols
  + change for branch [p1*

* Wed Oct 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.1-alt1
- 0.2 -> 0.2.1

* Mon Oct 20 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2-alt1
- 0.1 -> 0.2

* Sun Oct 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1-alt1
- Initial build for ALT Linux.
