Name: mousepad
Version: 0.6.0
Release: alt1

Summary: Mousepad - A simple text editor for Xfce
Summary (ru_RU.UTF-8): Простой текстовый редактор для Xfce
License: GPLv2+
Group: Editors
Url: https://docs.xfce.org/apps/mousepad/start
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/apps/mousepad.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools >= 4.14.0
BuildRequires: libgtk+3-devel intltool libgtksourceview4-devel
# For gspell plugin
BuildRequires: libgspell-devel
# For shortcuts plugin
BuildRequires: libxfce4ui-gtk3-devel

Obsoletes: xfce-mousepad < %version
Provides: xfce-mousepad = %version-%release

%define _unpackaged_files_terminate_build 1

%description
Mousepad is a text editor for Xfce based on Leafpad. The initial reason
for Mousepad was to provide printing support, which would have been
difficult for Leafpad for various reasons.

%description -l ru_RU.UTF-8
Mousepad - простой текстовый редактор для Xfce основанный на Leafpad.
Одной из причин разработки нового редактора было предоставление
возможности печати, что было сложно реализуемо для редактора Leafpad
по некоторым причинам.

%prep
%setup
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag mousepad_version_tag configure.ac.in

%build
%xfce4reconf
# Don't explicitly enable/disable shortcuts plugin:
# we are relly on libxfce4ui version check, so
# it will be automatically enabled with libxfce4ui-gtk3 >= 4.17.5
# (Sisyphus) and disabled otherwise (p10).
%configure \
	--enable-maintainer-mode \
	--enable-gtksourceview4 \
	--enable-plugin-gspell \
	--disable-plugin-test \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang mousepad

%files -f mousepad.lang
%doc NEWS README.md
%_bindir/*
%_libdir/*.so
%_libdir/*.so.*
%_libdir/%name/
%_datadir/polkit-1/actions/*.policy
%_datadir/glib-2.0/schemas/*.gschema.xml
%_datadir/metainfo/*.xml
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*

%exclude %_libdir/%name/plugins/*.la

%changelog
* Thu Feb 09 2023 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Remove 'menu' and 'button' toolbar icon sizes (closes: #42387).
- Updated to 0.6.0.

* Mon Jul 11 2022 Mikhail Efremov <sem@altlinux.org> 0.5.10-alt1
- Updated to 0.5.10.

* Mon Apr 04 2022 Mikhail Efremov <sem@altlinux.org> 0.5.9-alt1
- Added libxfce4ui-gtk3-devel to BR.
- Updated to 0.5.9.

* Fri Nov 26 2021 Mikhail Efremov <sem@altlinux.org> 0.5.8-alt1
- Updated to 0.5.8.

* Thu Sep 23 2021 Mikhail Efremov <sem@altlinux.org> 0.5.7-alt1
- Updated to 0.5.7.

* Mon Aug 02 2021 Mikhail Efremov <sem@altlinux.org> 0.5.6-alt1
- Explicitly disabled test plugin.
- Updated to 0.5.6.

* Wed May 12 2021 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt1
- Enabled gspell plugin.
- Dropped libxconf-devel from BR.
- Updated to 0.5.5.

* Tue Apr 06 2021 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1
- Built with libgtksourceview4.
- Updated to 0.5.4.

* Sun Feb 28 2021 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt1
- Updated to 0.5.3.

* Mon Feb 01 2021 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Updated to 0.5.1.

* Mon Nov 30 2020 Mikhail Efremov <sem@altlinux.org> 0.5-alt1
- Updated to 0.5.

* Fri Nov 20 2020 Mikhail Efremov <sem@altlinux.org> 0.4.90-alt1
- Dropped obsoleted configure option.
- Updated to 0.4.90.

* Sat Sep 12 2020 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt2.g03db74b
- Dropped exo-csource from BR.
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.
- Updated from upstream git.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- Updated to 0.4.2.

* Tue Aug 28 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt2
- Enable debug (minimum level).
- Update url.
- Use _unpackaged_files_terminate_build.
- Build with GTK+3.

* Mon Jun 04 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Updated to 0.4.1.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 0.4.0.

* Sat Jan 05 2013 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- From upstream git:
    + Set textdomain codeset to utf-8.
    + Fix desktop file.
    + Updated translations.
- Updated to 0.3.0.
- Renamed to mousepad.

* Wed Jun 09 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.99-alt2
- Fixed bug when the 'Undo' action works incorrectly with non-latin symbols.

* Sat May 22 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.99-alt1
- New development version.

* Mon May 17 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.16-alt2
- Added Debian patches for Mousepad.

* Mon May 17 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.16-alt1
- New version.

* Sat Nov 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.14-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for xfce-mousepad
  * postclean-05-filetriggers for spec file

* Sun Nov 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2.14-alt1
- Xfce 4.4.3 release

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 0.2.13-alt1
- Xfce 4.4.2 release
- rename package
* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.12-alt0.1
- Xfce 4.4 release

* Fri Nov 10 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.2.10-alt2
- strict build requires libgtk+2-devel

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  0.2.10-alt1
- First version of RPM package for Sisyphus.
