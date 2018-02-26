%define upstreamname xfbib

Name: xfce4-%upstreamname
Summary: A BibTeX editor for Xfce
Version: 0.0.2
Release: alt2
License: %gpl2plus
Url: http://goodies.xfce.org/projects/applications/%upstreamname
Source: http://goodies.xfce.org/releases/%upstreamname/%upstreamname-%version.tar

Group: Graphical desktop/XFce
Packager: XFCE Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: xfce4-dev-tools intltool

BuildRequires: flex libxfcegui4-devel

%description
Xfbib is a lightweight BibTeX editor developed for the Xfce
desktop manager. The intentions of Xfbib is to provide an easy
and efficient way of editing BibTeX files.

%prep
%setup -n %upstreamname-%version

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %upstreamname

%files -f %upstreamname.lang
%doc README ChangeLog NEWS INSTALL COPYING AUTHORS TODO
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.0.2-alt2
- tar.bz2 -> tar.
- Spec cleanup & update.
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Sat Nov 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for xfce4-xfbib
  * shared-mime-info for xfce4-xfbib
  * update_menus for xfce4-xfbib
  * postclean-05-filetriggers for spec file

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.2-alt1
- first build for Sisyphus

