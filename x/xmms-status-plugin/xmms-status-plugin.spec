Name: xmms-status-plugin
Version: 1.0
Release: alt1

Summary: A docklet for XMMS
Group: Sound
License: GPL
Url: http://www.hellion.org.uk/xmms-status-plugin/

Source0: %name-%version.tar.gz

Patch0: xmms-status-plugin-1.0-alt-linking.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sun Apr 15 2007
BuildRequires: librcc-gtk libxmms-devel

%description
A status docklet for XMMS, docks into the GNOME Status dock.

Should work with the KDE equivalent.

%prep
%setup -q
#patch0 -p1

%build
autoconf
%configure \
	--disable-fatal-warnings
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README CREDITS TODO
%xmms_generaldir/libstatusdocklet.so
%xmms_generaldir/libstatusdocklet.la
%dir %_datadir/xmms/status_docklet
%_datadir/xmms/status_docklet/*

%changelog
* Sun Apr 15 2007 Igor Zubkov <icesik@altlinux.org> 1.0-alt1
- 0.9 -> 1.0

* Tue Nov 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9-alt1
- 0.9
- Rebuilt in new environment
- Some spec cleanup
- Added buildrequires

* Fri Jun 29 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.6-alt1
- New version
- Fix optimization
- Some spec cleanup

* Thu Feb 22 2001 Kostya Timoshenko <kt@petr.kz> 0.5-ipl2mdk
- build for RE

* Fri Feb 16 2001  Lenny Cartier <lenny@mandrakesoft.com> 0.5-2mdk
- add url

* Mon Nov 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.5-1mdk
- updated by Götz Waschk <waschk@linux-mandrake.com> :
- 0.5

* Tue Nov 07 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.4-1mdk
- update from Götz Waschk <waschk@linux-mandrake.com> :
- 0.4

* Mon Sep 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3-1mdk
- used srpm from Götz Waschk :

* Tue Aug 03 2000 Götz Waschk <waschk@linux-mandrake.com> 0.3-1mdk
- upgraded to 0.3

* Tue Jul 25 2000 Götz Waschk <waschk@linux-mandrake.com> 0.2-1mdk
- initial Mandrake build
