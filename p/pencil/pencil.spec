# SPEC file for Pencil
#

Name:     pencil
Version:  2.0.5
Release:  alt2

Summary: GUI prototyping tool

Group:    Development/Tools
License:  %gpl2only
URL:      http://pencil.evolus.vn
#URL:     http://code.google.com/p/evoluspencil/
Packager: Nikolay Fetisov <naf@altlinux.ru>

BuildArch: noarch

Source0: %name-%version.tar

Patch0: %name-2.0.4-alt-desktop.patch
Patch1: %name-2.0.4-alt-xulrunner_versions.patch
Patch2: %name-2.0.5-alt-xulrunner.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: desktop-file-utils

%description
Pencil is a GUI prototyping tool that can be used to create
mockups in popular desktop platforms.

Pencil provides various built-in shapes collection for drawing
different types of user interface ranging from desktop to
mobile platforms. The list of built-in collections includes
general-purpose shapes, flowchart elements, desktop/web UI
shapes, Android and iOS GUI shapes.

%prep
%setup
%patch0
%patch1
%patch2

mv COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build

%install
install -D -m 0644 ./%_desktopdir/%name.desktop %buildroot%_desktopdir/%name.desktop
install -D -m 0755 ./%_bindir/%name %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/
cp -a ./%_datadir/%name %buildroot%_datadir/


%files
%doc --no-dereference COPYING

%_bindir/%name
%_datadir/%name

%_desktopdir/%name.desktop

%changelog
* Tue Feb 02 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.5-alt2
- Removing xulrunner usage

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.5-alt1
- New version

* Sun May 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.4-alt1
- Initial build for ALT Linux Sisyphus
