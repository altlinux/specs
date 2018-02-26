Name: fdutils

%define ver_base 5.5
%define ver_snap 20081027
%define srcname %name-%ver_base

%ifdef ver_snap
Version: %ver_base.%ver_snap
%else
Version: %ver_base
%endif
Release: alt1.qa1

Summary: Programs for dealing with floppy disks
License: GPLv2+
Group: System/Kernel and hardware
Url: http://fdutils.linux.lu
Packager: Dmitry V. Levin <ldv@altlinux.org>

# %url/%srcname.tar.gz
Source: %srcname.tar
%ifdef ver_snap
# %url/%name-%ver_base-%ver_snap.diff.gz
Patch1: %name-%ver_base-%ver_snap.diff
%endif
Patch2: fdutils-5.5-20060227-alt-headers.patch
Patch3: fdutils-5.4-alt-texinfo.patch

Requires: util-linux >= 2.11h-alt2

BuildRequires: flex libe2fs-devel tetex-latex

Summary(ru_RU.KOI8-R): Утилиты для форматирования дискет и управления флоппи-драйвером Линукса

%description
This package contains utilities for configuring and debugging the
Linux floppy driver, for formatting extra capacity disks (up to 1992K
on a high density disk), for sending raw commands to the floppy
controller, etc.

%description -l ru_RU.KOI8-R
Утилиты для настройки и отладки системного драйвера флоппи-дисков,
форматирования дискет с увеличенной плотностью (до 1992 килобайт),
прямого управления контроллером дисковода и т.д.

%prep
%setup -q -n %srcname
%ifdef ver_snap
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
sed -i 's|<linux/ext2_fs.h>|<ext2fs/ext2_fs.h>|' src/fdmount.c

%build
%configure
# SMP-incompatible
make

%install
mkdir -p %buildroot{%_sysconfdir,%_bindir,%_infodir,%_man1dir,%_man4dir}
%makeinstall UID=$(id -u) GID=$(id -g)

install -p -m644 src/mediaprm %buildroot%_sysconfdir
chmod 755 %buildroot%_bindir/*

%files
%config %_sysconfdir/mediaprm
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%doc CREDITS Changelog doc/FAQ.html doc/README doc/floppy_formats

%changelog
* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 5.5.20081027-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for fdutils
  * postclean-05-filetriggers for spec file

* Thu Nov 20 2008 Dmitry V. Levin <ldv@altlinux.org> 5.5.20081027-alt1
- Use ext2fs/ext2_fs.h instead of linux/ext2_fs.h for build.
- Updated to 20081027.

* Tue Feb 28 2006 Ilya Evseev <evseev@altlinux.ru> 5.5.20060227-alt1
- bugfix #9130: 'zero-based' attribute in /etc/mediaprm was not accepted by setfdprm

* Sun Mar 20 2005 Ilya Evseev <evseev@altlinux.ru> 5.5-alt1
- Updated to 5.5
- Little specfile cleanups

* Mon Feb 28 2005 Ilya Evseev <evseev@altlinux.ru> 5.4.20050213-alt1
- Updated to 20050213
- Disabled manpages patch (#2)

* Sat Jan  8 2005 Ilya Evseev <evseev@altlinux.ru> 5.4.20040228-alt1
- Updated to 20040228
- Specfile: added russian summary/description, fixed URLs
- Added %%doc files

* Sat Nov 02 2002 Dmitry V. Levin <ldv@altlinux.org> 5.4.20020222-alt1
- Updated to 20020222.
- Fixed texinfo documentation.

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.4-ipl3mdk
- Updated to 20010602.
- Resurrected _bindir/setfdprm.
- Requires: util-linux >= 2.11h-alt2

* Fri Mar 16 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.4-ipl2mdk
- Removed %_bindir/setfdprm (provided by util-linux).

* Sat Dec 16 2000 Dmitry V. Levin <ldv@fandra.org> 5.4-ipl1mdk
- 5.4.
- FHSification.

* Fri Jun 16 2000 Dmitry V. Levin <ldv@fandra.org> 5.3-ipl12mdk
- RE adaptions.

* Tue May 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 5.3-11mdk
- Fix buffer overvlow in fdmount (Yoann).

* Mon May 15 2000 Anton Graham <darkimage@bigfoot.com> 5.3.10mdk
- Add %%post and %%preun
- Use %%{_tmppath}
- Spec-helper cleanup

* Sun Apr 02 2000 Jerome Martin <jerome@mandrakesoft.com> 5.3-9mdk
- Fix rpm group and spec-helper issues

* Mon Jan 17 2000 Francis Galiegue <francis@mandrakesoft.com>
- Fixed build as non-root

* Thu Nov 18 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- build release

* Sun Jul 18 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.de>
- Fix up release number

* Wed Jul  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 5.3 version.
- Rewriting the .spec to be more Mandrake ;-)

* Sun Nov 29 1998 Paul H. Hargrove <hargrove@sccm.Stanford.EDU>
[5.2-4]
- Fix to be built by non-root
- Add conflict note in %%desrciption

* Wed Apr 15 1998 Paul H. Hargrove <hargrove@sccm.Stanford.EDU>
[5.2-3]
- Use buildroot
