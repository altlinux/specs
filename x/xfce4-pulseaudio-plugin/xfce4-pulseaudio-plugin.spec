Name: xfce4-pulseaudio-plugin
Version: 0.4.8
Release: alt2

Summary: A pulseaudio plugin for the Xfce panel
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-pulseaudio-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-pulseaudio-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%def_disable wnck
%def_enable libcanberra

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: libexo-gtk3-devel
BuildRequires: libxfconf-devel
BuildRequires: libpulseaudio-devel libnotify-devel
BuildRequires: libkeybinder3-devel
%{?_enable_wnck:BuildRequires: libwnck3-devel}
%{?_enable_libcanberra:BuildRequires: libcanberra-devel}
BuildRequires: intltool

Requires: xfce4-panel >= 4.11

%define _unpackaged_files_terminate_build 1

%description
A panel plugin for controlling PulseAudio mixer.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-keybinder \
	%{subst_enable wnck} \
	--disable-libxfce4windowing \
	%{subst_enable libcanberra} \
	--disable-silent-rules \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/*/*.*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Thu Oct 03 2024 Mikhail Efremov <sem@altlinux.org> 0.4.8-alt2
- Fixed build: added intltool to BR.

* Mon Oct 02 2023 Mikhail Efremov <sem@altlinux.org> 0.4.8-alt1
- Dropped %%xfce4_drop_gitvtag macro.
- Updated to 0.4.8.

* Thu Jun 01 2023 Mikhail Efremov <sem@altlinux.org> 0.4.7-alt1
- Updated to 0.4.7.

* Wed Mar 29 2023 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1
- Updated to 0.4.6.

* Fri Sep 16 2022 Mikhail Efremov <sem@altlinux.org> 0.4.5-alt1
- Enabled libcanberra support.
- Updated to 0.4.5.

* Sat Sep 03 2022 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1
- Updated Vcs tag.
- Updated to 0.4.4.

* Mon Mar 30 2020 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1
- Added libexo-gtk3-devel to BR.
- Updated url.
- Added Vcs tag.
- Don't use rpm-build-licenses.
- Dropped libdbus-glib-devel from BR.
- Dropped obsoleted patch.
- Updated to 0.4.3.

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- Updated to 0.4.2.

* Thu Aug 16 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt2
- Update url.
- Use dbus-glib CFLAGS.
- Add libdbus-glib-devel to BR.
- Rebuild with libxfconf-0.so.3.
- Fix debug level.

* Thu Apr 12 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Updated to 0.4.1.

* Tue Mar 20 2018 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Tue Feb 27 2018 Mikhail Efremov <sem@altlinux.org> 0.3.5-alt1
- Add knob for libwnck3 support.
- Updated to 0.3.5.

* Mon Nov 27 2017 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Mon Oct 30 2017 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.
- Disable silent rules.

* Fri Sep 29 2017 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Wed Sep 06 2017 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Mon Apr 24 2017 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Thu Apr 06 2017 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt3
- Enable keybinder support.

* Wed Mar 15 2017 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt2
- Fix menu translation.
- Use _unpackaged_files_terminate_build.
- Added translations from upstream git.

* Tue Oct 27 2015 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Thu May 14 2015 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Add libnotify-devel to BR.
- Updated to 0.2.3.

* Fri Mar 27 2015 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Thu Mar 19 2015 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Patches from upstream git:
  + Remove grab-broken.
  + Disconnect events and cleanup.
  + Removed grab_notify to avoid crashes.
- Initial build (closes: #30822).

