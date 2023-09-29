Name:           gigolo
Version:        0.5.3
Release:        alt1
Summary:        frontend to manage connections to remote filesystems using GIO/GVfs
Group:          File tools
License:        GPL-2.0-only
URL:            https://www.uvena.de/gigolo/
Packager: Xfce Team <xfce@packages.altlinux.org>
Vcs:        https://gitlab.xfce.org/apps/gigolo.git
Source:     %name-%version.tar
Patch:		%name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools >= 4.15.0
BuildRequires: libgtk+3-devel libgio-devel libX11-devel

%define _unpackaged_files_terminate_build 1

%description
Gigolo is a frontend to easily manage connections to remote filesystems
using GIO/GVfs. It allows you to quickly connect/mount a remote
filesystem and manage bookmarks of such.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc %_defaultdocdir/%name
%_bindir/%name
%_datadir/applications/gigolo.desktop
%_iconsdir/hicolor/*/apps/*
%_man1dir/%name.*

%changelog
* Fri Sep 29 2023 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt1
- Updated to 0.5.3.

* Thu Mar 25 2021 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Dropped obsoleted patch.
- Updated to 0.5.2.

* Sat Sep 12 2020 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt2.g6b50425
- Dropped exo-csource from BR.
- Updated Vcs tag.
- Updated from upstream git.

* Mon Mar 16 2020 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Added Vcs tag.
- Don't use rpm-build-licenses.
- Updated to 0.5.1.

* Tue Aug 13 2019 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- Updated to 0.5.0.

* Fri Mar 01 2019 Mikhail Efremov <sem@altlinux.org> 0.4.91-alt1
- Updated to 0.4.91.

* Mon Oct 29 2018 Mikhail Efremov <sem@altlinux.org> 0.4.90-alt1
- Explicitly enable debug (minimum level).
- Updated url.
- Updated to 0.4.90.

* Tue Nov 01 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- Fix icon.
- Spec updated.
- Updated to 0.4.2 (closes: #25308).

* Thu Jun 02 2011 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt1
- new version

* Wed Oct 21 2009 Mykola Grechukh <gns@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux
