Name:     sputnik-browser-preinstall
Version:  4.1.2537.0
Release:  alt2

Summary:  Preinstall packages and repository for install Sputnik Browser
License:  GPL
Group:    Other
Url:      http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: x86_64

Requires: alternatives
Requires: bash
Requires: ca-certificates
Requires: libnss
Requires: lsb-release
Requires: menu
Requires: rpm
Requires: service
Requires: vixie-cron
Requires: wget
Requires: xdg-utils

%description
This metapackage requires all needed packages for install Sputnik
Browser. Also this package adds apt repository with latest version of
Sputnik Browser for ALT.

You can install Sputnik Browser by command:

 apt-get update
 apt-get install sputnik-browser-stable

Check with sputnik-browser-stable-4.1.2537.0-1.

%install
mkdir -p %buildroot%_sysconfdir/apt/sources.list.d
echo "rpm http://browser-rpm.sputnik.ru/altlinux x86_64 classic" \
     > %buildroot%_sysconfdir/apt/sources.list.d/browser-sputnik.list

%files
%_sysconfdir/apt/sources.list.d/browser-sputnik.list

%changelog
* Mon Apr 15 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.2537.0-alt2
- Adapt for Sisyphus.

* Thu Apr 11 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.2537.0-alt0.M80C.1
- Backport to c8 branch.
- Provides menu and /usr/sbin/update-alternatives.

* Tue Apr 09 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.2537.0-alt1
- Initial build.
