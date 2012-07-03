Name: nautilus-open-terminal
Version: 0.19
Release: alt1

Summary:  An extension for Nautilus to open terminal in current location
Group: Graphical desktop/GNOME
License: %gpl2plus
Url: http://gnomefiles.org

Source: %gnome_ftp/%name/%version/%name-%version.tar.bz2

BuildPreReq: rpm-build-licenses rpm-build-gnome >= 0.5

# From configure.in
BuildRequires: libnautilus-devel >= 3.0.0
BuildRequires: libgnome-desktop3-devel >= 3.0.0
BuildRequires: glib2-devel >= 2.16.0
BuildRequires: intltool >= 0.35.0

BuildRequires: libGConf-devel libSM-devel

%description
This package contains a Nautilus extension makes it easy to open terminal
in current location.

%prep
%setup -q

%build
%configure --disable-schemas-install --disable-static
%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%nautilus_extdir/lib%name.so
%gconf_schemasdir/%name.schemas
%doc AUTHORS README TODO ChangeLog

%exclude %nautilus_extdir/*.la

%changelog
* Fri Sep 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.19-alt1
- 0.19

* Thu Mar 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt2
- rebuild against new libgnome-desktop

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt1
- 0.18

* Sun Aug 09 2009 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt1
- 0.17

* Tue Aug 04 2009 Yuri N. Sedunov <aris@altlinux.org> 0.16-alt1
- 0.16

* Mon Aug 03 2009 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt1
- 0.15

* Sun May 24 2009 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13

* Sun May 17 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12
- updated buildreqs

* Fri May 15 2009 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- new version
- removed unneeded patch
- updated buildreqs

* Fri Mar 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt3
- rebuild against libgnome-desktop-2.so.11
- fixed %%build
- updated buildreqs

* Fri Nov 07 2008 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt2
- rebuild against libgnome-desktop-2.so.7

* Wed May 14 2008 Alexey Rusakov <ktirf@altlinux.org> 0.9-alt1
- New version (0.9).
- Use a macro for License tag.
- Spec cleanup, updates to the file list and install scripts.

* Sat Jun 30 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8-alt1
- new version (0.8)
- Belarussian translation is now provided in the tarball.
- updated dependencies
- again, updated the patch for the careless C code.
- use macros from rpm-build-gnome
- added an explicit buildreq on libSM-devel (an implicit one has dropped).
- updated Source URL

* Wed Jan 24 2007 Alexey Rusakov <ktirf@altlinux.org> 0.6-alt2
- although upstream seems to be dead, the program is too good to be thrown away.
- fixed building
- spec cleanup, updated buildreqs from configure.in
- updated the patch in order to build the code still without warnings.

* Tue Mar 07 2006 Vital Khilko <vk@altlinux.ru> 0.6-alt1
- 0.6

* Wed May 04 2005 Vital Khilko <vk@altlinux.ru> 0.2-alt1
- initial build



