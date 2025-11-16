%define _unpackaged_files_terminate_build 1

Name: crystal-remix-icon-theme
Version: 2.7
Release: alt1

Summary: A Crystal icon theme for modern Linux desktop environments
License: LGPL
Group: Graphics
Url: https://github.com/dangvd/crystal-remix-icon-theme

Source: %name-%version.tar

BuildArch: noarch

%description
Crystal Remix is a Crystal icon theme for modern Linux desktop
environments, created from KDE 3's Crystal Project and Crystal
Clear icon themes (mainly Crystal Project).

%prep
%setup

%build
# norhing to build here

%install
install -d -m 755 %buildroot%_iconsdir/crystal-remix
cp -av * %buildroot%_iconsdir/crystal-remix

rm -v %buildroot%_iconsdir/crystal-remix/README.md
rm -v %buildroot%_iconsdir/crystal-remix/crystal-remix-icon-theme.jpg
rm -v %buildroot%_iconsdir/crystal-remix/install.sh

%files
%doc crystal-remix-icon-theme.jpg README.md
%dir %_iconsdir/crystal-remix
%_iconsdir/crystal-remix/*

%changelog
* Sun Nov 16 2025 Nikolay Strelkov <snk@altlinux.org> 2.7-alt1
- Initial build for Sisyphus
