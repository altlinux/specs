%define git_date .git20111125

%def_enable git
%def_enable subversion

Name: thunar-vcs-plugin
Version: 0.1.4
Release: alt2%git_date

Summary: Version Contol System plugin for Thunar
License: %gpl2plus
Group: Graphical desktop/XFce

URL: http://goodies.xfce.org/projects/thunar-plugins/thunar-vcs-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libThunar-devel libgio-devel libxfce4util-devel libexo-devel
BuildRequires: libgtk+2-devel
%if_enabled subversion
BuildRequires: libapr1-devel libsubversion-devel
%endif

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
    --enable-debug=no
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
* Wed Apr 18 2012 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt2.git20111125
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Mon Nov 28 2011 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.git20111125
- Drop subversion 1.7 support.
- Initial build
