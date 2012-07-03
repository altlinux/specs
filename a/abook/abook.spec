Name: abook
Version: 0.5.6
Release: alt3

Summary: Text-based addressbook program for mutt
License: GPL
Group: Networking/Mail

Url: http://abook.sourceforge.net/
Source: %name-%version.tar.bz2
Patch: abook-0.5.6-editor.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Jun 08 2008 (-bi)
BuildRequires: libncursesw-devel libreadline-devel libncurses-devel libtinfo-devel

Summary(ru_RU.UTF-8): Текстовая адресная книга для mutt

%description
Abook is a small and powerful text-based addressbook program
designed for use with the mutt mail client.

%description -l ru_RU.UTF-8
Abook это небольшая и полнофункциональная текстовая программа для хранения
адресов предназначенная для использования с почтовым клиентом mutt.

%prep
%setup -n %name-%version
%patch -p0

%build
%configure
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS BUGS ChangeLog README THANKS sample.abookrc FAQ ANNOUNCE
%_bindir/*
%_mandir/man?/*

# TODO:
# - 0.6.0pre2? (2006-09-07)

%changelog
* Sun Jun 08 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.6-alt3
- updated buildrequres

* Mon May 26 2008 Michael Shigorin <mike@altlinux.org> 0.5.6-alt2
- adopt/cleanup/rebuild
- added official patch to fix a segfault in editor

* Tue Jul 17 2007 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.6-alt1
- new version
- rebuilded vith utf-8 support

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.5-alt1.1
- Rebuilded with libreadline.so.5.

* Sat Dec 03 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.5-alt1
- 0.5.5

* Sun Oct 16 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.4-alt2
- updated spec

* Sat Sep 03 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Wed Oct 27 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Wed Mar 24 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.5.2-alt2
- 0.5.2

* Tue Feb 10 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.5.2-alt1.pre3
- 0.5.2pre3

* Wed Dec 03 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.5.2-alt1.pre1
- 0.5.2pre1

* Wed Dec 03 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.5.1-alt1
- 0.5.1
- updated spec

* Mon Jun 30 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.5.0-alt2
- 0.5.0

* Thu Jun 26 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.5.0-alt1.rc1
- 0.5.0rc1
- updated spec

* Fri Jun 20 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.4.18-alt0.2.cvs20030530
- daily cvs snapshot

* Tue Nov 05 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.4.18-alt0.1.cvs20021008
- daily cvs snapshot
- %%rlz1 logic is going back ;)

* Wed Oct 16 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.17-alt2
- rebuild with gcc3
- I had to remove %%rlz1 logic. See changelogs below ;)))
- removed extra translations

* Sun Apr 07 2002 Aleksandr Blohin <sass@altlinux.ru> 0.4.17-%%rlz1
- 0.4.17

* Fri Mar 15 2002 Aleksandr Blohin <sass@altlinux.ru> 0.4.16-%%rlz1
- 0.4.16

* Fri Mar 01 2002 Aleksandr Blohin <sass@altlinux.ru> 0.4.15-%%rlz1
- updates in spec

* Tue Jan 08 2002 Aleksandr Blohin <sass@altlinux.ru> 0.4.15-alt3
- added Summary & description in CP1251 encoding

* Mon Dec 24 2001 Aleksandr Blohin <sass@altlinux.ru> 0.4.15-alt2
- updated spec
- updated to rpm-4.0.3

* Thu Nov 7 2001 Aleksandr Blohin <sass@altlinux.ru> 0.4.15-alt1
- 0.4.15 final
- spec cleanup

* Sat Oct 27 2001 Aleksandr Blohin <sass@altlinux.ru> 0.4.15-alt0.pre2
- 0.4.15pre2
- spec cleanup

* Fri Oct 5 2001 Aleksandr Blohin <sass@altlinux.ru> 0.4.14-alt1
- 0.4.14

* Thu Jun 28 2001 Stanislav Ievlev <inger@altlinux.ru> 0.4.13-alt1
- 0.4.13

* Thu Apr 26 2001 Stanislav Ievlev <inger@altlinux.ru> 0.4.12-alt1
- 0.4.12

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 0.4.11-ipl1mdk
- 0.4.11

* Sun Dec 17 2000 Dmitry V. Levin <ldv@fandra.org> 0.4.10-ipl1mdk
- RE adaptions.

* Sat Dec 16 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.4.10-1mdk
- first mandrake version

* Wed Sep 20 2000 Gustavo Niemeyer <niemeyer@conectiva.com>
- First package.
