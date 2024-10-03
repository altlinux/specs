%def_enable git
%def_enable subversion

Name: thunar-vcs-plugin
Version: 0.2.0
Release: alt2

Summary: Version Contol System plugin for Thunar
License: GPL-2.0-or-later
Group: Graphical desktop/XFce

Url: https://docs.xfce.org/xfce/thunar/thunar-vcs-plugin
Vcs: https://gitlab.xfce.org/thunar-plugins/thunar-vcs-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libthunar-devel libgio-devel libxfce4util-devel libexo-gtk3-devel
BuildRequires: libgtk+3-devel
%if_enabled subversion
BuildRequires: libapr1-devel libsubversion-devel libaprutil1-devel
%endif
BuildRequires: intltool

%define _unpackaged_files_terminate_build 1

%description
The Thunar VCS Plugin provides a svn and git intergration to Thunar.
It allows you to do most of the svn and git actions from the context
menu. It also shows the svn file status in the file properties window.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
    --disable-static \
	%{subst_enable subversion} \
	%{subst_enable git} \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog
%_libexecdir/tvp-*
%_libdir/thunarx-*/*.so
%_iconsdir/hicolor/*/*/*.png

%exclude %_libdir/thunarx-*/*.la

%changelog
* Thu Oct 03 2024 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt2
- Fixed build: added intltool to BR.
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.

* Tue Aug 21 2018 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 0.2.0.

* Fri Jul 22 2016 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- Updated to 0.1.5.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt2.git20150306
- Rebuild with libxfce4util-4.12.
- Upstream git snapshot.

* Tue Apr 30 2013 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt2.git20130426
- Fix build with current libaprutil1.
- Enable subversion 1.7 support.
- Upstream git snapshot.

* Wed Apr 18 2012 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt2.git20111125
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Mon Nov 28 2011 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.git20111125
- Drop subversion 1.7 support.
- Initial build
