%define oname altbooster

Name: plafon-altbooster
Version: 5.6.8
Release: alt1

Summary: GTK4 App Booster for ALT Linux
License: MIT
Group: System/Configuration/Other

Url: https://github.com/plafonlinux/altbooster
Vcs: https://github.com/plafonlinux/altbooster

Requires: pip
Requires: gnome-extensions-cli

BuildRequires(pre): rpm-build-python3

BuildArch: noarch
AutoReq: nopython3

Source: %name-%version.tar

Patch: config-5.6.8-alt-fixes.patch

%description
%summary. 

%prep
%setup
%patch -p0

%build
%install
install -d %buildroot
%make_install \
    SHAREDIR=%buildroot%_datadir \
    PREFIXBIN=%buildroot%_bindir

%files
%doc LICENSE *.md
%_datadir/%oname
%_datadir/applications/%oname.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_bindir/%%oname

%changelog
* Wed Mar 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.8-alt1
- 5.6.7 -> 5.6.8

* Fri Mar 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.7-alt2
- used system package gnome-extensions-cli

* Mon Mar 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.7-alt1
- 5.6.5 -> 5.6.7

* Thu Mar 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.5-alt1
- 5.6.4 -> 5.6.5

* Wed Mar 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.4-alt1
- 5.6.3 -> 5.6.4

* Wed Mar 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.3-alt2
- added needs requaries
- disabled update check

* Tue Mar 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.3-alt1
- Initial build for ALT Linux.

