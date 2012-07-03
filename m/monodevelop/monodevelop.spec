# vim: set ft=spec: -*- rpm-spec -*-

%def_disable tests

Name: monodevelop
Version: 2.8.6.4
Release: alt1

Summary: MonoDevelop is a project to port SharpDevelop to Gtk#
License: LGPLv2.1
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://www.monodevelop.org/

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

# FIXME: check everytime
%add_findreq_skiplist %_prefix/lib/%name/AddIns/VersionControl/MonoDevelop.VersionControl.Subversion.dll

Requires: libsubversion
Requires: desktop-file-utils
Requires: firefox
Requires: shared-mime-info

BuildPreReq: rpm-build-mono mono-mcs
BuildPreReq: mono-devel >= 2.8
BuildPreReq: mono-addins-devel >= 0.6
BuildPreReq: libgtk-sharp2-devel >= 2.12.8
BuildPreReq: libgnome-desktop-sharp-devel >= 2.12.8
BuildPreReq: monodoc-devel >= 1.0

# BuildPreReq: libgecko-sharp2-devel >= 0.10

BuildRequires: intltool mono-mcs mono-web-devel mono-winforms
BuildRequires: desktop-file-utils mono-nunit-devel perl-XML-Parser shared-mime-info intltool
BuildRequires: zip
BuildRequires: /proc

BuildRequires: xsp

%description
This is MonoDevelop which is intended to be a full-featured
integrated development environment (IDE) for mono and Gtk#.
It was originally a port of SharpDevelop 0.98.

%prep
%setup -q -n %name-%version
%patch0 -p1

%__subst '/^Encoding=/d;
	s/^Exec=monodevelop$/Exec=monodevelop %%F/;
	s/^Categories=.*$/Categories=Development;IDE;/
	' monodevelop.desktop
%__subst "s|^pkgconfigdir *= \$(prefix)/lib/pkgconfig|pkgconfigdir = %_pkgconfigdir|" \
	Makefile.am

%build
#export PKG_CONFIG_PATH=%_pkgconfigdir MOZILLA_HOME=%_libdir/firefox
%autoreconf
%configure  \
	    --disable-update-mimedb --disable-update-desktopdb \
	    %{subst_enable tests}

mkdir -p build/bin

%make

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog INSTALL README
%_bindir/*
%_prefix/lib/%name
%_pkgconfigdir/*.pc
%_desktopdir/%name.desktop
%_iconsdir/hicolor/??x??/apps/%{name}*.png
%_iconsdir/hicolor/scalable/apps/%{name}*.svg
%_datadir/mime/packages/*
%_man1dir/*

%changelog
* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 2.8.6.4-alt1
- 2.8.6.4

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2
- build with internal Cecil

* Thu Jun 17 2010 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4

* Thu Mar 18 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2
- changed License

* Mon Oct 19 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Mon Jul 13 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt2
- update buildreq

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Fri Mar 13 2009 Alexey Shabalin <shaba@altlinux.ru> 1.9.2-alt1
- 1.9.2
- updated patches list

* Sun Feb 01 2009 Alexey Shabalin <shaba@altlinux.ru> 1.9.1-alt3.1
- rebuild with mono-2.2 (fix requires new cecil )

* Mon Jan 05 2009 Ildar Mulyukov <ildar@altlinux.ru> 1.9.1-alt3
- fixed manual deps to be x86_64-friendly

* Sat Jan 03 2009 Ildar Mulyukov <ildar@altlinux.ru> 1.9.1-alt2
- desktop file fixes according to repocop results

* Sun Nov 23 2008 Ildar Mulyukov <ildar@altlinux.ru> 1.9.1-alt1
- 1.9.1
- manual rpm reqs for MonoDevelop.VersionControl.Subversion.dll
- new switch: %%def_(en|dis)able tests - disabled

* Fri Oct 31 2008 Alexey Shabalin <shaba@altlinux.ru> 1.9-alt1.r117558
- 2.0 alpha1, svn version 117558
- main package and core addins. extra addins move to package monodevelop-extra

* Tue Apr 01 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt2
- use gtksourceview2-sharp

* Fri Mar 28 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Mon Feb 25 2008 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1
- 0.19
- revised patch3 (use system cecil)

* Wed Jan 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.18.1-alt1
- 0.18.1
- use system cecil (patch3)
- cleanup spec
- use gtksourceview1-sharp

* Wed Nov 28 2007 Alexey Shabalin <shaba@altlinux.ru> 0.17-alt0.20071121
- 0.17
- use gtksourceview-2.0 and gtksourceview2-sharp
- disable build database support - fail build with gtksourceview2-sharp
- use firefox instead seamonkey
- add man page mdtool

* Tue Oct 09 2007 Alexey Shabalin <shaba@altlinux.ru> 0.16-alt1
- 0.16
- add seamonkey, libgnomeui to Requires (#13033)

* Sat Sep 08 2007 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15
- fix build for x86_64

* Sat Jul 28 2007 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- Update to 0.14
- source from svn (no full archive in download homepage)

* Sun Mar 25 2007 Ildar Mulyukov <ildar@altlinux.ru> 0.13.1-alt1
- 0.13.1
- new translation ru.po
- disable nemerle AddIn, it's not working right now

* Tue Dec 12 2006 Ildar Mulyukov <ildar@altlinux.ru> 0.12-alt2
- added "enable-feature" switches

* Wed Sep 27 2006 Ildar Mulyukov <ildar@altlinux.ru> 0.12-alt1
- BuildRequires fixes
- new features on

* Wed Jul 19 2006 Ildar Mulyukov <ildar@altlinux.ru> 0.11-alt1
- 0.11
- automatic dependancies calculation (due to rpm-4.0.4-alt66.1)

* Sun May 22 2005 Evgeny Sinelnikov <sin@altlinux.ru> 0.7-alt1
- Update to release

* Mon May 16 2005 Evgeny Sinelnikov <sin@altlinux.ru> 0.6-alt1
- Initial build for ALTLinux.
