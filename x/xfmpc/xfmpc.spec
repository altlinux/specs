Name: xfmpc
Summary: MPD client written in GTK+ for Xfce
Version: 0.3.1
Release: alt1
License: GPL-2.0+
Url: https://docs.xfce.org/apps/xfmpc/start
Vcs: https://gitlab.xfce.org/apps/xfmpc.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Group: Graphical desktop/XFce

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4util-devel libxfce4ui-gtk3-devel
BuildRequires: libmpd-devel
BuildRequires: vala

Provides: xfce4-xfmpc = %version-%release
Obsoletes: xfce4-xfmpc < %version-%release

%define _unpackaged_files_terminate_build 1

%description
A graphical GTK+ MPD client focusing on low footprint.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--disable-silent-rules

# Disable parallel build for now
export NPROCS=1
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README.md NEWS COPYING AUTHORS
%_bindir/*
%_desktopdir/*.desktop
%_man1dir/xfmpc.1.*

%changelog
* Mon Apr 24 2023 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Added Vcs tag.
- Updated Url tag.
- Enabled build on aarch64.
- Updated to 0.3.1.

* Thu Nov 28 2019 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt2
- Don't use rpm-build-licenses.
- Fix types casting.

* Sat Jun 22 2019 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Tue Apr 09 2019 Mikhail Efremov <sem@altlinux.org> 0.2.90-alt2
- Fix BR: drop libxfcegui4-devel.

* Thu Feb 28 2019 Mikhail Efremov <sem@altlinux.org> 0.2.90-alt1
- Return to Sisyphus.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.7-alt1
- new version

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.6-alt1
- first build for Sisyphus

