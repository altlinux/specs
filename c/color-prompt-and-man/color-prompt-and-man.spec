Name:    color-prompt-and-man
Version: 1.2
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
install -Dm0755 %SOURCE1 %buildroot%_sysconfdir/bashrc.d/%name.sh

%files
%attr(0755,root,root) %_sysconfdir/bashrc.d/%name.sh

%changelog
* Sat Apr 01 2023 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Show user name for root too, change colors (ALT #45709) (thanks zerg@).

* Sun Jun 19 2016 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Move script to /etc/bashrc.d for use in any DE and shells

* Thu Jun 02 2016 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
