Name:     kde5-profile
Version:  1.2
Release:  alt1

Summary:  Profile for run KDE5 apps and show in menu in any other DE
License:  GPL
Group:    Other
Url:      http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

Requires: kf5-kinit

BuildArch: noarch

%description
%summary

%prep
%setup

%install
install -Dm 0755 kde5.sh %buildroot%_sysconfdir/profile.d/kde5.sh

%files
%_sysconfdir/profile.d/kde5.sh

%changelog
* Fri Dec 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Do not override completely XDG_DATA_DIRS.

* Tue Dec 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Require kf5-kinit.

* Thu Oct 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
