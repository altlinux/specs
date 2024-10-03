Name: xfce4-cpufreq-plugin
Version: 1.2.8
Release: alt2

Summary: Show CPU freqency and governours plugin for the Xfce panel
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-cpufreq-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>
Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-cpufreq-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel >= 4.16.0 libxfce4ui-gtk3-devel >= 4.16.0 libxfce4util-devel >= 4.17.2
BuildRequires: gcc-c++
BuildRequires: libX11-devel libgtk+3-devel
BuildRequires: intltool

Requires: xfce4-panel >= 4.17

%define _unpackaged_files_terminate_build 1

%description
xfce4-cpufreq-plugin shows the current CPU frequency and governor in the
panel, and the frequencies and governors and more information for all
CPUs in a separate overview. Note that at the moment, it does not permit
to change any of these CPU settings.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS NEWS
%_liconsdir/*.png
%_miconsdir/*.png
%_iconsdir/hicolor/*/apps/*.png
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Thu Oct 03 2024 Mikhail Efremov <sem@altlinux.org> 1.2.8-alt2
- Fixed build: added intltool to BR.

* Thu Nov 03 2022 Mikhail Efremov <sem@altlinux.org> 1.2.8-alt1
- Updated and fixed BR.
- Dropped obsoleted patch.
- Updated to 1.2.8.

* Wed Nov 02 2022 Mikhail Efremov <sem@altlinux.org> 1.2.7-alt2.ge6ad9d0
- Upstream git snapshot (fixes build).

* Wed Feb 02 2022 Mikhail Efremov <sem@altlinux.org> 1.2.7-alt1
- Updated to 1.2.7.

* Mon Jan 31 2022 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt1
- Fixed translations.
- Updated to 1.2.6.

* Wed Mar 03 2021 Mikhail Efremov <sem@altlinux.org> 1.2.5-alt1
- Updated to 1.2.5.

* Wed Feb 03 2021 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1
- Updated to 1.2.4.

* Tue Jan 12 2021 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt1
- Updated to 1.2.3.

* Thu Oct 15 2020 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Mon Sep 14 2020 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt2.gfc6f46b
- Fixed BR.
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.
- Upstream git snapshot.

* Mon Sep 24 2018 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1
- Explicitly enable debug (minimum level).
- Update url.
- Use _unpackaged_files_terminate_build.
- Updated to 1.2.1.

* Wed Apr 27 2016 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt1
- Updated to 1.1.3.

* Wed Jun 24 2015 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt1
- Updated to 1.1.2.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt2
- Rebuild with libxfce4util-4.12.

* Mon Dec 29 2014 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 1.1.1.

* Tue Sep 03 2013 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Updated description.
- Fix typo in panel-plugin/Makefile.am (from upstream).
- Updated to 1.1.0.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Rebuild with xfce4-panel-4.9.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.gz -> tar.
- Updated to 1.0.0.

* Wed Dec 26 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2-alt0svn3751
- new build from svn

* Tue Jan 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.0.1-alt1
- First build
