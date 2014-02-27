Name: xfbib
Summary: A BibTeX editor for Xfce
Version: 0.1.0
Release: alt1
License: %gpl2plus
Url: http://goodies.xfce.org/projects/applications/%name
Source: %name-%version.tar

Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildRequires: libxfce4util-devel libxfce4ui-devel
BuildRequires: intltool flex

Provides: xfce4-xfbib = %version-%release
Obsoletes: xfce4-xfbib < %version-%release

%description
Xfbib is a lightweight BibTeX editor developed for the Xfce
desktop manager. The intentions of Xfbib is to provide an easy
and efficient way of editing BibTeX files.

%prep
%setup
# Use all languages, not from LINGUAS only
rm po/LINGUAS

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-debug=no
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS TODO
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.*
%_pixmapsdir/%name/

%changelog
* Thu Feb 27 2014 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Use all translations.
- Fix Xfce name (XFCE -> Xfce).
- Rename package: xfce4-xfbib -> xfbib.
- Updated to 0.1.0.

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

