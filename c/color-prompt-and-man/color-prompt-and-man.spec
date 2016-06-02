Name:    color-prompt-and-man
Version: 1.0
Release: alt1

Summary: Colorize shell prompt and man page view
License: GPL
Group:   Graphics
URL:     http://altlinux.org
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source1:  %name.sh

%description
Colorize shell prompt and man page view.

%install
install -Dm0755 %SOURCE1 %buildroot%_sysconfdir/profile.d/%name.sh

%files
%_sysconfdir/profile.d/%name.sh

%changelog
* Thu Jun 02 2016 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
