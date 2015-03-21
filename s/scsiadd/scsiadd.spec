Summary: Utility to add and remove SCSI devices on the fly
Name: scsiadd
Version: 1.97
Release: alt1
License: GPL2
Group: System/Configuration/Hardware
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar
Url: http://llg.cubic.org/tools/

%description
scsiadd lets you insert or remove SCSI devices from the linux SCSI
subsystem on the fly. This is useful for external devices
like scanners or tapes which can be powered on after system boot.
Devices can be added or removed at any time.

%description -l UTF-8
scsiadd - утилита, позволяющая вставлять или удалять SCSI устройств 
в Linux SCSI подсистеме "на лету". Это полезно для внешних устройств, таких,
как сканеры или ESATA диски, которые могут быть включены после загрузки
системы. Утилита позволяет добавить или удалить устройства в любое время.
См. так-же http://www.tldp.org/HOWTO/SCSI-2.4-HOWTO/index.html

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README NEWS
%_sbindir/%name
%_man8dir/%name.8*

%changelog
* Sat Mar 21 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.97-alt1
- initial build for ALT Linux Sisyphus

* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1:1.95-5mdv2010.0
+ Revision: 433633
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:1.95-4mdv2009.0
+ Revision: 260573
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:1.95-3mdv2009.0
+ Revision: 252219
- rebuild
+ Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1:1.95-1mdv2008.1
+ Revision: 127101
- kill re-definition of %%buildroot on Pixel's request
- use mkrel
- import scsiadd

* Mon Feb 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.95-1mdk
- 1.95

* Thu Jan 13 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.6-1mdk
- 1.6
- add epoch tag to handle upgrade
- update %%docs

* Mon Dec 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.52-1mdk
- 1.52
- regenerate patch

* Sat Dec 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.51-1mdk
- 1.51
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- quiet setup
- use %%configure macro
- fix install (P0)

* Mon Jan 27 2003 Götz Waschk <waschk@linux-mandrake.com> 1.41-3mdk
- fix URL
- fix rpmlint warnings

* Mon Jan 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.41-2mdk
- rebuild

* Mon Nov 26 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.41-1mdk
- 1.41

* Mon Aug 29 2001 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.4-2mdk
- added man page.

* Tue Aug 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4-1mdk
- 1.4.

* Mon Jan 29 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.3-1mdk
- updated to 1.3.

* Fri Aug 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1-1mdk
- used srpm from John Johnson <jjohnson@linux-mandrake.com>
- Made mandrake rpm and changed compression to bz2 
- macros
- BM
