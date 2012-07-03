BuildRequires: desktop-file-utils
Name: lekhonee-gnome
Version: 0.11
Release: alt1

Summary: The GNOME frontend for lekhonee wordpress client
Group: Networking/Other
License: GPLv2+
Url: http://fedorahosted.org/lekhonee
Source: https://fedorahosted.org/releases/l/e/lekhonee/%name-%version.tar.bz2

BuildRequires: intltool libsoup-devel libgtksourceview-devel libgtkspell-devel libxml2-devel vala
BuildRequires: libwebkitgtk2-devel libgee-devel

%description
Lekhonee-gnome is a desktop Wordpress blog client for GNOME

%prep
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=WebDevelopment \
	%buildroot%_desktopdir/lekhonee-gnome.desktop

%files -f %name.lang
%_bindir/lekhonee-gnome
%_datadir/lekhonee-gnome
%_datadir/pixmaps/*
%_datadir/applications/*.desktop

%changelog
* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- 0.11

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for lekhonee-gnome

* Fri Oct 08 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt2
- rebuild against new webkit

* Tue Apr 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Sat Feb 13 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- first build for Sisyphus

