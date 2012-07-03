%def_enable xinerama

Name: qiv
Version: 2.2.4
Release: alt1
Serial: 1

Summary: Quick Image Viewer
License: GPL2
Group: Graphics

Url: http://spiegl.de/qiv
Source: %url/download/%name-%version.tgz
# dfo:
Patch: %name-jumping.patch

BuildRequires: imlib2-devel libgtk+2-devel libmagic-devel
%{?_enable_xinerama:BuildRequires: libXinerama-devel}

Summary(ru_RU.CP1251): Быстрая программа просмотра изображений
Summary(uk_UA.CP1251): Швидкий проглядач зображень

%description
%name is a small and fast image viewer for X based on gdk and imlib2.

%description -l ru_RU.CP1251
%name - это небольшая и быстрая программа просмотра изображений для X,
основанная на gdk и imlib2.

%description -l uk_UA.CP1251
%name - це малий та швидкий проглядач зображень для X, оснований на gdk
та imlib2.

%prep
%setup -n %name-%version
%patch -p1

%{?_disable_xinerama:subst 's/^GTD_XINERAMA/#&/' Makefile}

%build
%define _optlevel 3
%add_optflags %optflags_shared
%make_build CFLAGS="%optflags"

%install
install -pdm0755 %buildroot/{%_bindir,%_man1dir}
install -pm0755 %name %buildroot/%_bindir/
install -pm0644 %name.1 %buildroot/%_man1dir/
bzip2 --best --keep --force Changelog

%files
%doc README Changelog.* README.TODO %name-command.example
%_bindir/*
%_man1dir/*

%changelog
* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1:2.2.4-alt1
- 2.2.4

* Fri Mar  5 2010 Terechkov Evgenii <evg@altlinux.ru> 1:2.2.3-alt1
- 2.2.3. Thanks to dfo@ for pointing to project's new home site
- Old patches dropped
- Spec cleanup

* Mon Jul 16 2007 Terechkov Evgenii <evg@altlinux.ru> 1:2.1-alt3.pre12
- Patch3,4 added (#1 replaced by #4) - thanks to dfo@.

* Tue Jul  3 2007 Terechkov Evgenii <evg@altlinux.ru> 1:2.1-alt2.pre12
- Patch1,2 added (#11975)

* Thu Jun 21 2007 Michael Shigorin <mike@altlinux.org> 1:2.1-alt1.pre12
- merged Daedalus build by led@
- left Serial: in place ("pre" suffix in version was a bad idea)
- demacrified Url:
- renamed spec to qiv.spec

* Wed Jun 13 2007 Led <led@altlinux.ru> 1:2.1-alt0.1
- 2.1-pre12
- fixed Summary and %%description
- fixed %%optflags to prevent segmentation fault on x86_64
- fixed License
- fixed version numeration
- cleaned up %%install section
- fixed BuildRequires
- compressed Changelog
- removed README.INSTALL from docs
- added README.TODO and %name-command.example to docs

* Thu Apr 26 2007 Sergey Pinaev <dfo@altlinux.ru> 2.1pre11-alt1
- New upstream version

* Mon Oct 11 2004 Sergey Pinaev <dfo@altlinux.ru> 2.0-alt2
- Makefile patches

* Mon Sep 20 2004 Sergey Pinaev <dfo@altlinux.ru> 2.0-alt1
- 2.0

* Sat Dec 28 2002 Michael Shigorin <mike@altlinux.ru> 1.8-alt1
- 1.8

* Tue Mar 26 2002 Stanislav Ievlev <inger@altlinux.ru> 1.7-alt2
- Removed menu entry (bug  #0000252) 'cause this is command-line utility

* Mon Jul 23 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.7-alt1
- new version

* Tue Jan 16 2001 AEN <aen@logic.ru>
- RE adaptations

* Wed Nov 29 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.5-1mdk
- Release 1.5
- Dadou compliant (uses RPM_OPT_FLAGS)

* Tue Nov 07 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-4mdk
- add a menu entry
- add some doc
- spec cleaning

* Tue Sep 19 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.3-3mdk
- Correct manpage used
- Prevent running qiv when generating package

* Sat Sep 16 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.3-2mdk
- rebuild this for the big move.

* Wed May 24 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 1.3-1mdk
- first spec

