%define exID netspeedsimplified@prateekmedia.extension
%define nameU netspeedsimplified

Name: gnome-shell-extension-netspeedsimplified
Version: 43
Release: alt1

Summary: Net speed Simplified

BuildArch: noarch

License:  GPL-3.0 license
Group:  Graphical desktop/GNOME
Url: https://github.com/prateekmedia/netspeedsimplified
VCS: https://github.com/prateekmedia/netspeedsimplified

Source: %nameU-%version.tar

Requires: gnome-shell >= 47.0

%description
A Net Speed monitor With Loads of Customization.

%prep
%setup -n %nameU-%version

%build
%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -R schemas %buildroot%_datadir/gnome-shell/extensions/%exID/schemas
cp *.js %buildroot%_datadir/gnome-shell/extensions/%exID/
cp LICENSE %buildroot%_datadir/gnome-shell/extensions/%exID/LICENSE
cp metadata.json %buildroot%_datadir/gnome-shell/extensions/%exID/metadata.json
cp stylesheet.css %buildroot%_datadir/gnome-shell/extensions/%exID/stylesheet.css

%files
%_datadir/gnome-shell/extensions/%exID/*
%doc *.md LICENSE 

%changelog
* Sun Dec 01 2024 Aleksandr Shamaraev <shad@altlinux.org> 43-alt1
- Initial build for Sisyphus.
