Name: elementary-wallpapers
Version: 0.1.4
Release: alt1.r40

Summary: elementary OS Wallpapers
Group: Graphical desktop/Other
License: See copyright inside package
Url: https://code.launchpad.net/~elementary-design/elementaryos/elementary-wallpapers

# https://code.launchpad.net/~elementary-design/elementaryos/elementary-wallpapers
Source0: %name.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

%description
A special selection of wallpapers that ships with elementary OS.

%prep
%setup -q -n %name

%build

%install
mkdir -p %buildroot%_datadir/backgrounds/

install -p -m0644 *.jpg *.xml elementaryos-default %buildroot%_datadir/backgrounds/

%files
%doc debian/copyright
%_datadir/backgrounds/*

%changelog
* Mon Nov 25 2013 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt1.r40
- 0.1.4-r40

