Name: xfce4-terminal
Version: 1.1.3
Release: alt3

Summary: Terminal emulator application for Xfce
Summary (ru_RU.UTF-8): Эмулятор терминала для Xfce
License: GPLv2+
Group: Terminals
Url: https://docs.xfce.org/apps/terminal/start
Packager: Xfce Team <xfce@packages.altlinux.org>
Vcs: https://gitlab.xfce.org/apps/xfce4-terminal.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%if_xfce4_wayland_support
%def_enable wayland
%else
%def_disable wayland
%endif

BuildRequires(pre): rpm-build-xfce4 >= 0.3.0 xfce4-dev-tools >= 4.18.1
BuildRequires: libxfconf-devel >= 4.16 libxfce4ui-gtk3-devel >= 4.17.5
BuildRequires: libpcre2-devel
BuildRequires: docbook-dtds docbook-style-xsl intltool libvte3-devel
%{?_enable_wayland:Buildrequires: libgtk-layer-shell-devel}
BuildRequires: xsltproc

Requires: xfce4-common

Obsoletes: Terminal < %version
Provides: Terminal = %version-%release

Provides: x-terminal-emulator

%define _unpackaged_files_terminate_build 1

%description
This is the xfce4-terminal emulator application. xfce4-terminal is
a lightweight and easy to use terminal emulator for X windowing system
with some new ideas and features that makes it unique among X terminal
emulators.

%description -l ru_RU.UTF-8
xfce4-terminal - легкий и удобный эмулятор терминала для Xfce.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-x11 \
	%{subst_enable wayland} \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

mkdir -p %buildroot%_altdir
cat << __EOF__ > %buildroot%_altdir/%name
%_bindir/x-terminal-emulator	%_bindir/%name	42
__EOF__

%files -f %name.lang
%doc README.md NEWS THANKS
%_bindir/*
%_altdir/%name
%_man1dir/*
%_datadir/xfce4/terminal
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*

%changelog
* Fri Sep 27 2024 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt3
- Enabled wayland support in the Sisyphus only.

* Fri May 31 2024 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt2
- Explicitly enabled wayland support.

* Fri Mar 01 2024 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt1
- Updated to 1.1.3.

* Mon Feb 05 2024 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt1
- Updated to 1.1.2.

* Wed Oct 18 2023 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt2
- Don't require rpm-build-xfce4 >= 0.2.0-alt1.
- Require xfce4-dev-tools >= 4.18.1.
- Dropped patch for xfce4-dev-tools-4.18.0.

* Mon Oct 16 2023 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1
- Don't use xfce4-dev-tools-4.19.
- Updated to 1.1.1.

* Wed Sep 27 2023 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt2
- Replaced %%xfce4_drop_gitvtag macro with %%xfce4_cleanup_version.
- Updated translations from upstream git.
- Fix F10 handling (patch from upstream):
  + app: Put GtkSettings:gtk-menu-bar-accel overwrite back in place.

* Tue Aug 22 2023 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Added x-terminal-emulator alternative (closes: #45565).
- Dropped workaround for Russian translation.
- Dropped obsoleted patch.
- Updated to 1.1.0.

* Fri May 12 2023 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt2
- Updated Russian translation.
- Patch from upstream:
    + Make strings translatable.

* Sun May 22 2022 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1
- Updated to 1.0.4.

* Fri May 13 2022 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1
- Updated to 1.0.3.

* Wed Apr 20 2022 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Thu Apr 14 2022 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Updated to 1.0.1.

* Mon Apr 04 2022 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Updated to 1.0.0.

* Fri Mar 04 2022 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Drop gtk-doc check.
- Cleanup BR.
- Updated to 0.9.2.

* Sat Dec 11 2021 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1
- Updated to 0.9.1.

* Sat Oct 16 2021 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- Updated to 0.9.0.

* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 0.8.10-alt1
- Updated Url tag.
- Updated Vcs tag.
- Updated to 0.8.10.

* Mon Mar 30 2020 Mikhail Efremov <sem@altlinux.org> 0.8.9.2-alt1
- Add Vcs tag.
- Drop obsoleted configure option.
- Updated to 0.8.9.2.

* Sat Dec 28 2019 Mikhail Efremov <sem@altlinux.org> 0.8.9.1-alt1
- Updated to 0.8.9.1.

* Fri Dec 27 2019 Mikhail Efremov <sem@altlinux.org> 0.8.9-alt1
- Don't use rpm-build-licenses.
- Updated to 0.8.9.

* Sat Sep 28 2019 Mikhail Efremov <sem@altlinux.org> 0.8.8-alt2
- Fix BR: Add libpcre2-devel.

* Wed Jul 03 2019 Mikhail Efremov <sem@altlinux.org> 0.8.8-alt1
- Updated to 0.8.8.

* Tue May 15 2018 Mikhail Efremov <sem@altlinux.org> 0.8.7.4-alt1
- Updated to 0.8.7.4.

* Thu Mar 29 2018 Mikhail Efremov <sem@altlinux.org> 0.8.7.3-alt1
- Updated to 0.8.7.3.

* Thu Mar 15 2018 Mikhail Efremov <sem@altlinux.org> 0.8.7.2-alt1
- Updated to 0.8.7.2.

* Mon Feb 26 2018 Mikhail Efremov <sem@altlinux.org> 0.8.7.1-alt1
- Updated to 0.8.7.1.

* Tue Aug 01 2017 Mikhail Efremov <sem@altlinux.org> 0.8.6-alt1
- Updated to 0.8.6.

* Tue May 16 2017 Mikhail Efremov <sem@altlinux.org> 0.8.5.1-alt1
- Updated to 0.8.5.1.

* Mon Feb 06 2017 Mikhail Efremov <sem@altlinux.org> 0.8.4-alt1
- Updated to 0.8.4.

* Mon Jan 16 2017 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1
- Updated to 0.8.3.

* Tue Nov 01 2016 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- Updated to 0.8.1.

* Mon Oct 17 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Wed Sep 07 2016 Mikhail Efremov <sem@altlinux.org> 0.6.92-alt1
- Updated to 0.6.92.

* Wed Aug 31 2016 Mikhail Efremov <sem@altlinux.org> 0.6.91-alt1
- Updated to 0.6.91.

* Fri Aug 05 2016 Mikhail Efremov <sem@altlinux.org> 0.6.90-alt1
- Enable debug (minimum level).
- Updated to 0.6.90 (closes: #31856, #32252).

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt2
- Rebuild with libxfce4util-4.12.

* Fri Dec 27 2013 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt1
- Drop obsoleted patches.
- Updated to 0.6.3.

* Thu Dec 26 2013 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt3
- Fix terminal session restore.
- Fix Xfce name (XFCE -> Xfce).

* Wed Oct 23 2013 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt2
- Fix up the encoding menu creation (closes: #29513).

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Updated to 0.6.2.

* Tue Apr 23 2013 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt2
- Updated translations from upstream git.
- Autotools updates from upstream git.

* Fri Jan 04 2013 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1
- Docs fix from upstream git.
- Updated translations from upstream git.
- Updated to 0.6.1.

* Fri Dec 28 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Drop misc-tab-position patch.
- Rename to xfce4-terminal.
- Updated to 0.6.0.

* Fri May 18 2012 Mikhail Efremov <sem@altlinux.org> 0.4.8-alt6
- Updated from upstream's git (e377a69286).
- Drop obsoleted documentation's hacks.

* Thu May 17 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4.8-alt5
- drop previous hack and just add misc-tab-position to Glade dialog

* Wed May 16 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4.8-alt4
- move tabs to the bottom of window

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.4.8-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Mon Jan 16 2012 Mikhail Efremov <sem@altlinux.org> 0.4.8-alt2
- Set charset utf8 for man pages.

* Wed Jun 22 2011 Mikhail Efremov <sem@altlinux.org> 0.4.8-alt1
- Updated to 0.4.8.

* Tue May 31 2011 Mikhail Efremov <sem@altlinux.org> 0.4.7-alt3
- Fix help URI.

* Mon Apr 18 2011 Mikhail Efremov <sem@altlinux.org> 0.4.7-alt2
- Convert Russian man page to KOI8-R.

* Sat Apr 16 2011 Mikhail Efremov <sem@altlinux.org> 0.4.7-alt1
- Drop obsoleted patches.
- Updated to 0.4.7.

* Wed Feb 16 2011 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1
- Patches from upstream:
    + Protect against NULL borders.
    + Avoid racing on the size-changed signal.
- workaround for rpm bug #25096.
- Updated to 0.4.6.

* Wed Jan 26 2011 Mikhail Efremov <sem@altlinux.org> 0.4.5-alt1
- Spec updated, tar.bz2 -> tar.
- Updated to 0.4.5.

* Thu Nov 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.4.0-alt3
- Fixed repocop warnings.

* Mon Aug 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.4.0-alt2
- Russian translation updated.

* Sat Aug 08 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.4.0-alt1
- Version update.

* Wed Jun 03 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.2.12-alt3
- Libvte soname changed. Requires rebuild.

* Wed May 06 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.2.12-alt2
- Updated russian translation

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.2.12-alt1
Xfce 4.6.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.6-alt0.1
- Xfce 4.4 release

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.5.8-alt1.1
- Rebuilt due to libdbus-1.so.2 -> libdbus-1.so.3 soname change.

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.2.5.8-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  0.2.5.6rc1-alt2
- Fix buildreq and cleanup spec 

* Sat Sep 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.2.5.6rc1-alt1
- Xfce 4.4rc1

* Wed Apr 19 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.4-alt1.1.1
- Rebuild with dbus-0.61-alt1 .

* Sat Jul 16 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.4-alt1.1
- rebuild with new libdbus-1.so.0 .

* Sun Mar 20 2005 Andrey Astafiev <andrei@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Sat Dec 25 2004 Andrey Astafiev <andrei@altlinux.ru> 0.2.2pre1-alt0.2
- First version of RPM package for Sisyphus.
