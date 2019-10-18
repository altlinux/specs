Name: polkit-efl
Version: 0.1.0
Release: alt1

Summary: EFL polkit authentication agent

License: GPLv3
Group: Graphical desktop/Enlightenment
Url: https://git.enlightenment.org/misc/polkit-efl.git

Packager: Paul Wolneykien <manowar@altlinux.org>

Source: %name-%version.tar

Requires: python3-module-psutil

BuildRequires(pre): rpm-build-xdg
BuildRequires: efl-libs-devel >= 1.10
BuildRequires: libelementary-devel >= 1.10
BuildRequires: python3-module-efl >= 1.10

BuildArch: noarch

%description
Polkit-EFL is a user desktop session authentication agent.

Install and leave it running in your desktop session.

The easiest way to do this is to add it to xdg autostart, a desktop file is
installed on your system for this purpose, use your DE's settings to enable it.

You may also launch it in a terminal.

%prep
%setup

%build
%python_build

%install
%python_build_install
%find_lang %name

%define _unpackaged_files_terminate_build 1

%files -f %name.lang
%doc README COPYING-ICONS
%_xdgconfigdir/autostart/%name-*.desktop
%_bindir/%name-*
%python_sitelibdir_noarch/polkit_efl-%version-*.egg-info
%_datadir/%name

%changelog
* Fri Oct 18 2019 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build of the version 0.1.0 for ALT.
