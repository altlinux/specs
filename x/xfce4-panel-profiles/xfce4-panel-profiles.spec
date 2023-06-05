Name: xfce4-panel-profiles
Version: 1.0.14
Release: alt1

Summary: A simple application to manage Xfce panel layouts
License: GPL-3.0+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/apps/xfce4-panel-profiles/start

Vcs: https://gitlab.xfce.org/apps/xfce4-panel-profiles.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>
BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: intltool
%add_python3_path %_datadir/%name

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
Xfce4 Panel Profiles (xfce4-panel-profiles, formerly known as xfpanel-switch)
is a simple application to manage Xfce panel layouts.
With the modular Xfce Panel, a multitude of panel layouts can be
created. This tool makes it possible to backup, restore, import, and
export these panel layouts.

%prep
%setup
%patch -p1

%build
# It is not autotools configure
./configure \
	--prefix=%_prefix \
	--python=python3
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc %_defaultdocdir/%name
%_bindir/%name
%_datadir/%name/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.appdata.xml
%_man1dir/%name.*

%changelog
* Mon Jun 05 2023 Mikhail Efremov <sem@altlinux.org> 1.0.14-alt1
- Dropped Simply Linux 9 profile.
- Added Simply Linux 10 profile.
- Updated to 1.0.14.

* Wed Feb 24 2021 Mikhail Efremov <sem@altlinux.org> 1.0.13-alt1
- Dropped workaround for libxfce4ui < 4.15.7.
- Updated to 1.0.13.

* Tue Dec 29 2020 Mikhail Efremov <sem@altlinux.org> 1.0.12-alt1
- Workaround for libxfce4ui < 4.15.7.
- Don't try to use libxfce4ui-2.0.typelib.
- Updated Url tag.
- Updated Vcs tag.
- Updated to 1.0.12.

* Wed Jan 15 2020 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt1
- Added Vcs tag.
- Added Simply Linux 9 profile.
- Updated to 1.0.10.

* Tue Dec 03 2019 Mikhail Efremov <sem@altlinux.org> 1.0.9-alt2
- Don't use rpm-build-licenses.
- Fix requires: use rpm-build-gir.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 1.0.9-alt1
- Updated to 1.0.9.

* Mon Jun 24 2019 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt2
- Fix python3 requires (closes: #36942).

* Mon Aug 27 2018 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt1
- Initial build.
