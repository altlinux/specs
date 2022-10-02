%define effect_name foldpopups

Name: kde5-plasma-%effect_name
Version: 1.0
Release: alt1
Summary: Plasma5 kwin popups effect
License: GPL-3
Group: Graphical desktop/KDE
Url: https://github.com/kde-yyds/kwin4_effects_foldpopups
Source: %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%_datadir/kf5/kwin/effects
cp -pr kwin4_effects_%effect_name %buildroot%_datadir/kf5/kwin/effects

%files
%_datadir/kf5/kwin/effects/kwin4_effects_%effect_name
%doc LICENSE

%changelog
* Sun Oct 02 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.0-alt1
- Initial build for ALT
