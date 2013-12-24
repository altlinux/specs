Version: 0.2.2
Release: alt1
Name: udev-discover

Summary: A tool for helping browsing the sysfs tree via udev
License: GPLv3+
Group: System/Configuration/Hardware
URL: https://github.com/fontanon/udev-discover

Source0: %name-%version.tar

Packager: Paul Wolneykien <manowar@altlinux.org>

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-pygobject-devel
BuildRequires: python-module-gudev
BuildRequires: libgtk+3-gir-devel

%description
A tool for helping browsing the sysfs tree via udev focused on being
helpfull for udev testers, coders, hackers and consumers.

%prep
%setup

%build
%python_build

%install
%python_install --prefix=%_usr
%find_lang udevdiscover

%files -f udevdiscover.lang
%doc AUTHORS README.rst TODO
%_bindir/*
%_sysconfdir/gconf/schemas/*.schemas
%python_sitelibdir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/devices/*.svg
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/scalable/devices/*.svg
%_pixmapsdir/*.svg
%_datadir/%name

%changelog
* Wed Dec 25 2013 Paul Wolneykien <manowar@altlinux.org> 0.2.2-alt1
- Freshed up to v0.2.2 with the help of cronbuild and update-source-functions.
