Name:    document-templates
Version: 1.0
Release: alt1

Summary: Set of office documents templates 
License: GPL-3.0+
Group:   Other
Url:     http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

Conflicts: branding-alt-education-kde-settings <= 9.2-alt4

BuildArch: noarch

%description
Set of office documents templates suitable for KDE5.

%prep
%setup

%install
install -Dm0644 -t %buildroot%_datadir/templates templates/*

%files
%_datadir/templates

%changelog
* Thu Aug 05 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus.
