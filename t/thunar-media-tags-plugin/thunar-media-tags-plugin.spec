Name: thunar-media-tags-plugin
Version: 0.3.0
Release: alt1

Summary: Thunar media tag plugin
License: GPL
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/thunar-plugins/thunar-media-tags-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libthunar-devel libexo-gtk3-devel libxfce4util-devel
BuildRequires: libgtk+3-devel libtag-devel
BuildRequires: perl-XML-Parser intltool

%define _unpackaged_files_terminate_build 1

%description
The thunar-media-tags-plugin is a plugin for the Thunar File Manager,
which adds ID3/OGG tag support to the bulk rename dialog.

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
%doc README AUTHORS
%exclude %_libdir/thunarx-*/*.la
%_libdir/thunarx-*/*.so

# Seems glibc doesn't support uz@Latn
%exclude %_datadir/locale/uz@Latn/LC_MESSAGES/thunar-media-tags-plugin.mo

%changelog
* Tue Aug 21 2018 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Don't package uz@Latn translation.
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Fix Xfce name (XFCE -> Xfce).
- Updated to 0.3.0.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Updated to 0.2.1.

* Tue Dec 06 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt2
- Don't use empty string as separator.

* Tue Dec 06 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Drop obsoleted patches.
- Updated to 0.2.0.

* Thu Jan 27 2011 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt3
- Spec update & cleanup.
- Fix Url.
- tar.bz2 -> tar.
- Add patches from Debian (port to exo-1 and thunarx-2).

* Fri May 08 2009 Ilya Mashkin <oddity@altlinux.ru> 0.1.2-alt2
- fix build, update requires

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.1.2-alt1
- new version

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.1.1-alt1
- First build for Sisyphus.

