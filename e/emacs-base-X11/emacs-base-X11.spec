Name: emacs-base-X11
Version: 0.0.1
Release: alt1

Group: Editors
Summary: Common GNU Emacs icons and other X11 stuff
License: GPLv2+
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>
BuildArch: noarch
Conflicts: viy-desktop < 0.17

Source: %{name}-%{version}.tar

%description
This package contains GNU Emacs icon 'emacs' and possibly other X11 stuff
that does not contain GNU Emacs version in its name for use in WM toolbars, etc.

%prep
%setup -q

%install
mkdir -p %buildroot%_iconsdir/
cp -a icons/hicolor %buildroot%_iconsdir/

%files
%_iconsdir/hicolor/*/apps/emacs.*

%changelog
* Sat Sep 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus

