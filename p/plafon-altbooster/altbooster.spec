%define oname altbooster

Name: plafon-altbooster
Version: 5.6.9
Release: alt4

Summary: GTK4 App Booster for ALT Linux
License: MIT
Group: System/Configuration/Other

Url: https://altlinux.space/plafonlinux/altbooster
Vcs: https://altlinux.space/plafonlinux/altbooster

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
    
#https://bugzilla.altlinux.org/59387
install -d %buildroot%_datadir/icons/hicolor/scalable/apps
install -d %buildroot%_datadir/icons/hicolor/scalable/devices
install -d %buildroot%_datadir/icons/hicolor/symbolic/devices
cp -p -r icons/hicolor/scalable icons/hicolor/symbolic %buildroot%_datadir/icons/hicolor/

%files
%doc LICENSE *.md
%_datadir/%oname
%_datadir/applications/%oname.desktop
%_iconsdir/hicolor/*/*/*.svg
%_bindir/%%oname

%changelog
* Thu Jun 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.9-alt4
- changed url && vcs

* Tue Jun 16 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.9-alt3
- fixed: load icons (ALT #59387)

* Wed May 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.9-alt2
- updated to git.aada969bcb

* Tue Mar 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.9-alt1
- 5.6.8 -> 5.6.9

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

