%define ver_major 2.22

Name: gnome-audio
Version: %ver_major.2
Release: alt1

Summary: Sounds for GTK and GNOME events
Group: Sound
License: CCSAv2 CCA-SAv2G CCAv3
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.bz2

BuildArchitectures: noarch

Obsoletes: gnome-audio-extra < 2.22.0
Provides: gnome-audio-extra = %version-%release

%description
If you use the GNOME desktop environment, you may want to
install this package of complementary sounds.

%prep
%setup -q

%install
mkdir -p %buildroot
%makeinstall

%files
%_datadir/sounds/*
%doc README ChangeLog

%changelog
* Thu May 15 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2
- add Packager

* Sun Apr 06 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1
- drop package extra

* Sun Apr 03 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Mon Oct 28 2002 AEN <aen@altlinux.ru> 1.4.0-alt2
- rebuilt with gcc-3.2

* Fri Jan 04 2002 Rider <rider@altlinux.ru> 1.4.0-alt1
- 1.4.0
- spec cleanup

* Fri Jan 05 2001 AEN <aen@logic.ru>
- adopted for RE

* Wed Jul 26 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.0-10mdk
- BM + macroszification

* Mon Apr 10 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0.0-9mdk
- adjust group

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Rebuild

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adatations.

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- switched generic and question sounds

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- redid defaults

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.0 - made extra subpackage

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.8

* Tue Jan 26 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.4

* Thu Dec 17 1998 Michael Fulbright <drmike@redhat.com>
- first pass at a spec file
