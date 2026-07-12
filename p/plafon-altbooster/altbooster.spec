%define oname altbooster

Name: plafon-altbooster
Version: 5.8
Release: alt1

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

%description
%summary. 

%prep
%setup
subst 's|/usr/local/share|/usr/share|' src/ui/help_altbooster.py
subst 's|/usr/local/share|%buildroot/usr/share|' Makefile

%build
%install
install -d %buildroot
%make_install \
    SHAREDIR=%buildroot%_datadir \
    BINDIR=%buildroot%_bindir

%find_lang --all-name %name

%files -f %name.lang
%doc LICENSE *.md
%_datadir/%oname
%_datadir/applications/%oname.desktop
%_iconsdir/hicolor/*/*/*.svg
%_bindir/%%oname
%_datadir/help/C/%oname

%changelog
* Sun Jul 12 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.8-alt1
- 5.7 -> 5.8 (closes: #59691, #59690, #59688, #59686, #59681, #59678, #59671)
- drop patchs

* Wed Jul 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.7-alt5
- fixed show welcome page (ALT #59687)

* Tue Jun 30 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.7-alt4
- fixed: apply mount points (ALT #59683)

* Tue Jun 30 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.7-alt3
- added help information (ALT #59679)

* Tue Jun 30 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.7-alt2
- excluded HEAnet (ftp.heanet.ie) mirror (ALT #59673)

* Fri Jun 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.7-alt1
- 5.6.9 -> 5.7

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

