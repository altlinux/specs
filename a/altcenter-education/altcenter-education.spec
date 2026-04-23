Name:    altcenter-education
Version: 1.2
Release: alt1

Summary: Manage plugins and component list for Alt Center
License: GPL-3.0+
Group:   Other
Url:     http://altlinux.org

Source: %name-%version.tar

BuildArch: noarch

Requires: altcenter

%description
%summary

%prep
%setup

%install
install -Dm 0644 skip-plugins %buildroot%_sysconfdir/altcenter/skip-plugins
install -Dm 0644 list-components %buildroot%_sysconfdir/altcenter/list-components

%files
%config(noreplace) %_sysconfdir/altcenter/*

%changelog
* Thu Apr 23 2026 Ilya Muhamadeev <nicourced@altlinux.org> 1.2-alt1
- Add scan utilities.

* Thu Feb 26 2026 Ilya Muhamadeev <nicourced@altlinux.org> 1.1-alt1
- Remove yandex from list-components.

* Sun Jun 08 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
