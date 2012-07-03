%define upstreamname lxterminal
Name: lxde-lxterminal
Version: 0.1.11
Release: alt3

Summary: Desktop-independent VTE-based terminal emulator for LXDE
License: GPLv2+
Group: Graphical desktop/Other
Url: http://lxde.sourceforge.net/
Packager: LXDE Development Team <lxde at packages.altlinux.org>

Source: %upstreamname-%version.tar.gz
Patch: lxterminal-0-1-11-f10-true.patch

Buildrequires: docbook-dtds docbook-style-xsl xsltproc libvte-devel intltool
BuildRequires: desktop-file-utils

%description
%summary  without any unnecessary dependency (All instances share the same process to reduce memory usage)

%prep
%setup -n %upstreamname-%version
%patch -p2

%build
%autoreconf
%configure --enable-man

%make_build

%install
%makeinstall_std
%find_lang %upstreamname
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=System \
	%buildroot%_desktopdir/lxterminal.desktop

%files -f %upstreamname.lang
%doc ChangeLog INSTALL README
%_bindir/*
%_desktopdir/*.desktop
%_datadir/%upstreamname
%_man1dir/*
%_pixmapsdir/*.png

%changelog
* Tue Jun 12 2012 Radik Usupov <radik@altlinux.org> 0.1.11-alt3
- new upstreame snapshot

* Thu Sep 22 2011 Radik Usupov <radik@altlinux.org> 0.1.11-alt2
- F10 included to default

* Tue Aug 30 2011 Radik Usupov <radik@altlinux.org> 0.1.11-alt1
- 0.1.9
- moved files to folder

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.9-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for lxde-lxterminal

* Sat Oct 16 2010 Radik Usupov <radik@altlinux.org> 0.1.9-alt1
- 0.1.9

* Sun Aug 08 2010 Radik Usupov <radik@altlinux.org> 0.1.8-alt1
- 0.1.8
- change packager

* Fri May 28 2010 Radik Usupov <radik@altlinux.org> 0.1.7-alt4
- buildrequires are corrected
- added autoreconf -fisv parameters
- added --enable-man fot %configure parameters
- closed #23524

* Tue May 25 2010 Radik Usupov <radik@altlinux.org> 0.1.7-alt2
- update upstream

* Wed Mar 03 2010 Radik Usupov <radik@altlinux.org> 0.1.7-alt1
- 0.7.1

* Sat Jan 30 2010 Radik Usupov <radik@altlinux.org> 0.1.6-alt1
- new packager
- new version
- new buildrequires

* Fri Jan 09 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.1.4-alt1
- new version
- remove obsoletes %%update_menu macros

* Fri Jul 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1.3-alt1
- First version of RPM package for Sisyphus.
