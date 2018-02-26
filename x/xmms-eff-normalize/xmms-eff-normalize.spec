%define rname volnorm

Name: xmms-eff-normalize
Version: 0.8.3
Release: alt2.1

Summary: Normalizing plugin for XMMS
License: GPL2+
Group: Sound
Packager: Evgenii Terechkov <evg@altlinux.ru>

Url: http://volnorm.sourceforge.net
Source: %rname-%version.tar.gz
Patch1: 0.8.1-free-fix.patch
Patch2: volnorm-0.8.3-alt-linking.patch

# Automatically added by buildreq on Fri Oct 12 2007
BuildRequires: gcc-c++ libxmms-devel xmms

Obsoletes: xmms-normalize < 0.8.1

%description
Volume Normalizer is an XMMS plugin that will set the volume of any played
song to some preset level. It ensures that all songs will have the same
volume and you will not need to hit the volume knob for each song.

%prep
%setup -q -n %rname-%version
%patch1 -p1 -b .orig
%patch2 -p1 -b .orig

%build
%__autoreconf
unset CC CXX
%configure --enable-one-plugin-dir
%make_build

%install
mkdir -p %buildroot%xmms_effectdir
install -m755 src/.libs/*.so %buildroot%xmms_effectdir

%files
%doc AUTHORS README RELEASE TODO NEWS ChangeLog BUGS
%xmms_effectdir/*.so

%changelog
* Sun Nov 18 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8.3-alt2.1
- Patch2 added (fixes #11436, thanks to icesik@!)

* Fri Oct 12 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8.3-alt2
- Spec cleanups (un__.sh, others)
- Packager tag added to spec
- BuildRequires updated
- Patch1 added (fixes #13051)
- Licence tag updated and cleaned up

* Fri Oct 12 2007 Evgenii Terechkov <evg@altlinux.ru> 0.8.3-alt2
- spec macro abuse cleanup

* Sat Jan 27 2007 Michael Shigorin <mike@altlinux.org> 0.8.3-alt1
- 0.8.3

* Sun Jan 04 2004 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt1
- 0.8.1
- renamed to %name as per xmms subpackaging policy
- spec cleanup

* Fri Nov 15 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.4.1-ipl3mdk
- Rebuilt in new environment
- Added buildrequires
- Some spec cleanup

* Thu Jun 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.4.1-ipl2mdk
- Rebuild with xmms-1.2.5
- Some spec cleanup
- Fix makefile

* Thu Feb 22 2001 Kostya Timoshenko <kt@petr.kz> 0.4.1-ipl1mdk
- build for RE

* Fri Feb 16 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4.1-1mdk
- upgraded to 0.4.1

* Thu Oct 19 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.5-1mdk
- update to 0.3.5 from rufus t firefly <rufus.t.firefly@linux-mandrake.com>

* Fri Sep 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.4-1mdk
- update to 0.3.4 from rufus t firefly <rufus.t.firefly@linux-mandrake.com>

* Mon Sep 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-1mdk
- used srpm from rufus t firefly :
	Fri Sep 15 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
	- v0.3.1-1mdk

* Thu Sep 14 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
  - v0.3-1mdk

* Thu Aug 31 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
  - v0.2-1mdk
  - bz2 archive
