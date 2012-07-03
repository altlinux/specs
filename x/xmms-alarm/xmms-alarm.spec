Name:		xmms-alarm
Version:	0.3.6
Release:	alt1
Summary:	An alarm plugin for XMMS
Summary(ru_RU.KOI8-R): Плагин-будильник для XMMS
Group:		Sound
License:	GPL

Source:		http://www.snika.uklinux.net/%name-%version.tar.gz
Patch0:		xmms-alarm-configure.patch

Requires: xmms >= 1.0.1
BuildPreReq: libxmms-devel >= 1.0.1
# ???
Obsoletes: %name
Provides: %name = %version-%release

%description
%name is a general plugin to use with XMMS that fades up the volume in
the morning and wakes you up.

%description -l ru_RU.KOI8-R
%name это плагин общего назначения для XMMS, который плавно поднимает громкость
утром и будит вас.

%define _xmms_general_plugin_dir %(xmms-config --general-plugin-dir)

%prep
%setup -q
%patch0 -p1

%build
autoconf
# makes no sense, but let's leave it here as a reminder
#%configure --libdir=/%_libdir/xmms/General
%configure
%make_build

%install
# same
#%makeinstall libdir=$RPM_BUILD_ROOT%_libdir/xmms/General
%makeinstall DESTDIR=%buildroot
%__rm -f %buildroot%_xmms_general_plugin_dir/*.la

%files
%_xmms_general_plugin_dir/*.so
%doc AUTHORS ChangeLog README

%changelog
* Mon May 10 2004 Denis Ovsienko <pilot@altlinux.ru> 0.3.6-alt1
- rebuilt for current Sisyphus
- Russian tags

* Fri Nov 15 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.3.2-alt1
- 0.3.2
- Added buildrequires
- Some spec cleanup

* Wed Jun 27 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.3.0-alt0.2
- New version - 0.3.0-pre2
- Fixed configure

* Thu Feb 22 2001 Kostya Timoshenko <kt@petr.kz> 0.2.2-ipl2mdk
- build for RE

* Thu Feb 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2.2-2mdk
- rebuild

* Tue Oct 30 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.2.2-1mdk
- update to 0.2.2

* Thu Sep 21 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.01-2mdk
- bm
- macros

* Thu Jun 22 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com> 0.01-1mdk
- v0.01 (initial packaging)
- bz2 archive
